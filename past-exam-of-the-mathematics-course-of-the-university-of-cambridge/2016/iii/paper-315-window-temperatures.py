"""Original schematic; writes only to the current working directory.
Tested: Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({'font.size': 10, 'axes.spines.top': False, 'axes.spines.right': False})

fig, ax=plt.subplots(figsize=(9,4), dpi=100)
p=np.geomspace(.003,10,400)
t=np.interp(np.log10(p),np.log10([.003,.01,.05,.1,.3,1,3,10]),[1100,1250,1450,1500,2200,3080,3600,4500])
ax.plot(t,p,color='#273b69',lw=2.5)
for temp,pres,label,col in [(1500,.1,r'$4.5\,\mu$m: $T_2=1500$ K','#c0433c'),(3080,1,r'$20\,\mu$m: $T_1\simeq3080$ K','#007f74'),(3600,3,r'J window: $T_3\gtrsim T_1$','#8155a5')]:
 ax.scatter([temp],[pres],color=col,s=45,zorder=5)
 ax.annotate(label,(temp,pres),xytext=(13,-4),textcoords='offset points',color=col,fontsize=11)
ax.set_yscale('log'); ax.set_ylim(13,.002); ax.set_xlim(900,4900)
ax.set_xlabel('Temperature (K)'); ax.set_ylabel('Pressure (bar; increases downward)')
ax.set_title('Different infrared contribution depths on a non-inverted profile',pad=12)
ax.grid(alpha=.16)
fig.text(.53,.02,'Illustrative depths, not pressures measured from brightness alone.',ha='center',fontsize=9)
fig.subplots_adjust(left=.10,right=.98,bottom=.19,top=.85)

fig.savefig(Path.cwd() / 'paper-315-window-temperatures.png', dpi=100, facecolor='white', transparent=False)
plt.close(fig)
