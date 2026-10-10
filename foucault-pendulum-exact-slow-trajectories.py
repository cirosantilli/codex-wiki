"""Exact trajectories of the stated truncated linear ODE, not a full Earth model.
Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7. Run from _media.
Equal-amplitude release from rest, length 20 m, g=9.81 m/s²; physical Earth rate.
Each coloured segment spans one fast period, starting at the stated elapsed time.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

OMEGA = 7.292115e-5
LENGTH = 20.0
G = 9.81

def trajectory(t, latitude):
    alpha = OMEGA * np.sin(np.deg2rad(latitude))
    beta = np.sqrt(G / LENGTH + alpha**2)
    return np.exp(-1j * alpha * t) * (np.cos(beta * t) + 1j * alpha / beta * np.sin(beta * t))

if __name__ == '__main__':
    plt.rcParams.update({'font.size': 11, 'figure.facecolor': 'white', 'axes.facecolor': 'white'})
    fig, axes = plt.subplots(1, 3, figsize=(11.4, 4.8), layout='constrained')
    for ax, latitude, name in zip(axes, (45, 0, -45), ('45° north: clockwise', 'Equator: no slow turning', '45° south: anticlockwise')):
        alpha = OMEGA * np.sin(np.deg2rad(latitude))
        beta = np.sqrt(G / LENGTH + alpha**2)
        for hours, color, style in ((0, '#235b91', '-'), (3, '#cf7a18', '--'), (6, '#9b365e', ':')):
            t = hours * 3600 + np.linspace(0, 2 * np.pi / beta, 1500)
            z = trajectory(t, latitude)
            ax.plot(z.real, z.imag, color=color, ls=style, lw=2.2, label=f'{hours} h')
        ax.axhline(0, color='.8', lw=.8)
        ax.axvline(0, color='.8', lw=.8)
        ax.set(xlim=(-1.13, 1.13), ylim=(-1.13, 1.13), aspect='equal', xlabel='East displacement / A', ylabel='North displacement / A', title=name)
        ax.set_xticks([-1, 0, 1])
        ax.set_yticks([-1, 0, 1])
        ax.legend(loc='upper right', fontsize=9)
    fig.suptitle('Rapid swings, slowly rotating direction\nExact linear solution at the real Earth rotation rate', weight='bold', fontsize=15)
    fig.supxlabel('20 m illustrative pendulum: fast period ≈ 8.97 s; snapshots start 3 hours apart.\nEach segment is one full swing; the tiny transverse width is below this drawing’s resolution.', fontsize=10)
    fig.savefig(Path(__file__).stem + '.png', dpi=100, facecolor='white')
