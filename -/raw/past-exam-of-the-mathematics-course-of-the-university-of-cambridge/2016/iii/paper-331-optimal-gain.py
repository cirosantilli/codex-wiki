"""Python 3.14; NumPy 2.3.5, Matplotlib 3.10.7. Output only to the cwd."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
tau=np.linspace(0,10,700)
a=np.exp(-tau);d=np.exp(-tau/4)
fig,ax=plt.subplots(figsize=(7.2,3.6),dpi=100)
for r,color in [(5,'#3977a2'),(15,'#b07327'),(50,'#668a39')]:
 b=4*r*(d-a)/3
 S=a*a+b*b+d*d
 gain=(S+np.sqrt(np.maximum(0,S*S-4*a*a*d*d)))/2
 ax.plot(tau,gain/(r*r),color=color,label=fr'$\mathrm{{Re}}={r}$')
limit=16*(d-a)**2/9
ax.plot(tau,limit,'k--',linewidth=1.5,label=r'Large-$\mathrm{Re}$ limit')
A=4*np.log(4)/3
ax.axvline(A,color='#777777',linestyle=':',linewidth=1)
ax.set(xlim=(0,10),ylim=(0,.45),xlabel=r'Scaled time $t/\mathrm{Re}$',ylabel=r'Optimal gain $G_{\mathrm{opt}}/\mathrm{Re}^2$',title='Transient amplification in the triangular shear model')
ax.legend(fontsize=8,frameon=False,loc='upper right')
ax.spines[['top','right']].set_visible(False)
fig.tight_layout()
fig.savefig('paper-331-optimal-gain.png',dpi=100,facecolor='white',transparent=False)
plt.close(fig)
