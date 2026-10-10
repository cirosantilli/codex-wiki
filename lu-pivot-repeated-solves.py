"""Original zero-pivot and reusable triangular-solve diagram.

Writes its matching PNG in the CWD. Tested with Python 3.14,
Matplotlib 3.10.7 and NumPy 2.3.5. Run from _media with Agg.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch
import numpy as np


def matrix(ax, x, y, values, label, highlight=None):
    cell = 0.53
    ax.text(x+cell,y+0.35,label,ha='center',fontsize=14)
    for i,row in enumerate(values):
        for j,value in enumerate(row):
            color = '#ffe2a1' if (i,j)==highlight else '#f2f6fa'
            ax.add_patch(Rectangle((x+j*cell,y-(i+1)*cell),cell,cell,
                                   facecolor=color,edgecolor='#b9c4cf'))
            ax.text(x+(j+0.5)*cell,y-(i+0.5)*cell,str(value),
                    ha='center',va='center',fontsize=16,color='#172c40')


def box(ax, x, y, w, h, text, color):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.04',
                               facecolor=color,edgecolor='#7d98ab',lw=1.1))
    ax.text(x+w/2,y+h/2,text,ha='center',va='center',fontsize=12)


def main():
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12})
    a=np.array([[0,1],[2,3]]); p=np.array([[0,1],[1,0]])
    l=np.eye(2,dtype=int); u=np.array([[2,3],[0,1]])
    b=np.array([[1,-1,1],[5,-3,7]]); x=np.array([[1,0,2],[1,-1,1]])
    assert np.array_equal(p @ a,l @ u)
    assert np.array_equal(a @ x,b)
    fig,ax=plt.subplots(figsize=(9.4,6.3),facecolor='white')
    fig.subplots_adjust(left=0.015,right=0.985,bottom=0.025,top=0.97)
    ax.set(xlim=(0,9.4),ylim=(0,6.3)); ax.axis('off')
    ax.text(4.7,6.0,'A row swap fixes a zero pivot; reuse the factors for every b',
            ha='center',fontsize=16,fontweight='bold',color='#172c40')
    matrix(ax,0.6,5.2,a,'$A_0$',highlight=(0,0))
    ax.text(1.13,3.9,'First pivot is zero,\nbut det A₀ = −2.',ha='center',va='top',fontsize=11,color='#6d4908')
    ax.annotate('',xy=(4.0,4.65),xytext=(1.9,4.65),arrowprops={'arrowstyle':'->','lw':2,'color':'#31678d'})
    ax.text(3.0,5.05,'Swap rows 1 and 2',ha='center',fontsize=12)
    ax.text(3.0,4.2,'$P$ records the swap',ha='center',fontsize=11)
    matrix(ax,4.2,5.2,u,'$PA_0=U$',highlight=(0,0))
    matrix(ax,6.15,5.2,l,'$L=I$')
    ax.text(8.0,4.65,'$PA_0=LU$\n\nFactor once',ha='center',va='center',fontsize=13)
    ax.plot([0.4,9.0],[3.45,3.45],color='#d8dee5')
    ax.text(4.7,3.16,'Use the same P, L and U on each row below',ha='center',fontsize=13,color='#31678d')
    box(ax,0.45,2.48,1.4,0.4,'Input b','#ffffff')
    box(ax,2.4,2.48,1.4,0.4,'Permute: Pb','#eef4fa')
    box(ax,4.38,2.48,1.78,0.4,'Forward: Ly = Pb','#e7f2ed')
    box(ax,6.77,2.48,2.05,0.4,'Back: Ux = y','#eef4fa')
    for x0,x1 in [(1.92,2.31),(3.88,4.29),(6.24,6.67)]:
        ax.annotate('',xy=(x1,2.68),xytext=(x0,2.68),arrowprops={'arrowstyle':'->','lw':1.6,'color':'#31678d'})
    for j,y in enumerate([2.03,1.46,0.89]):
        texts=[f'({b[0,j]}, {b[1,j]})ᵀ',f'({b[1,j]}, {b[0,j]})ᵀ',
               f'({b[1,j]}, {b[0,j]})ᵀ',f'({x[0,j]}, {x[1,j]})ᵀ']
        for mid,t in zip([1.15,3.1,5.27,7.8],texts):
            ax.text(mid,y,t,ha='center',va='center',fontsize=14)
        ax.plot([0.45,8.82],[y-0.26,y-0.26],color='#e1e7ed',lw=0.8)
    ax.text(4.7,0.27,'Here L = I, so y = Pb. In general, forward substitution also does arithmetic.',
            ha='center',fontsize=11,color='#52606d')
    fig.savefig(Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white',transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
