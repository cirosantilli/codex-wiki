"""Original crust column. PNG written in CWD.
Tested: Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
fig, ax = plt.subplots(figsize=(9.0, 7.0), facecolor='white')
fig.subplots_adjust(left=.08,right=.98,top=.9,bottom=.12)
layers = [
(0, 2, '#ede0c5', 'Sedimentary cover (variable)', ''),
(2, 15, '#f3bba9', 'Felsic upper crust', 'Granite, granodiorite, gneiss\nQuartz + feldspar'),
(15, 25, '#b8d8dd', 'Intermediate middle crust', 'Gneiss, amphibolite\nDioritic to granodioritic composition'),
(25, 38, '#8bafd0', 'More mafic lower crust', 'Mafic granulite, metamorphosed gabbro\nPlagioclase + pyroxene, locally garnet'),
(38, 45, '#b8c891', 'Upper mantle', 'Peridotite: olivine + pyroxene'),
]
for z0, z1, color, name, detail in layers:
    ax.add_patch(Rectangle((0,z0),3.15,z1-z0,facecolor=color,edgecolor='white',linewidth=1.5))
    mid=(z0+z1)/2
    if z0==0:
        ax.annotate(name,(1.6,mid),(3.45,.4),fontsize=10,va='center',arrowprops={'arrowstyle':'-','color':'#555555'})
    else:
        ax.text(1.575,mid,name,ha='center',va='center',fontsize=11,weight='bold')
        ax.text(3.45,mid,detail,ha='left',va='center',fontsize=10)
ax.plot([0,3.2],[38,38],color='#343434',lw=2.5)
ax.text(3.45,38,'Moho at 38 km in this example',va='center',fontsize=10,weight='bold')
ax.set(xlim=(0,8.7),ylim=(45,-3),yticks=[0,2,15,25,38,45],xticks=[])
ax.set_ylabel('Depth below surface (km)',fontsize=11)
for side in ['top','right','bottom']: ax.spines[side].set_visible(False)
ax.set_title('Modern continental crust: a compositional idealization',fontsize=14,pad=12)
fig.text(.53,.015,'Layer boundaries and dominant rocks vary between provinces. Not a universal column.',ha='center',fontsize=9)
fig.savefig(Path.cwd()/'2024-continental-crust.png',dpi=140,facecolor='white',metadata={'Software':'codex-wiki matplotlib generator'})
plt.close(fig)
