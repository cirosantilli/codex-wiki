"""B-type Dynkin diagrams. Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Writes paper-4-dynkin-diagrams.png to caller CWD, preserving MPLCONFIGDIR.
"""
import os
import tempfile
os.environ.setdefault('MPLCONFIGDIR', tempfile.gettempdir() + '/codex-wiki-matplotlib')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np


def bond(ax, a, b, double=False, arrow=False, dashed=False):
    a, b = np.array(a, float), np.array(b, float)
    direction = (b-a)/np.linalg.norm(b-a)
    side = np.array([-direction[1], direction[0]])
    for offset in ([-.045, .045] if double else [0]):
        ends = np.array([a+.13*direction+offset*side, b-.13*direction+offset*side])
        ax.plot(ends[:,0], ends[:,1], color='black', lw=1.5, ls='--' if dashed else '-')
    if arrow:
        tip = a+.62*(b-a)
        left = tip-.17*direction+.105*side
        right = tip-.17*direction-.105*side
        ax.plot([left[0], tip[0], right[0]], [left[1], tip[1], right[1]], color='black', lw=1.5)


def nodes(ax, positions):
    for label, point in positions.items():
        ax.add_patch(Circle(point, .13, edgecolor='black', facecolor='white', lw=1.5, zorder=3))
        ax.text(point[0], point[1]-.31, '$'+label+'$', ha='center', va='top', fontsize=12)


def draw(ax, rank, affine):
    if rank == 'general':
        p = {'\\alpha_1':(0,0), '\\alpha_2':(1.1,0), '\\alpha_{n-1}':(3.1,0), '\\alpha_n':(4.2,0)}
        bonds=[('\\alpha_1','\\alpha_2',False,False,False),('\\alpha_2','\\alpha_{n-1}',False,False,True),('\\alpha_{n-1}','\\alpha_n',True,True,False)]
        ax.text(2.1,.08,r'$\cdots$',ha='center',fontsize=14)
        title=r'$B_n$, $n\geq4$'
    else:
        p={f'\\alpha_{i}':(1.35*(i-1),0) for i in range(1,rank+1)}
        bonds=[(f'\\alpha_{i}',f'\\alpha_{i+1}',i==rank-1, i==rank-1,False) for i in range(1,rank)]
        title=f'$B_{rank}$' if rank>1 else r'$B_1=A_1$'
    if affine:
        if rank == 1:
            p['\\alpha_0']=(-1.35,0)
            bonds.append(('\\alpha_0','\\alpha_1',True,False,False))
        elif rank == 2:
            p={'\\alpha_0':(-1.35,0),'\\alpha_2':(0,0),'\\alpha_1':(1.35,0)}
            bonds=[('\\alpha_0','\\alpha_2',True,True,False),('\\alpha_1','\\alpha_2',True,True,False)]
        else:
            p['\\alpha_0']=(p['\\alpha_1'][0],.95)
            p['\\alpha_1']=(p['\\alpha_1'][0],-.8)
            bonds.append(('\\alpha_0','\\alpha_2',False,False,False))
        title+=': affine extension'
    for a,b,double,arrow,dashed in bonds:bond(ax,p[a],p[b],double,arrow,dashed)
    nodes(ax,p)
    xs=[a[0] for a in p.values()]
    ax.set_xlim(min(xs)-.5,max(xs)+.5)
    ax.set_ylim(-1.4,1.5)
    ax.set_aspect('equal')
    ax.set_title(title,fontsize=12)
    ax.axis('off')


def main():
    fig,axes=plt.subplots(4,2,figsize=(10,8),constrained_layout=True)
    for row,rank in enumerate(['general',3,2,1]):
        draw(axes[row,0],rank,False)
        draw(axes[row,1],rank,True)
    fig.suptitle('Double bonds point toward short roots; rank-one roots have equal length',fontsize=13)
    fig.savefig('paper-4-dynkin-diagrams.png',dpi=130,facecolor='white',transparent=False)
    plt.close(fig)


if __name__=='__main__':main()
