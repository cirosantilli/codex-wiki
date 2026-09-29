"""Original explanatory chemistry drawing; Python 3.14 / Matplotlib 3.10.7 / NumPy 2.3.5."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from tools.chemistry_diagram import atom,bond,ring,curly,flow,finish,save
BLUE='#245c9f'
def label(ax,p,text,size=10):
    ax.text(*p,text,ha='center',va='center',fontsize=size,color=BLUE)

fig,ax=plt.subplots(figsize=(10,5),layout='constrained')
nodes=[((0,2),'LNi–H(SiPh₃)\n+ terminal alkene'),((4.2,2),'LNi(alkyl)(SiPh₃)\nH added at terminal carbon'),((4.2,-.2),'LNi–H or LNi–D\n+ shifted alkene'),((0,-.2),'Shared hydride pool\nexchanges between substrates')]
for xy,t in nodes:ax.text(*xy,t,ha='center',va='center',fontsize=11,bbox={'boxstyle':'round,pad=.5','facecolor':'#eef4fa','edgecolor':BLUE})
for a,b,t in [((1.4,2),(2.8,2),'insertion'),((4.2,1.3),(4.2,.5),'β-H/D elimination'),((2.8,-.2),(1.5,-.2),'exchange'),((0,.5),(0,1.2),'binding')]:flow(ax,a,b,t)
ax.text(2,-1.4,'Intermolecular crossover follows from exchange through Ni–H / Ni–D.',ha='center',fontsize=10)
finish(ax,(-2.3,6.8),(-1.9,3.3),'Nickel hydride insertion / elimination')

save(fig,Path(__file__).with_suffix('.png').name,dpi=150)
