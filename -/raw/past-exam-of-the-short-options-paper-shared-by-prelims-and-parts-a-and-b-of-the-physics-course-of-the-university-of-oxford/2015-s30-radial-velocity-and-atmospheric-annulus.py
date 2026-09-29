"""Original orbit curves and atmospheric annulus; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

fig,axs=plt.subplots(1,3,figsize=(14.5,4.6),layout='constrained',facecolor='white')
p=np.linspace(0,1,1000)
a=axs[0];a.plot(p,-np.sin(2*np.pi*p),lw=2.5,color='#2563eb');a.axhline(0,color='#94a3b8',lw=1);a.scatter([0,.5],[0,0],color=['#dc2626','#7c3aed'],zorder=4);a.annotate('Transit',xy=(0,0),xytext=(.05,.52),arrowprops=dict(arrowstyle='->'),fontsize=10);a.annotate('Occultation',xy=(.5,0),xytext=(.43,-.66),arrowprops=dict(arrowstyle='->'),fontsize=10);a.set(title='Circular: edge-on',xlabel='Phase from transit',ylabel=r'$(V-V_0)/K$',xlim=(0,1),ylim=(-1.2,1.2));a.grid(alpha=.2)
b=axs[1];M=2*np.pi*p;e=.5;E=M.copy()
for _ in range(12):E-=(E-e*np.sin(E)-M)/(1-e*np.cos(E))
nu=2*np.arctan2(np.sqrt(1+e)*np.sin(E/2),np.sqrt(1-e)*np.cos(E/2));b.plot(p,np.cos(nu)+e,lw=2.5,color='#dc2626');b.axhline(0,color='#94a3b8',lw=1);b.set(title=r'Eccentric: $e=0.5$, $\varpi=0$',xlabel='Phase from periastron',ylabel=r'$(V-V_0)/K$',xlim=(0,1),ylim=(-.7,1.7));b.grid(alpha=.2)
c=axs[2];c.add_patch(Circle((0,0),1.12,facecolor='#facc15',edgecolor='#d97706',lw=2));c.add_patch(Circle((0,0),1,facecolor='#475569',edgecolor='#1e293b',lw=2));c.annotate('',xy=(1,0),xytext=(0,0),arrowprops=dict(arrowstyle='<->',color='white',lw=1.8));c.text(.35,.10,r'$R_p$',color='white',fontsize=13);c.annotate('Atmospheric annulus',xy=(.78,.78),xytext=(-1.35,1.45),arrowprops=dict(arrowstyle='->'),fontsize=10);c.text(0,-1.46,r'$\Delta\delta\simeq 2R_pNH/R_*^2$',ha='center',fontsize=12);c.set(title='Transmission-depth change',xlim=(-1.65,1.65),ylim=(-1.7,1.75));c.set_aspect('equal');c.axis('off')
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=140,facecolor='white')
