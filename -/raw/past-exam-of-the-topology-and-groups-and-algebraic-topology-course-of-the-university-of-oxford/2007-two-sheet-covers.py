"""Python 3.14.4; Matplotlib 3.10.7. PNG output in CWD."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
fig,axes=plt.subplots(1,2,figsize=(9.2,3.7),layout='constrained',facecolor='white')
for ax,cross,loop in zip(axes,['a','b'],['b','a']):
 ax.set_facecolor('white');ax.set_aspect('equal');ax.axis('off');ax.set(xlim=(-1.45,1.45),ylim=(-.65,1.05),title=f'{cross}-edges exchange sheets; {loop}-edges are loops')
 for x,y in [(-.8,.8),(.8,-.8)]:ax.add_patch(FancyArrowPatch((x,0),(y,0),connectionstyle='arc3,rad=.35',arrowstyle='-|>',mutation_scale=15,lw=1.8,color='#2166ac',shrinkA=12,shrinkB=12))
 ax.text(0,.36,'$'+cross+'$',ha='center',fontsize=13,color='#2166ac');ax.text(0,-.40,'$'+cross+'$',ha='center',fontsize=13,color='#2166ac')
 for i,x in enumerate([-.8,.8]):
  ax.add_patch(FancyArrowPatch((x-.11,.02),(x+.11,.02),connectionstyle='arc3,rad=-2.2',arrowstyle='-|>',mutation_scale=14,lw=1.8,color='#b35806'));ax.text(x,.66,'$'+loop+'$',ha='center',fontsize=13,color='#b35806');ax.scatter([x],[0],s=320,c='black'if i==0 else 'white',edgecolors='black',zorder=5);ax.text(x,0,str(i),c='white'if i==0 else 'black',ha='center',va='center',fontsize=10,zorder=6)
fig.suptitle('Degree two does not determine a based covering')
fig.savefig(Path.cwd()/'2007-two-sheet-covers.png',dpi=170,facecolor='white')
