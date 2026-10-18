"""Plot Question 5's four wave sections; write the PNG only to cwd.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Dependencies are declared in the repository's root pyproject.toml.
Run from _media/past-exam-of-the-mathematics-course-of-the-university-of-oxford/2017/prelims.
"""
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def initial_profile(x):
    """The continuous, odd, compactly supported initial displacement."""
    x = np.asarray(x)
    inside = ((-2 * np.pi <= x) & (x <= -np.pi)) | ((np.pi <= x) & (x <= 2 * np.pi))
    return np.where(inside, np.sin(x), 0.0)


def solution(x, t):
    return (initial_profile(x - t) + initial_profile(x + t)) / 2


def main():
    plt.rcParams.update({'font.size': 11, 'figure.facecolor': 'white', 'savefig.facecolor': 'white'})
    fig, axes = plt.subplots(2, 2, figsize=(11, 6.5), layout='constrained')
    x = np.linspace(-4 * np.pi, 4 * np.pi, 6401)
    t = np.linspace(0, 4 * np.pi, 3201)
    specifications = [
        (axes[0, 0], x / np.pi, solution(x, np.pi), r'$u(x,\pi)$', r'$x/\pi$', '#1869a4'),
        (axes[0, 1], x / np.pi, solution(x, 3 * np.pi / 2), r'$u(x,3\pi/2)$', r'$x/\pi$', '#1869a4'),
        (axes[1, 0], t / np.pi, solution(0, t), r'$u(0,t)$', r'$t/\pi$', '#b64b22'),
        (axes[1, 1], t / np.pi, solution(np.pi / 2, t), r'$u(\pi/2,t)$', r'$t/\pi$', '#b64b22'),
    ]
    for ax, horizontal, vertical, title, xlabel, color in specifications:
        ax.axhline(0, color='#999999', lw=.7)
        ax.axvline(0, color='#999999', lw=.7)
        ax.plot(horizontal, vertical, color=color, lw=2.2)
        ax.set(title=title, xlabel=xlabel, ylabel='$u$', ylim=(-.62, .62))
        ax.set_yticks([-.5, 0, .5])
        ax.grid(alpha=.18)
        ax.spines[['top', 'right']].set_visible(False)
    axes[0, 0].set(xlim=(-4, 4), xticks=np.arange(-4, 5))
    axes[0, 1].set(xlim=(-4, 4), xticks=[-3.5, -2.5, 0, 2.5, 3.5])
    for ax in axes[1]:
        ax.set(xlim=(0, 4), xticks=np.arange(0, 4.5, .5))
    axes[0, 1].annotate('central contributions cancel', xy=(0, 0), xytext=(0, .35),
                        ha='center', fontsize=10, arrowprops={'arrowstyle': '->', 'color': '#666666'})
    axes[1, 0].text(2, .14, r'$u(0,t)=0$ for all $t\geq0$', ha='center')
    fig.savefig(Path.cwd() / 'mathematics-v-wave-sections.png', dpi=100, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
