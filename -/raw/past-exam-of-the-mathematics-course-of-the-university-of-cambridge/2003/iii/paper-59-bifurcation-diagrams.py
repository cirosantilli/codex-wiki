"""Original bifurcation diagrams. Python 3.14, numpy and matplotlib.
Writes only the PNG basename in the caller's working directory.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 3, figsize=(12, 4), constrained_layout=True)
ax = axes[0]
k = np.linspace(-1.65, -.5, 300)
ax.plot(k, 2-k, color='#0068a3', label='Pitchfork')
ax.plot(k[k < -1], np.full(np.sum(k < -1), 3.), color='#d44825', label='Hopf (subcritical)')
k2 = np.linspace(-1.65, -1, 180)
ax.plot(k2, 3-.15*(k2+1)**2, '--', color='#8c4398', label='Actual global curve (leading)')
ax.plot(-1,3,'ko',ms=4)
ax.set(xlabel=r'$\kappa$',ylabel=r'$\lambda$',title='1. Printed spherical system',ylim=(2.65,3.65))
ax.legend(fontsize=7,loc='upper right')
ax.annotate('double zero',(-1,3),(-.98,2.73),arrowprops={'arrowstyle':'->'},fontsize=8)
ax = axes[1]
s=.5
q=np.linspace(0,5,301)
pitch=1+q; hopf=2*(1+s)+2*s*s*q/(1+s)
ax.plot(q,pitch,color='#0068a3',label='Pitchfork')
ax.plot(q[q>=3],hopf[q>=3],color='#d44825',label='Hopf')
ax.plot(q[q<3],hopf[q<3],':',color='#d44825',label='Algebraic extension only')
ax.fill_between(q,0,np.minimum(pitch,hopf),color='#d9edf6')
ax.plot(3,4,'ko',ms=4)
ax.annotate('TB',(3,4),(3.6,3.3),arrowprops={'arrowstyle':'->'},fontsize=8)
ax.text(.5,.6,'stable zero state',fontsize=9)
ax.set(xlabel=r'$q=r_\Omega^2$',ylabel=r'$r$',title=r'2. Rotating convection ($\sigma=1/2$)',xlim=(0,5),ylim=(0,6))
ax.legend(fontsize=7,loc='upper left')
ax=axes[2]
a=np.linspace(0,.32,301)
ax.plot(-2*a,-a*a,color='#0068a3',label='Unperturbed Hopf')
ax.plot(2*a,-a*a,color='#0068a3')
ax.plot(-2*a-a*a,-a*a,':',color='#555555',label='Hopf with added term')
ax.plot(2*a-a*a,-a*a,':',color='#555555')
ax.axhline(0,color='black',lw=1,label='Equilibrium fold')
ax.plot(np.zeros_like(a),-a*a,'--',color='#cc7940',label='Secondary torus / degeneracy')
ax.plot(-a*a/4,-a*a,color='#8c4398',lw=2,label='Perturbed global curve (leading)')
ax.plot(0,0,'ko',ms=4)
ax.text(-.47,-.078,'stable periodic orbit',fontsize=7)
ax.set(xlabel=r'$\mu_1$',ylabel=r'$\mu_2$',title='4. Fold–Hopf unfolding',xlim=(-.75,.7),ylim=(-.105,.015))
ax.legend(fontsize=6.6,loc='upper left')
for ax in axes:
    ax.spines[['top','right']].set_visible(False)
    ax.grid(alpha=.15)
fig.savefig('paper-59-bifurcation-diagrams.png',dpi=120,facecolor='white')
plt.close(fig)
