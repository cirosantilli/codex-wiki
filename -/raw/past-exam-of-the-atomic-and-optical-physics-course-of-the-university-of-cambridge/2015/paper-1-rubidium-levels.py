"""Original explanatory figure. Python 3.14, numpy and matplotlib.
Writes one PNG basename to cwd; no source-image pixels or hardcoded media paths.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Circle, Rectangle, FancyArrowPatch
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','savefig.facecolor':'white','axes.spines.top':False,'axes.spines.right':False})
fig=plt.figure(figsize=(10,6),layout='constrained');g=fig.add_gridspec(2,2);up=fig.add_subplot(g[0,0]);lo=fig.add_subplot(g[1,0]);a=fig.add_subplot(g[:,1]);B=np.linspace(0,10,300);muBh=1.39962449361
for ax,F,gF in [(up,2,.5),(lo,1,-.5)]:
 for m in range(-F,F+1):
  y=gF*m*muBh*B;ax.plot(B,y,lw=2 if m==0 else 1.3,color='#c33c29' if m==0 else '#1766a5');ax.text(10.25,y[-1],fr'$m_F={m}$',va='center',fontsize=8)
 ax.set(xlabel='B (G)',ylabel='Shift from manifold centre (MHz)',xlim=(0,13.5),title=fr'$F={F}$; centre '+(r'$3A/4$' if F==2 else r'$-5A/4$'));ax.axvline(0,color='gray',lw=.5)
shift=(muBh*1e6)**2/(3.4e9)*B*B/1000;a.plot(B,shift,color='#c33c29',lw=2);a.set(xlabel='B (G)',ylabel='Clock shift (kHz)',title=r'$m_F=0\leftrightarrow0$ quadratic sensitivity');a.text(.5,49,r'$\Delta_{\rm hf}=2A\simeq h\times6.8$ GHz');a.annotate(r'$|\Delta\mu|\simeq0.0082\mu_B$',(10,shift[-1]),(1,35),arrowprops=dict(arrowstyle='->'))
fig.suptitle('All weak-field substates; left panels use separate hyperfine-centre offsets',fontsize=11);fig.savefig('paper-1-rubidium-levels.png',dpi=165);plt.close(fig)
