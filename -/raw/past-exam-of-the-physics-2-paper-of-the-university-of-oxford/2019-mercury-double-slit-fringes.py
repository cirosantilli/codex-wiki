"""Original double-slit layout and two-line fringes; Python 3.14, NumPy/Matplotlib."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse, Rectangle

plt.rcParams.update({'font.size':11, 'axes.spines.top':False, 'axes.spines.right':False})
fig = plt.figure(figsize=(10, 7.2), layout='constrained', facecolor='white')
grid = fig.add_gridspec(3, 1, height_ratios=[1.25, 1.8, 0.7])
layout = fig.add_subplot(grid[0])
layout.set(xlim=(-0.35, 9.2), ylim=(-1.5, 1.7), title='Practical layout (schematic; not to scale)')
layout.axis('off')
layout.text(0, 0, 'Hg\nlamp', ha='center', va='center', bbox={'boxstyle':'round', 'fc':'#eeeeee', 'ec':'#777777'})
for x, label in [(1.2, 'Narrow\nsource slit'), (3.8, 'Green\nfilter'), (5.2, 'Double\nslit'), (8.5, 'Screen')]:
    if x == 1.2:
        for lo, hi in [(-0.9,-0.05),(0.05,0.9)]:
            layout.plot([x,x],[lo,hi],color='#444444',lw=4)
    elif x == 5.2:
        for lo, hi in [(-0.9,-0.3),(-0.2,0.2),(0.3,0.9)]:
            layout.plot([x,x],[lo,hi],color='#444444',lw=4)
    elif x == 3.8:
        layout.add_patch(Rectangle((x-0.07,-0.8),0.14,1.6,facecolor='#86b68a',edgecolor='#333333'))
    else:
        layout.plot([x,x],[-1,1],color='#444444',lw=4)
    layout.text(x,-1.03,label,ha='center',va='top')
layout.add_patch(Ellipse((2.5,0),0.22,1.75,facecolor='#d7e8ef',edgecolor='#446677'))
layout.text(2.5,1.04,'Collimating lens',ha='center')
for sign in [-1,1]:
    layout.plot([1.2,2.5,5.2],[0,sign*0.25,sign*0.25],color='#378c45',lw=1)
    for target in [-0.75,0,0.75]:
        layout.plot([5.2,8.5],[sign*0.25,target],color='#378c45',lw=0.8,alpha=0.7)
layout.annotate('',xy=(8.5,1.25),xytext=(5.2,1.25),arrowprops={'arrowstyle':'<->','color':'#444444'})
layout.text(6.85,1.35,r'$D$',ha='center')
ax = fig.add_subplot(grid[1])
y = np.linspace(-15,15,5001)
g = np.cos(np.pi*y/2.730)**2
b = np.cos(np.pi*y/2.185)**2
ax.plot(y,g,color='#25864b',label='546 nm; spacing 2.730 mm',lw=1.3)
ax.plot(y,b,color='#315bd2',label='437 nm; spacing 2.185 mm',lw=1.3)
ax.plot(y,g+b,color='#252525',label='Sum (equal illustrative peak intensities)',lw=1.7)
ax.set(xlim=(-15,15),ylim=(0,2.2),ylabel='Relative intensity',xlabel='Screen position (mm)')
ax.set_xticks(np.arange(-15,16,3))
ax.grid(alpha=0.2)
ax.legend(loc='upper center',ncol=1,fontsize=9)
strip = fig.add_subplot(grid[2])
colors = np.zeros((32,y.size,3))
colors[:,:,1] = 0.9*g
colors[:,:,2] = b
strip.imshow(colors,extent=(-15,15,0,1),origin='lower',aspect='auto')
strip.set(xlim=(-15,15),xlabel='Illustrative additive colour; actual line strengths are unspecified',yticks=[],xticks=np.arange(-15,16,3))
fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name, dpi=120, facecolor='white', transparent=False)
