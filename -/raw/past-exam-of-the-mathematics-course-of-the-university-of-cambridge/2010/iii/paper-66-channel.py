"""Original Paper 66 sketches. Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Write paper-66-channel.png to the caller's CWD; respect MPLCONFIGDIR.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
fig,axes=plt.subplots(1,2,figsize=(11,4.1),layout='constrained',facecolor='white')
ax=axes[0];tau=np.linspace(1,35,1600);peak=(7/3)**(7/4);f=np.maximum(tau**(-1)*(tau**(4/7)-1),0)**(1/3);fp=(peak**(-1)*(peak**(4/7)-1))**(1/3)
ax.plot([0,1],[0,0],color='#176a9c',lw=2.5);ax.plot(tau,f/fp,color='#176a9c',lw=2.5);ax.axvline(1,color='gray',ls=':',lw=1);ax.scatter([peak],[1],color='#ab3f2f',s=25,zorder=5);ax.annotate(r'$X^2=7x_*^2/3$',(peak,1),xytext=(peak+4,.91),arrowprops={'arrowstyle':'->','color':'#ab3f2f'},fontsize=11);ax.text(.85,.1,'arrival',rotation=90,va='bottom',ha='right',color='gray');ax.set(xlim=(0,35),ylim=(-.015,1.14),xlabel=r'$t/t_{\rm arrival}$',ylabel=r'$h_0(x_*,t)/h_{\rm max}$',title='Depth at a fixed nonzero station');ax.spines[['top','right']].set_visible(False)
ax=axes[1];ax.plot([-1.2,0,1.2],[1.2,0,1.2],color='#454545',lw=3);ax.fill([-0.5,0,0.5], [.5,0,.5],color='#9ed2e8');ax.plot([-.5,.5],[.5,.5],color='#176a9c',lw=2);ax.plot([-1,1],[1,1],color='gray',ls='--',lw=1)
s=np.linspace(.48,1,200);b=.035*np.sqrt(np.maximum(s-.48,0)/.52)
for sign in [-1,1]:
 outer=sign*s;inner=sign*(s-b);ax.add_patch(Polygon(np.c_[np.r_[outer,inner[::-1]],np.r_[s,s[::-1]]],facecolor='#4386b1',edgecolor='none'))
 # Downhill gravity component on each wall.
 ax.annotate('',xy=(sign*.68,.65),xytext=(sign*.86,.83),arrowprops={'arrowstyle':'->','lw':1.7,'color':'#ab3f2f'})
ax.annotate('residual draining films',(.84,.8),xytext=(.03,1.2),arrowprops={'arrowstyle':'->','color':'#176a9c'},ha='center',fontsize=10);ax.text(0,1.025,'previous maximum level',ha='center',fontsize=10,color='gray');ax.text(0,.54,'current level: half maximum',ha='center',fontsize=10,color='#176a9c');ax.text(0,.18,'bulk liquid',ha='center',fontsize=10);ax.text(-.94,.57,r'$g_{\parallel}$',color='#ab3f2f',fontsize=11);ax.set(xlim=(-1.28,1.28),ylim=(-.04,1.4),aspect='equal',xlabel=r'$y/h_{\rm max}$',ylabel=r'$z/h_{\rm max}$',title=r'Receding cross-section, $\alpha=\pi/4$');ax.spines[['top','right']].set_visible(False)
fig.savefig('paper-66-channel.png',dpi=130,facecolor='white',transparent=False)
