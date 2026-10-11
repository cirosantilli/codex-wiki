"""Original figure; tested with Python 3.14.4.
Uses NumPy 2.3.5 and Matplotlib 3.10.7 from the root pyproject.toml.
Writes its PNG basename to the current working directory.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":10,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white","axes.spines.top":False,"axes.spines.right":False})
fig=plt.figure(figsize=(10.3,4.7),layout="constrained")
ax=fig.add_subplot(121,projection="3d");cut=fig.add_subplot(122)
phase=.8;vf=1.;omega=1.;length=phase;focus=1/np.tan(phase)
t=np.linspace(0,phase,240)
# Paraxial model, deliberately drawn at a visible transverse scale.
for angle,col in [(0,"#1565a8"),(np.pi/2,"#ca6720"),(np.pi,"#33865b"),(3*np.pi/2,"#805c9c")]:
 u0=.25*np.exp(1j*angle)
 u=u0*np.cos(t)*np.exp(-1j*t)
 ax.plot(t,u.real,u.imag,color=col,lw=1.7)
 extra=np.linspace(0,focus,80)
 out=(.25*np.cos(phase)-.25*np.sin(phase)*extra)*np.exp(1j*(angle-phase))
 ax.plot(phase+extra,out.real,out.imag,color=col,lw=1.3,ls="--")
ax.plot([0,phase+focus],[0,0],[0,0],color=".4",ls=":",lw=1)
ax.scatter([phase+focus],[0],[0],color="black",s=18)
ax.set(xlabel="Axial coordinate z",ylabel="x",zlabel="y",title="Four paraxial rays; dashed: field-free exit paths")
ax.set_box_aspect((2,.9,.9));ax.view_init(elev=24,azim=-58)
for coordinate_axis in [ax.xaxis,ax.yaxis,ax.zaxis]:
 coordinate_axis.pane.set_facecolor("white")
t=np.linspace(0,2*np.pi,700)
u=.5*(1+np.exp(-2j*t))
cut.plot(u.real,u.imag,color="#1565a8",lw=1.8)
cut.plot([0,1],[0,0],color=".5",ls=":",lw=1)
cut.scatter([0,.5,1],[0,0,0],color="black",s=18)
cut.text(.5,.08,"guiding centre",ha="center",fontsize=9)
cut.annotate("entry",xy=(1,0),xytext=(1.05,.28),arrowprops={"arrowstyle":"->"})
cut.text(-.1,-.12,"axis",fontsize=9)
cut.set(xlim=(-.18,1.3),ylim=(-.67,.67),xlabel=r"$x/\rho_0$",ylabel=r"$y/\rho_0$",title="Transverse orbit at fixed guiding centre",aspect="equal")
cut.grid(alpha=.13)
fig.suptitle("Ideal solenoid lens: the exit fringe removes azimuthal velocity; plot uses the paraxial approximation")
fig.savefig(Path(__file__).with_suffix('.png').name,dpi=135)
