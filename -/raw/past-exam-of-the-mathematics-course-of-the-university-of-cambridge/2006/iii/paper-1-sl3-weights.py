"""sl3 tensor decomposition weight diagrams; writes basename PNG to caller CWD.
Tested Python 3.14.4, matplotlib 3.10.7, numpy 2.3.5; preserves MPLCONFIGDIR.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
L=np.array([[1.,0.],[-.5,np.sqrt(3)/2],[-.5,-np.sqrt(3)/2]])
base=[(L[i],rf'$L_{i+1}$','L') for i in range(3)]
base +=[(-2*L[i],rf'$-2L_{i+1}$','dual') for i in range(3)]
base +=[(2*L[i]-L[k],rf'$2L_{i+1}-L_{k+1}$','outer') for i in range(3) for k in range(3) if i!=k]
patterns=[({'L':5,'dual':2,'outer':1},r'$Z=W\otimes W\otimes W^*$, dimension 27'),
          ({'L':2,'dual':1,'outer':1},r'$V(2\omega_1+\omega_2)$, dimension 15'),
          ({'L':1,'dual':1},r'$V(2\omega_2)$, dimension 6'),
          ({'L':1},r'$W$: first defining copy, dimension 3'),
          ({'L':1},r'$W$: second defining copy, dimension 3')]
fig,axs=plt.subplots(2,3,figsize=(12,8.6),layout='constrained')
for ax,(pattern,title) in zip(axs.flat,patterns):
    pts=[(p,label,pattern[kind]) for p,label,kind in base if kind in pattern]
    for j,(p,_,_) in enumerate(pts):
        for q,_,_ in pts[j+1:]:
            if np.isclose(np.linalg.norm(p-q),np.sqrt(3)):
                ax.plot([p[0],q[0]],[p[1],q[1]],color='#bdcbd5',lw=.7,zorder=1)
    for p,label,mult in pts:
        ax.scatter([p[0]],[p[1]],s=250,color='white',edgecolors='#176fac',linewidths=1.8,zorder=2)
        ax.text(*p,str(mult),ha='center',va='center',fontsize=11,zorder=3)
        offset=(0,13 if p[1]>=0 else -22)
        ax.annotate(label,p,xytext=offset,textcoords='offset points',ha='center',fontsize=8.5)
    ax.set_title(title,fontsize=11)
    ax.set_aspect('equal');ax.set_xlim(-3.45,3.45);ax.set_ylim(-3.35,3.65)
    ax.set_xticks([]);ax.set_yticks([])
    for spine in ax.spines.values():spine.set_visible(False)
key=axs.flat[5];key.axis('off')
key.text(.05,.90,'Coordinates and notation',fontsize=14,weight='bold',va='top')
key.text(.05,.78,r'$L_1=(1,0)$'+'\n'+r'$L_2=(-1/2,\sqrt{3}/2)$'+'\n'+r'$L_3=(-1/2,-\sqrt{3}/2)$',fontsize=12,linespacing=1.7,va='top')
key.text(.05,.40,'Number inside a point = multiplicity\nFaint edges join weights differing\nby a root; they do not encode\noperator coefficients.',fontsize=11,linespacing=1.6,va='top')
fig.suptitle('The tensor product and all four irreducible summands',fontsize=16)
fig.savefig('paper-1-sl3-weights.png',dpi=140,facecolor='white',transparent=False)
plt.close(fig)
