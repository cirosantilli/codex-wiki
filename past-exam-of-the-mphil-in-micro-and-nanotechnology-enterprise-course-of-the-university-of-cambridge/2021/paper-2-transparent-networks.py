"""Original explanatory model figure; Python 3.14, NumPy and Matplotlib.
Run from the desired output directory. No exam image or experimental data used.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False})
fig,axs=plt.subplots(1,3,figsize=(10,3.8),layout='constrained')
rng=np.random.default_rng(410)
for ax,count,title in zip(axs[:2],[10,30],['Sparse: disconnected paths','Connected: loading vs transmission']):
    for _ in range(count):
        x,y=rng.uniform(-.2,1.2,2);theta=rng.uniform(0,np.pi);length=.72
        dx,dy=length*np.cos(theta)/2,length*np.sin(theta)/2
        ax.plot([x-dx,x+dx],[y-dy,y+dy],lw=2.5,color='#2479ad',alpha=.8)
    ax.axvspan(0,.035,color='#555555');ax.axvspan(.965,1,color='#555555')
    ax.set(xlim=(0,1),ylim=(0,1),aspect='equal',title=title,xticks=[],yticks=[])
ax=axs[2]
for y in [.7,.25]:
    ax.plot([.06,.94],[y,y],lw=12,color='#bbbbbb',solid_capstyle='round')
ax.plot([.45,.45],[.52,.88],lw=12,color='#bbbbbb',solid_capstyle='round')
ax.plot([.45,.45],[.07,.43],lw=12,color='#bbbbbb',solid_capstyle='round')
ax.add_patch(plt.Circle((.45,.25),.085,color='#d87b28',zorder=5))
ax.plot([.35,.55],[.7,.7],lw=4,color='#803d81')
ax.text(.55,.84,'Ligand/contact barrier',fontsize=8,ha='center')
ax.text(.53,.40,'Local weld',fontsize=9)
ax.set(xlim=(0,1),ylim=(0,1),aspect='equal',title='Junctions set network resistance',xticks=[],yticks=[])
fig.suptitle('Qualitative original schematics; no calibrated percolation threshold')
fig.savefig('paper-2-transparent-networks.png',dpi=170,facecolor='white')
