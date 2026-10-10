"""Plot an ideal CHSH visibility/count model, not measurements. Python 3.14; numpy 2.3.5; matplotlib 3.10.7."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 11, 'font.family': 'DejaVu Sans'})
fig, (ax, counts_ax) = plt.subplots(1, 2, figsize=(10, 4.5), dpi=120, facecolor='white')
v = np.linspace(0, 1, 401)
ax.plot(v, 2*np.sqrt(2)*v, lw=2.5, color='#2466a5', label=r'$S=2\sqrt{2}\,v$')
ax.axhline(2, color='#ad4432', ls='--', lw=1.7, label='Local bound: 2')
ax.axvline(1/np.sqrt(2), color='#747b81', ls=':', lw=1.5)
ax.fill_between(v, 2, 2*np.sqrt(2)*v, where=v>1/np.sqrt(2), color='#dcecf7')
ax.plot(.8, 2*np.sqrt(2)*.8, 'o', color='#2466a5')
ax.annotate(r'$v=0.8$', xy=(.8, 2*np.sqrt(2)*.8), xytext=(.47, 2.63),
            arrowprops={'arrowstyle':'->', 'color':'#2466a5'})
ax.text(.69, .18, r'$1/\sqrt{2}$', ha='right', color='#555b60')
ax.set(xlim=(0, 1), ylim=(0, 3), xlabel='Visibility v', ylabel='CHSH expression S', title='Visibility controls the violation')
ax.legend(loc='upper left', fontsize=10, frameon=False)
ax.grid(alpha=.18)
M, eta_a, eta_b, visibility = 1000, .8, .75, .8
correlation = visibility*np.cos(2*np.deg2rad(0-22.5))
probabilities = np.array([1+correlation, 1-correlation, 1-correlation, 1+correlation])/4
counts = M*eta_a*eta_b*probabilities
bars = counts_ax.bar(['++', '+−', '−+', '−−'], counts,
                     color=['#2466a5', '#dfb06d', '#dfb06d', '#2466a5'], width=.65)
for bar, value in zip(bars, counts):
    counts_ax.text(bar.get_x()+bar.get_width()/2, value+6, f'{value:.2f}', ha='center', fontsize=11)
counts_ax.set(ylim=(0, 300), xlabel='Joint analyzer outcomes', ylabel='Expected joint count',
              title=r'Example: $(a_0,b_0)=(0^\circ,22.5^\circ)$')
counts_ax.text(.5, .94, '600 expected detected pairs', transform=counts_ax.transAxes,
               ha='center', fontsize=10)
counts_ax.text(.5, .57, r'$E=0.56569$', transform=counts_ax.transAxes, ha='center',
               bbox={'facecolor':'white','edgecolor':'none','pad':3})
counts_ax.grid(axis='y', alpha=.18)
counts_ax.set_axisbelow(True)
fig.suptitle('Ideal model predictions • no experimental counts', weight='bold', fontsize=14)
fig.text(.5, .025, r'Stipulated: $M=1000$, $\eta_A=0.8$, $\eta_B=0.75$, $v=0.8$; losses independent of setting and outcome.',
         ha='center', fontsize=10)
fig.subplots_adjust(left=.07, right=.98, bottom=.17, top=.82, wspace=.3)
fig.savefig(Path(__file__).stem+'.png', facecolor='white', transparent=False)
plt.close(fig)
