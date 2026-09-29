"""Original explanatory figure; Python3.14, NumPy2.3.5, Matplotlib3.10.7.
Output uses the PNG basename in the current working directory.
"""
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":10,"figure.facecolor":"white","savefig.facecolor":"white"})
# Colour is categorical: annotation gives the actual symbolic mode count.
labels0=[['0','0','M','0'],['0','0','0','M'],['M','0','0','N−M'],['0','M','N−M','0']]
labelsp=[['0','0','0','M'],['M','0','0','0'],['0','M','0','N−M'],['0','0','N','0']]
labelsm=np.array(labelsp).T.tolist();fig,axs=plt.subplots(1,3,figsize=(9.8,4.1),layout='constrained')
colors={'0':0,'M':1,'N−M':2,'N':3}
from matplotlib.colors import ListedColormap
cm=ListedColormap(['#f8f8f8','#b8d8eb','#d9c3e5','#afd9bf'])
for ax,labs,title in zip(axs,[labels0,labelsp,labelsm],[r'$B=0$',r'$B=+B_0$',r'$B=-B_0$']):
 mat=np.array([[colors[v] for v in row] for row in labs]);ax.imshow(mat,cmap=cm,vmin=0,vmax=3)
 for i in range(4):
  for j in range(4):ax.text(j,i,labs[i][j],ha='center',va='center',fontsize=13)
 ax.set(xticks=range(4),yticks=range(4),xticklabels=['1','2','3','4'],yticklabels=['1','2','3','4'],xlabel='Injecting lead j',ylabel='Collecting lead i',title=title)
 ax.set_xticks(np.arange(-.5,4,1),minor=True);ax.set_yticks(np.arange(-.5,4,1),minor=True);ax.grid(which='minor',color='white',lw=2);ax.tick_params(which='minor',bottom=False,left=False)
fig.suptitle(r'Balanced mode routing: $T_{ij}$, $N>M>0$ (all spin branches counted)')
fig.savefig('paper-1-bend-routing.png',dpi=170)
