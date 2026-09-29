"""Original explanatory figure; Python 3.14, numpy and matplotlib.
Writes a literal PNG basename to cwd. No source-image pixels or media paths.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, FancyArrowPatch
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','savefig.facecolor':'white','axes.spines.top':False,'axes.spines.right':False})
fig,axs=plt.subplots(1,3,figsize=(12,3.7),layout='constrained');a,b,c=axs
x=np.linspace(-1.6,1.6,400);profile=np.exp(-2*x*x);a.plot(x,profile,label='Focusing, n₂ > 0');a.plot(x,-profile,label='Defocusing, n₂ < 0');a.set(xlabel=r'$r/w$',ylabel='Nonlinear index (scaled)',title='Intensity creates index curvature');a.legend(frameon=False,fontsize=9)
b.plot(x,profile-profile[200],label='Exact Gaussian phase');b.plot(x,-2*x*x,label='Central quadratic fit');b.set(xlim=(-1.2,1.2),ylim=(-2,0.1),xlabel=r'$r/w$',ylabel='Phase relative to centre (scaled)',title='Kerr lens is a local approximation');b.legend(frameon=False,fontsize=9)
q=np.linspace(0,2.4,500);g2=q*q/2*(2-q*q/2);c.plot(q,np.sqrt(np.maximum(g2,0)));c.axvline(np.sqrt(2),color='gray',ls=':');c.set(xlabel=r'$q/\sqrt{k\gamma I_0}$',ylabel=r'$g/(\gamma I_0)$',ylim=(0,1.12),title='Focusing transverse instability');c.text(1.42,1.04,'fastest mode',fontsize=9);c.fill_between(q,0,np.sqrt(np.maximum(g2,0)),alpha=.13)
fig.savefig('paper-1-transverse-nonlinearity.png',dpi=150);plt.close(fig)
