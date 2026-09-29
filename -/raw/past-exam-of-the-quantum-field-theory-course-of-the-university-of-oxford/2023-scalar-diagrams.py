"""Original QFT diagrams; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(11.2, 7.8), facecolor='white', layout='constrained')
grid = fig.add_gridspec(2, 6)
axes = [fig.add_subplot(grid[0, :2]), fig.add_subplot(grid[0, 2:4]),
        fig.add_subplot(grid[0, 4:]), fig.add_subplot(grid[1, 1:3]),
        fig.add_subplot(grid[1, 3:5])]
ink = '#16334c'

def line(ax, a, b, heavy=False, arrow=True):
    a, b = np.asarray(a), np.asarray(b)
    ax.plot([a[0], b[0]], [a[1], b[1]], color=ink, lw=1.8,
            ls=(0, (4, 2.5)) if heavy else '-')
    if arrow:
        mid = (a+b)/2
        delta = (b-a)*.13
        ax.annotate('', xy=mid+delta, xytext=mid-delta,
                    arrowprops=dict(arrowstyle='-|>', color=ink, lw=1.5,
                                    mutation_scale=11))

def vertex(ax, p):
    ax.plot(*p, 'o', ms=4.3, color=ink)

def label(ax, p, s, **kw):
    ax.text(*p, s, ha='center', va='center', fontsize=11, color=ink, **kw)

for ax in axes:
    ax.set(xlim=(-1.4, 1.4), ylim=(-1.22, 1.3), aspect='equal')
    ax.axis('off')

ax = axes[0]
line(ax, (-1.1, -.45), (0, -.45), arrow=False)
line(ax, (0, -.45), (1.1, -.45), arrow=False)
t = np.linspace(-np.pi/2, 3*np.pi/2, 220)
ax.plot(.46*np.cos(t), .20+.65*np.sin(t), color=ink, lw=1.8)
vertex(ax, (0, -.45))
label(ax, (-.9, -.68), '$p$'); label(ax, (.9, -.68), '$p$')
label(ax, (.68, .6), '$k$')
ax.set_title('(a) One-loop tadpole\nreal scalar in 1+1 dimensions', fontsize=11)

ax = axes[1]; a=(-.38,0); b=(.38,0)
for p in [(-1.12,.65),(-1.12,-.65)]: line(ax,p,a)
line(ax,a,b,heavy=True)
for p in [(1.12,.65),(1.12,-.65)]: line(ax,b,p)
for p in [a,b]: vertex(ax,p)
label(ax,(-1.08,.9),'$\\phi_1$');label(ax,(-1.08,-.9),'$\\phi_2$')
label(ax,(1.08,.9),'$\\phi_3$');label(ax,(1.08,-.9),'$\\phi_4$')
label(ax,(0,.27),'$\\Phi$')
ax.set_title('(b) Light particles\n$s$-channel exchange',fontsize=11)

ax = axes[2]; a=(0,.48);b=(0,-.48)
line(ax,(-1.12,.78),a);line(ax,(1.12,.78),a)
line(ax,a,b,heavy=True)
line(ax,b,(-1.12,-.78));line(ax,b,(1.12,-.78))
for p in [a,b]:vertex(ax,p)
label(ax,(-1.12,1.03),'$\\phi_1$');label(ax,(1.12,1.03),'$\\bar\\phi_4$')
label(ax,(-1.12,-1.03),'$\\bar\\phi_2$');label(ax,(1.12,-1.03),'$\\phi_3$')
label(ax,(.3,0),'$\\Phi$')
ax.set_title('(c) Light particle–antiparticle\n$u$-channel exchange',fontsize=11)

for ax, mixed in zip(axes[3:], [False,True]):
    a=(-.53,.5);b=(.53,.5);c=(.53,-.5);d=(-.53,-.5)
    for start,end in [(a,b),(a,d),(c,b),(c,d)]:line(ax,start,end)
    ends=[(-1.12,.94),(1.12,.94),(1.12,-.94),(-1.12,-.94)]
    for p,end,source in zip([a,b,c,d],ends,[True,False,True,False]):
        line(ax,end,p,heavy=True) if source else line(ax,p,end,heavy=True)
        vertex(ax,p)
    texts=['$\\Phi_1$ in','$\\Phi_3$ out',
           '$\\bar\\Phi_4$ out' if mixed else '$\\Phi_2$ in',
           '$\\bar\\Phi_2$ in' if mixed else '$\\Phi_4$ out']
    for end,s in zip(ends,texts):label(ax,(end[0]*.83,end[1]+(.19 if end[1]>0 else -.19)),s)
    ax.set_title('(e) Heavy particle–antiparticle box' if mixed else '(d) Heavy-particle box',fontsize=11)
fig.suptitle('Positive charge follows each arrow: solid = 1, dashed = 2', fontsize=13, color=ink)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name, dpi=115, facecolor='white', transparent=False)
plt.close(fig)
