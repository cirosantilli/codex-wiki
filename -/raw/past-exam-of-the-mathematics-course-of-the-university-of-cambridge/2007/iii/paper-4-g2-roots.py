"""G2 roots and fundamental weights. Python 3.14, NumPy 2.3.5,
Matplotlib 3.10.7. Output paper-4-g2-roots.png to CWD; preserves MPLCONFIGDIR.
"""
import os
import tempfile
os.environ.setdefault('MPLCONFIGDIR', tempfile.gettempdir()+'/codex-wiki-matplotlib')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np


def main():
    a1=np.array([1.,0.]);a2=np.array([-1.5,np.sqrt(3)/2])
    pairs=[(1,0),(0,1),(1,1),(2,1),(3,1),(3,2)]
    fig,ax=plt.subplots(figsize=(6.6,6.6),constrained_layout=True)
    for u,v in pairs:
        positive=u*a1+v*a2
        color='#2677a9' if np.dot(positive,positive)<2 else '#aa482b'
        for sign in [-1,1]:
            point=sign*positive
            ax.annotate('',point,(0,0),arrowprops=dict(arrowstyle='->',lw=1.7,color=color))
            ax.scatter(*point,color=color,s=35)
    w1=2*a1+a2;w2=3*a1+2*a2
    for point,label,offset in [(w1,r'$\omega_1=2\alpha_1+\alpha_2$',(12,12)),(w2,r'$\omega_2=3\alpha_1+2\alpha_2$',(14,2))]:
        ax.scatter(*point,marker='*',s=160,color='#248347',edgecolor='white',zorder=5)
        ax.annotate(label,point,xytext=offset,textcoords='offset points',color='#136332',fontsize=11)
    ax.annotate(r'$\alpha_1$',a1,xytext=(8,-20),textcoords='offset points',fontsize=13)
    ax.annotate(r'$\alpha_2$',a2,xytext=(-25,12),textcoords='offset points',fontsize=13)
    ax.axhline(0,color='#bbbbbb',lw=.7);ax.axvline(0,color='#bbbbbb',lw=.7)
    ax.scatter(0,0,color='black',s=15)
    ax.set(xlim=(-2,2.5),ylim=(-2.05,2.05));ax.set_aspect('equal')
    ax.set_title('G2 root system: short root numbered first')
    ax.legend(handles=[Line2D([0],[0],color='#2677a9',label='6 short roots'),Line2D([0],[0],color='#aa482b',label='6 long roots'),Line2D([0],[0],marker='*',color='#248347',lw=0,label='Fundamental weights')],loc='lower right')
    ax.set_xticks([]);ax.set_yticks([])
    fig.savefig('paper-4-g2-roots.png',dpi=135,facecolor='white',transparent=False)
    plt.close(fig)


if __name__=='__main__':main()
