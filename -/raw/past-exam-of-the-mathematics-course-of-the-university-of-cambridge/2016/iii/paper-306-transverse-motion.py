"""Tilted string motion, using existing NumPy/Matplotlib dependencies.
Tested with Python 3.14.4. Writes only the basename PNG to the caller's cwd.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

k=2
fig,ax=plt.subplots(figsize=(7.2,3.6),dpi=100,facecolor='white')
fig.subplots_adjust(left=.09,right=.97,bottom=.15,top=.83)
x=np.linspace(-1.5,1.5,300)
ax.plot(x,k*x,color='#2166ac',label='String at t = 0')
ax.plot(x,k*x+k,ls='--',color='#2166ac',alpha=.6,label='String at t = 1')
origin=np.array([0.,0.]);coordinate=np.array([0.,k]);normal=np.array([-k*k,k])/(1+k*k)
for end,color,label,offset in [(coordinate,'#b2182b',r'Coordinate velocity: $|v|=2$',(.05,.1)),(normal,'#1b7837',r'Normal velocity: $|v_\perp|=2/\sqrt{5}$',(-.7,-.7))]:
 ax.annotate('',xy=end,xytext=origin,arrowprops=dict(arrowstyle='->',color=color,lw=2.5))
 ax.text(end[0]+offset[0],end[1]+offset[1],label,color=color,fontsize=10)
ax.plot([normal[0],coordinate[0]],[normal[1],coordinate[1]],color='#777777',ls=':',lw=1.2)
ax.set(xlim=(-1.9,2.5),ylim=(-1.4,3),xlabel=r'$X^1$',ylabel=r'$X^2$',aspect='equal')
ax.set_title('A moving tilted string: tangential label motion is removable',fontsize=12,pad=11)
ax.legend(loc='lower right',fontsize=9,framealpha=1)
fig.savefig('paper-306-transverse-motion.png',dpi=100,facecolor='white',transparent=False)
plt.close(fig)
