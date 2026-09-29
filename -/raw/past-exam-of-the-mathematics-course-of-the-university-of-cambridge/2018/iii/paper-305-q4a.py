"""Generate an original inclusive DIS diagram; Python 3.14, matplotlib 3.10.7."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch,Circle

def line(ax,a,b,arrow=True):
    ax.plot([a[0],b[0]],[a[1],b[1]],color='black',lw=1.7)
    if arrow:
        a,b=np.array(a),np.array(b);m=(a+b)/2;d=(b-a)*.13
        ax.add_patch(FancyArrowPatch(m-d,m+d,arrowstyle='-|>',mutation_scale=13,color='black',lw=1))
def wave(ax,a,b):
    a,b=np.array(a),np.array(b);d=b-a;n=np.array([-d[1],d[0]])/np.linalg.norm(d);u=np.linspace(0,1,250)
    xy=a+u[:,None]*d+.013*np.sin(12*np.pi*u)[:,None]*n
    ax.plot(xy[:,0],xy[:,1],color='black',lw=1.5)
fig,ax=plt.subplots(figsize=(7.2,3.5),dpi=100,facecolor='white');ax.set(xlim=(0,1.1),ylim=(0,1));ax.axis('off')
vertex=(.46,.73);blob=(.53,.30)
line(ax,(.08,.88),vertex);line(ax,vertex,(.9,.88));wave(ax,vertex,(.52,.38));line(ax,(.08,.22),(.46,.29))
for end in [(.91,.49),(.95,.30),(.91,.11)]:line(ax,(.59,.30),end,False)
ax.add_patch(Circle(blob,.075,edgecolor='black',facecolor='#eeeeee',lw=1.5,zorder=5));ax.text(*blob,r'$J^\mu$',ha='center',va='center',fontsize=13,zorder=6);ax.plot(*vertex,'ko',ms=4)
for x,y,text in [(.16,.95,r'$e^-(p)$'),(.87,.95,r'$e^-(p^\prime)$'),(.38,.54,r'$\gamma^*(q)$'),(.17,.14,r'$H(P_H)$'),(1.0,.30,r'$X(P_X)$')]:ax.text(x,y,text,ha='center',va='center',fontsize=15)
fig.subplots_adjust(left=.02,right=.98,bottom=.02,top=.98)
fig.savefig(Path('paper-305-q4a.png'),facecolor='white',transparent=False);plt.close(fig)
