from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig,ax=plt.subplots(1,2,figsize=(8,3.6),layout='constrained');t=np.linspace(0,2*np.pi,300)
for a,sgn,title in zip(ax,[1,-1],['Positive root: counterclockwise','Negative root: clockwise']):
 a.plot(1+.3*np.cos(t),.3*np.sin(t),lw=2);a.plot(1,0,'o',color='gray');a.text(1.02,-.05,r'$(\rho_0,0)$',fontsize=10)
 u=sgn*np.pi/4;point=np.array([1+.3*np.cos(u),.3*np.sin(u)]);v=sgn*np.array([-np.sin(u),np.cos(u)])*.14
 a.annotate('',point+v/2,point-v/2,arrowprops=dict(arrowstyle='->',lw=2,color='#9e4a10'))
 a.set(xlim=(.5,1.5),ylim=(-.48,.48),xlabel=r'$x$',ylabel=r'$y$',title=title);a.set_aspect('equal');a.grid(alpha=.2)
fig.suptitle('First-order circles about the same shifted equilibrium; illustrative coordinate scale',fontsize=10)

fig.savefig(Path(__file__).stem+'.png',dpi=140,facecolor='white')
