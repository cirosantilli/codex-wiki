"""Original local velocity comparison at R=8mu. Python 3.14; numpy, matplotlib."""
import numpy as np
import matplotlib.pyplot as plt
u=1/np.sqrt(6);w=.5;g=1/np.sqrt(1-u*u)
fig,ax=plt.subplots(1,2,figsize=(9,4.6),layout='constrained',facecolor='white')
def arrow(axis,x,y,color,label,tx,ty):
 axis.annotate('',xy=(x,y),xytext=(0,0),arrowprops=dict(arrowstyle='->',lw=2.5,color=color));axis.text(tx,ty,label,color=color,fontsize=10)
arrow(ax[0],0,u,'#cc6e25',r'Bob: $u/c=0.408$',.025,.32)
arrow(ax[0],-w,0,'#166b9d',r'Carol: $w/c=0.500$',-.59,-.09)
arrow(ax[1],-w/g,-u,'#166b9d',r'Carol: $v/c=0.612$',-.57,-.52)
ax[1].plot([-w/g,-w/g,0],[0,-u,-u],'--',color='.45')
ax[1].text(-.56,.05,r'$-w/(c\gamma_u)=-0.456$',fontsize=9)
ax[1].text(.03,-.30,r'$-u/c=-0.408$',fontsize=9)
for x,title in zip(ax,["Alice's static frame","Bob's instantaneous rest frame"]):
 x.axhline(0,color='.7',lw=.7);x.axvline(0,color='.7',lw=.7);x.set(xlim=(-.65,.47),ylim=(-.65,.57),xlabel='Outward radial velocity / c',ylabel='Tangential velocity / c',title=title,aspect='equal');x.grid(alpha=.15)
fig.suptitle(r'Local comparison at $R=8\mu$: perpendicular velocities require a Lorentz boost',fontsize=11)
fig.savefig('paper-1-local-relative-velocities.png',dpi=150,facecolor='white')
