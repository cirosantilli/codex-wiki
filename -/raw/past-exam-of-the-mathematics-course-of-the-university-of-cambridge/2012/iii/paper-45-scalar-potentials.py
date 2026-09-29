"""Real potential slices. Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7+dfsg1.
Writes only paper-45-scalar-potentials.png to cwd; honors caller MPLCONFIGDIR.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, axes=plt.subplots(2,2,figsize=(10.4,6.6),dpi=100,facecolor='white')
blue='#235c91';green='#23734e';orange='#aa501c'
x=np.linspace(-1.35,.35,900);ax=axes[0,0]
ax.plot(x,x*x*(1+x)**2,color=blue,lw=2)
ax.scatter([-1,0],[0,0],color=green,zorder=4)
ax.scatter([-.5],[1/16],color=orange,zorder=4)
ax.annotate('barrier = 1/16',(-.5,1/16),(-.42,.115),fontsize=9,arrowprops={'arrowstyle':'->','color':orange})
ax.set(title=r'Two vacua: $M=1,\ g=2$',xlabel=r'Shifted real field $u$',ylabel=r'$V=u^2(1+u)^2$',ylim=(-.008,.25))
x=np.linspace(-1.15,1.15,900);ax=axes[0,1]
ax.plot(x,x**4,color=blue,lw=2);ax.scatter([0],[0],color=green,zorder=4)
ax.set(title=r'Double root: $M=0,\ g=2$',xlabel=r'Shifted real field $u$',ylabel=r'$V=u^4$',ylim=(-.08,1.9))
x=np.linspace(-1.1,1.1,900);ax=axes[1,0]
ax.plot(x,(1+x*x)**2,color=blue,lw=2);ax.scatter([0],[1],color=orange,zorder=4)
ax.text(.04,.9,r'Complex vacua: $\varphi=\pm i$'+'\n(not on this real slice)',transform=ax.transAxes,fontsize=9,va='top')
ax.set(title=r'No real critical-point shift: $\kappa=1,m=0,g=2$',xlabel=r'Original real field $\varphi$',ylabel=r'$V=(1+\varphi^2)^2$',ylim=(.7,5.3))
x=np.linspace(-1.5,1.5,500);ax=axes[1,1]
ax.plot(x,np.ones_like(x),color=orange,lw=2)
ax.text(.04,.87,r'$F\ne0$: supersymmetry broken'+'\nScalar is a flat direction',transform=ax.transAxes,fontsize=9,va='top')
ax.set(title=r'Pure linear branch: $\kappa=1,m=g=0$',xlabel=r'Real field $\varphi$',ylabel=r'$V=1$',ylim=(.5,1.5))
for ax in axes.flat:
    ax.set_facecolor('white');ax.grid(alpha=.2);ax.spines[['top','right']].set_visible(False)
fig.suptitle('Real slices of a complex chiral-scalar potential',fontsize=14,y=.98)
fig.subplots_adjust(top=.89,bottom=.09,left=.085,right=.975,hspace=.55,wspace=.35)
fig.savefig('paper-45-scalar-potentials.png',dpi=100,facecolor='white',transparent=False)
plt.close(fig)
