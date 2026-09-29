"""Original diagrams. Tested with Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

plt.rcParams.update({'font.size': 12, 'mathtext.fontset': 'dejavusans'})
fig, axes = plt.subplots(3, 2, figsize=(10.6, 9.0), facecolor='white')

def setup(ax, title):
    ax.set(xlim=(0, 1), ylim=(0, 1), aspect='auto')
    ax.axis('off')
    ax.set_title(title, loc='left', fontsize=13, pad=5)

def line(ax, a, b, scalar=False, label='', offset=(0, .055)):
    ax.plot([a[0], b[0]], [a[1], b[1]], color='#20252b', lw=1.7,
            linestyle=(0, (4, 3)) if scalar else '-')
    # Scalar arrows denote momentum only; solid arrows denote fermion flow.
    mid = tuple((x+y)/2 for x, y in zip(a, b))
    d = tuple((y-x)*.10 for x, y in zip(a, b))
    ax.add_patch(FancyArrowPatch((mid[0]-d[0], mid[1]-d[1]),
                                (mid[0]+d[0], mid[1]+d[1]),
                                arrowstyle='-|>', mutation_scale=12,
                                color='#416a9b' if scalar else '#20252b', lw=1.0))
    if label:
        ax.text(mid[0]+offset[0], mid[1]+offset[1], label,
                ha='center', va='center', fontsize=11,
                bbox={'facecolor':'white','edgecolor':'none','pad':1})

def dot(ax, p, label):
    ax.plot(*p, 'o', color='#20252b', ms=4)
    ax.text(p[0], p[1]-.11, label, ha='center', fontsize=11)

ax = axes[0, 0]
setup(ax, '(i) Fermion–fermion scattering')
a, b = (.34, .5), (.69, .5)
line(ax, (.04,.88), a, label=r'$\Psi,p_1$', offset=(-.035,.04))
line(ax, a, (.04,.12), label=r'$\chi,p_4$', offset=(-.035,-.04))
line(ax, (.97,.12), b, label=r'$\chi,p_2$', offset=(.035,-.04))
line(ax, b, (.97,.88), label=r'$\Psi,p_3$', offset=(.035,.04))
line(ax, a, b, True, r'$q=p_1-p_4$', (0,.10))
dot(ax, a, '$g$'); dot(ax, b, '$g$')

for ax, tag, u in [(axes[0,1], '(ii) First ordering', False),
                   (axes[1,0], '(ii) Second ordering', True)]:
    setup(ax, tag)
    a,b = (.34,.38),(.69,.38)
    line(ax,(.03,.38),a,label=r'$\Psi,p_1$',offset=(0,-.13))
    line(ax,a,b,label=r'$\chi,p_1-k_2$' if u else r'$\chi,p_1+k_1$',offset=(0,-.17))
    line(ax,b,(.98,.38),label=r'$\Psi,p_2$',offset=(0,-.13))
    if u:
        line(ax,a,(.08,.93),True,r'$k_2$',(-.03,.02))
        line(ax,(.95,.93),b,True,r'$k_1$',(.03,.02))
    else:
        line(ax,(.08,.93),a,True,r'$k_1$',(-.03,.02))
        line(ax,b,(.95,.93),True,r'$k_2$',(.03,.02))
    dot(ax,a,'$g$');dot(ax,b,'$g$')

ax=axes[1,1]
setup(ax,'(iii) Two-body decay')
a=(.48,.5)
line(ax,(.04,.5),a,label=r'$\Psi,p_1$',offset=(0,.09))
line(ax,a,(.94,.12),label=r'$\chi,p_2$',offset=(.025,-.065))
line(ax,a,(.94,.88),True,r'$\phi,p_3$',(.025,.065))
dot(ax,a,'$g$')

ax=axes[2,0]
setup(ax,'(iv) Three-body decay')
a,b=(.35,.5),(.69,.73)
line(ax,(.02,.5),a,label=r'$\Psi,p_1$',offset=(0,.09))
line(ax,a,(.58,.08),label=r'$\chi,p_2$',offset=(-.02,-.055))
line(ax,a,b,True,r'$q=k_1+k_2$',(-.025,.15))
line(ax,b,(.96,.95),True,r'$k_1$',(.04,-.05))
line(ax,b,(.96,.5),True,r'$k_2$',(.04,.05))
dot(ax,a,'$g$');dot(ax,b,r'$\lambda$')

ax=axes[2,1]
setup(ax,'Line and arrow conventions')
line(ax,(.12,.75),(.65,.75),label='')
ax.text(.12,.57,'Solid: fermion flow',fontsize=12)
line(ax,(.12,.37),(.65,.37),True)
ax.text(.12,.19,'Dashed: scalar; blue arrow: momentum',fontsize=11)
fig.tight_layout(pad=1.7,h_pad=2.2,w_pad=2.5)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,
            dpi=120,facecolor='white',transparent=False)
plt.close(fig)
