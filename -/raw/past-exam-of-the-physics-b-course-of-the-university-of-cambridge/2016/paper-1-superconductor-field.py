"""Original teaching diagram. Tested with Python 3.14, numpy, matplotlib.
Run in the desired output directory; PNG is written as a basename in cwd.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

x=np.linspace(-2,2,240);z=np.linspace(.003,2.5,240);X,Z=np.meshgrid(x,z)
Bx=np.zeros_like(X);Bz=np.zeros_like(X)
for h,m in [(1,1),(-1,-1)]:
 dz=Z-h;rr=X*X+dz*dz
 Bx+=3*m*X*dz/rr**2.5;Bz+=m*(2*dz*dz-X*X)/rr**2.5
norm=np.hypot(Bx,Bz);mask=X*X+(Z-1)**2<.025
Bx=np.ma.masked_where(mask,Bx/norm);Bz=np.ma.masked_where(mask,Bz/norm)
fig,ax=plt.subplots(figsize=(7,6),layout="constrained")
ax.axhspan(-.7,0,color="#dedede")
ax.streamplot(x,z,Bx,Bz,density=1.25,color="#326a97",linewidth=.9)
ax.axhline(0,color="black",lw=2)
ax.plot([-.12,.12],[1,1],color="black",lw=3)
ax.annotate("",xy=(0,1.35),xytext=(0,.9),arrowprops=dict(arrowstyle="->",color="#aa3939",lw=2))
ax.text(.15,1.25,"real moment +m",fontsize=10,bbox=dict(facecolor="white",edgecolor="none"))
ax.annotate("",xy=(.55,1.28),xytext=(.55,.94),arrowprops=dict(arrowstyle="->",color="#398244",lw=2))
ax.text(.6,1.1,"repulsive force",fontsize=9,bbox=dict(facecolor="white",edgecolor="none"))
ax.text(0,-.18,"B = 0 in physical superconductor",ha="center",fontsize=10)
ax.annotate("",xy=(0,-.58),xytext=(0,-.3),arrowprops=dict(arrowstyle="->",color="#aa3939",lw=2,linestyle="dashed"))
ax.text(.15,-.48,"opposite image moment (schematic only)",fontsize=9)
ax.set(xlim=(-2,2),ylim=(-.7,2.5),xlabel="x/h",ylabel="z/h",aspect="equal",title="Dipole-scale field with zero normal component at the plane")
fig.savefig("paper-1-superconductor-field.png",dpi=150,facecolor="white")
