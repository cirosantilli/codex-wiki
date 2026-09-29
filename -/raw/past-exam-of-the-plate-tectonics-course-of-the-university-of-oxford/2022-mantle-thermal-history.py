#!/usr/bin/env python3
"""Original conceptual models, not digitized observations.
Python 3.14.4; NumPy 2.3.5; Matplotlib 3.10.7. Outputs PNG to CWD.
Dependencies are pinned in the repository top-level pyproject.toml.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'figure.facecolor':'white','axes.facecolor':'white','savefig.facecolor':'white'})
fig,(ax,bx)=plt.subplots(1,2,figsize=(8.2,3.8),layout='constrained')
ages=np.array([0,1,2,2.8,3.5,4.2,4.5])
ax.plot(ages,[1350,1410,1490,1550,1500,1450,2100],color='#b2182b',lw=2,label='Possible early warming after crystallization')
ax.plot(ages,[1350,1430,1510,1570,1630,1730,2100],color='#2166ac',lw=2,ls='--',label='Alternative continuous solid-state cooling')
ax.axvspan(4.25,4.5,color='#fdd49e',alpha=.65)
ax.fill_between([2.5,3.0],1500,1600,color='#888888',alpha=.25)
ax.text(2.4,1670,'Illustrative late-Archean\npetrological range',ha='center',fontsize=9)
ax.annotate('Early accretion\nand magma ocean',xy=(4.38,2020),xytext=(3.7,1940),ha='center',fontsize=8,arrowprops={'arrowstyle':'->','lw':.7})
ax.set(xlim=(4.55,-.05),ylim=(1250,2180),xlabel='Age before present (Ga)',ylabel='Mantle potential temperature (°C)',title='Thermal history: schematic alternatives')
ax.legend(loc='lower left',fontsize=7,frameon=False)
ax.grid(alpha=.15)
z=np.linspace(0,2890,1000)
# Linear adiabatic slopes are solely illustrative; boundary layers use exponentials.
for tp,col,label in [(1350,'#2166ac','Present-day illustrative geotherm'),(1550,'#b2182b','Hotter solid mantle')]:
 adiabat=tp+.30*z
 temp=adiabat*(1-np.exp(-z/45))+700*np.exp(-(2890-z)/100)
 bx.plot(temp,z,color=col,lw=2,label=label)
 bx.plot(adiabat[z<2550],z[z<2550],color=col,lw=.8,ls=':')
 bx.scatter([tp],[0],color=col,s=20)
bx.text(1460,950,'Convecting interior:\nnear an adiabat',fontsize=9)
bx.text(1800,2690,'Core-side boundary layer',fontsize=8,ha='center')
bx.set(ylim=(2890,0),xlim=(0,3200),xlabel='Temperature (°C)',ylabel='Depth (km)',title='Adiabat and thermal boundary layers')
bx.legend(loc='center left',bbox_to_anchor=(0,.48),fontsize=7,frameon=False)
bx.grid(alpha=.15)
fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=120,transparent=False,metadata={'Software':'Original conceptual thermal-history diagram'})
plt.close(fig)
