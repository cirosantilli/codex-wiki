"""Adjoint A2 weights. Output paper-1-adjoint.png to caller CWD only.
Tested: Python 3.14.4, matplotlib 3.10.7, numpy 2.3.5.
The caller's MPLCONFIGDIR is unchanged; dependencies are root pyproject entries.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
L=np.array([[1.,0.],[-.5,np.sqrt(3)/2],[-.5,-np.sqrt(3)/2]])
fig,ax=plt.subplots(figsize=(8,6.4),layout='constrained')
colors=['#176fac','#d17820','#5b8c3c','#777777']
groups=[[(0,1),(1,0)],[(0,2),(1,2)],[(2,1),(2,0)]]
labels=[r'$\Gamma_2$: adjoint triple',r'$\Gamma_1$: first doublet',r'$\Gamma_1$: second doublet']
for k,group in enumerate(groups):
    pts=np.array([L[i]-L[j] for i,j in group])
    if k==0:pts=np.vstack((pts[0],np.zeros(2),pts[1]))
    ax.plot(pts[:,0],pts[:,1],'-',color=colors[k],lw=2,alpha=.7)
    ax.scatter(pts[:,0],pts[:,1],s=150,color=colors[k],label=labels[k],zorder=3)
    for i,j in group:
        p=L[i]-L[j]
        ax.annotate(rf'$L_{i+1}-L_{j+1}$'+'\n'+rf'$E_{{{i+1}{j+1}}}$',p,
                    xytext=(7,10 if p[1]>=0 else -32),textcoords='offset points',fontsize=11)
ax.scatter([0],[0],s=40,color=colors[3],label=r'$\Gamma_0$: trivial line',zorder=4)
ax.annotate(r'$0$ (multiplicity $2$)'+'\n'+r'$H_{12}\in\Gamma_2$'+'\n'+r'$\mathrm{diag}(1,1,-2)\in\Gamma_0$',(0,0),xytext=(12,-18),textcoords='offset points',fontsize=11)
ax.set_aspect('equal');ax.set_xlim(-2.2,2.2);ax.set_ylim(-2.3,2.4)
ax.set_xticks([]);ax.set_yticks([])
ax.set_title(r'Adjoint $\mathfrak{sl}_3$ restricted to $\mathfrak{s}_{L_1-L_2}$',fontsize=16)
ax.legend(loc='upper left',fontsize=10,framealpha=.95)
for spine in ax.spines.values():spine.set_visible(False)
fig.savefig('paper-1-adjoint.png',dpi=140,facecolor='white',transparent=False)
plt.close(fig)
