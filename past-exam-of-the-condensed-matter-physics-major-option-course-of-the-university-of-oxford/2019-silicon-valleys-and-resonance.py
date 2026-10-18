"""Original schematic; Python 3.14, NumPy, Matplotlib. Sole output: CWD/basename.png."""
from pathlib import Path
from itertools import permutations, product
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11})
fig=plt.figure(figsize=(14.4,4.8),dpi=100,facecolor='white')
vertices=np.array(sorted({tuple(s*np.array(p)) for p in permutations([0.,.5,1.]) for s in map(np.array,product([-1,1],repeat=3))}))


def zone(ax):
    for i,a in enumerate(vertices):
        for b in vertices[i+1:]:
            if abs(np.linalg.norm(a-b)-np.sqrt(.5))<1e-8:
                ax.plot(*np.array([a,b]).T,color='#97a3ad',lw=.6,alpha=.65)
    for j,label in enumerate(['$k_x$','$k_y$','$k_z$']):
        end=np.zeros(3);end[j]=1.22
        ax.plot(*np.array([np.zeros(3),end]).T,color='#283e50',lw=.9)
        ax.text(*end,label,fontsize=10)
        point=np.zeros(3);point[j]=1.04
        ax.text(*point,'X',fontsize=9)
    ax.text(0,0,-.12,r'$\Gamma$',fontsize=11)
    ax.set(xlim=(-1.12,1.25),ylim=(-1.12,1.25),zlim=(-1.12,1.25))
    ax.set_box_aspect((1,1,1));ax.set_axis_off();ax.view_init(22,35)


def ellipsoid(ax,center,radii,color):
    u=np.linspace(0,2*np.pi,30);v=np.linspace(0,np.pi,18)
    xx=np.outer(np.cos(u),np.sin(v));yy=np.outer(np.sin(u),np.sin(v));zz=np.outer(np.ones_like(u),np.cos(v))
    ax.plot_surface(center[0]+radii[0]*xx,center[1]+radii[1]*yy,center[2]+radii[2]*zz,color=color,alpha=.9,linewidth=0,shade=True)


ax=fig.add_subplot(131,projection='3d');zone(ax)
for j in range(3):
    for sign in [-1,1]:
        center=np.zeros(3);center[j]=sign*.80
        radii=np.full(3,.075);radii[j]=.164
        ellipsoid(ax,center,radii,'#267daf')
ax.set_title('Electron-doped Si: six valleys',pad=2)
ax.text2D(.1,.01,r'Schematic pockets; axes in $2\pi/a$',transform=ax.transAxes,fontsize=9)
ax=fig.add_subplot(132,projection='3d');zone(ax)
ellipsoid(ax,np.zeros(3),np.array([.34,.34,.34]),'#cf6c34')
ax.set_title(r'Lower $\mu$: hole surface about $\Gamma$',pad=2)
ax.text2D(.08,.01,'Schematic: resolved valence sheets omitted',transform=ax.transAxes,fontsize=9)
ax=fig.add_subplot(133)
field=np.linspace(0,2.8,900);center=1.40;width=.10
absorption=1/(1+((field-center)/width)**2)
ax.plot(field,absorption,color='#247eac',lw=2)
ax.axvline(center,ls='--',lw=1,color='#6d7980')
ax.text(center+.10,.9,'1.4 T',fontsize=12)
ax.set(xlabel='$|B|$ (T)',ylabel='Normalized absorption',xlim=(0,2.8),ylim=(0,1.1),title=r'$\mathbf{B}\parallel[111]$: one resonance')
ax.text(.05,.95,'Illustrative linewidth',transform=ax.transAxes,va='top',fontsize=10)
ax.spines[['top','right']].set_visible(False)
fig.tight_layout(pad=1.8)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,facecolor='white',transparent=False,metadata={'Software':'Matplotlib'})
plt.close(fig)
