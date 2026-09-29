from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Polygon
plt.rcParams.update({"font.size":11,"font.family":"DejaVu Sans","figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})

astar,cstar=2*np.pi/.353,2*np.pi/1.05;rho=(cstar/astar)**2
vertices=np.array([[(1+rho)/2,0],[(1-rho)/2,1],[-(1-rho)/2,1],[-(1+rho)/2,0],[-(1-rho)/2,-1],[(1-rho)/2,-1]])*np.array([astar,cstar])
width_cm=4.34*astar/5; height_cm=5.2*cstar/5
fig_width_cm=width_cm+3.; fig_height_cm=height_cm+3.
fig=plt.figure(figsize=(fig_width_cm/2.54,fig_height_cm/2.54))
ax=fig.add_axes([1.8/fig_width_cm,1.3/fig_height_cm,width_cm/fig_width_cm,height_cm/fig_height_cm])
ax.add_patch(Polygon(vertices,fc='#e2edf7',ec='#174c75',lw=2))
for h in range(-2,3):
 for l in range(-2,3):
  if (h+l)%2:continue
  inside=abs(h)<2 and abs(l)<2
  ax.scatter(h*astar,l*cstar,s=60,facecolor='#174c75' if inside else 'white',edgecolor='#174c75',zorder=4)
  ax.text(h*astar,l*cstar+.6,f'({h},0,{l})',ha='center',fontsize=9)
for l in [-1,1]:ax.axhline(l*cstar,color='gray',ls=':',lw=1)
ax.axhline(0,color='gray',lw=.6);ax.axvline(0,color='gray',lw=.6)
ax.set(xlim=(-2.17*astar,2.17*astar),ylim=(-2.6*cstar,2.6*cstar),xlabel=r'$Q_x$ (nm$^{-1}$)',ylabel=r'$Q_z$ (nm$^{-1}$)',title='Filled points: -2 < h,l < 2; h + l even')
ax.set_aspect('equal');ax.grid(alpha=.15)
fig.suptitle('Body-centered tetragonal (h,0,l) section: 1 cm = 5 nm$^{-1}$',fontsize=12)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=140,transparent=False)
