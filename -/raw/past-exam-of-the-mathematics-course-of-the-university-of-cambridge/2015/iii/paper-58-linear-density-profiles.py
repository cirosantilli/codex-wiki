"""Generate the normalized hydrostatic profiles; output PNG basename in cwd.

Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    x = np.linspace(0.0, 1.0, 700)
    q = 1 + 2*x - 1.8*x*x
    fig, ax = plt.subplots(figsize=(6.4, 4), dpi=100, facecolor='white')
    ax.set_facecolor('white')
    for y, label, color in [
        (4*x**3 - 3*x**4, r'$m/M$', '#6243a5'),
        (1-x, r'$\rho/\rho_c$', '#333333'),
        ((1-x)**2*q, r'$P/P_c$', '#0077aa'),
        ((1-x)*q, r'$T/T_c$', '#b34a00'),
    ]:
        ax.plot(x, y, label=label, color=color, linewidth=2)
    ax.set(xlim=(0, 1), ylim=(0, 1.16), xlabel=r'Fractional radius $r/R$', ylabel='Normalized profile', title='Linear-density hydrostatic stellar model')
    ax.grid(alpha=0.2)
    ax.legend(loc='center right', framealpha=1)
    ax.annotate('Temperature initially rises outward', xy=(0.13, (1-.13)*(1+2*.13-1.8*.13**2)), xytext=(.27, 1.12), fontsize=8, arrowprops={'arrowstyle': '->', 'color': '#b34a00'}, color='#b34a00')
    fig.tight_layout()
    fig.savefig('paper-58-linear-density-profiles.png', dpi=100, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
