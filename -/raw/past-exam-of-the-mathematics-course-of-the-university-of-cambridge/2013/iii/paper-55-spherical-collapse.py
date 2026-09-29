"""Original spherical-collapse sketch. Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Writes one opaque PNG basename in the caller's cwd; does not alter MPLCONFIGDIR.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

theta=np.linspace(0,2*np.pi,1001)
x=(theta-np.sin(theta))/np.pi
y=(1-np.cos(theta))/2
fig,ax=plt.subplots(figsize=(8,4.8),dpi=100,facecolor='white')
ax.set_facecolor('white')
ax.plot(x,y,color='#173d73',linewidth=2.5,label='Pressureless overdense shell')
# Same enclosed mass evolving with the homogeneous EdS background.
background=0.5*(9*np.pi**2/2)**(1/3)*x**(2/3)
ax.plot(x,background,color='#777777',linewidth=1.6,linestyle='--',label='Homogeneous background, same mass')
ax.scatter([1,2],[1,0],color='#173d73',s=35,zorder=4)
ax.scatter([2],[.5],facecolor='white',edgecolor='#a74218',s=65,linewidth=2,zorder=5,label='Virialized radius at collapse epoch')
ax.annotate('Turnaround\u00a0(\u03b8 = \u03c0)',(1,1),xytext=(.32,1.25),arrowprops={'arrowstyle':'->','color':'#173d73'},fontsize=10)
ax.annotate('Formal collapse\u00a0(\u03b8 = 2\u03c0)',(2,0),xytext=(1.05,.13),arrowprops={'arrowstyle':'->','color':'#173d73'},fontsize=10)
ax.axhline(.5,color='#a74218',linewidth=1,linestyle=':',alpha=.8)
ax.set(xlim=(0,2.12),ylim=(-.05,2.95),xlabel=r'Time $t/t_{\rm max}$',ylabel=r'Radius $R/R_{\rm max}$',title='Spherical collapse and virialization')
ax.grid(alpha=.2);ax.legend(loc='upper left',fontsize=9,framealpha=1)
fig.tight_layout()
fig.savefig('paper-55-spherical-collapse.png',dpi=100,facecolor='white',transparent=False)
plt.close(fig)
