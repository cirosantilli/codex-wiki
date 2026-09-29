"""Original coupling map for NST IA Chemistry 2025 Q1; Python 3.14."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

def arc(ax, start, end, label, rad, label_xy):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle='<->', connectionstyle=f'arc3,rad={rad}', mutation_scale=12, color='#245e91', linewidth=1.6, shrinkA=10, shrinkB=10))
    ax.text(*label_xy, label, ha='center', va='center', fontsize=11, color='#17476f', bbox={'facecolor': 'white', 'edgecolor': 'none', 'pad': 1.5})

fig, axes = plt.subplots(2, 1, figsize=(10, 6.3), facecolor='white')
x = [0.6, 2.1, 3.6, 5.0, 6.1, 7.6, 9.1]
for ax in axes:
    ax.set(xlim=(-0.1, 9.8), ylim=(-1.5, 1.65))
    ax.axis('off')
for ax, labels in zip(axes, [
    [r'$\mathrm{F_3C}$', r'$\mathrm{CH}_a$', r'$\mathrm{CH}_b$', r'$\mathrm{C(=O)}$', r'$\mathrm{O}$', r'$\mathrm{CH}_{c,2}$', r'$\mathrm{CH}_{d,3}$'],
    [r'$\mathrm{C}_e$', r'$\mathrm{C}_f$', r'$\mathrm{C}_g$', r'$\mathrm{C}_h(=O)$', r'$\mathrm{O}$', r'$\mathrm{C}_j$', r'$\mathrm{C}_k$']]):
    for a, b in zip(x[:-1], x[1:]):
        ax.plot([a + .39, b - .39], [0, 0], color='black', lw=1.3)
    ax.plot([x[1] + .39, x[2] - .39], [-.09, -.09], color='black', lw=1.3)
    for xx, label in zip(x, labels):
        ax.text(xx, 0, label, fontsize=14, ha='center', va='center', bbox={'facecolor': 'white', 'edgecolor': 'none', 'pad': 1})
axes[0].text(0, 1.48, 'Proton couplings (Hz)', fontsize=13, weight='bold')
arc(axes[0], (x[1], .12), (x[2], .12), '15.6', -.7, (2.85, .72))
arc(axes[0], (x[0], -.12), (x[1], -.12), '6.6 to each F', .65, (1.35, -.7))
arc(axes[0], (x[0], -.23), (x[2], -.23), '1.8 to each F', .75, (2.1, -1.26))
arc(axes[0], (x[5], .12), (x[6], .12), '7.2–7.3', -.7, (8.35, .72))
axes[1].set_ylim(-1.25, 2.6)
axes[1].text(0, 2.42, 'Carbon–fluorine couplings (Hz)', fontsize=13, weight='bold')
axes[1].text(x[0], 1.0, r'$\mathrm{F}_3$', fontsize=14, ha='center')
axes[1].plot([x[0], x[0]], [.25, .82], color='black', lw=1.2)
arc(axes[1], (x[0]-.16, .98), (x[0]-.16, .1), '268.5', .6, (-.01, .55))
arc(axes[1], (x[0]+.15, 1.04), (x[1], .15), '35.25', -.6, (1.7, 1.03))
arc(axes[1], (x[0]+.25, 1.08), (x[2], .15), '6.0', -.67, (3.2, 1.23))
axes[1].text(5.2, -.9, 'C–H splittings removed by proton decoupling.\nArrows to F₃ represent coupling to each equivalent F.', fontsize=11, ha='center')
fig.tight_layout(h_pad=2.5)
fig.savefig('2025-nmr-couplings.png', dpi=140, facecolor='white', bbox_inches='tight')
plt.close(fig)
