"""Original damped Fourier response and undamped causal cone; output PNG to cwd."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np


def main():
    fig, (mode, cone) = plt.subplots(1, 2, figsize=(10, 4.5), layout='constrained')
    time = np.linspace(-1, 14, 850)
    positive = np.maximum(time, 0)
    gamma = 0.8
    omega = np.sqrt(1-gamma*gamma/4)
    damped = -np.exp(-gamma*positive/2)*np.sin(omega*positive)/omega
    undamped = -np.sin(positive)
    mode.plot(time, undamped, color='#999999', ls='--', lw=1.5, label=r'No damping: $\gamma=0$')
    mode.plot(time, damped, color='#174ea6', lw=2.2, label=r'Damped: $\gamma=0.8$')
    mode.axhline(0, color='#777777', lw=0.8)
    mode.axvline(0, color='#777777', ls=':', lw=0.8)
    mode.set(xlim=(-1, 14), ylim=(-1.15, 1.15), xlabel='Time t',
             ylabel=r'$\widetilde G_R(k=1,t)$', title='Causal impulse: initial derivative is −1')
    mode.legend(loc='upper left', fontsize=9, frameon=False)
    mode.grid(alpha=0.15)

    x = np.linspace(-5, 5, 601)
    t = np.linspace(-1, 5, 401)
    xx, tt = np.meshgrid(x, t)
    response = np.where(tt > np.abs(xx), -0.5, 0)
    cone.pcolormesh(x, t, response, shading='nearest', cmap=ListedColormap(['#2166ac', '#ffffff']), vmin=-0.5, vmax=0)
    edge = np.linspace(0, 5, 150)
    cone.plot(edge, edge, color='#333333', lw=1.2)
    cone.plot(-edge, edge, color='#333333', lw=1.2)
    cone.scatter([0], [0], color='#111111', s=20, zorder=4)
    cone.text(0, 3.2, r'$G_R=-1/2$', ha='center', color='white', fontsize=12)
    cone.text(-3.9, 1.2, r'$G_R=0$', fontsize=11)
    cone.annotate('Impulse', xy=(0, 0), xytext=(-3.8, -0.55),
                  arrowprops={'arrowstyle':'->', 'color':'#333333'}, fontsize=10)
    cone.set(xlim=(-5, 5), ylim=(-1, 5), xlabel='Position x', ylabel='Time t',
             title='Undamped response fills the forward cone')
    fig.savefig(Path.cwd() / '2018-q4-retarded-rod-response.png', dpi=150, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
