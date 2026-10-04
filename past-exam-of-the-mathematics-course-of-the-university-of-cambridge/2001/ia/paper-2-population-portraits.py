"""Representative logistic predator-prey portraits, Python3.14/root numpy+matplotlib.

Each trajectory uses RK4. Output basename to caller CWD; respects MPLCONFIGDIR.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def field(z,b):
    p,h=z
    return np.array([p*(1-p-h),h*(p/b-1)/8])

def trajectory(z,b,dt=.025,steps=7200):
    vals=[np.array(z,dtype=float)]
    for _ in range(steps):
        v=vals[-1];k1=field(v,b);k2=field(v+.5*dt*k1,b);k3=field(v+.5*dt*k2,b);k4=field(v+dt*k3,b)
        nxt=v+dt*(k1+2*k2+2*k3+k4)/6
        if not np.all(np.isfinite(nxt)) or np.min(nxt)<0:raise RuntimeError('invalid population integration')
        vals.append(nxt)
    return np.array(vals)

fig,axes=plt.subplots(1,2,figsize=(10,4.25),facecolor='white')
starts=[(.07,.15),(.12,1.5),(.85,.15),(1.7,.12),(1.55,1.05)]
for ax,b,title in zip(axes,[.25,1.5],['b = 0.25: stable coexistence','b = 1.5: hunters die out']):
    pp,hh=np.meshgrid(np.linspace(.045,1.92,17),np.linspace(.035,1.77,16))
    dp=pp*(1-pp-hh);dh=hh*(pp/b-1)/8;norm=np.hypot(dp,dh)
    ax.quiver(pp,hh,dp/norm,dh/norm,color='#aaaaaa',alpha=.7,angles='xy',scale_units='xy',scale=18,width=.0026)
    for start in starts:
        vals=trajectory(start,b)
        ax.plot(vals[:,0],vals[:,1],lw=1.3,alpha=.88)
        # An early arrow gives trajectory direction without hiding the equilibrium.
        j=100;k=125
        ax.annotate('',xy=vals[k],xytext=vals[j],arrowprops={'arrowstyle':'->','color':'#224466','lw':1.1})
    u=np.linspace(0,1,150);ax.plot(u,1-u,color='#333333',ls='--',lw=1,label='prey nullcline')
    ax.axvline(b,color='#855c1b',ls=':',lw=1,label='hunter nullcline')
    saddles=[(0,0)]+([(1,0)] if b<1 else [])
    for p,h in saddles:ax.scatter([p],[h],s=32,facecolors='white',edgecolors='black',zorder=6,clip_on=False)
    eq=(b,1-b) if b<1 else (1,0)
    ax.scatter([eq[0]],[eq[1]],s=45,color='black',zorder=7,clip_on=False)
    ax.annotate('attractor',xy=eq,xytext=(.52,1.18) if b<1 else (1.15,.35),arrowprops={'arrowstyle':'->'},fontsize=9)
    ax.set(xlim=(0,2),ylim=(0,1.85),xlabel='prey p',ylabel='hunters h',title=title)
    ax.spines[['top','right']].set_visible(False)
axes[1].legend(loc='upper right',frameon=False,fontsize=8)
fig.tight_layout(w_pad=2);fig.savefig(Path.cwd()/'paper-2-population-portraits.png',dpi=150,facecolor='white',transparent=False);plt.close(fig)
