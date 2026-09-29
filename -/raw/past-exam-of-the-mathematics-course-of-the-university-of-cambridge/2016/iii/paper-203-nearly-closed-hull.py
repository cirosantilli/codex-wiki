"""Illustrate the sharp hull-displacement example. Python 3.14, matplotlib 3.10.7.

Run in the intended output directory. Only the PNG output uses the current cwd.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig,ax=plt.subplots(figsize=(7,3.3),dpi=100,facecolor='white')
theta=np.linspace(.22,np.pi,500)
ax.plot(np.cos(theta),np.sin(theta),color='#2467a9',lw=3,label=r'$K_L$: semicircular slit')
ax.plot([-1.35,1.4],[0,0],color='#545454',lw=1.2)
ax.scatter([-.86],[.14],s=48,color='#ba392f',zorder=4)
ax.text(-.75,.14,r'$z_\delta\to-1$',color='#922b23',fontsize=11,va='center')
ax.text(-1.08,-.10,r'$-1$',fontsize=10)
ax.text(.97,-.10,r'$1$',fontsize=10)
ax.text(-.20,.55,'Interior bay',fontsize=11,ha='center')
ax.annotate('Narrow passage',xy=(.98,.11),xytext=(1.12,.55),fontsize=10,
            ha='center',arrowprops={'arrowstyle':'->','color':'#545454'})
ax.text(-.15,.29,r'$g_{K_L}(z_\delta)\to2$',fontsize=11,ha='center')
ax.set(xlim=(-1.35,1.75),ylim=(-.17,1.17),aspect='equal')
ax.axis('off')
fig.suptitle('A nearly closed slit makes the displacement approach 3',fontsize=11,y=.97)
fig.subplots_adjust(left=.035,right=.985,bottom=.08,top=.87)
fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=100,facecolor='white',transparent=False)
plt.close(fig)
