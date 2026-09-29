"""Planar-sheet slice force diagram. Python 3.14; NumPy 2.3.5, Matplotlib 3.10.7.

Run from the desired output directory; emits only the PNG basename there.
Uses the caller's MPLCONFIGDIR unchanged.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

fig,ax=plt.subplots(figsize=(8,5),dpi=140)
fig.patch.set_facecolor('white');ax.set_facecolor('white')
z1,z2=.7,3.2
h1,h2=.8,1.2
ax.add_patch(Polygon([(-h1,z1),(h1,z1),(h2,z2),(-h2,z2)],closed=True,facecolor='#edf3f8',edgecolor='#294864',linewidth=2))
def arrow(start,end,color='#294864',lw=2):
    ax.annotate('',xy=end,xytext=start,arrowprops={'arrowstyle':'-|>','color':color,'lw':lw,'mutation_scale':15})
arrow((0,z1),(0,-.1));ax.text(.12,.1,r'$-h(z)\sigma_{zz}(z)\,\mathbf{e}_z$',va='center',fontsize=12)
arrow((0,z2),(0,4.05));ax.text(.13,3.78,r'$+h(z+\delta z)\sigma_{zz}(z+\delta z)\,\mathbf{e}_z$',va='center',fontsize=12)
for z in [1.4,2.5]:
    half=h1+(h2-h1)*(z-z1)/(z2-z1)
    for side in [-1,1]:
        arrow((side*(half+.7),z-.112),(side*(half-.12),z+.02),color='#9a5938')
ax.text(-2.65,1.68,r'$-p_a\mathbf{n}$',color='#9a5938',fontsize=12)
ax.text(1.8,1.68,r'$-p_a\mathbf{n}$',color='#9a5938',fontsize=12)
arrow((-.12,1.58),(-.12,2.45),color='#3f7250')
ax.text(.02,2.04,r'$\rho g h\,\delta z\,\mathbf{e}_z$',color='#3f7250',fontsize=12)
ax.annotate('',xy=(-h1,.45),xytext=(h1,.45),arrowprops={'arrowstyle':'<->','color':'#5b6470'})
ax.text(-.72,.34,r'$h(z)$',fontsize=11)
ax.annotate('',xy=(2.85,z1),xytext=(2.85,z2),arrowprops={'arrowstyle':'<->','color':'#5b6470'})
ax.text(2.94,1.95,r'$\delta z$',fontsize=12)
arrow((-2.9,3.3),(-2.9,4.0),color='#555555',lw=1.5);ax.text(-3.08,3.85,r'$z$',fontsize=12)
arrow((-2.9,3.3),(-2.18,3.3),color='#555555',lw=1.5);ax.text(-2.22,3.15,r'$x$',fontsize=12)
ax.set_xlim(-3.25,3.9);ax.set_ylim(4.4,-.4);ax.axis('off')
ax.set_title('Signed tractions, ambient pressure and weight on a sheet slice',fontsize=13,pad=13)
fig.text(.5,.025,'Arrows at the cuts show positive tensile stress; pressure arrows follow the inward normals.',ha='center',fontsize=9)
fig.tight_layout(rect=(0,.05,1,1))
fig.savefig('paper-44-sheet-forces.png',facecolor='white',transparent=False)
plt.close(fig)
