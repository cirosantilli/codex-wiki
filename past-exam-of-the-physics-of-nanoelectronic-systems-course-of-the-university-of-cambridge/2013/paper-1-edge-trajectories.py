"""Original explanatory model; output is a basename in the working directory."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, FancyArrowPatch
plt.rcParams.update({'font.size':9,'axes.titlesize':10,'axes.labelsize':10})

fig,ax=plt.subplots(figsize=(8,3.8),layout='constrained');ax.axhspan(-2.15,2.15,color='#eef4f6');colors=['#2166ac','#b2182b','#4393c3','#ef8a62']
for j,col in enumerate(colors):
 yy=1.91-.22*j;ax.plot([-3.7,3.7],[yy,yy],color=col,lw=1.8);ax.annotate('',xy=(.4,yy),xytext=(-.4,yy),arrowprops={'arrowstyle':'->','color':col,'lw':2});ax.plot([-3.7,3.7],[-yy,-yy],color=col,lw=1.8);ax.annotate('',xy=(-.4,-yy),xytext=(.4,-yy),arrowprops={'arrowstyle':'->','color':col,'lw':2});ax.text(3.85,yy,['0,-','0,+','1,-','1,+'][j],va='center',fontsize=8)
ax.plot([-4,4],[2.15,2.15],color='black');ax.plot([-4,4],[-2.15,-2.15],color='black');ax.text(0,.25,'No extended bulk channel at the chosen Fermi energy',ha='center');ax.text(0,-.4,r'$B$ points out of the page; arrows are electron drift',ha='center');ax.set(xlim=(-4.2,4.6),ylim=(-2.5,2.5),xlabel='Along Hall bar',ylabel='Across Hall bar',title='Four spin-resolved guiding centres at each edge');ax.set_xticks([]);ax.set_yticks([])
fig.savefig('paper-1-edge-trajectories.png',dpi=170,facecolor='white');plt.close(fig)
