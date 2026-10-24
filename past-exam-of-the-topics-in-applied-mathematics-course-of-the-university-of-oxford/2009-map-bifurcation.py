"""Original solution diagram; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7. Output to CWD."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'figure.facecolor':'white','axes.facecolor':'white','font.size':10,'axes.spines.top':False,'axes.spines.right':False})

fig,ax=plt.subplots(figsize=(9,5.3),layout='constrained');aa=np.linspace(.03,5,500);ax.plot(aa,np.zeros_like(aa),'--',color='black',label='Unstable fixed point')
for lo,hi,ls in [(2.00001,3,'--'),(3,3.5,'-'),(3.5,5,'--')]:
 a=np.linspace(lo,hi,300);v=np.sqrt(3-6/a)
 for sign in [-1,1]:ax.plot(a,sign*v,ls,color='#237b4b',lw=2,label='Fixed-point branches' if lo==3 and sign==1 else None)
for lo,hi,ls in [(.03,.5,'-'),(.5,5,'--')]:
 for sign in [-1,1]:ax.plot([lo,hi],[sign*np.sqrt(3)]*2,ls,color='#227caa',lw=1.7,label='Antipodal two-cycle' if lo==.03 and sign==1 else None)
a=np.linspace(3.00001,5,400)
for first in [-1,1]:
 for second in [-1,1]:ax.plot(a,(first*np.sqrt(3+3/a)+second*np.sqrt(3-9/a))/2,':',color='#d17a24',lw=1.6,label='Unstable asymmetric two-cycles' if first==second==1 else None)
for a in [.5,2,3,3.5]:ax.axvline(a,color='.85',lw=.7)
ax.set(xlabel='a',ylabel='x component',title='Solid: attracting; dashed/dotted: nonattracting',xlim=(0,5),ylim=(-2,2));ax.legend(fontsize=8,loc='center right')
fig.savefig(Path.cwd()/'2009-map-bifurcation.png',dpi=150,facecolor='white');plt.close(fig)
