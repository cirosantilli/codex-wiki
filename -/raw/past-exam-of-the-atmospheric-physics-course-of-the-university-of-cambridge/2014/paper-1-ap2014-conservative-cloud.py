"""Original analytical diagram, Python3.14/NumPy2.3/Matplotlib3.10; basename PNG output to cwd."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False})

from matplotlib.patches import Rectangle
fig,ax=plt.subplots(figsize=(7,4.5),layout='constrained');ax.set(xlim=(0,10),ylim=(0,7));ax.axis('off')
ax.add_patch(Rectangle((1.5,2),7,2.5,ec='#235789',fc='#eaf2f7'))
ax.text(5,3.1,'conservative cloud: no absorption',ha='center');ax.text(5,2.55,'material heating = 0',ha='center',weight='bold')
for start,end,text,xy in [((3,6.2),(3,4.6),'incoming 9.1275',(1.3,6.5)),((7,4.6),(7,6.2),'upward 1.1409',(6.5,6.5)),((5,2),(5,.4),'downward 7.9866',(5,.1))]:
 ax.annotate('',end,start,arrowprops={'arrowstyle':'->','lw':3,'color':'#ce5a24'});ax.text(*xy,text,ha='center')
ax.set_title(r'Band fluxes in $\mathrm{W\,m^{-2}}$: single-scattering escape approximation')
fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white')
