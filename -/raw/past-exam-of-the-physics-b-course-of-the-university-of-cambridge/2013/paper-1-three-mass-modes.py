"""Original mode vectors of a free spring chain and analytical frequency branches. Output cwd."""
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({"axes.titlesize":10,"axes.labelsize":10})
fig,ax=plt.subplots(1,2,figsize=(9,3.6),layout='constrained');a=ax[0]
for j,(v,label) in enumerate([(np.array([1,1,1]),'Translation'),(np.array([1,0,-1]),'Antisymmetric'),(np.array([1,-2,1]),'Symmetric internal')]):
 y=2-j;xx=np.array([-1.,0,1.]);a.scatter(xx,np.full(3,y),c='k',s=40);a.quiver(xx,np.full(3,y),.3*v,np.zeros(3),angles='xy',scale_units='xy',scale=1,color='#3569ac',width=.008);a.text(-1.5,y+.25,label,fontsize=9)
a.set(xlim=(-1.6,1.6),ylim=(-.4,2.6),title='Equal-mass displacement vectors');a.axis('off');alpha=np.geomspace(.1,10,400);a=ax[1];a.semilogx(alpha,np.zeros_like(alpha),label='Translation');a.semilogx(alpha,np.ones_like(alpha),label='Antisymmetric');a.semilogx(alpha,np.sqrt(1+2/alpha),label='Symmetric internal');a.set(xlabel='Middle / outer mass ratio alpha',ylabel=r'$\omega/\sqrt{k/m}$',title='Frequencies versus middle mass');a.legend(fontsize=8);a.grid(alpha=.2)
fig.savefig('paper-1-three-mass-modes.png',dpi=150,facecolor='white')
