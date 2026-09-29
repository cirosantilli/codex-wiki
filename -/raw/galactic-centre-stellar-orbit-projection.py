"""Original chosen orbit, not observed S2 astrometry."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

def orbit(phase):
    M=2*np.pi*np.asarray(phase);E=M.copy()
    for _ in range(20):E-=(E-.7*np.sin(E)-M)/(1-.7*np.cos(E))
    plane=825*np.array([np.cos(E)-.7,np.sqrt(1-.7**2)*np.sin(E),np.zeros_like(E)])
    i,w,O=np.deg2rad([55,35,20])
    rz=lambda a:np.array([[np.cos(a),-np.sin(a),0],[np.sin(a),np.cos(a),0],[0,0,1]])
    rx=np.array([[1,0,0],[0,np.cos(i),-np.sin(i)],[0,np.sin(i),np.cos(i)]])
    sky=(rz(O)@rx@rz(w))@plane
    return plane,sky/7.5  # AU at 7.5 kpc -> mas in the small-angle model.
phase=np.linspace(0,1,1201);plane,sky=orbit(phase)
marks=np.arange(12)/12;mp,ms=orbit(marks)
fig,axs=plt.subplots(1,2,figsize=(12,5),dpi=140,facecolor='white')
for ax,xy,pts,title,xlabel,ylabel in zip(axs,[plane,sky],[mp,ms],['True orbital plane','Apparent sky path'],[r"$x'$ (AU)",'Sky x (mas)'],[r"$y'$ (AU)",'Sky y (mas)']):
    ax.plot(xy[0],xy[1],color='#8a9298',lw=1.8)
    points=ax.scatter(pts[0],pts[1],c=marks,cmap='viridis',vmin=0,vmax=1,s=48,zorder=4)
    ax.scatter([0],[0],marker='*',s=135,color='#222',zorder=5)
    ax.annotate('Central mass',(0,0),xytext=(-80,-24),textcoords='offset points',fontsize=10,arrowprops=dict(arrowstyle='->',lw=.8,color='#666'))
    ax.set(title=title,xlabel=xlabel,ylabel=ylabel);ax.set_aspect('equal',adjustable='datalim');ax.grid(alpha=.16)
axs[0].text(.025,.96,'True focus at the mass',transform=axs[0].transAxes,va='top',fontsize=10)
axs[1].text(.025,.96,'Projected mass position need not be\na focus of this apparent ellipse',transform=axs[1].transAxes,va='top',fontsize=10)
fig.suptitle('The same stellar orbit in its own plane and on the sky',fontsize=16,y=.98)
fig.subplots_adjust(left=.075,right=.88,top=.84,bottom=.22,wspace=.30)
cax=fig.add_axes([.91,.25,.015,.50]);cbar=fig.colorbar(points,cax=cax);cbar.set_label('Time / period');cbar.set_ticks([0,.5,1])
fig.text(.5,.055,'Chosen orbit: a = 825 AU, P = 18 years, e = 0.70, i = 55°, ω = 35°, Ω = 20°, D = 7.5 kpc. Equal-time markers; no observed points.',ha='center',fontsize=10)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,facecolor='white')
