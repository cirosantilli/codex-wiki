"""Original sedimentation profiles. Python 3.14; NumPy 2.3.5, Matplotlib 3.10.7.
Emit the basename PNG to the caller's CWD; caller controls MPLCONFIGDIR.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def main():
    z = np.linspace(-3.2, 3.2, 1001)
    times = [0., .6, 1.35, 2.1]
    fig, axes = plt.subplots(1, 2, figsize=(9.4, 3.8), constrained_layout=True)
    for tau in times:
        width = 1 + .6*tau
        s = np.clip(.5 + .3*z/width, .2, .8)
        axes[0].plot(z, s, label=fr'$V_0t={tau:g}$')
        if tau < 5/3:
            width = 1-.6*tau
            s = np.clip(.5-.3*z/width, .2, .8)
            axes[1].plot(z, s, label=fr'$V_0t={tau:g}$')
        else:
            axes[1].plot([-3.2, 0, 0, 3.2], [.8, .8, .2, .2], label=fr'$V_0t={tau:g}$')
    for ax, title in zip(axes, ['Increasing ramp: spreading', 'Decreasing ramp: stationary shock']):
        ax.set(xlabel=r'Upward coordinate $z$', ylabel=r'Particle fraction $s=\phi/\phi_{\max}$', ylim=(.05, .95), xlim=(-3.2, 3.2), title=title)
        ax.grid(alpha=.2)
        ax.legend(fontsize=8, loc='best')
    fig.savefig(Path.cwd() / 'paper-52-settling-ramps.png', dpi=130, facecolor='white', transparent=False)
    plt.close(fig)

if __name__ == '__main__':
    main()
