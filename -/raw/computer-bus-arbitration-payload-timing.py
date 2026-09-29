"""Original stipulated, nonoverlapping shared-bus timing example.

Python 3.14, matplotlib 3.10.7. Run from _media to write the matching PNG.
This is a teaching model, not an implementation of a named bus protocol.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Patch, Rectangle

fig, ax = plt.subplots(figsize=(10, 5), dpi=140, facecolor='white')
colors = {'arbitration': '#c7d1de', 'command': '#f0c777', 'payload': '#67b6a5'}
rows = [('A selected first', 'A', 0, 4), ('B selected second', 'B', 6, 2)]
for y, (label, owner, start, n) in zip([1.65, .65], rows):
    for t, kind, text in [(start, 'arbitration', 'arb'), (start+1, 'command', 'addr')]:
        ax.add_patch(Rectangle((t, y), 1, .65, facecolor=colors[kind], edgecolor='white'))
        ax.text(t+.5, y+.325, text, ha='center', va='center', fontsize=10)
    for k in range(n):
        t = start+2+k
        ax.add_patch(Rectangle((t, y), 1, .65, facecolor=colors['payload'], edgecolor='white'))
        ax.text(t+.5, y+.325, f'{owner}{k+1}', ha='center', va='center', fontsize=11)
    completion = start+2+n
    ax.plot([completion, completion], [y-.08, y+.72], color='#334155', lw=1.4)
    ax.text(completion, y+.85, f'{owner} completes: {completion*10} ns',
            ha='right', fontsize=11)
    if owner == 'B':
        ax.annotate('', xy=(6, y+.325), xytext=(0, y+.325),
                    arrowprops=dict(arrowstyle='<->', color='#6b7280', lw=1.4))
        ax.text(3, y+.47, 'B waits for 60 ns', ha='center', fontsize=11)
ax.set(xlim=(-.1, 10.1), ylim=(.3, 3.25), yticks=[1.975, .975],
       yticklabels=['Initiator A', 'Initiator B'], xticks=range(11))
ax.set_xlabel('Bus-cycle boundaries (one cycle = 10 ns)', fontsize=11)
ax.tick_params(axis='y', length=0, labelsize=11)
ax.grid(axis='x', color='#e5e7eb', zorder=0)
for s in ('top', 'left', 'right'):
    ax.spines[s].set_visible(False)
ax.set_axisbelow(True)
ax.set_title('Two simultaneous requests, one serialized shared bus',
             fontsize=15, weight='bold', pad=15)
ax.text(5, 3.05, '100 MHz • 32-bit payload • no overlap • target always ready',
        ha='center', fontsize=11)
ax.legend(handles=[Patch(facecolor=colors[k], label=v) for k,v in
                   [('arbitration', 'Selection (1 cycle)'), ('command', 'Address / command (1 cycle)'),
                    ('payload', 'Payload (4 bytes / cycle)')]],
          loc='upper center', bbox_to_anchor=(.5, -.22), ncol=3, frameon=False, fontsize=10)
fig.text(.5, .03, '24 bytes / 100 ns = 240 MB/s  |  Raw capacity: 400 MB/s  |  Payload fraction: 60%',
         ha='center', fontsize=11)
fig.subplots_adjust(left=.13, right=.98, top=.84, bottom=.29)
fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), facecolor='white')
plt.close(fig)
