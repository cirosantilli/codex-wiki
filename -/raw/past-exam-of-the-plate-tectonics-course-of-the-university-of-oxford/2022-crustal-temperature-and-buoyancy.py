#!/usr/bin/env python3
"""Original calculations under explicitly assumed conductive/isostatic models.
Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7; PNG written to CWD.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'figure.facecolor':'white','axes.facecolor':'white','savefig.facecolor':'white'})
fig,(ax,bx)=plt.subplots(1,2,figsize=(8,3.8),layout='constrained')
z=np.linspace(0,7000,301);k=1.3
for q,col,name in [(.20,'#b2182b','Young crust: q = 0.20 W/m²'),(.07,'#2166ac','Old crust: q = 0.07 W/m²')]:
 ax.plot(q*z/k,z/1000,color=col,lw=2,label=name)
 ax.plot([q*7000/(2*k)]*2,[0,7],color=col,lw=1,ls=':')
ax.set(ylim=(7,0),xlim=(0,1200),xlabel='Temperature above seafloor (°C)',ylabel='Depth within oceanic crust (km)',title='Illustrative conductive geotherms')
ax.legend(loc='lower left',fontsize=8,frameon=True,facecolor='white',framealpha=.9)
ax.text(30,1,'Mean temperature = half basal value\nfor these linear profiles',fontsize=8,bbox={'facecolor':'white','edgecolor':'none','alpha':.9})
ax.grid(alpha=.15)
L=np.linspace(0,15,300)
delta=(.20-.07)*7000/(2*k)
h=1e-5*delta*L*1000
bx.plot(L,h,color='#5c3183',lw=2)
bx.scatter([7],[24.5],color='#5c3183',s=32)
bx.annotate('7 km → 24.5 m',xy=(7,24.5),xytext=(1.2,40),arrowprops={'arrowstyle':'->'},fontsize=9)
bx.set(xlim=(0,15),ylim=(0,55),xlabel='Thermally anomalous column thickness (km)',ylabel='Isostatic height difference (m)',title='Crust-only thermal support is modest')
bx.text(.5,5,'α = 10⁻⁵ K⁻¹; ΔT = 350 K\nUnit density ratio assumed',fontsize=8)
bx.grid(alpha=.15)
fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=120,transparent=False,metadata={'Software':'Original linear-conduction and isostatic calculations'})
plt.close(fig)
