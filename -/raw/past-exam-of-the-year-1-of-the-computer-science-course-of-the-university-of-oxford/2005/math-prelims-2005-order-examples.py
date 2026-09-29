"""Illustrate Q6. Run from an output directory; writes a PNG there.

Tested with Python 3.14, Matplotlib 3.10.7, NumPy 2.3.5.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11,
                     'figure.facecolor': 'white', 'savefig.facecolor': 'white'})
fig, (left, right) = plt.subplots(1, 2, figsize=(10, 4.5), dpi=120)
left.set_title('Two chains: complete, not continuous', fontsize=12, pad=13)
left.set_xlim(-1.75, 1.75)
left.set_ylim(-0.45, 4.75)
left.axis('off')
blue, orange = '#17679b', '#a74f00'
left.plot(0, 0, 'ko', ms=5)
left.text(0.13, 0, r'$\bot$', va='center')
left.plot(0, 4, 'ko', ms=5)
left.text(0.13, 4, r'$\top$', va='center')
for x, name, colour in [(-1, 'a', blue), (1, 'b', orange)]:
    left.plot([0, x], [0, 1], color=colour, lw=1.7)
    left.plot([x, x], [1, 3], color=colour, lw=1.7)
    left.plot([x, 0], [3, 4], color=colour, lw=1.7, linestyle=':')
    for n in range(1, 4):
        left.plot(x, n, 'o', color=colour, ms=5)
        left.text(x + (-0.14 if x < 0 else 0.14), n,
                  rf'${name}_{n}$', ha='right' if x < 0 else 'left', va='center')
left.text(0, 4.5, r'$\sup_n a_n=\sup_n b_n=\top$', ha='center')
left.text(0, -0.38, 'Interior points on different branches are incomparable.',
          ha='center', fontsize=9)
right.set_title('Unit interval: continuous, not algebraic', fontsize=12, pad=13)
right.set_xlim(-0.12, 1.12)
right.set_ylim(-0.45, 1.2)
right.axis('off')
y, x = .42, .72
right.plot([0, 1], [y, y], color='#777777', lw=2)
right.plot([0, x], [y, y], color=blue, lw=5, solid_capstyle='butt')
for t, label in [(0, '$0$'), (x, '$x$'), (1, '$1$')]:
    right.plot([t, t], [y-.035, y+.035], color='black', lw=1)
    right.text(t, y-.09, label, ha='center', va='top')
right.plot(x, y, 'o', markerfacecolor='white', markeredgecolor=blue, ms=8, mew=2)
right.annotate(r'$[0,x)$', xy=(x/2, y), xytext=(x/2, .78),
               ha='center', arrowprops={'arrowstyle': '->', 'color': blue}, color=blue)
right.text(.5, .98, r'$\sup[0,x)=x\quad (x>0)$', ha='center')
right.text(.5, -.05, 'Every positive point is approached from below.', ha='center', fontsize=9)
right.text(.5, -.2, 'No positive point is compact.', ha='center', fontsize=9)
fig.subplots_adjust(left=.045, right=.98, bottom=.12, top=.85, wspace=.35)
fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), facecolor='white', metadata={'Software': 'Matplotlib'})
plt.close(fig)
