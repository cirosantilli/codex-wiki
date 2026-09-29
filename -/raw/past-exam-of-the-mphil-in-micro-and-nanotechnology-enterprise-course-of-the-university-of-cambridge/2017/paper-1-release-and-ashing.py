"""Original explanatory diagram; run in the desired output directory. Tested with Python 3.14, numpy and matplotlib."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon, Circle, FancyArrowPatch
plt.rcParams.update({"font.size":10,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})
fig,axs=plt.subplots(1,2,figsize=(10,4.3),layout='constrained')
a=axs[0];a.set_title('Sacrificial support and anchored release');a.set(xlim=(0,5),ylim=(0,5));a.axis('off')
for yy,release in [(2.9,False),(.4,True)]:
 a.add_patch(Rectangle((.25,yy),4.5,.35,fc='#8a8a8a',ec='black'))
 if not release:a.add_patch(Rectangle((1.1,yy+.35),3.25,.6,fc='#f0cb6c',ec='#aa832d'))
 a.add_patch(Rectangle((.55,yy+.35),.55,.8,fc='#2a75a1',ec='#154261'));a.add_patch(Rectangle((.55,yy+.95),3.8,.2,fc='#2a75a1',ec='#154261'))
 
 if not release:a.text(2.5,yy-.18,'silicon substrate',ha='center',va='top',fontsize=8)
 a.text(2.8,yy+.65,'released gap' if release else 'sacrificial oxide',ha='center',va='center',fontsize=9)
a.text(1.1,4.4,'anchor',ha='center');a.annotate('',(.8,3.7),(1.1,4.35),arrowprops={'arrowstyle':'->'})
a.annotate('selective lateral oxide removal',(2.9,1.95),(2.9,2.35),ha='center',fontsize=9,arrowprops={'arrowstyle':'->'})
a.text(2.5,.05,'Vapor release or critical-point drying limits drying stiction.',ha='center',fontsize=8)
a=axs[1];a.set_title('Remote oxygen-plasma ashing');a.set(xlim=(0,5),ylim=(0,5));a.axis('off')
a.add_patch(Rectangle((1.2,2.8),2.6,1.3,fc='#e9d9ec',ec='#87578e'));a.text(2.5,3.45,'RF / microwave\noxygen plasma',ha='center',va='center');a.annotate('O₂ feed',(2.5,4.1),(2.5,4.75),ha='center',arrowprops={'arrowstyle':'->'})
a.add_patch(Rectangle((.65,.5),3.7,1.75,fc='#f3f7f9',ec='#596d78'));a.add_patch(Rectangle((1.1,.82),2.8,.18,fc='#8a8a8a'));a.plot([1.1,3.9],[1.03,1.03],color='#bc7831',lw=4)
for xx in [1.5,2.5,3.5]:a.annotate('O radicals',(xx,1.15),(xx,2.7),ha='center',fontsize=8,arrowprops={'arrowstyle':'->','color':'#b94b2f'})
a.annotate('pump: volatile products',(4.3,1.3),(4.3,.1),ha='right',fontsize=8,arrowprops={'arrowstyle':'<-'});a.text(2.5,.55,'unbiased wafer',ha='center',fontsize=8)
fig.savefig('paper-1-release-and-ashing.png',dpi=160);plt.close(fig)
