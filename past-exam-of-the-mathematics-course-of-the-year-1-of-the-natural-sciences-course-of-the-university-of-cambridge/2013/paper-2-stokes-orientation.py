"""Original Stokes orientation sketch. Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

The white PNG is saved to cwd, normally the mirrored _media directory.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

th=np.linspace(0,np.pi/2,35);ph=np.linspace(0,2*np.pi,90)
TH,PH=np.meshgrid(th,ph)
X=np.sin(TH)*np.cos(PH);Y=np.sin(TH)*np.sin(PH);Z=np.cos(TH)
fig=plt.figure(figsize=(6.7,5.0),layout='constrained',facecolor='white')
ax=fig.add_subplot(projection='3d')
ax.plot_surface(X,Y,Z,color='#78b9dc',alpha=.32,linewidth=.15,edgecolor='#d9e8ef')
p=np.linspace(0,2*np.pi,500)
ax.plot(np.cos(p),np.sin(p),np.zeros_like(p),color='#0072b2',lw=2.2)
for q in [.15*np.pi,1.35*np.pi]:
    ax.quiver(np.cos(q),np.sin(q),0,-.35*np.sin(q),.35*np.cos(q),0,
              color='#0072b2',arrow_length_ratio=.3,lw=2)
P=np.array([.6,-.35,np.sqrt(1-.6**2-.35**2)])
ax.quiver(*P,*(.45*P),color='#d55e00',arrow_length_ratio=.2,lw=2)
ax.text(*(1.5*P),r'$\mathbf{n}\,dA=d\mathbf{S}$',fontsize=11,color='#b84a00')
q=1.35*np.pi
ax.text(np.cos(q)-.2,np.sin(q)-.15,.04,r'$d\mathbf{r}$',color='#0072b2',fontsize=11)
ax.text(-.6,.3,.9,'$S$',fontsize=14)
ax.text(.6,.8,0,'$C$',fontsize=13,color='#0072b2')
ax.quiver(0,0,0,0,0,1.4,color='#555555',arrow_length_ratio=.06,lw=.8)
ax.text(0,0,1.43,'$z$',fontsize=11)
ax.set(xlim=(-1.25,1.25),ylim=(-1.3,1.2),zlim=(-.08,1.5))
ax.set_box_aspect((1,1,.72));ax.view_init(elev=25,azim=-55);ax.set_axis_off()
ax.set_title('Outward hemisphere normal\nBoundary counterclockwise from above')
fig.savefig(Path(__file__).with_suffix('.png').name,dpi=160,facecolor='white')
