"""Original derived primitive-cell construction; Python 3.14 and matplotlib.

No source illustration is used. Save the PNG basename to the working directory.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

fig, axes = plt.subplots(1, 2, figsize=(8.4, 5.4), layout='constrained')
fig.patch.set_facecolor('white')
points = [(x,y) for x in range(-3,4) for y in range(-1,5) if (x-y)%2 == 0]
for ax in axes:
    ax.scatter(*zip(*points), s=21, color='#303d48', zorder=3)
    ax.set(xlim=(-2.5,2.5), ylim=(-0.6,3.7), xlabel=r'$x/a$', ylabel=r'$y/a$')
    ax.set_aspect('equal')
    ax.set_xticks(range(-2,3))
    ax.set_yticks(range(0,4))
    ax.grid(alpha=0.15)
    ax.spines[['top','right']].set_visible(False)
    ax.text(0.97,0.02,r'$A_c=2a^2$',ha='right',transform=ax.transAxes,fontsize=12)
for ax, vectors, title in [
    (axes[0], [(1,1),(-1,1)], 'Orthogonal primitive basis'),
    (axes[1], [(1,1),(0,2)], 'Sheared primitive basis')]:
    u,v=vectors
    poly=[(0,0),u,(u[0]+v[0],u[1]+v[1]),v]
    ax.add_patch(Polygon(poly,facecolor='#d9eae9',edgecolor='#377575',lw=2,zorder=2))
    for i,vec in enumerate(vectors):
        ax.annotate('',xy=vec,xytext=(0,0),arrowprops={'arrowstyle':'-|>','lw':2,'color':['#b7532b','#674292'][i]})
        offset=(0.12,-0.08) if i==0 else (-0.65,0.05)
        label=rf'$\mathbf{{a}}_{i+1}$' if ax is axes[0] else rf"$\mathbf{{a}}'_{i+1}$"
        ax.text(vec[0]*0.6+offset[0],vec[1]*0.6+offset[1],label,fontsize=12)
    ax.set_title(title,fontsize=12)
fig.savefig('paper-2-primitive-cells.png',dpi=160,facecolor='white')
plt.close(fig)
