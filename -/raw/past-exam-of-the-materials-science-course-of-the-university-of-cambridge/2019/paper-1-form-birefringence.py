"""Original mathematical illustration; write the matching PNG to cwd."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon,Rectangle,Circle
plt.rcParams.update({"font.size":11,"axes.titlesize":13,"figure.facecolor":"white","savefig.facecolor":"white"})
def save(fig):
    fig.savefig(Path(__file__).with_suffix(".png").name,dpi=150,facecolor="white")
    plt.close(fig)
fig,axs=plt.subplots(1,3,figsize=(12,4.2),layout='constrained')
ax=axs[0]
for y in np.linspace(.2,.8,8):ax.plot([.08,.92],[y,y],lw=6,c='#3882aa')
ax.annotate('Slow direction',(.9,.93),(.12,.93),arrowprops={'arrowstyle':'->'},va='center')
ax.set(xlim=(0,1),ylim=(0,1),title='Subwavelength parallel rods');ax.set_aspect('equal');ax.axis('off')
ax=axs[1];x=np.linspace(0,8,300);gam=.009*x*1e6*np.tan(np.deg2rad(.5));g0=.009*5e6*np.tan(np.deg2rad(.5))
ax.plot(x,gam,label='Quartz wedge');ax.axhline(g0,c='#b85733',ls='--',label='Film magnitude');ax.plot(x,gam-g0,c='.25',label='Signed difference')
ax.axhline(0,c='.65',lw=.7);ax.scatter([5],[0],c='black',zorder=4)
ax.annotate('White-light compensation\n5 mm; film ≈ 393 nm',(5,0),(.2,-220),arrowprops={'arrowstyle':'->'},fontsize=9)
ax.set(xlabel='Distance from wedge tip / mm',ylabel='Optical path difference / nm',title='Perpendicular slow axes');ax.legend(fontsize=8,loc='upper left')
ax=axs[2];v=np.linspace(-1,1,501);xx,yy=np.meshgrid(v,v);r=np.hypot(xx,yy);phi=np.arctan2(yy,xx);im=np.sin(2*phi)**2;im=np.where(r<=.95,im,np.nan)
ax.imshow(im,extent=(-1,1,-1,1),origin='lower',cmap='inferno',vmin=0,vmax=1);ax.set_title('Radial rods: extinction cross');ax.set_xticks([]);ax.set_yticks([])
ax.set_xlabel('Polarizer axes: horizontal / vertical',fontsize=9)
fig.suptitle('Ideal optical response; radial image is monochromatic normalized intensity')
save(fig)
