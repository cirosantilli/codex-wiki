"""Draw the original scalar-exchange graphs; tested with Python 3.14.

Run from the desired output directory. The only output is the matching PNG.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def line(ax, a, b, reverse=False):
    a, b = np.array(a), np.array(b)
    ax.plot([a[0], b[0]], [a[1], b[1]], color='#17324d', lw=1.8)
    mid = (a+b)/2
    delta = (b-a)*.13*(-1 if reverse else 1)
    ax.annotate('', xy=mid+delta, xytext=mid-delta,
                arrowprops=dict(arrowstyle='-|>', color='#17324d', lw=1.5, mutation_scale=12))


def draw():
    fig, axes = plt.subplots(1, 2, figsize=(11.4, 4.35), dpi=120, facecolor='white')
    for ax in axes:
        ax.set(xlim=(-.1, 4.1), ylim=(-.55, 3.25), aspect='equal')
        ax.axis('off')
    ax = axes[0]
    left, right = (1.25, 1.3), (2.75, 1.3)
    line(ax, (0, 2.45), left)
    line(ax, (0, .15), left, reverse=True)
    line(ax, right, (4, 2.45))
    line(ax, right, (4, .15), reverse=True)
    ax.plot([1.25, 2.75], [1.3, 1.3], '--', color='#a34a28', lw=2)
    ax.plot([1.25, 2.75], [1.3, 1.3], 'o', color='#17324d', ms=4)
    ax.text(2, 1.55, r'$\phi,\ k=p_1+p_2$', ha='center', fontsize=11)
    for x, y, txt, align in [
        (0, 2.65, r'$f_1(p_1,s_1)$', 'left'),
        (0, -.15, r'$\bar f_1(p_2,s_2)$', 'left'),
        (4, 2.65, r'$f_j(p_3,s_3)$', 'right'),
        (4, -.15, r'$\bar f_j(p_4,s_4)$', 'right')]:
        ax.text(x, y, txt, ha=align, fontsize=12)
    ax.set_title(r'$s$ channel: $j=2$ in 2(c), $j=1$ in 2(d)', fontsize=12, pad=18)
    ax = axes[1]
    line(ax, (0, 2.1), (4, 2.1))
    line(ax, (0, .45), (4, .45), reverse=True)
    ax.plot([2, 2], [.45, 2.1], '--', color='#a34a28', lw=2)
    ax.plot([2, 2], [.45, 2.1], 'o', color='#17324d', ms=4)
    ax.text(2.17, 1.3, r'$\phi$'+'\n'+r'$k=p_1-p_3$', fontsize=11, va='center')
    for x, y, txt, align in [
        (0, 2.4, r'$f_1(p_1,s_1)$', 'left'),
        (0, -.05, r'$\bar f_1(p_2,s_2)$', 'left'),
        (4, 2.4, r'$f_1(p_3,s_3)$', 'right'),
        (4, -.05, r'$\bar f_1(p_4,s_4)$', 'right')]:
        ax.text(x, y, txt, ha=align, fontsize=12)
    ax.set_title(r'$t$ channel: same-species elastic scattering, 2(d)', fontsize=12, pad=18)
    fig.text(.5, .04, 'Solid arrows: fermion-number flow. Dashed line: scalar propagator.',
             ha='center', fontsize=11, color='#333333')
    fig.subplots_adjust(left=.035, right=.975, top=.84, bottom=.14, wspace=.19)
    fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    draw()
