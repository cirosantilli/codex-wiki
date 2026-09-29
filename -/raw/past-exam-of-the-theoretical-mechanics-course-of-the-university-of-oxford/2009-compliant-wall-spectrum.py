"""Original mode-intersection figure. Python 3.14.4; numpy 2.3.5; matplotlib 3.10.7.
Run from output directory; dependencies in wiki pyproject.toml.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig,ax=plt.subplots(figsize=(8,5),constrained_layout=True)
for j in range(3):
    a=np.linspace(j*np.pi+.001,(j+.5)*np.pi-.001,300)
    b=np.linspace((j+.5)*np.pi+.001,(j+1)*np.pi-.001,300)
    ax.plot(a,-np.tan(a),color='black',lw=1.4)
    ax.plot(b,-np.tan(b),color='black',lw=1.4,label=r'$-\tan\beta$' if j==0 else None)
    ax.axvline((j+.5)*np.pi,color='#bbbbbb',ls=':',lw=.8)
beta=np.linspace(.02,3*np.pi,1000)
for n,col in [(0,'#2878aa'),(1,'#c07b22'),(2,'#4a8b50')]:
    ax.plot(beta,beta+(n*np.pi)**2/beta,color=col,lw=2,label=rf'$n={n}$: $\beta+n^2\pi^2/\beta$')
ax.set(xlim=(0,3*np.pi),ylim=(-2,46),xlabel=r'$\beta$',ylabel='dimensionless curve value',title=r'Compliant-wall real modes: $c_0^2/(kb)=1$, $b/a=1$')
ax.set_xticks([0,np.pi/2,np.pi,3*np.pi/2,2*np.pi,5*np.pi/2,3*np.pi],['0',r'$\pi/2$',r'$\pi$',r'$3\pi/2$',r'$2\pi$',r'$5\pi/2$',r'$3\pi$'])
ax.grid(alpha=.15);ax.legend(loc='upper right',fontsize=9)
fig.savefig('2009-compliant-wall-spectrum.png',dpi=150,facecolor='white')
