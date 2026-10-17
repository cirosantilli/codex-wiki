"""Original calculated single-step reflection and finite-section transmission. Output cwd."""
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({"axes.titlesize":10,"axes.labelsize":10})
fig,ax=plt.subplots(1,2,figsize=(9,3.5),layout='constrained');alpha=np.geomspace(.1,10,500);rv=(alpha-1)/(alpha+1)
ax[0].semilogx(alpha,rv,label='Signed voltage reflection');ax[0].axhline(0,color='.5',lw=.8);ax[0].axvline(1,color='.5',ls=':');ax[0].set(xlabel='Impedance ratio alpha',ylabel='Voltage reflection coefficient',title='Reciprocal gaps reverse voltage reflection');ax[0].grid(alpha=.2)
x=np.linspace(0,3,900)
for a in [1,2,4]:ax[1].plot(x,1/(1+(a*a-1)**2/(4*a*a)*np.sin(np.pi*x)**2),label=f'alpha = {a}')
ax[1].set(xlabel=r'$f/[v/(2\ell)]$',ylabel='Whole-section power transmission',ylim=(0,1.05),title='Finite-section power resonances');ax[1].legend();ax[1].grid(alpha=.2)
fig.savefig('paper-1-line-resonances.png',dpi=150,facecolor='white')
