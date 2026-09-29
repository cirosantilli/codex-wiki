"""Moment-free driven filament: exact dimensionless attenuating wave components.
Python 3.14; NumPy 2.3.5 and Matplotlib 3.10.7 from root pyproject.
Writes paper-83-filament-waves.png to caller CWD; honors caller MPLCONFIGDIR.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def main():
    eta = np.linspace(0, 8, 800)
    c, s = np.cos(np.pi/8), np.sin(np.pi/8)
    fig, axes = plt.subplots(1, 3, figsize=(12, 4.1), dpi=130, facecolor='white')
    phases = [0, np.pi/2, np.pi, 3*np.pi/2]
    colors = ['#22668f', '#db8730', '#955496', '#43805d']
    for phase, color in zip(phases, colors):
        axes[0].plot(eta, 0.5*np.exp(-c*eta)*np.cos(phase+s*eta), color=color, lw=1.8, label=rf'$\omega t={phase/np.pi:g}\pi$')
        axes[1].plot(eta, 0.5*np.exp(-s*eta)*np.cos(phase-c*eta), color=color, lw=1.8)
    for ax, rate in zip(axes[:2], [c, s]):
        envelope = 0.5*np.exp(-rate*eta)
        ax.plot(eta, envelope, ls=':', color='#444444', lw=1.2)
        ax.plot(eta, -envelope, ls=':', color='#444444', lw=1.2)
        ax.set(ylim=(-0.53, 0.53), ylabel='Contribution to h / h₀')
    axes[0].set_title('Left-travelling: faster decay')
    axes[1].set_title('Right-travelling: slower decay')
    axes[0].legend(fontsize=8.5, loc='lower right')
    axes[2].semilogy(eta, 0.5*np.exp(-c*eta), lw=2, color='#22668f', label='Left wave envelope')
    axes[2].semilogy(eta, 0.5*np.exp(-s*eta), lw=2, color='#db8730', label='Right wave envelope')
    axes[2].set(title='Envelope comparison', ylabel='Amplitude / h₀', ylim=(2e-4, 0.7))
    axes[2].legend(fontsize=8.5, loc='lower left')
    for ax in axes:
        ax.set(xlim=(0, 8), xlabel=r'Distance $\eta=x/\ell_\omega$')
        ax.grid(alpha=0.2)
    fig.tight_layout()
    fig.savefig('paper-83-filament-waves.png', facecolor='white', transparent=False)
    plt.close(fig)

if __name__ == '__main__':
    main()
