"""Python 3.14.4; NumPy 2.3.5; Matplotlib 3.10.7. PNG output in CWD."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
n=6;theta=np.pi/2-2*np.pi*np.arange(n)/n;pos=np.c_[np.cos(theta),np.sin(theta)];colors=['#0072b2','#d55e00','#009e73','#cc79a7','#e69f00']
fig,axes=plt.subplots(1,2,figsize=(9.7,4.6),layout='constrained',facecolor='white')
for ax in axes:
 ax.set_facecolor('white');ax.set_aspect('equal');ax.axis('off');ax.set(xlim=(-1.45,1.45),ylim=(-1.35,1.4))
 for i,(x,y)in enumerate(pos):ax.scatter([x],[y],s=230,c='white',edgecolor='black',zorder=5);ax.text(x,y,str(i+1),ha='center',va='center',zorder=6,fontsize=10)
for i in range(n):
 for j in range(i+1,n):axes[0].plot(pos[[i,j],0],pos[[i,j],1],c=colors[i],lw=1.8,alpha=.8)
axes[0].set_title('Disjoint edge blocks by lower endpoint');axes[0].legend(handles=[Line2D([0],[0],color=colors[i],label=f'Block {i+1}')for i in range(n-1)],loc='lower center',bbox_to_anchor=(.5,-.1),ncol=3,fontsize=8)
for j in [3,4,5]:axes[1].plot(pos[[2,j],0],pos[[2,j],1],c=colors[2],lw=3,alpha=.5)
for i,j in [(0,3),(1,4),(2,5)]:axes[1].plot(pos[[i,j],0],pos[[i,j],1],c='black',lw=2.3,ls='--')
axes[1].set_title('A matching uses one edge of the green block');axes[1].text(0,-1.28,'Green: block 3. Dashed: one possible matching.',ha='center',fontsize=9)
fig.savefig(Path.cwd()/'2007-matching-blocks.png',dpi=170,facecolor='white')
