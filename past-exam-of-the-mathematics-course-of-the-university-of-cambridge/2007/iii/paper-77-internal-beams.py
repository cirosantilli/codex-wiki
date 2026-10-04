"""Two radiating internal-wave beams; tested with Python 3.14.4.

Dependencies: numpy 2.3.5, matplotlib 3.10.7 (root pyproject.toml).
Output is a PNG basename in the caller's current working directory.
The caller's MPLCONFIGDIR is respected without modification.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    alpha = 0.75
    x, z = np.meshgrid(np.linspace(0, 4, 25), np.linspace(-4.5, 4.5, 39))
    f1 = 0.5 * np.exp(-(z + alpha*x)**2)
    f2 = 0.5 * np.exp(-(z - alpha*x)**2)
    u, w = f1 + f2, alpha*(f2 - f1)
    fig, ax = plt.subplots(figsize=(8.2, 6.2), facecolor='white')
    ax.set_facecolor('white')
    ax.quiver(x, z, u, w, np.hypot(u, w), cmap='viridis',
              angles='xy', scale_units='xy', scale=2.8, width=0.004)
    xx = np.linspace(0, 4, 200)
    for sign in [-1, 1]:
        ax.plot(xx, sign*alpha*xx, '--', color='tab:orange', lw=1.3)
    ax.axvline(0, color='black', lw=2)
    ax.text(2.7, 3.3, 'Upward energy beam', fontsize=10)
    ax.text(2.7, -3.5, 'Downward energy beam', fontsize=10)
    ax.set(xlim=(-0.12, 4.2), ylim=(-4.5, 4.5), xlabel=r'$x/H$', ylabel=r'$z/H$',
           title='Internal-wave velocity at maximum boundary speed\n'
                 r'$u_0=e^{-(z/H)^2},\quad \alpha=3/4$')
    ax.set_aspect('equal')
    fig.tight_layout()
    fig.savefig('paper-77-internal-beams.png', dpi=130, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
