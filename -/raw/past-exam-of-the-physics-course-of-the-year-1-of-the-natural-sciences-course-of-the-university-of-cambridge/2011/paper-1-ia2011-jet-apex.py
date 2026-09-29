"""Original ballistic-jet solution plot; Python 3.14, NumPy, Matplotlib.
Writes the basename PNG to cwd. Ideal projectile model; g=9.81 m/s².
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
g=9.81;h=2.5;w=5
uy=np.sqrt(2*g*h);ux=w*g/uy;ta=uy/g
t=np.linspace(0,1.22*ta,401);x=ux*t;y=uy*t-g*t*t/2
fig,ax=plt.subplots(figsize=(7.8,4.5),layout='constrained')
ax.plot(x,y,color='#286a9e',linewidth=2.5,label='Ideal ballistic trajectory')
ax.scatter([w],[h],color='#a54727',zorder=4)
ax.annotate('Horizontal arrival',xy=(w,h),xytext=(3.4,1.65),arrowprops={'arrowstyle':'->'},fontsize=11)
ax.annotate('',xy=(w+.7,h),xytext=(w,h),arrowprops={'arrowstyle':'->','color':'#a54727','lw':2})
ax.axhline(h,ls=':',color='gray',linewidth=1)
ax.set(xlabel='Horizontal distance (m)',ylabel='Height (m)',xlim=(-.1,6.25),ylim=(-.05,3.05),title='Target at the trajectory apex')
ax.grid(alpha=.2);ax.legend(loc='lower right')
fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=145,facecolor='white')
