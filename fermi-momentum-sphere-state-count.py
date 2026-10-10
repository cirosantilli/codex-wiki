"""Original zero-temperature state-count diagram; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Run from _media; writes fermi-momentum-sphere-state-count.png to the current directory.
The displayed lattice is schematic, with arbitrary spacing, not experimental data.
"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle
import numpy as np

plt.rcParams.update({'font.size': 11, 'figure.facecolor': 'white', 'axes.facecolor': 'white'})
fig = plt.figure(figsize=(11, 5.5), dpi=110)
ax = fig.add_subplot(121, projection='3d')
u = np.linspace(0, 2*np.pi, 60)
v = np.linspace(0, np.pi, 35)
ax.plot_surface(np.outer(np.cos(u), np.sin(v)), np.outer(np.sin(u), np.sin(v)),
                np.outer(np.ones_like(u), np.cos(v)), color='#5ca9d6', alpha=.23,
                linewidth=0, shade=False)
for z in [-.6, 0, .6]:
    r = np.sqrt(1-z*z)
    ax.plot(r*np.cos(u), r*np.sin(u), np.full_like(u,z), color='#27789f', lw=.8, alpha=.8)
points = np.array([(x,y,z) for x in np.arange(-.8, .81, .4)
                   for y in np.arange(-.8, .81, .4) for z in np.arange(-.8, .81, .4)
                   if x*x+y*y+z*z < 1])
ax.scatter(*points.T, s=9, color='#145b87', alpha=.55, depthshade=False)
ax.quiver(0,0,0,1,0,0,color='#bc5722',arrow_length_ratio=.13,linewidth=2)
ax.text(.45,-.04,.13,r'$p_F$',color='#9a441a',fontsize=13)
ax.set(xlabel=r'$p_x/p_F$',ylabel=r'$p_y/p_F$',zlabel=r'$p_z/p_F$',
       xlim=(-1.15,1.15),ylim=(-1.15,1.15),zlim=(-1.15,1.15))
ax.set_xticks([-1,0,1]); ax.set_yticks([-1,0,1]); ax.set_zticks([-1,0,1])
ax.set_box_aspect((1,1,1)); ax.view_init(elev=20,azim=-58)
ax.set_title('Filled sphere in momentum space',pad=17)
fig.text(.065,.09,'Each point: two occupied spin states\nInterior filled; exterior empty',fontsize=11)

bx = fig.add_subplot(122)
q = np.arange(-1.2,1.21,.3)
x,y = np.meshgrid(q,q)
inside = x*x+y*y < 1+1e-12
bx.scatter(x[~inside],y[~inside],s=25,facecolors='white',edgecolors='#a2aab0',zorder=3)
bx.scatter(x[inside],y[inside],s=25,color='#145b87',zorder=3)
bx.add_patch(Circle((0,0),1,color='#e6f1f8'))
bx.add_patch(Circle((0,0),1,fill=False,ec='#27789f',lw=1.5))
bx.axhline(0,color='#c5cbd0',lw=.8);bx.axvline(0,color='#c5cbd0',lw=.8)
bx.add_patch(Rectangle((.15,.15),.3,.3,fill=False,ec='#bc5722',lw=1.8,zorder=4))
bx.annotate(r'$\Delta p=2\pi\hbar/L$',xy=(.3,.45),xytext=(.38,.88),
            arrowprops={'arrowstyle':'->','color':'#bc5722'},fontsize=11)
bx.set(xlim=(-1.4,1.4),ylim=(-1.4,1.4),xlabel=r'$p_x/p_F$',ylabel=r'$p_y/p_F$')
bx.set_xticks([-1,0,1]);bx.set_yticks([-1,0,1]);bx.set_aspect('equal')
bx.set_title(r'A lattice slice ($p_z=0$)',pad=17)
fig.text(.61,.065,r'Cell volume in 3D: $(2\pi\hbar/L)^3$'+'\n'+
        r'$N\simeq 2\,\dfrac{4\pi p_F^3/3}{(2\pi\hbar/L)^3}$',fontsize=12)
fig.suptitle('Zero temperature: count occupied states, including spin',fontsize=15,y=.98)
fig.subplots_adjust(left=.03,right=.97,top=.85,bottom=.30,wspace=.25)
fig.savefig(Path.cwd()/'fermi-momentum-sphere-state-count.png',facecolor='white')
plt.close(fig)
