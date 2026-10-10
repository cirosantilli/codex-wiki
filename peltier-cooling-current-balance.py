"""Plot an explicitly stipulated constant-property thermoelectric cooler.

Run from _media; emits this script's basename.png to the working directory.
Tested: Python 3.14.4, Matplotlib 3.10.7, NumPy 2.3.5. No extra dependencies.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11})
    alpha, tc, th, resistance, conductance = .040, 280., 300., 2., .40
    current = np.linspace(0, 12, 401)
    peltier = alpha*tc*current
    joule = -.5*resistance*current**2
    leak = -conductance*(th-tc)
    cooling = peltier+joule+leak
    reverse = -peltier+joule+leak
    optimum = alpha*tc/resistance
    roots = (alpha*tc+np.array([-1, 1])*np.sqrt((alpha*tc)**2-2*resistance*conductance*(th-tc)))/resistance
    fig, (a, b) = plt.subplots(1, 2, figsize=(11, 5.2), dpi=120)
    fig.patch.set_facecolor('white')
    for ax in (a, b):
        ax.set_facecolor('white')
        ax.axhline(0, color='#555555', lw=1)
        ax.grid(alpha=.16)
        ax.set(xlim=(0, 12), xlabel='Current magnitude I (A)', ylabel='Heat extraction rate (W)')
    a.set_title('Net cooling has a maximum', fontsize=14, weight='bold')
    a.plot(current, peltier, color='#177eab', label=r'Peltier: $\alpha T_c I$')
    a.plot(current, joule+leak, color='#ba4c21', linestyle='--', label=r'Loss: $-I^2R/2-K\Delta T$')
    a.plot(current, cooling, color='#176b3b', lw=2.7, label=r'Net $Q_c$')
    a.fill_between(current, 0, cooling, where=cooling>0, color='#88c7a2', alpha=.3)
    a.scatter([optimum], [alpha*tc*optimum-.5*resistance*optimum**2+leak], color='#176b3b', zorder=5)
    a.annotate('23.36 W at 5.60 A', (optimum, 23.36), (6.3, 44),
               arrowprops={'arrowstyle': '->', 'color': '#176b3b'}, fontsize=10)
    a.scatter(roots, [0, 0], color='#176b3b', s=20, zorder=5)
    a.text(5.5, -130, 'Cooling: 0.767 < I < 10.433 A', ha='center', fontsize=10)
    a.set(ylim=(-160, 150))
    a.legend(loc='upper left', fontsize=10, framealpha=1)
    b.set_title('Reversal at fixed face temperatures', fontsize=14, weight='bold')
    b.plot(current, (cooling-reverse)/2, color='#177eab', lw=2,
           label=r'Odd: $[Q_c(I)-Q_c(-I)]/2$')
    b.plot(current, (cooling+reverse)/2, color='#ba4c21', lw=2,
           label=r'Even: $[Q_c(I)+Q_c(-I)]/2$')
    b.plot(current, joule, color='#713f9a', linestyle='--',
           label=r'Even minus $Q_c(0)$: $-I^2R/2$')
    b.set(ylim=(-160, 150))
    b.legend(loc='upper left', fontsize=9, framealpha=1)
    b.text(5.4, 15, 'Odd = transported heat', color='#177eab', fontsize=10)
    b.text(.5, -130, 'Even includes the −8 W leak', color='#ba4c21', fontsize=10)
    fig.suptitle('Stipulated model • calculated curves, not measurements', fontsize=15, y=.985)
    fig.text(.5, .025, 'α = 0.040 V/K   •   R = 2.0 Ω   •   K = 0.40 W/K   •   Tc = 280 K   •   Th = 300 K',
             ha='center', fontsize=11)
    fig.subplots_adjust(left=.07, right=.985, bottom=.16, top=.84, wspace=.23)
    fig.savefig(Path(__file__).stem+'.png', facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
