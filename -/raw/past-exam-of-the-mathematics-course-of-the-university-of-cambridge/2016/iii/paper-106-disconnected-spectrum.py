"""Draw a disconnected normal-operator spectrum and its indicator projection.

Writes paper-106-disconnected-spectrum.png in the current working directory.
Tested with Python 3.14.4, matplotlib 3.10.7, and numpy 2.3.5.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

fig, axes = plt.subplots(1, 2, figsize=(7.6, 3.6), dpi=100, facecolor='white')
for ax in axes:
    ax.set_facecolor('white')
    ax.axhline(0, color='#b8b8b8', lw=0.7, zorder=0)
    ax.axvline(0, color='#b8b8b8', lw=0.7, zorder=0)
    ax.set(xlim=(-3.3, 3.3), ylim=(-1.6, 1.6), aspect='equal')
    ax.set_xticks([-2, 0, 2])
    ax.set_yticks([-1, 0, 1])
    ax.tick_params(labelsize=8)
    ax.set_xlabel(r'$\operatorname{Re}z$', fontsize=10)
    ax.set_ylabel(r'$\operatorname{Im}z$', fontsize=10)
    for spine in ax.spines.values():spine.set_visible(False)
axes[0].add_patch(Circle((-2, 0), 0.8, facecolor='#cee5ef', edgecolor='#226b91', lw=1.8))
axes[0].add_patch(Circle((2, 0), 0.8, facecolor='#fde0cc', edgecolor='#b65e27', lw=1.8))
axes[0].text(-2, 0, r'$K_1$', ha='center', va='center', fontsize=13)
axes[0].text(2, 0, r'$K_2$', ha='center', va='center', fontsize=13)
axes[0].set_title(r'$K=\sigma(T)=K_1\sqcup K_2$', fontsize=12, pad=15)
axes[1].add_patch(Circle((-2, 0), 0.8, facecolor='#72b6ce', edgecolor='#226b91', lw=1.8))
axes[1].add_patch(Circle((2, 0), 0.8, facecolor='#eeeeee', edgecolor='#777777', lw=1.8))
axes[1].text(-2, 0, r'$f=1$', ha='center', va='center', fontsize=12)
axes[1].text(2, 0, r'$f=0$', ha='center', va='center', fontsize=12)
axes[1].set_title(r'$P=f(T),\quad f=\mathbf{1}_{K_1}$', fontsize=12, pad=15)
fig.text(0.5, 0.07, r'$P^2=P=P^*,\quad PT=TP,\quad Y=PH$', ha='center', fontsize=12)
fig.subplots_adjust(left=0.07, right=0.98, bottom=0.22, top=0.88, wspace=0.25)
fig.savefig(Path.cwd() / 'paper-106-disconnected-spectrum.png', dpi=100, facecolor='white', transparent=False)
plt.close(fig)
