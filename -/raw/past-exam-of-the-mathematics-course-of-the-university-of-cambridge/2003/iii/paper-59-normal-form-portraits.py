"""Original phase portraits; numpy/matplotlib, Python 3.14.
The displayed coordinates scale x by sqrt(abs(mu2)) and y by abs(mu2).
Only the PNG basename is written in the caller's working directory.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def field(p,c,sign=1):
    x,y=p
    return np.array([y,-sign*x+x**3+.2*(c-x*x)*y])

def integrate(p,c,steps=38000,dt=.014):
    p=np.array(p,dtype=float);points=[]
    for j in range(steps):
        k1=field(p,c);k2=field(p+dt*k1/2,c)
        k3=field(p+dt*k2/2,c);k4=field(p+dt*k3,c)
        p+=dt*(k1+2*k2+2*k3+k4)/6
        if np.max(np.abs(p))>3:break
        if j>steps-2500:points.append(p.copy())
    return np.array(points)

fig,axes=plt.subplots(2,2,figsize=(9,6.7),constrained_layout=True)
xx=np.linspace(-1.6,1.6,95);yy=np.linspace(-1.25,1.25,80)
X,Y=np.meshgrid(xx,yy)
settings=[(0,-1,r'$\mu_2<0$: saddle'),(-.14,1,r'$\mu_2>0,\ \mu_1<0$: attracting origin'),(.08,1,r'$0<\mu_1<h(\mu_2)$: attracting cycle'),(.38,1,r'$\mu_1>h(\mu_2)$: open escape channels')]
for ax,(c,sign,title) in zip(axes.flat,settings):
    V=-sign*X+X**3+.2*(c-X**2)*Y
    scale=1+np.hypot(Y,V)
    ax.streamplot(xx,yy,Y/scale,V/scale,density=.8,color='#8996a3',linewidth=.65,arrowsize=.8)
    if sign>0:
        ax.plot([-1,1],[0,0],'kx',ms=7,mew=1.5)
        ax.plot(0,0,'o',color='#0068a3' if c<0 else '#d44825',ms=5)
        if 0<c<.2:
            cycle=integrate([.13,0],c)
            if len(cycle):ax.plot(cycle[:,0],cycle[:,1],color='#0068a3',lw=2,label='stable cycle')
    else:ax.plot(0,0,'kx',ms=7,mew=1.5)
    ax.axhline(0,color='black',alpha=.15,lw=.5)
    ax.axvline(0,color='black',alpha=.15,lw=.5)
    ax.set(xlabel='scaled x',ylabel='scaled y',title=title,xlim=(-1.6,1.6),ylim=(-1.25,1.25))
    ax.spines[['top','right']].set_visible(False)
fig.suptitle('The supplied cubic normal form (not the printed spherical vector field)',fontsize=11)
fig.savefig('paper-59-normal-form-portraits.png',dpi=120,facecolor='white')
plt.close(fig)
