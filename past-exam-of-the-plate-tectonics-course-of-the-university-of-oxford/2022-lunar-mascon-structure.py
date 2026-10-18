#!/usr/bin/env python3
"""Original illustrative section and gravity decomposition; not a GRAIL fit.
Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7; writes PNG in CWD.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'figure.facecolor':'white','axes.facecolor':'white','savefig.facecolor':'white'})
x=np.linspace(-250,250,1001)
relief=-3*np.exp(-(x/85)**6)+1.5*np.exp(-((np.abs(x)-110)/25)**2)
moho=-40+16*np.exp(-(x/65)**2)-3*np.exp(-((np.abs(x)-125)/35)**2)
basalt_bottom=relief-4*np.exp(-(x/62)**8)
fig,(ax,bx)=plt.subplots(2,1,figsize=(7.4,5.0),layout='constrained',sharex=True)
ax.fill_between(x,-65,moho,color='#cf9e73')
ax.fill_between(x,moho,relief,color='#e6dec5')
ax.fill_between(x,basalt_bottom,relief,color='#72777b')
ax.plot(x,relief,color='black',lw=1);ax.plot(x,moho,color='#7f4e23',lw=1.2)
ax.axhline(0,color='#777777',lw=.7,ls=':')
ax.annotate('Dense basalt fill',xy=(0,-4),xytext=(35,-15),arrowprops={'arrowstyle':'->'},fontsize=9)
ax.text(-235,-20,'Lower-density crust',fontsize=9)
ax.annotate('Dense mantle rises\nbeneath the basin',xy=(0,-25),xytext=(-105,-57),arrowprops={'arrowstyle':'->'},fontsize=9)
ax.set(ylim=(-65,10),ylabel='Elevation (km)',title='An impact basin can hide a subsurface mass excess')
# Arbitrary functions isolate the signs; they are not observations or a gravity inversion.
subsurface=250*np.exp(-(x/78)**2)-65*np.exp(-((np.abs(x)-125)/33)**2)
topography=-115*np.exp(-(x/85)**6)+60*np.exp(-((np.abs(x)-110)/25)**2)
bx.plot(x,subsurface+topography,color='#2166ac',lw=2,label='Free-air: relief + subsurface')
bx.plot(x,subsurface,color='#b2182b',lw=2,label='Bouguer: modeled relief removed')
bx.plot(x,topography,color='#555555',lw=1,ls='--',label='Topography contribution')
bx.axhline(0,color='black',lw=.6)
bx.set(xlim=(-250,250),xlabel='Distance from basin center (km)',ylabel='Illustrative anomaly (mGal)',title='Subtracting relief can expose the positive center')
bx.legend(fontsize=8,loc='upper right',frameon=False)
bx.grid(alpha=.15)
fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=120,transparent=False,metadata={'Software':'Original schematic; no observed GRAIL pixels or fitted values'})
plt.close(fig)
