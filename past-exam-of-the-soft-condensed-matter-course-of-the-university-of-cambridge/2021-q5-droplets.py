"""Original equal-volume caps; Python 3.14, NumPy 2.3, Matplotlib 3.10.
The volume and lengths are illustrative. Output is in cwd.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
import numpy as np

plt.rcParams.update({'font.size':11,'figure.facecolor':'white'})
fig,ax=plt.subplots(figsize=(8.4,3.3),layout='constrained')
ax.axhline(0,color='0.3',lw=2)
for centre,angle,color,label in [(-1.85,102,'#5badd6','water'),(1.25,25,'#d9ac49','oil')]:
    th=np.deg2rad(angle)
    radius=(3/(np.pi*(2-3*np.cos(th)+np.cos(th)**3)))**(1/3)
    t=np.linspace(-th,th,600)
    x=centre+radius*np.sin(t)
    y=radius*(np.cos(t)-np.cos(th))
    ax.fill(x,y,color=color,alpha=.45)
    ax.plot(x,y,color=color,lw=2.5)
    foot=centre+radius*np.sin(th)
    arc_radius=.23 if angle==102 else .40
    ax.add_patch(Arc((foot,0),2*arc_radius,2*arc_radius,theta1=180-angle,theta2=180,color='0.25',lw=1))
    mid=np.deg2rad(180-angle/2)
    lab_r=arc_radius+.14
    ax.text(foot+lab_r*np.cos(mid),lab_r*np.sin(mid),f'{angle}°',ha='center',va='center',fontsize=10)
    ax.text(centre,radius*(1-np.cos(th))+.12,label,ha='center',color=color,fontsize=13)
ax.text(-3,-.16,'Teflon',color='0.3')
ax.set(xlim=(-3.1,3.1),ylim=(-.25,1.2),aspect='equal',title='Equal volume: water beads up, oil spreads')
ax.axis('off')
fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white')
plt.close(fig)
