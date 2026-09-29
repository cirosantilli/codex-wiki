"""Original schematic; writes only to the current working directory.
Tested: Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({'font.size': 10, 'axes.spines.top': False, 'axes.spines.right': False})

fig,axes=plt.subplots(1,3,figsize=(12,4.3),dpi=100)
blue='#2574a9'; red='#c4473e'
def curve(ax,pr,tr,rcb):
 p=np.geomspace(pr[0],pr[-1],350); t=np.interp(np.log10(p),np.log10(pr),tr)
 ax.plot(t[p<=rcb],p[p<=rcb],color=blue,lw=2.5)
 ax.plot(t[p>=rcb],p[p>=rcb],color=red,lw=2.5)
 ax.axhline(rcb,ls=':',color='0.35'); ax.set_yscale('log');ax.set_ylim(pr[-1],pr[0])
 ax.set_xlabel('Temperature (K)');ax.grid(alpha=.13)
 ax.text(.03,.07,f'Nominal RCB: {rcb:g} bar',transform=ax.transAxes,fontsize=9,bbox={'facecolor':'white','edgecolor':'none','alpha':.9})
curve(axes[0],[1e-4,.001,.01,.1,1],[270,260,240,210,288],.1)
axes[0].set_xlim(185,320);axes[0].set_title('Solar-system example: Earth')
axes[0].text(294,.004,'Radiative',color=blue,rotation=90,va='center')
axes[0].text(292,.4,'Convective',color=red,rotation=90,va='center')
axes[0].set_ylabel('Pressure (bar; downward)')
curve(axes[1],[1e-4,.001,.1,1,10,100,1000],[1300,1400,1500,1550,1700,2000,3850],100)
axes[1].plot([2100,1900,1500],[1e-4,.001,.1],ls='--',lw=1.8,color='#a86d19')
axes[1].text(2150,.003,'Optional\ninversion',fontsize=9,color='#a86d19')
axes[1].text(2400,1,'Radiative',color=blue);axes[1].text(2200,450,'Convective',color=red)
axes[1].set_xlim(1000,4150);axes[1].set_title('Strongly irradiated hot Jupiter')
curve(axes[2],[1e-4,.001,.01,.1,1,10,100],[600,650,800,1050,1400,2050,3050],1)
axes[2].text(1900,.01,'Radiative',color=blue);axes[2].text(2100,30,'Convective',color=red)
axes[2].set_xlim(400,3350);axes[2].set_title('Young, distant giant planet')
fig.text(.5,.015,'Qualitative examples; boundary pressures depend on opacity, gravity and intrinsic luminosity.',ha='center',fontsize=9)
fig.subplots_adjust(left=.065,right=.98,wspace=.27,bottom=.17,top=.88)

fig.savefig(Path.cwd() / 'paper-315-atmosphere-profiles.png', dpi=100, facecolor='white', transparent=False)
plt.close(fig)
