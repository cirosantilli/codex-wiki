"""Original exam-solution diagrams; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(12.2, 5.0), layout='constrained', facecolor='white')
a = axes[0]
a.set_title('Active-region energy levels (schematic)', fontsize=13)
for left, right, label in [(0, 1.6, 'Equilibrium'), (2.4, 4, 'Injected')]:
    a.fill_between([left, right], 1, 1.65, color='#dbeafe')
    a.fill_between([left, right], -.65, 0, color='#fce7df')
    a.hlines([0, 1], left, right, color='#334155', lw=2)
    a.text((left+right)/2, 1.78, label, ha='center', fontsize=11)
a.hlines(.5, 0, 1.6, color='#7c3aed', ls='--', lw=2)
a.text(.8, .59, 'one Fermi level', ha='center', fontsize=10)
a.hlines([-.3, 1.3], 2.4, 4, color='#7c3aed', ls='--', lw=2)
a.text(3.9, 1.37, r'$F_c$', ha='right', fontsize=12)
a.text(3.9, -.51, r'$F_v$', ha='right', fontsize=12)
a.annotate('', xy=(3, -.1), xytext=(3, 1.1), arrowprops=dict(arrowstyle='->', lw=2.5, color='#dc2626'))
a.text(3.12, .48, r'$\hbar\omega$', fontsize=13)
a.text(.08, 1.12, 'conduction band', fontsize=10)
a.text(.08, -.45, 'valence band', fontsize=10)
a.set(xlim=(-.15, 4.15), ylim=(-.8, 2), ylabel='Energy (chosen units)', xticks=[])
a.spines[['top', 'right', 'bottom']].set_visible(False)
b=axes[1]
u=np.linspace(0,4,600)
j=np.ones_like(u); term=np.ones_like(u)
for m in range(1,40):
    term *= -(u/2)**2/m**2
    j += term
b.plot(u,j,lw=2.5,color='#2563eb',label=r'$J_0(u)$')
b.axhline(0,color='#475569',lw=1)
b.axvline(2.4048255577,color='#dc2626',ls='--',label=r'$j_{0,1}=2.4048\ldots$')
b.scatter([2.4048255577],[0],color='#dc2626',zorder=4)
b.annotate('First additional spatial family\nreaches cutoff here',xy=(2.4048,0),xytext=(1.0,-.37),arrowprops=dict(arrowstyle='->'),fontsize=10)
b.set(title='Weak-guidance cutoff',xlabel=r'Core transverse parameter $u$',ylabel=r'$J_0(u)$',xlim=(0,4),ylim=(-.5,1.1))
b.grid(alpha=.2);b.legend(loc='upper right',fontsize=10)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=140,facecolor='white')
