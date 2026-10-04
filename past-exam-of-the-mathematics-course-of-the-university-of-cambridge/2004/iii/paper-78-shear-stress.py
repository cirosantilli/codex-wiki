"""Original constitutive curves; Python 3.14, root NumPy/Matplotlib.

Writes the matching PNG basename to caller CWD; respects MPLCONFIGDIR.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
x=np.linspace(0,10,900)
fig,ax=plt.subplots(figsize=(7.4,4.2),layout='constrained',facecolor='white')
for beta,color,style in [(.30,'#226b9c','-'),(.125,'#5b685f','--'),(.02,'#a74331','-')]:
    ax.plot(x,x*(beta+1/(1+x*x)),style,color=color,lw=1.9,label=fr'$b={beta:g}$')
    if beta<.125:
        z=np.array([1-2*beta-np.sqrt(1-8*beta),1-2*beta+np.sqrt(1-8*beta)])/(2*beta)
        turning=np.sqrt(z)
        ax.scatter(turning,turning*(beta+1/(1+turning*turning)),color=color,s=28)
ax.set(xlim=(0,10),ylim=(0,3.2),xlabel=r'Scaled shear rate $x=\tau\sqrt{1-\alpha^2}\,\dot\gamma$',ylabel=r'Scaled shear stress $S=x[b+(1+x^2)^{-1}]$',title='Johnson–Segalman shear-stress curves')
ax.legend(title=r'$b=\mu_0/(\alpha^2G_0\tau)$',loc='upper left')
ax.text(5.1,.65,'Decreasing segment for $b<1/8$',fontsize=10,color='#a74331')
ax.grid(alpha=.15);ax.set_facecolor('white')
fig.savefig('paper-78-shear-stress.png',dpi=130,facecolor='white',transparent=False)
plt.close(fig)
