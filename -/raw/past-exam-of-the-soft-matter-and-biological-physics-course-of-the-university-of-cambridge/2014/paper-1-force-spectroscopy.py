"""Original generic-physics figure; Python 3.14, numpy and matplotlib.
PNG basename output to cwd; no source figures or media paths.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','savefig.facecolor':'white','axes.spines.top':False,'axes.spines.right':False})
fig,(a,b)=plt.subplots(1,2,figsize=(9,3.5),layout='constrained')
for x,txt,col in [(0,'stage\nZ','#dadada'),(2,'single synthetic\nchain x','#e8c7a2'),(4,'cantilever\ndeflection d','#b8d2e8')]:a.add_patch(Rectangle((x,0),1.5,.8,facecolor=col,edgecolor='gray'));a.text(x+.75,.4,txt,ha='center',va='center',fontsize=9)
for x in [1.5,3.5]:a.plot([x,x+.5],[.4,.4],color='black')
a.text(2.8,-.6,'Series compliance: Z = x + d; force F = kc d',ha='center',fontsize=10);a.set(xlim=(-.2,5.8),ylim=(-1.2,1.6),title='Measurement chain (schematic)');a.axis('off')
f=np.linspace(.005,8,500);x=1/np.tanh(f)-1/f;d=f/10;b.plot(x,f,label='Molecular extension x/L');b.plot(x+d,f,label='Stage travel Z/L');b.set(xlabel='Scaled displacement',ylabel='Force in chosen thermal units',title='Illustrative freely-jointed-chain response');b.legend(frameon=False,fontsize=8)
fig.savefig('paper-1-force-spectroscopy.png',dpi=150);plt.close(fig)
