"""Original Schwarzschild causal diagrams; tested with Python 3.14.4.

Uses declared NumPy/Matplotlib dependencies. Output is the PNG basename in
caller CWD. The caller's MPLCONFIGDIR is preserved.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def main():
    fig, axes = plt.subplots(1, 2, figsize=(11.6, 5.3), dpi=120)
    fig.patch.set_facecolor('white')
    black, white, exterior = '#e1eaf5', '#f8eddc', '#eef4ef'
    ax = axes[0]
    x = np.linspace(-2.05, 2.05, 401)
    h = np.sqrt(1+x*x)
    ax.fill_between(x, abs(x), h, color=black)
    ax.fill_between(x, -h, -abs(x), color=white)
    ax.fill_between(x, -abs(x), abs(x), color=exterior)
    ax.plot(x, h, color='#9c332c', lw=2)
    ax.plot(x, -h, color='#9c332c', lw=2)
    ax.plot(x, x, '--', color='#535353', lw=1)
    ax.plot(x, -x, '--', color='#535353', lw=1)
    ax.scatter([0], [0], color='#333333', s=18, zorder=4)
    for X,T,label in [(1.35,0,'I: right exterior'),(-1.35,0,'III: left exterior'),
                       (0,.60,'II\nblack hole'),(0,-.60,'IV\nwhite hole')]:
        ax.text(X,T,label,ha='center',va='center',fontsize=10)
    ax.text(0,1.17,r'$r=0$: future singularity',ha='center',fontsize=9,color='#9c332c')
    ax.text(0,-1.28,r'$r=0$: past singularity',ha='center',fontsize=9,color='#9c332c')
    ax.annotate('',xy=(.5,.80),xytext=(1.05,.25),arrowprops={'arrowstyle':'->','color':'#236192','lw':1.5})
    ax.text(1.02,.62,'ingoing light',fontsize=8,color='#236192')
    ax.set(xlim=(-2.15,2.15),ylim=(-2.45,2.45),xlabel=r'$X_K$',ylabel=r'$T_K$')
    ax.set_title('Kruskal coordinates: horizons are regular',fontsize=12)
    ax.set_aspect('equal')
    ax.tick_params(labelsize=8)
    ax=axes[1]
    polygons=[([(0,0),(1,1),(2,0),(1,-1)],exterior),
              ([(0,0),(-1,1),(-2,0),(-1,-1)],exterior),
              ([(0,0),(-1,1),(1,1)],black),
              ([(0,0),(-1,-1),(1,-1)],white)]
    for points,color in polygons:ax.add_patch(Polygon(points,facecolor=color,edgecolor='none'))
    for side in [-1,1]:
        for time in [-1,1]:
            ax.plot([0,side],[0,time],'--',color='#535353',lw=1)
            ax.plot([side,2*side],[time,0],color='#236192',lw=1.5)
            label=r'$\mathcal{I}^+$' if time>0 else r'$\mathcal{I}^-$'
            ax.text(1.62*side,.65*time,label,ha='center',va='center',fontsize=12,color='#236192')
    sx=np.linspace(-1,1,101)
    for sign in [-1,1]:
        zig=sign*(1+.025*np.where(np.arange(len(sx))%2==0,1,-1))
        ax.plot(sx,zig,color='#9c332c',lw=1.7)
    for X,T,label in [(1.1,0,'I: right exterior'),(-1.1,0,'III: left exterior'),
                       (0,.58,'II: black hole'),(0,-.58,'IV: white hole')]:
        ax.text(X,T,label,ha='center',va='center',fontsize=10)
    ax.text(0,1.17,'spacelike future singularity',ha='center',color='#9c332c',fontsize=9)
    ax.text(0,-1.21,'spacelike past singularity',ha='center',color='#9c332c',fontsize=9)
    ax.text(2.08,0,r'$i^0$',ha='left',va='center',fontsize=11)
    ax.text(-2.08,0,r'$i^0$',ha='right',va='center',fontsize=11)
    ax.scatter([0],[0],color='#333333',s=18,zorder=4)
    ax.annotate('future',xy=(2.12,.98),xytext=(2.12,.48),ha='center',fontsize=9,
                arrowprops={'arrowstyle':'->','color':'#333333'})
    ax.set(xlim=(-2.4,2.4),ylim=(-1.4,1.4))
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('Penrose diagram: null infinities compactified',fontsize=12,pad=22)
    fig.suptitle('The maximal Schwarzschild extension',fontsize=15,y=.98)
    fig.text(.5,.025,'Dashed lines: horizons. Each diagram point represents a symmetry two-sphere.',
             ha='center',fontsize=9)
    fig.tight_layout(rect=(0,.055,1,.93),w_pad=1.8)
    output=Path(Path(__file__).with_suffix('.png').name)
    fig.savefig(output,facecolor='white',transparent=False)
    plt.close(fig)
    print(output)


if __name__=='__main__':main()
