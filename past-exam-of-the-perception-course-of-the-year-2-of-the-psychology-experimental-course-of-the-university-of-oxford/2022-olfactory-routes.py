#!/usr/bin/env python3
"""Original functional sensory-route diagram; not an anatomical reconstruction.
Python 3.14.4, Matplotlib 3.10.7; writes same-basename opaque PNG to CWD.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'figure.facecolor':'white','axes.facecolor':'white','savefig.facecolor':'white'})
fig,ax=plt.subplots(figsize=(7.8,3.6),layout='constrained');ax.set(xlim=(0,10),ylim=(0,5));ax.set_axis_off()
def box(x,y,w,h,label,col):
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.08',facecolor=col,edgecolor='#555555',lw=1))
 ax.text(x+w/2,y+h/2,label,ha='center',va='center',fontsize=10)
def arrow(a,b,label,x,y):
 ax.annotate('',xy=b,xytext=a,arrowprops={'arrowstyle':'->','lw':1.6,'color':'#444444'})
 ax.text(x,y,label,ha='center',va='center',fontsize=8,bbox={'facecolor':'white','edgecolor':'none','pad':1})
box(.2,3.5,2.1,.8,'External odor\nvolatiles','#dce9f4')
box(.2,1.9,2.1,.8,'Food odor\nvolatiles','#e2edf4')
box(.2,.3,2.1,.8,'Dissolved\ntastants','#f5e3d0')
box(4,2.7,2.1,1,'Olfactory\nreceptors','#dce9f4')
box(4,.4,2.1,.9,'Taste\nreceptors','#f5e3d0')
box(7.7,1.5,2,.9,'Flavor and\nobject attribution','#e6e4ef')
arrow((2.4,3.9),(3.9,3.5),'Via nostrils\n(orthonasal)',3.15,4.2)
arrow((2.4,2.3),(3.9,2.9),'Via nasopharynx\n(retronasal)',3.1,2.25)
arrow((2.4,.7),(3.9,.8),'Contact in mouth',3.15,.4)
arrow((6.2,3.2),(7.6,2.2),'Olfactory input',7,3.2)
arrow((6.2,.85),(7.6,1.65),'Gustatory input',7,.8)
ax.set_title('Two odor routes, distinct taste transduction, integrated flavor',fontsize=12)
fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=120,transparent=False,metadata={'Software':'Original functional diagram; no experimental or source-figure pixels'})
plt.close(fig)
