"""Original reconstructed gamma-level solutions, Python 3.14."""
import numpy as np
import matplotlib.pyplot as plt
energies=np.array([133.02,136.25,345.85,482.0,615.5]);sigma=np.array([.02,.02,.2,.2,.5])
graphs=[[(1,0),(2,1),(3,2),(3,1),(3,0)],[(1,0),(3,2),(2,1),(3,1),(3,0)],[(3,2),(1,0),(2,1),(2,0),(3,0)],[(3,2),(2,1),(1,0),(2,0),(3,0)]]
fig,axes=plt.subplots(2,2,figsize=(10,7),layout='constrained')
colors=['#2158a0','#397c49','#8c4ba3','#b66a0d','#bd332e']
for name,edges,ax in zip(['I','II','III','IV'],graphs,axes.flat):
    M=np.zeros((5,3))
    for j,(u,v) in enumerate(edges):
        M[j,u-1]=1
        if v:M[j,v-1]=-1
    levels=np.r_[0,np.linalg.lstsq(M/sigma[:,None],energies/sigma,rcond=None)[0]]
    for label,E in zip('ABCD',levels):
        ax.hlines(E,.2,5.8,color='.6',lw=.9)
        ax.text(5.9,E,f'{label}: {E:.2f}',va='center',fontsize=9)
    for j,((u,v),col) in enumerate(zip(edges,colors)):
        xpos=.7+j*1.05
        ax.annotate('',xy=(xpos,levels[v]+3),xytext=(xpos,levels[u]-3),arrowprops={'arrowstyle':'-|>','color':col,'lw':1.5 if j<4 else .9})
        ax.text(xpos+.10,(levels[u]+levels[v])/2,str(j+1),color=col,fontsize=10,fontweight='bold')
    ax.set(title='Arrangement '+name,xlim=(0,7.3),ylim=(-35,665),ylabel='Excitation energy (keV)')
    ax.set_xticks([]);ax.spines[['top','right','bottom']].set_visible(False)
fig.suptitle('Calculated alternatives; arrow labels are spectral-line numbers',fontsize=13)
fig.savefig('paper-1-four-level-arrangements.png',dpi=155,facecolor='white')
