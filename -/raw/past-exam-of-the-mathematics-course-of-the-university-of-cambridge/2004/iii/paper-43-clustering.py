"""Python 3.14, NumPy 2.3 and Matplotlib 3.10. Output PNG basename to caller cwd.
Uses caller MPLCONFIGDIR unchanged. Exact Jaccard/complete-linkage calculation.
Ties are resolved by original row order; other tied trees are also valid.
"""
from fractions import Fraction
import numpy as np
import matplotlib.pyplot as plt

NAMES = ['Taeko','Luitgard','Alet','Tom','LinYee','Pio','LingChen','HuiChin','Martin','Nicolas','Mohammad','Meg']
DATA = np.array([[1,1,0,1,1,1,0,0,0],[0,1,0,0,1,1,1,1,0],
 [1,1,1,0,0,1,0,1,0],[1,1,1,1,1,0,1,1,0],[1,1,0,0,0,0,1,1,0],
 [1,1,0,0,0,0,1,0,0],[1,0,0,0,0,1,1,0,0],[1,1,0,0,0,1,1,1,0],
 [1,1,1,1,0,0,1,1,0],[1,1,1,0,0,0,1,1,1],[1,1,0,0,0,0,0,1,0],
 [1,1,0,0,0,1,1,0,0]], dtype=bool)


def exact_distances():
    return [[Fraction(int(np.count_nonzero(x != y)), int(np.count_nonzero(x | y)))
             for y in DATA] for x in DATA]


def merges():
    distances = exact_distances()
    clusters = {i:(i,) for i in range(len(NAMES))}
    history = []
    for new_id in range(len(NAMES), 2*len(NAMES)-1):
        keys = sorted(clusters)
        candidates = [(max(distances[i][j] for i in clusters[a] for j in clusters[b]),
                       clusters[a], clusters[b], a, b)
                      for ia,a in enumerate(keys) for b in keys[ia+1:]]
        height, _, _, a, b = min(candidates)
        history.append((a,b,new_id,height,clusters[a],clusters[b]))
        clusters[new_id] = tuple(sorted(clusters.pop(a)+clusters.pop(b)))
    return history


def main():
    n = len(NAMES)
    history = merges()
    children = {new:(a,b) for a,b,new,*_ in history}
    def leaves(node):
        return [node] if node<n else leaves(children[node][0])+leaves(children[node][1])
    order = leaves(2*n-2)
    positions = {node:(i,0.) for i,node in enumerate(order)}
    fig, (ax, heat) = plt.subplots(1,2,figsize=(12,6), gridspec_kw={'width_ratios':[1.5,1]})
    for a,b,new,height,*_ in history:
        x1,y1=positions[a]; x2,y2=positions[b]; y=float(height)
        ax.plot([x1,x1,x2,x2],[y1,y,y,y2],color='#245b82',lw=1.6)
        positions[new]=((x1+x2)/2,y)
    ax.set_xticks(range(n),[NAMES[i] for i in order],rotation=65,ha='right')
    ax.set_ylim(0,.86);ax.set_ylabel('Complete-linkage Jaccard distance')
    ax.set_title('One valid dendrogram (ties resolved by row order)')
    ax.axhline(.65,color='#ad601a',ls='--',lw=1,label='Illustrative cut at 0.65')
    ax.legend(fontsize=8,loc='upper left');ax.spines[['top','right']].set_visible(False)
    distances=np.array(exact_distances(),dtype=float)
    im=heat.imshow(distances[np.ix_(order,order)],vmin=0,vmax=.8,cmap='Blues')
    heat.set_xticks(range(n),[NAMES[i] for i in order],rotation=90,fontsize=8)
    heat.set_yticks(range(n),[NAMES[i] for i in order],fontsize=8)
    heat.set_title('Pairwise distances in dendrogram order')
    fig.colorbar(im,ax=heat,shrink=.65,label='Jaccard distance')
    fig.tight_layout();fig.savefig('paper-43-clustering.png',dpi=110,facecolor='white',transparent=False)
    plt.close(fig)


if __name__=='__main__':
    main()
