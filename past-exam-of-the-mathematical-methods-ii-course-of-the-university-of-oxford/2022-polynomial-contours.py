"""Contours and gradient directions of a polynomial; output only into cwd."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import TwoSlopeNorm
import numpy as np

x = np.linspace(0, 3.2, 550)
X,Y = np.meshgrid(x,x)
Z = X*Y*(X**2-4)*(Y**2-4)
fig,ax = plt.subplots(figsize=(8.1,6.6),dpi=150,facecolor='white')
levels = [-65,-40,-20,-10,-5,0,5,9,20,40,80,160,300]
cf = ax.contourf(X,Y,Z,levels=levels,cmap='RdBu_r',norm=TwoSlopeNorm(vmin=-65,vcenter=0,vmax=300),alpha=.8,extend='min')
cs = ax.contour(X,Y,Z,levels=[-40,-20,-5,5,9,20,40,80,160],colors='#555555',linewidths=.65)
ax.clabel(cs,fontsize=8,inline=True,fmt='%g')
g = np.linspace(.13,3.06,17)
U,V = np.meshgrid(g,g)
gx = (3*U**2-4)*V*(V**2-4)
gy = (3*V**2-4)*U*(U**2-4)
norm = np.hypot(gx,gy)
ax.quiver(U,V,gx/norm,gy/norm,color='#20232a',angles='xy',scale_units='xy',scale=10,width=.0028,alpha=.75)
for z in [0,2]:
 ax.axvline(z,color='black',linestyle='--',lw=1.3)
 ax.axhline(z,color='black',linestyle='--',lw=1.3)
s=2/np.sqrt(3)
ax.scatter([0,0,2,2],[0,2,0,2],color='black',marker='D',s=40,label='Saddle (on full plane)',zorder=5,clip_on=False)
ax.scatter([s],[s],marker='*',s=160,color='#f1c232',edgecolor='black',lw=.9,label='Local maximum',zorder=6)
ax.annotate(r'$(2/\sqrt{3},2/\sqrt{3})$',(s,s),xytext=(1.18,.48),arrowprops=dict(arrowstyle='->',lw=.8),fontsize=11)
ax.set(xlim=(0,3.2),ylim=(0,3.2),xlabel='$x$',ylabel='$y$')
ax.set_aspect('equal')
ax.set_title(r'$z=xy(x^2-4)(y^2-4)$: contours and gradient directions',fontsize=13,pad=12)
ax.legend(loc='upper left',fontsize=9,framealpha=1)
fig.colorbar(cf,ax=ax,label='$z$',shrink=.86,pad=.035)
fig.tight_layout()
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,facecolor='white')
