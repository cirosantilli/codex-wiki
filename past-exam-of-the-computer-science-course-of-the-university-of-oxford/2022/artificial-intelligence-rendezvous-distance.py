"""Original simultaneous-meeting example; Python 3.14.4, Matplotlib 3.10.7."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 10})
fig, (ax, tx) = plt.subplots(1, 2, figsize=(7.2, 3.45), dpi=100,
                            gridspec_kw={'width_ratios': [1, 1.3]})
fig.patch.set_facecolor('white')
path = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0),
        (5, 1), (5, 2), (5, 3), (5, 4)]
p_trace = path[:6]
q_trace = list(reversed(path[5:])) + [path[5]]
for i in range(7):
    ax.axhline(i - .5, color='#d3dbe0', linewidth=.8, zorder=0)
    ax.axvline(i - .5, color='#d3dbe0', linewidth=.8, zorder=0)
ax.plot(*zip(*p_trace), color='#177ca4', linewidth=4, zorder=2)
ax.plot(*zip(*q_trace), color='#b34c27', linewidth=4, zorder=2)
for trace, color in [(p_trace, '#177ca4'), (q_trace, '#b34c27')]:
    for first, second in zip(trace, trace[1:]):
        if first != second:
            dx, dy = second[0] - first[0], second[1] - first[1]
            ax.annotate('', xy=(first[0]+.72*dx, first[1]+.72*dy),
                        xytext=(first[0]+.3*dx, first[1]+.3*dy),
                        arrowprops={'arrowstyle': '->', 'color': 'white', 'lw': 1.4})
ax.scatter([0, 5], [0, 4], c=['#177ca4', '#b34c27'], s=140, edgecolors='white', zorder=4)
ax.scatter([5], [0], marker='*', c='#613f8e', s=230, edgecolors='white', zorder=5)
ax.text(0, .42, 'P starts', ha='center', color='#126885')
ax.text(4.7, 4.45, 'Q starts', ha='center', color='#92391f')
ax.text(4.9, -.65, 'meet at step 5', ha='right', color='#613f8e')
ax.set(xlim=(-.65, 5.65), ylim=(-1.05, 5.55), aspect='equal', xticks=[], yticks=[])
ax.set_title('A 9-edge connecting route', fontsize=11)
for spine in ax.spines.values():
    spine.set_visible(False)
D = [abs(p[0]-q[0]) + abs(p[1]-q[1]) for p,q in zip(p_trace,q_trace)]
assert D == [9,7,5,3,1,0]
t = list(range(6))
tx.plot(t, D, 'o-', color='#343e49', label='separation D', linewidth=2)
tx.step(t, [(d+1)//2 for d in D], where='post', color='#613f8e', linewidth=2,
        label='ceil(D / 2)')
tx.set(xlim=(-.15,5.2), ylim=(-.3,10), xticks=t, yticks=[0,1,3,5,7,9],
       xlabel='Simultaneous steps', ylabel='Grid distance / remaining steps')
tx.grid(axis='y', color='#e5e9ed')
tx.set_title('Q waits in the last step', fontsize=11)
tx.legend(frameon=False, fontsize=9, loc='upper right')
tx.annotate('1 apart → meet', xy=(4.8,.2), xytext=(2.5,2.5),
            arrowprops={'arrowstyle':'->', 'color':'#613f8e'}, color='#613f8e', fontsize=9)
fig.tight_layout(pad=1.2, w_pad=1.3)
fig.savefig(Path(__file__).with_suffix('.png').name, facecolor='white', transparent=False)
