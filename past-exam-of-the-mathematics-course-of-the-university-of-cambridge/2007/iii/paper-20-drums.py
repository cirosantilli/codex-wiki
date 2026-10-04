"""Generate paper-20-drums.png in the caller's CWD with declared root dependencies."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.lines import Line2D


def permutations(dual=False):
    vectors=np.array([[(i>>j)&1 for j in range(3)] for i in range(1,8)],int)
    result=[]
    for i,j in [(0,1),(1,2),(2,0)]:
        matrix=np.eye(3,dtype=int);matrix[i,j]=1
        if dual:matrix=matrix.T
        result.append([next(k for k,w in enumerate(vectors) if np.array_equal(matrix@v%2,w)) for v in vectors])
    return result


def reflect(points,a,b):
    direction=(b-a)/np.linalg.norm(b-a)
    matrix=2*np.outer(direction,direction)-np.eye(2)
    return (points-a)@matrix+a


def assemble(actions):
    triangle=np.array([[0.,0.],[1.,0.],[.45,.82]])
    tiles={7:triangle};queue=[7]
    while queue:
        label=queue.pop(0)
        for side,p in enumerate(actions):
            target=p[label-1]+1
            if target!=label and target not in tiles:
                endpoints=[i for i in range(3) if i!=side]
                tiles[target]=reflect(tiles[label],*tiles[label][endpoints]);queue.append(target)
    assert len(tiles)==7
    return tiles


def main():
    fig,axes=plt.subplots(1,2,figsize=(12,6),dpi=96,facecolor='white')
    colors=['#bc3a31','#2c7a52','#3266a8']
    for ax,dual,title in zip(axes,[False,True],['Point action','Line action']):
        actions=permutations(dual);tiles=assemble(actions)
        for label,t in tiles.items():
            ax.add_patch(Polygon(t,facecolor='#fff1b3' if label==7 else '#edf1f6',edgecolor='none'))
            center=t.mean(axis=0);ax.text(*center,str(label),ha='center',va='center',fontsize=12)
            for side,p in enumerate(actions):
                endpoints=[i for i in range(3) if i!=side];edge=t[endpoints]
                if p[label-1]==label-1:ax.plot(*edge.T,color='#17232f',lw=2.4)
                elif label<p[label-1]+1:ax.plot(*edge.T,color=colors[side],lw=1.6)
        points=np.concatenate(list(tiles.values()));lo=points.min(axis=0);hi=points.max(axis=0)
        ax.set_xlim(lo[0]-.2,hi[0]+.2);ax.set_ylim(lo[1]-.2,hi[1]+.2)
        ax.set_aspect('equal');ax.axis('off');ax.set_title(title,fontsize=15)
    fig.suptitle('Two noncongruent domains with the same Dirichlet spectrum',fontsize=17,y=.96)
    fig.legend(handles=[Line2D([0],[0],color=c,lw=2,label=s)for c,s in zip(colors,['Side a gluing','Side b gluing','Side c gluing'])],loc='lower center',ncol=3,frameon=False)
    fig.subplots_adjust(left=.035,right=.965,bottom=.11,top=.87,wspace=.08)
    fig.savefig(Path.cwd()/'paper-20-drums.png',facecolor='white',transparent=False,dpi=96)
    plt.close(fig)


if __name__=='__main__':main()
