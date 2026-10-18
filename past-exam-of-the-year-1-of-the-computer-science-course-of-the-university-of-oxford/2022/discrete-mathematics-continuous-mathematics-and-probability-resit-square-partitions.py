"""Original pigeonhole partitions. Python 3.14; NumPy 2.3.5; Matplotlib 3.10.7.
Writes one opaque PNG to the working directory; uses only root-declared packages.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np

NAME = 'discrete-mathematics-continuous-mathematics-and-probability-resit-square-partitions.png'
P = np.array([(0,0),(.5,0),(.5,.25),(.25,.5),(0,.25)])
LEFT = np.array([(0,.25),(.25,.5),(0,.75)])
DIAMOND = np.array([(.25,.5),(.5,.25),(.75,.5),(.5,.75)])

def reflection(poly, right=False, top=False):
    out = poly.copy()
    if right:
        out[:,0] = 1-out[:,0]
    if top:
        out[:,1] = 1-out[:,1]
    return out

def main():
    fig, axes = plt.subplots(1, 2, figsize=(9, 5.8), facecolor='white')
    fig.subplots_adjust(left=.075, right=.985, bottom=.14, top=.79, wspace=.24)
    colours = ['#c7e9c0', '#c6dbef', '#fdd0a2', '#dadaeb', '#f7d6e0', '#fff2ae', '#b2e2e2']
    four = [np.array([(x,y),(x+.5,y),(x+.5,y+.5),(x,y+.5)])
            for y in (0,.5) for x in (0,.5)]
    seven = [reflection(P,r,t) for t in (False,True) for r in (False,True)]
    seven += [LEFT, reflection(LEFT, True), DIAMOND]
    for ax, polygons, title, subtitle in zip(axes, [four,seven],
            ['5 points, 4 regions', '8 points, 7 regions'],
            [r'Each diameter $\leq\sqrt{2}/2$', r'Each diameter $\leq\sqrt{5}/4$']):
        ax.set_facecolor('white')
        for i, poly in enumerate(polygons):
            ax.add_patch(Polygon(poly, closed=True, facecolor=colours[i], edgecolor='#25344a', linewidth=1.5))
            c=poly.mean(axis=0)
            ax.text(c[0],c[1],str(i+1),ha='center',va='center',fontsize=11,color='#172538')
        ax.set(xlim=(0,1), ylim=(0,1), aspect='equal', xticks=[0,.25,.5,.75,1], yticks=[0,.25,.5,.75,1])
        ax.set_xticklabels(['0','¼','½','¾','1'])
        ax.set_yticklabels(['0','¼','½','¾','1'])
        ax.tick_params(length=3,labelsize=10)
        ax.set_title(title+'\n'+subtitle, fontsize=12, pad=12)
        ax.set_xlabel('Horizontal coordinate')
        ax.set_ylabel('Vertical coordinate')
    fig.suptitle('Assign shared boundaries to one region before counting', fontsize=11)
    fig.savefig(Path.cwd()/NAME, dpi=150, facecolor='white', transparent=False,
                metadata={'Software':'Matplotlib','Title':'Original four- and seven-region pigeonhole partitions'})
    plt.close(fig)

if __name__ == '__main__':
    main()
