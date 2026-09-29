"""Oxford 2015 geometric modelling Q1: circular fillet and local CSG.

Run from any directory; writes geometric-modelling-2015-fillet.png there.
Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
"""
import os
import tempfile
os.environ.setdefault('MPLCONFIGDIR', tempfile.mkdtemp(prefix='gmod-fillet-mpl-'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Circle
import numpy as np

q = np.sqrt(3.)
A, B, C, D, EE, O = np.array([[2-q, 0], [2, 1], [1, 1], [1, 2], [0, 2], [0, 0]])
M = np.array([2-q/4, .75])
N = np.array([1.5, 1.])
K = np.array([1.5, q/2])
r = 1-q/2
theta = np.linspace(-np.pi/3, np.pi/2, 160)
arc = K+r*np.column_stack((np.cos(theta), np.sin(theta)))
fig, (ax, tree) = plt.subplots(1, 2, figsize=(9, 4.6), layout='constrained', gridspec_kw={'width_ratios':[1.35, 1]})
ax.add_patch(Polygon([A, B, C, D, EE, O], facecolor='#f9dcd6', edgecolor='.5', lw=1))
ax.add_patch(Polygon(np.vstack([A, M, arc, N, C, D, EE, O]), facecolor='#dbeaf6', edgecolor='#123e67', lw=1.5))
ax.add_patch(Circle(K, r, fill=False, edgecolor='#29906a', ls=':', lw=1.5))
ax.plot(*arc.T, color='#167b50', lw=3, zorder=5, label='retained circular arc')
x = np.linspace(1.35, 2.1, 100)
ax.plot(x, 1-(x-1.5)/(2-q), '--', color='#81519b', lw=1.5, label='chord clipping line g = 0')
for p in [M, N]:
    ax.plot([K[0], p[0]], [K[1], p[1]], ':', color='#167b50', lw=1.5)
for label, p, offset in [('M',M,(6,-15)),('N',N,(-17,7)),('K',K,(-19,-2)),('B',B,(7,3))]:
    ax.plot(*p, 'o', color='#123e67', ms=4, zorder=6)
    ax.annotate(label, p, xytext=offset, textcoords='offset points', fontsize=11, zorder=6)
ax.text(1.89, .9, 'removed\ntip', color='#9c3631', ha='center', fontsize=10)
ax.set(xlim=(1.35, 2.08), ylim=(.48, 1.12), xlabel='x', ylabel='y')
ax.set_aspect('equal')
ax.grid(alpha=.15)
ax.legend(loc='lower right', fontsize=8)
ax.set_title('Tangent circle and localized cut')

tree.set(xlim=(0,1), ylim=(0,1))
tree.axis('off')
nodes = {'root':(.5,.85),'original':(.2,.56),'union':(.75,.56),'halfplane':(.56,.25),'disk':(.94,.25)}
for a,b in [('root','original'),('root','union'),('union','halfplane'),('union','disk')]:
    pa,pb=nodes[a],nodes[b]
    tree.plot([pa[0],pb[0]],[pa[1],pb[1]], color='.4', zorder=1)
for name,text in [('root','intersection'),('original','original P'),('union','union'),('halfplane','g ≤ 0'),('disk','disk')]:
    tree.text(*nodes[name],text,ha='center',va='center',fontsize=11,
              bbox=dict(boxstyle='round,pad=.4',fc='white',ec='#123e67'),zorder=2)
tree.text(.5,.04,'Keep the old solid AND\n(the far side of MN OR the disk)',ha='center',va='center',fontsize=10)
tree.set_title('Blend embedded in the CSG tree')
fig.savefig('geometric-modelling-2015-fillet.png',dpi=125,facecolor='white',transparent=False)
plt.close(fig)
