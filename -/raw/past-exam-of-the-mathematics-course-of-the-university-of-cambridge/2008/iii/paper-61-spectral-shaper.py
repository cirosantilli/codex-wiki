"""Original 4f pulse-shaper schematic. Python 3.14, root NumPy/Matplotlib.
Writes the PNG basename into the caller's CWD and honors MPLCONFIGDIR.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

fig,ax=plt.subplots(figsize=(11,4.8),layout='constrained',facecolor='white')
ax.set_xlim(-.8,4.85);ax.set_ylim(-1.55,1.9);ax.axis('off')
ax.axhline(0,color='#a8a8a8',lw=.8,ls='--',zorder=0)
for ypos,color,label in [(.65,'#246dc5','high frequency'),(0,'#248951','central frequency'),(-.65,'#d14c33','low frequency')]:
 ax.plot([0,1,2,3,4],[0,ypos,ypos,ypos,0],color=color,lw=2)
 ax.text(1.05,ypos+.08,label,color=color,fontsize=10)
for x in (1,3):
 ax.plot([x,x],[-.95,.95],color='#272727',lw=2)
 ax.annotate('',xy=(x,.95),xytext=(x,.72),arrowprops={'arrowstyle':'->','color':'#272727'})
 ax.annotate('',xy=(x,-.95),xytext=(x,-.72),arrowprops={'arrowstyle':'->','color':'#272727'})
for x in (0,4):
 ax.plot([x-.12,x+.12],[-.3,.3],color='#222222',lw=4)
ax.add_patch(Rectangle((1.95,-.92),.1,1.84,facecolor='#bcb8d2',edgecolor='#4b416a',lw=1.5,zorder=6))
ax.annotate('',xy=(0,0),xytext=(-.7,0),arrowprops={'arrowstyle':'->','lw':2,'color':'#222222'})
ax.annotate('',xy=(4.7,0),xytext=(4,0),arrowprops={'arrowstyle':'->','lw':2,'color':'#222222'})
ax.text(-.6,.18,'input pulse',ha='center',fontsize=10)
ax.text(4.5,.18,'shaped pulse',ha='center',fontsize=10)
labels=['dispersing\ngrating','lens 1','complex mask\nor amplitude/phase SLM','lens 2','recombining\ngrating']
for x,label in enumerate(labels):ax.text(x,-1.02,label,ha='center',va='top',fontsize=10)
for left in range(4):
 ax.annotate('',xy=(left+.08,-1.42),xytext=(left+.92,-1.42),arrowprops={'arrowstyle':'<->','lw':1,'color':'#444444'})
 ax.text(left+.5,-1.39,'f',ha='center',va='bottom',fontsize=11)
ax.text(2,1.48,'Fourier plane: frequency maps to transverse position',ha='center',fontsize=12)
ax.annotate('',xy=(2,.97),xytext=(2,1.34),arrowprops={'arrowstyle':'->','color':'#4b416a'})
ax.text(2,1.82,r'$\widetilde E_{\rm out}(\omega)=A(\omega)e^{i\varphi(\omega)}\widetilde E_{\rm in}(\omega)$',ha='center',fontsize=14)
fig.savefig('paper-61-spectral-shaper.png',dpi=120,facecolor='white')
plt.close(fig)
