from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 11, "figure.facecolor": "white", "axes.facecolor": "white"})

# Each line segment is plotted separately; slope jumps are not joined.
def h(v):
    return np.where(np.abs(v)<=1,np.sin(np.pi*v),0.)
fig,axs=plt.subplots(2,2,figsize=(10.2,6.5),constrained_layout=True)
color='#2166ac'
for row,s in enumerate([.5,1.]):
    u=np.linspace(-3,3,6001)
    axs[row,0].plot(u,(h(u-s)+h(u+s))/2,color=color,lw=1.8)
    axs[row,0].set(ylabel='Displacement y',ylim=(-.6,.6),title=rf'$x/(ca)={s:g}$: displacement')
    if s==.5:
        pieces=[(-3,-1.5,lambda v:np.zeros_like(v)),
                (-1.5,-.5,lambda v:-np.pi/2*np.sin(np.pi*v)),
                (-.5,.5,lambda v:-np.pi*np.sin(np.pi*v)),
                (.5,1.5,lambda v:-np.pi/2*np.sin(np.pi*v)),
                (1.5,3,lambda v:np.zeros_like(v))]
        for ax in axs[row]: ax.axvspan(-.5,.5,color='#fddbc7',alpha=.5)
        axs[row,0].text(0,.43,'overlap: y = 0',ha='center',fontsize=9)
    else:
        pieces=[(-3,-2,lambda v:np.zeros_like(v)),
                (-2,0,lambda v:-np.pi/2*np.cos(np.pi*v)),
                (0,2,lambda v:np.pi/2*np.cos(np.pi*v)),
                (2,3,lambda v:np.zeros_like(v))]
    ax=axs[row,1]
    for lo,hi,fun in pieces:
        v=np.linspace(lo,hi,401)
        ax.plot(v,fun(v),color=color,lw=1.7)
        for edge in [lo,hi]:
            if -3<edge<3: ax.plot(edge,fun(np.array([edge]))[0],'o',mfc='white',mec=color,ms=5,zorder=5)
    if s==1:
        ax.plot(0,0,'o',color='#b2182b',ms=5,zorder=6)
        ax.annotate('value at t = 0',(0,0),(.22,.65),arrowprops={'arrowstyle':'->'},fontsize=9)
    ax.set(ylabel=r'Scaled slope $ca\,y_x$',ylim=(-3.55,3.55),title=rf'$x/(ca)={s:g}$: spatial slope')
for ax in axs.flat:
    ax.axhline(0,color='.6',lw=.7,zorder=0);ax.set(xlim=(-3,3),xlabel=r'$t/a$');ax.grid(alpha=.16)
fig.suptitle('Incoming and outgoing sine windows\nOpen circles show one-sided limits, filled point an exceptional defined value',fontsize=12)
fig.savefig(Path(__file__).with_suffix('.png').name,dpi=140,facecolor='white')
