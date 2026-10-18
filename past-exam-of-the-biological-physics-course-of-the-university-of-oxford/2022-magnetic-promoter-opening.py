"""Original magnetic-tweezer schematic; Python 3.14, numpy 2.3.5, matplotlib 3.10.7."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle

fig, axes = plt.subplots(1, 2, figsize=(10, 4.4), layout='constrained')
a = axes[0]
a.set(xlim=(0, 1), ylim=(0, 1), title='Torsionally constrained tether')
a.axis('off')
a.add_patch(Rectangle((.1, .03), .8, .055, color='0.65'))
a.text(.5, .0, 'fixed surface', ha='center', va='top')
z = np.linspace(.09, .60, 240)
a.plot(.46+.028*np.sin(z*76), z, color='#2563a6', lw=2)
a.plot(.46-.028*np.sin(z*76), z, color='#b74732', lw=2)
a.add_patch(Circle((.46, .70), .10, color='#d4a72c', ec='black'))
a.text(.65, .70, 'magnetic bead', va='center')
a.annotate('', xy=(.46, .97), xytext=(.46, .84), arrowprops={'arrowstyle':'->'})
a.text(.60, .91, 'field gradient:\nupward force', va='center')
a.annotate('rotation controls turns', xy=(.36, .76), xytext=(.02, .87), arrowprops={'arrowstyle':'->'})
a.add_patch(Circle((.46, .35), .047, color='#388650'))
a.annotate('RNAP opening\none local turn', xy=(.5, .35), xytext=(.65, .36), arrowprops={'arrowstyle':'->'})
a.annotate('', xy=(.17, .69), xytext=(.17, .085), arrowprops={'arrowstyle':'<->'})
a.text(.14, .39, 'height', rotation=90, va='center', ha='right')
b = axes[1]
t = np.array([0, 1.9, 2, 5.9, 6, 8])
b.plot(t, [0, 0, 1, 1, 0, 0], lw=2, label='negative supercoiling')
b.plot(t, [0, 0, -1, -1, 0, 0], lw=2, label='positive supercoiling')
b.axhline(0, color='0.6', lw=.7)
b.axvspan(2, 6, alpha=.1, color='green')
b.text(4, 1.18, 'promoter open', ha='center')
b.set(xlabel='time (schematic)', ylabel='height change (arbitrary units)', title='Unwinding signal at fixed linking number', ylim=(-1.55, 1.5))
b.legend(loc='lower center', fontsize=9)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name, dpi=130, facecolor='white', transparent=False)
plt.close(fig)
