"""Original explanatory schematic. Python 3.14; NumPy, Matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white','savefig.facecolor':'white'})

fig,axs=plt.subplots(1,3,figsize=(11,3.6),layout='constrained',sharey=True)
x=np.linspace(-3,3,500);b=np.exp(-(x/.8)**2);fore=.10*(np.exp(-((x-1.5)/.45)**2)+np.exp(-((x+1.5)/.45)**2))
for ax,depth,ice,title in zip(axs,[.24,.65,.24],[.65,1,0],['Ice accumulation','Long-lived ice load','After melting']):
 y=-depth*b+fore*(depth/.65);ax.fill_between(x,-1.2,y,color='#decdb4');ax.plot(x,y,color='#5c4c3a',lw=2);ax.axhline(0,ls=':',c='gray',lw=1)
 if ice:ax.fill_between(x,y,y+ice*np.maximum(0,1-(x/1.25)**2),where=np.abs(x)<1.25,color='#bcdde9',edgecolor='#6597ac')
 ax.text(0,-1.1,'viscous mantle',ha='center',fontsize=9)
 inward=ice==0
 for side in [-1,1]:
  ax.annotate('',xy=(side*(.4 if inward else 2),-.8),xytext=(side*(2 if inward else .4),-.8),arrowprops={'arrowstyle':'->','color':'#a14524','lw':2})
 if inward:
  ax.annotate('',xy=(0,.35),xytext=(0,-.16),arrowprops={'arrowstyle':'->','color':'#397343','lw':2});ax.text(.35,.35,'uplift',color='#397343')
 ax.set(title=title,xlim=(-3,3),ylim=(-1.25,1.1));ax.axis('off')
axs[0].text(0,1,'load grows',ha='center');axs[1].text(0,1,'depression + forebulge',ha='center');axs[2].text(0,1,'residual depression',ha='center')
fig.suptitle('Glacial loading and delayed recovery — schematic stages')

fig.savefig(Path(__file__).stem+'.png',dpi=150,bbox_inches='tight',facecolor='white');plt.close(fig)
