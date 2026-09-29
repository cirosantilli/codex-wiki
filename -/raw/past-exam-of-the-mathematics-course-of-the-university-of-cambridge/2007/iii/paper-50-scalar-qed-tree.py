"""Original tree diagrams. Python 3.14, Matplotlib/NumPy from root pyproject.
Emits opaque PNG basename to caller CWD, honoring supplied MPLCONFIGDIR.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def directed(ax, start, end, reverse=False):
    p=np.array(start,dtype=float);q=np.array(end,dtype=float)
    ax.plot([p[0],q[0]],[p[1],q[1]],color='#222222',lw=1.7)
    if reverse:p,q=q,p
    middle=(p+q)/2;direction=(q-p)/np.linalg.norm(q-p)
    ax.annotate('',xy=middle+.14*direction,xytext=middle-.14*direction,
                arrowprops={'arrowstyle':'->','color':'#222222','lw':1.5,'shrinkA':0,'shrinkB':0})


def internal(ax,p,q,photon):
    p=np.array(p);q=np.array(q);s=np.linspace(0,1,220)
    if photon:
        normal=np.array([-(q-p)[1],(q-p)[0]])/np.linalg.norm(q-p)
        xy=p[None,:]+s[:,None]*(q-p)[None,:]+.07*np.sin(10*np.pi*s)[:,None]*normal[None,:]
        ax.plot(xy[:,0],xy[:,1],color='#2166ac',lw=1.6)
    else:ax.plot([p[0],q[0]],[p[1],q[1]],color='#a65b12',ls='--',lw=1.7)


def panel(ax,channel,anti=False,photon=False):
    left=[(-2.25,1.15),(-2.25,-1.15)];right=[(2.25,1.15),(2.25,-1.15)]
    if channel=='s':
        v1=(-.8,0);v2=(.8,0)
        directed(ax,left[0],v1);directed(ax,left[1],v1,reverse=anti)
        directed(ax,v2,right[0]);directed(ax,v2,right[1],reverse=anti)
        internal(ax,v1,v2,photon)
        ax.text(0,.21,r'$k=p+q$',ha='center',fontsize=11)
    else:
        v1=(0,.65);v2=(0,-.65)
        directed(ax,left[0],v1);directed(ax,left[1],v2,reverse=anti)
        if channel=='u':
            directed(ax,v1,right[1]);directed(ax,v2,right[0])
        else:
            directed(ax,v1,right[0]);directed(ax,v2,right[1],reverse=anti)
        internal(ax,v1,v2,photon)
        ax.text(.17,0,r"$k=p-p'$" if channel=='t' else r"$k=p-q'$",ha='left',fontsize=11)
    for v in [v1,v2]:ax.plot(v[0],v[1],'o',color='black',ms=4)
    part=r'\varphi' if photon else r'\psi'
    antipart=r'\bar\varphi' if photon else r'\bar\psi'
    labels=[f'${part}(p)$',f'${antipart if anti else part}(q)$',f"${part}(p')$",f"${antipart if anti else part}(q')$"]
    for (x,y),lab in zip(left+right,labels):
        ax.text(x,y+(0.16 if y>0 else -.16),lab,ha='center',va='bottom' if y>0 else 'top',fontsize=12)
    ax.set_xlim(-3.15,3.15);ax.set_ylim(-1.8,1.8);ax.set_aspect('equal');ax.axis('off')

fig,axes=plt.subplots(1,2,figsize=(9.0,3.5),layout='constrained',facecolor='white')
for ax,channel,title in zip(axes,['t','s'],['Scalar particle–antiparticle: t channel','Scalar particle–antiparticle: s channel']):
    panel(ax,channel,anti=True,photon=True)
    ax.set_title(title,fontsize=12)
fig.supxlabel('Incoming on left, outgoing on right. Solid arrows show charge flow; wavy lines are photons.',fontsize=10)
fig.savefig('paper-50-scalar-qed-tree.png',dpi=150,facecolor='white',transparent=False)
plt.close(fig)
