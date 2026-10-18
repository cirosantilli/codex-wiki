"""Original conceptual schematic; Python 3.14.4 / Matplotlib 3.10.7.

Uses existing project dependencies. Outputs the matching PNG into the CWD.
Selected connections only: this is not an anatomical tracing or measured data.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 10})
fig, ax = plt.subplots(figsize=(9, 5), dpi=100, facecolor='white')
fig.subplots_adjust(left=.025, right=.975, bottom=.075, top=.87)
ax.set(xlim=(0, 1), ylim=(-.10, 1.06))
ax.axis('off')
nodes = {
    'H': (.13, .77, 'Hippocampal\nformation'),
    'M': (.49, .77, 'Mammillary\nbodies'),
    'A': (.86, .77, 'Anterior thalamic\nnuclei'),
    'E': (.13, .30, 'Entorhinal\ncortex'),
    'R': (.86, .30, 'Retrosplenial /\ncingulate regions'),
    'G': (.49, .30, "Gudden's ventral\ntegmental nucleus"),
    'P': (.13, -.015, 'Perirhinal\ncortex'),
}
for key, (x, y, label) in nodes.items():
    ax.add_patch(FancyBboxPatch((x-.105, y-.074), .21, .148,
        boxstyle='round,pad=.012', facecolor='#edf4fb' if key!='G' else '#fff1dd',
        edgecolor='#284e70', linewidth=1.15, zorder=3))
    ax.text(x, y, label, ha='center', va='center', zorder=4)

def arrow(start, end, *, color='#284e70', style='-|>', rad=0, dashed=False):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle=style,
        connectionstyle=f'arc3,rad={rad}', mutation_scale=13,
        linewidth=1.5, color=color, linestyle='--' if dashed else '-', zorder=2))

arrow((.247,.77),(.373,.77))
ax.text(.31,.875,'Postcommissural\nfornix',ha='center',va='center',fontsize=9)
arrow((.607,.77),(.743,.77))
ax.text(.675,.875,'Mammillothalamic\ntract',ha='center',va='center',fontsize=9)
arrow((.86,.68),(.86,.39))
arrow((.743,.30),(.247,.30),rad=-.47)
ax.text(.50,-.038,'Selected cortical return routes',ha='center',fontsize=9,color='#284e70')
arrow((.13,.39),(.13,.68),style='<|-|>')
arrow((.13,.077),(.13,.21),style='<|-|>')
arrow((.49,.39),(.49,.68),color='#b56b12')
ax.text(.505,.52,'Additional input',ha='left',va='center',color='#9b5809',fontsize=9)
arrow((.20,.855),(.78,.855),rad=-.37,dashed=True)
ax.text(.50,1.025,'Direct hippocampal–thalamic route also exists',ha='center',fontsize=9)
fig.suptitle('An extended memory network, not one interchangeable relay chain',y=.975,fontsize=13)
fig.text(.5,.025,'Conceptual diagram: selected connections, no scale, many reciprocal pathways omitted.',ha='center',fontsize=9)
fig.savefig(Path.cwd() / (Path(__file__).stem+'.png'),dpi=100,facecolor='white',transparent=False,
    metadata={'Software':'Matplotlib','Description':'Original conceptual memory-network schematic'})
plt.close(fig)
