"""Original timing solution under exact transport delays; outputs to cwd."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

signals = [('c', 1, [(0, 0)]), ('x', 0, []), ('y', 1, [(10, 0)]),
           ('z', 0, [(20, 1)]), ('w', 1, [(20, 0), (30, 1)]),
           ('q', 1, [(30, 0), (40, 1)])]
fig, axes = plt.subplots(6, 1, figsize=(7.6, 6.0), dpi=100, sharex=True, facecolor='white')
for ax, (name, initial, transitions) in zip(axes, signals):
    times, values = [-10], [initial]
    for time, value in transitions:
        times.append(time); values.append(value)
    times.append(60); values.append(values[-1])
    ax.step(times, values, where='post', color='#aa2828' if name=='q' else '#1264a3', lw=2)
    ax.set(ylim=(-0.22, 1.25), yticks=[0, 1], ylabel=name)
    ax.set_ylabel(name, rotation=0, fontsize=13, labelpad=14)
    ax.set_xticks(range(-10, 61, 10)); ax.grid(axis='x', alpha=0.23)
    for spine in ['top', 'right']: ax.spines[spine].set_visible(False)
axes[-1].axvspan(30, 40, facecolor='#f4c8c8', alpha=0.8, zorder=0)
axes[-1].annotate('10 ns incorrect low pulse', xy=(35, 0.03), xytext=(43, 0.65),
                  fontsize=9, arrowprops=dict(arrowstyle='->', color='#aa2828'), color='#aa2828')
axes[-1].set(xlim=(-10, 60), xlabel='Time after input transition (ns)')
fig.suptitle('Static-one hazard from unequal path delays', fontsize=14, y=0.98)
fig.subplots_adjust(left=0.11, right=0.97, top=0.92, bottom=0.10, hspace=0.20)
fig.savefig(Path(__file__).with_suffix('.png').name, facecolor='white', dpi=100)
plt.close(fig)
