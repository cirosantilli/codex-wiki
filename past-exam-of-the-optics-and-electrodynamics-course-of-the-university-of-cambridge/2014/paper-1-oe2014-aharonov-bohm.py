"""Original educational diagram. Python 3.14, NumPy and Matplotlib; writes a PNG basename in the current working directory."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white'})
from matplotlib.patches import Circle
fig,axs=plt.subplots(1,2,figsize=(8.8,3.5),layout='constrained')
x=np.linspace(-2.8,2.8,300);y=.95*(1-(x/2.8)**2)
for s,col in [(1,'#225c91'),(-1,'#b25424')]:
 axs[0].plot(x,s*y,color=col,lw=2)
 axs[0].annotate('',xy=(1.9,s*.95*(1-(1.9/2.8)**2)),xytext=(1.65,s*.95*(1-(1.65/2.8)**2)),arrowprops={'arrowstyle':'->','color':col,'lw':2})
axs[0].add_patch(Circle((0,0),.43,facecolor='#e8e8e8',edgecolor='black',hatch='xx'))
axs[0].scatter([-2.8,2.8],[0,0],color='black');axs[0].text(-2.8,-.45,'Split',ha='center');axs[0].text(2.8,-.45,'Recombine',ha='center')
axs[0].text(0,0,r'$\Phi_B$',ha='center',va='center',bbox={'facecolor':'white','edgecolor':'none','pad':1})
axs[0].text(0,-1.45,r'Paths avoid the confined field; $\Delta\phi=q\Phi_B/\hbar$',ha='center')
axs[0].set(xlim=(-3.1,3.1),ylim=(-1.7,1.65),aspect='equal',title='Conceptual two-path geometry');axs[0].axis('off')
u=np.linspace(-1.5,1.5,1000);axs[1].plot(u,1+np.cos(2*np.pi*u),label='Zero flux',color='#225c91');axs[1].plot(u,1+np.cos(2*np.pi*u-np.pi),label=r'$\Phi_B=h/(2e)$',color='#b25424',ls='--')
axs[1].set(xlabel='Screen position / fringe period',ylabel='Normalized intensity',ylim=(-.1,2.4),title='Half-period flux-induced fringe shift');axs[1].legend(fontsize=9);axs[1].grid(alpha=.2)
fig.savefig('paper-1-oe2014-aharonov-bohm.png',dpi=150,facecolor='white');plt.close(fig)
