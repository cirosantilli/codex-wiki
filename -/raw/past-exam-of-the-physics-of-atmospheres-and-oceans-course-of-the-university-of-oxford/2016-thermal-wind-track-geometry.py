"""Original explanatory figure. Tested with Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Run from any directory; the only output is a same-basename PNG in that directory.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 12, "axes.titlesize": 14, "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white"})

from matplotlib.patches import Ellipse
fig,axs=plt.subplots(1,3,figsize=(11.7,4.2),layout='constrained')
x=np.linspace(-1.2,1.2,100);xx,yy=np.meshgrid(x,x)
axs[0].contour(xx,yy,xx+yy,levels=[-1.2,-.6,0,.6,1.2],colors='#adb8c2',linewidths=1.3)
axs[0].annotate('',xy=(.7,-.7),xytext=(-.3,.3),arrowprops={'arrowstyle':'-|>','lw':3,'color':'#126782'})
axs[0].annotate('Denser water',xy=(.75,.75),xytext=(-1.05,.9),arrowprops={'arrowstyle':'->','color':'#a44418'},color='#a44418',fontsize=11)
axs[0].text(.13,-1.0,'Current',color='#126782',fontsize=12)
axs[0].set(aspect='equal',xlim=(-1.2,1.2),ylim=(-1.2,1.2),xlabel='East',ylabel='North',title='Denser water lies to the left')
axs[0].set_xticks([]);axs[0].set_yticks([])
for angle,color,label in [(0,'#126782','East-going ship'),(5,'#a44418','Other ship: 5°'),(90,'#626767','Alternative: 90°')]:
    th=np.deg2rad(angle);v=np.array([np.cos(th),np.sin(th)])
    axs[1].annotate('',xy=v,xytext=(0,0),arrowprops={'arrowstyle':'-|>','lw':2.4,'color':color})
    position={'East-going ship':(.03,-.16),'Other ship: 5°':(.03,.20),'Alternative: 90°':(.08,.91)}[label]
    axs[1].text(*position,label,fontsize=11,color=color)
axs[1].set(aspect='equal',xlim=(-.12,1.13),ylim=(-.25,1.15),xlabel='East',ylabel='North',title='Nearly parallel tracks are redundant')
axs[1].set_xticks([]);axs[1].set_yticks([])
C=5.654e-5;sig=2e-7
for angle,color in [(5,'#a44418'),(90,'#126782')]:
    th=np.deg2rad(angle);s=np.sin(th);c=np.cos(th)
    cov=(sig/C)**2*np.array([[(1+c*c)/(s*s),c/s],[c/s,1.]])
    vals,vecs=np.linalg.eigh(cov);direction=np.rad2deg(np.arctan2(vecs[1,1],vecs[0,1]))
    axs[2].add_patch(Ellipse((0,0),2*np.sqrt(vals[1]),2*np.sqrt(vals[0]),angle=direction,facecolor='none',edgecolor=color,lw=2.3,label=f'{angle}° tracks'))
axs[2].axhline(0,color='#cccccc',lw=.8);axs[2].axvline(0,color='#cccccc',lw=.8)
axs[2].set(xlim=(-.066,.066),ylim=(-.0055,.0055),xlabel=r'Zonal error $\delta u$ (m/s)',ylabel=r'Meridional error $\delta v$ (m/s)',title='Unit covariance ellipses')
axs[2].tick_params(axis='both',labelsize=9);axs[2].legend(fontsize=10,loc='upper left');axs[2].grid(alpha=.16)
fig.suptitle('Thermal-wind inference from ship tracks in a steady Northern-Hemisphere density field',fontsize=15)

fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name, dpi=140, facecolor='white', transparent=False)
plt.close(fig)
