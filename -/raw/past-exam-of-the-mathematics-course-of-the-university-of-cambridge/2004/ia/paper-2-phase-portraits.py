"""Original conservative phase portraits; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Writes an opaque PNG basename in caller CWD and honors caller MPLCONFIGDIR.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig,axes=plt.subplots(1,3,figsize=(12,4.3),layout='constrained',facecolor='white')
configs=[('Pendulum: ẍ + cos x = 0',(np.pi/2-.9,5*np.pi/2+.9),(-2.8,2.8),None),('Quartic: λ = 1',(-2.1,1.65),(-2.8,2.8),1),('Quartic: λ = 5/2',(-2.95,.85),(-1.7,1.7),2.5)]
for ax,(title,xlim,vlim,lam) in zip(axes,configs):
    x=np.linspace(*xlim,800)
    v=np.linspace(*vlim,650)
    X,V=np.meshgrid(x,v)
    pot=lambda x: np.sin(x) if lam is None else x**4/4+lam*x**3/3+x*x/2
    force=lambda x:-np.cos(x) if lam is None else -x*(x*x+lam*x+1)
    h=V*V/2+pot(X)
    levels=[-.7,-.2,.4,.8,1.5,2.4] if lam is None else ([.12,.4,.85,1.65,2.7] if lam==1 else [-.6,-.35,-.08,.012,.025,.09,.28,.58])
    ax.contour(X,V,h,levels=levels,colors='#3876a2',linewidths=.85)
    ax.set(xlim=xlim,ylim=vlim,xlabel='x',ylabel='v = ẋ',title=title)
    ax.axhline(0,color='0.65',lw=.65)
    ax.grid(alpha=.13)
    xx,vv=np.meshgrid(np.linspace(*xlim,16),np.linspace(*vlim,15))
    ff=force(xx)
    nn=np.hypot(vv,ff)
    good=nn>1e-8
    ax.quiver(xx[good],vv[good],(vv/np.maximum(nn,1e-8))[good],(ff/np.maximum(nn,1e-8))[good],angles='xy',scale_units='xy',scale=8,color='0.45',width=.0028)
    if lam is None:
        saddles=np.array([np.pi/2,5*np.pi/2]);centers=[3*np.pi/2]
        # Exact saddle and center knots ensure zero separatrix velocity at saddles.
        sx=np.unique(np.r_[x,saddles,centers])
        speed=np.sqrt(np.maximum(2*(1-np.sin(sx)),0))
        for sign in [-1,1]:ax.plot(sx,sign*speed,color='#b84628',lw=1.6)
    elif lam==1:
        saddles=[];centers=[0]
    else:
        saddles=[-.5];centers=[-2,0]
        left,right=(-7-np.sqrt(70))/6,(-7+np.sqrt(70))/6
        hs=7/192
        for lo,hi in [(left,-.5),(-.5,right)]:
            sx=np.unique(np.r_[np.linspace(lo,hi,700),lo,hi])
            speed=np.sqrt(np.maximum(2*(hs-pot(sx)),0))
            speed[[0,-1]]=0  # Exact turning point and saddle values.
            for sign in [-1,1]:ax.plot(sx,sign*speed,color='#b84628',lw=1.6)
    ax.scatter(centers,np.zeros(len(centers)),s=38,c='#1668a7',zorder=6,label='Center')
    if len(saddles):ax.scatter(saddles,np.zeros(len(saddles)),s=40,c='#b84628',marker='x',zorder=6,label='Saddle')
    ax.legend(fontsize=8,loc='lower left')
fig.savefig('paper-2-phase-portraits.png',dpi=130,facecolor='white',transparent=False)
plt.close(fig)
