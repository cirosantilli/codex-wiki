"""Original potential contours; Python 3.14 and root NumPy/Matplotlib.

Writes paper-68-effective-potentials.png to caller CWD. Honors MPLCONFIGDIR.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

r=np.linspace(.16,3.5,550);z=np.linspace(-2.2,2.2,550)
R,Z=np.meshgrid(r,z);grav=-1/np.hypot(R,Z)
fig,axes=plt.subplots(1,2,figsize=(9,4.7),facecolor='white',layout='constrained')
for ax,V,levels,title,name in zip(axes,[grav+.5/R**2,grav-.5*R**2],
        [[-.49,-.46,-.4,-.32,-.22,0,.5],[-3.,-2.4,-1.9,-1.65,-1.5,-1.35,-1.15,-.9]],
        [r'Fixed angular momentum: $\Phi_1$',r'Fixed angular velocity: $\Phi_2$'],['minimum','saddle']):
    ax.set_facecolor('white')
    contours=ax.contour(R,Z,V,levels=levels,colors='#1d6ba0',linewidths=1.15)
    ax.clabel(contours,inline=True,fontsize=8,fmt='%g')
    ax.scatter([1],[0],color='#af3b30',s=25,zorder=5)
    ax.annotate(name,xy=(1,0),xytext=(1.68,.26),fontsize=10,
        arrowprops={'arrowstyle':'->','color':'#af3b30'},color='#af3b30')
    ax.axhline(0,color='#aaaaaa',lw=.65,zorder=0)
    ax.set(xlim=(.16,3.5),ylim=(-2.2,2.2),xlabel=r'Normalized cylindrical radius $r$',ylabel=r'Normalized height $z$',title=title)
    ax.set_aspect('equal')
fig.suptitle('Point-mass effective potentials in a meridional plane',fontsize=13)
fig.savefig('paper-68-effective-potentials.png',dpi=130,facecolor='white',transparent=False)
plt.close(fig)
