"""Original generic bond pulling and illustrative dimensionless predictions."""
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':9,'axes.titlesize':10})
fig,axs=plt.subplots(1,3,figsize=(12,3.8),layout='constrained');ax=axs[0]
ax.plot([0,1],[3,3],color='black',lw=4);ax.plot([.9,1.2],[3,2.75],color='black',lw=2);ax.plot([1.2,1.2],[2.75,2],color='#2166ac',lw=2);ax.plot([1.2,1.2],[1.8,.7],color='black',lw=2);ax.plot([.5,1.9],[.7,.7],color='grey',lw=5);ax.plot(1.2,1.9,'o',color='#b2182b',ms=8);ax.annotate('',xy=(1.9,.9),xytext=(1.9,1.5),arrowprops={'arrowstyle':'->'});ax.text(.1,3.23,'Calibrated cantilever');ax.text(.02,1.15,'Generic link');ax.text(.55,.35,'Stage retreats');ax.set(xlim=(-.1,2.2),ylim=(.2,3.7),title='Generic pulling geometry');ax.axis('off')
x=np.linspace(-.35,3.35,600);G=10*(x*(x-3)/2.25)**2
axs[1].plot(x,G,label=r'$G_0(x)$',lw=2);axs[1].plot(x,G-1.5*x,label=r'$G_0(x)-Fx$',lw=2);axs[1].scatter([0,1.5,3],[0,10,0],s=16,color='black');axs[1].text(-.2,1,'Initial');axs[1].text(1.25,10.6,'Saddle');axs[1].text(2.6,1,'Escaped');axs[1].set(xlabel='Reaction coordinate (chosen units)',ylabel='Free energy (chosen units)',ylim=(-6,13),title='Illustrative landscape tilt');axs[1].legend(fontsize=8)
u=np.linspace(0,5.5,800)
for rho in [.1,1,10]:axs[2].plot(u,np.exp(-np.expm1(u)/rho),lw=2,label=rf'$f/(k_0F_0)={rho:g}$')
axs[2].axhline(.5,color='grey',ls=':');axs[2].set(xlabel=r'$F/F_0$',ylabel='Survival probability',title='Rate-dependent survival',ylim=(0,1.04));axs[2].legend(fontsize=8);axs[2].grid(alpha=.2)
fig.savefig('paper-1-generic-force-ramp.png',dpi=170,facecolor='white');plt.close(fig)
