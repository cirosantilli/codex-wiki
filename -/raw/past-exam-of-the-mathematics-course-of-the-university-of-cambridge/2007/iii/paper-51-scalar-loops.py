"""One-loop 1PI graphs of real quartic scalar theory; Python 3.14.

Use the root Matplotlib/NumPy environment and write the PNG basename to CWD.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 4, figsize=(10.5, 3.3), layout='constrained', facecolor='white')
ink = '#243746'
ax = axes[0]
ax.plot([-1.15, 1.15], [0, 0], color=ink, lw=2)
t = np.linspace(-np.pi/2, 3*np.pi/2, 201)
ax.plot(.48*np.cos(t), .48+.48*np.sin(t), color=ink, lw=2)
ax.scatter([0], [0], color=ink, s=40, zorder=3)
ax.text(-1.15, -.18, '$p$', ha='center', fontsize=12)
ax.text(1.15, -.18, '$-p$', ha='center', fontsize=12)
ax.set_title('Two-point tadpole', fontsize=12)
ax.text(0, -.91, 'symmetry factor 1/2', ha='center', fontsize=10)

for ax, channel, left, right in zip(axes[1:], ['s', 't', 'u'],
                                  [('1','2'), ('1','3'), ('1','4')],
                                  [('3','4'), ('2','4'), ('2','3')]):
    x = np.linspace(-.55, .55, 101)
    y = .43*(1-(x/.55)**2)
    ax.plot(x, y, color=ink, lw=2)
    ax.plot(x, -y, color=ink, lw=2)
    for vx, side, labels in [(-.55, -1, left), (.55, 1, right)]:
        for sign, label in zip([1,-1], labels):
            ax.plot([vx, side*1.15], [0, sign*.6], color=ink, lw=2)
            ax.text(side*1.19, sign*.65, '$p_'+label+'$', ha='center', fontsize=12)
        ax.scatter([vx], [0], color=ink, s=40, zorder=3)
    ax.set_title(channel+'-channel bubble', fontsize=12)
    ax.text(0, -.91, 'symmetry factor 1/2', ha='center', fontsize=10)
for ax in axes:
    ax.set(xlim=(-1.45, 1.45), ylim=(-1.15, 1.2))
    ax.set_aspect('equal')
    ax.axis('off')
fig.suptitle(r'Connected one-loop 1PI graphs for $-\lambda\phi^4/4!$', fontsize=15)
fig.text(.5, .015, 'All external momenta are incoming; cutting either bubble edge leaves a connected graph.',
         ha='center', fontsize=10)
fig.savefig('paper-51-scalar-loops.png', dpi=120, facecolor='white')
plt.close(fig)
