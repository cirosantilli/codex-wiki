"""Original subcritical Roche-model sketch. Python 3.14.4, NumPy 2.3.5,
Matplotlib 3.10.7. Writes basename to caller CWD; honors caller MPLCONFIGDIR.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

# Dimensionless GM=polar radius=1; w is below the Roche breakup value 8/27.
w=.25
theta=np.linspace(0,2*np.pi,721)
s2=np.sin(theta)**2
lo=np.ones_like(theta);hi=np.full_like(theta,1.5)
for _ in range(60):
    r=(lo+hi)/2
    potential=1/r+w*r*r*s2/2
    lo=np.where(potential>1,r,lo);hi=np.where(potential>1,hi,r)
r=(lo+hi)/2
radial=1/r**2-w*r*s2
polar=-w*r*np.sin(theta)*np.cos(theta)
gravity=np.hypot(radial,polar)
te=gravity**.25
points=np.column_stack((r*np.sin(theta),r*np.cos(theta)))
segments=np.stack((points[:-1],points[1:]),axis=1)
fig,ax=plt.subplots(figsize=(7.4,5.5),layout='constrained',facecolor='white')
ax.fill(points[:,0],points[:,1],color='#fff2df')
lines=LineCollection(segments,cmap='inferno',norm=plt.Normalize(te.min(),1),linewidth=8)
lines.set_array((te[:-1]+te[1:])/2);ax.add_collection(lines)
ax.plot([0,0],[-1.4,1.4],color='#667788',ls='--',lw=1)
ax.annotate('Rotation axis Ω',(0,1.38),(.2,1.3),fontsize=10)
ax.annotate('Hot pole: high effective gravity',(0,1),(-2.1,1.1),arrowprops={'arrowstyle':'->'},fontsize=10)
ax.annotate('Cool equator:\ncentrifugal support', (points[180,0],0),(.7,-1.1),arrowprops={'arrowstyle':'->'},fontsize=10)
ax.annotate('Hot pole',(0,-1),(-1.7,-1.2),arrowprops={'arrowstyle':'->'},fontsize=10)
ax.text(0,0,'Oblate stellar\nequipotential',ha='center',va='center',fontsize=12)
ax.set(xlim=(-2.2,1.95),ylim=(-1.45,1.55),aspect='equal',title='Radiative gravity darkening: Te ∝ g¹⁄⁴')
ax.set_axis_off()
fig.colorbar(lines,ax=ax,shrink=.7,label='Effective temperature / polar value')
fig.savefig('paper-70-gravity-darkening.png',dpi=110,facecolor='white',transparent=False)
