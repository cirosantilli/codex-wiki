"""Original conformal-geodesic plot. Python 3.14; root NumPy/Matplotlib deps.
Writes its opaque PNG basename to caller CWD. Honors caller MPLCONFIGDIR.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def compact(t, r):
    p=np.arctan(t-r)
    q=np.arctan(t+r)
    return q-p, q+p


s=np.linspace(-np.pi/2+1e-4,np.pi/2-1e-4,2200)
parameter=np.tan(s)
fig,ax=plt.subplots(figsize=(6.4,6.8),layout='constrained',facecolor='white')
ax.plot([0,np.pi,0],[-np.pi,0,np.pi],color='#222222',lw=1.7)
ax.plot([0,0],[-np.pi,np.pi],color='#555555',lw=1.0)
R,T=compact(parameter,abs(.4*parameter+1.0))
ax.plot(R,T,color='#2166ac',lw=2,label='Timelike inertial geodesic')
R,T=compact(parameter,abs(parameter+1.0))
ax.plot(R,T,color='#b2182b',lw=2,label='Complete radial null geodesic')
R,T=compact(.3*parameter+.7,abs(parameter))
ax.plot(R,T,color='#4d9221',lw=1.9,ls='--',label='Spacelike geodesic')
for X,Y,label,dx,dy in [(0,np.pi,r'$i^+$',-.12,.18),(0,-np.pi,r'$i^-$',-.12,-.25),(np.pi,0,r'$i^0$',.24,.02)]:
    ax.plot(X,Y,'ko',ms=4)
    ax.text(X+dx,Y+dy,label,fontsize=15,ha='center',va='center')
ax.text(1.77,1.73,r'$\mathcal{I}^+$',fontsize=16,rotation=-45,ha='center')
ax.text(1.77,-1.73,r'$\mathcal{I}^-$',fontsize=16,rotation=45,ha='center')
ax.text(-.22,0,r'$R=0$'+'\nordinary centre',fontsize=10,rotation=90,ha='center',va='center')
ax.text(2.08,-2.6,'Interior: physical Minkowski region\n'+r'$R\geq0,\quad |T|+R<\pi$',ha='center',fontsize=9)
ax.set_xlim(-.55,np.pi+.5)
ax.set_ylim(-np.pi-.5,np.pi+.48)
ax.set_aspect('equal')
ax.set_xlabel('Compactified radial coordinate '+r'$R$')
ax.set_ylabel('Compactified time '+r'$T$')
ax.set_xticks([0,np.pi/2,np.pi],['0',r'$\pi/2$',r'$\pi$'])
ax.set_yticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi],[r'$-\pi$',r'$-\pi/2$','0',r'$\pi/2$',r'$\pi$'])
ax.spines[['top','right']].set_visible(False)
ax.set_title('Minkowski conformal compactification',fontsize=13)
ax.legend(loc='upper right',bbox_to_anchor=(1.12,1.02),framealpha=1,fontsize=8)
fig.supxlabel('Curves are images of physical straight geodesics. Only null geodesic\npaths are conformally preserved; the boundary is at physical infinity.',fontsize=9)
fig.savefig('paper-61-conformal-geodesics.png',dpi=150,facecolor='white',transparent=False)
plt.close(fig)
