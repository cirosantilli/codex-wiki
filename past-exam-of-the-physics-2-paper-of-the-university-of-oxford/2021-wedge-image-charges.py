"""Original method-of-images construction; Python 3.14, numpy/matplotlib."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Wedge

fig,ax=plt.subplots(figsize=(6.5,6),facecolor='white')
ax.add_patch(Wedge((0,0),1.55,0,60,color='#e5eef7'))
for angle in [0,np.pi/3]:
    ax.plot([0,1.55*np.cos(angle)],[0,1.55*np.sin(angle)],color='#26364a',lw=2.5)
t=np.linspace(0,2*np.pi,361);ax.plot(np.cos(t),np.sin(t),'--',color='#9eabb8',lw=1)
for j,deg in enumerate(range(30,360,60)):
    th=np.deg2rad(deg);x,y=np.cos(th),np.sin(th)
    positive=j%2==0;color='#b33134' if positive else '#2466a7'
    ax.scatter(x,y,s=330,c=color,zorder=5)
    ax.text(x,y,'+' if positive else '−',color='white',ha='center',va='center',fontsize=17,zorder=6)
    ax.text(1.25*x,1.25*y,f'{deg}°\n'+('real q' if j==0 else ('+q image' if positive else '−q image')),ha='center',va='center',fontsize=11)
ax.plot([0,np.sqrt(3)/2],[0,.5],color='#b33134',lw=1.2)
ax.text(.37,.12,'d',fontsize=13,color='#b33134')
ax.text(.68,.11,'physical wedge',fontsize=11,color='#385571')
ax.annotate('',xy=(.43,.248),xytext=(.81,.468),arrowprops={'arrowstyle':'->','color':'#26364a','lw':2})
ax.text(-.12,-.45,'Force towards\nthe intersection',fontsize=11,ha='center')
ax.plot(0,0,'ko',ms=4);ax.set_aspect('equal');ax.set_xlim(-1.6,1.7);ax.set_ylim(-1.6,1.6);ax.axis('off')
ax.set_title('Grounded 60° wedge: real charge and five images',fontsize=13,pad=15)
fig.tight_layout()
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white',transparent=False)
