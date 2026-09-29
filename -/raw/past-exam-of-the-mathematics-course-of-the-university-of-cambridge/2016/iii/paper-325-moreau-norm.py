import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":10,"axes.spines.top":False,"axes.spines.right":False})
x=np.linspace(-3,3,900);r=abs(x);env=np.where(r<=1,x*x/2,r-.5);grad=np.clip(x,-1,1)
fig,axes=plt.subplots(1,2,figsize=(7.6,3.6),dpi=100)
axes[0].plot(x,r,label=r'$|x|$',color='gray',lw=2);axes[0].plot(x,env,label=r'$f_1(x)$',lw=2,color='tab:blue')
axes[0].set(xlabel='x',ylabel='Function value',title='Quadratic smoothing of the norm');axes[0].legend()
axes[1].plot(x,grad,color='tab:blue',lw=2,label=r'$\nabla f_1(x)$')
for a,b,y in [(-3,0,-1),(0,3,1)]:axes[1].plot([a,b],[y,y],color='gray',ls='--',lw=1.5)
axes[1].set(xlabel='x',ylabel='Gradient',ylim=(-1.3,1.3),title='A continuous, Lipschitz gradient');axes[1].legend()
for ax in axes:
 ax.axhline(0,color='gray',lw=.5);ax.axvline(0,color='gray',lw=.5)
 for z in [-1,1]:ax.axvline(z,color='gray',ls=':',alpha=.5)
 ax.grid(alpha=.15)
fig.tight_layout();fig.savefig('paper-325-moreau-norm.png',facecolor='white',transparent=False)
