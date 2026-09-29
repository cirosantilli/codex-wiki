"""Original teaching diagram. Tested with Python 3.14, numpy, matplotlib.
Run in the desired output directory; PNG is written as a basename in cwd.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

x=np.linspace(-2.5,2.5,260);z=np.linspace(-2,2,240)
X,Z=np.meshgrid(x,z);az=np.abs(Z)
Bx=np.sign(Z)*(np.arctan((.5-X)/az)+np.arctan((.5+X)/az))
Bz=.5*np.log(((X-.5)**2+Z**2)/((X+.5)**2+Z**2))
mask=(np.abs(Z)<.035)&(np.abs(X)<.54)
length=np.hypot(Bx,Bz);Bx=np.ma.masked_where(mask,Bx/length);Bz=np.ma.masked_where(mask,Bz/length)
fig,ax=plt.subplots(figsize=(8,5),layout="constrained")
ax.streamplot(x,z,Bx,Bz,density=1.3,color="#326a97",linewidth=.9,arrowsize=1)
ax.plot([-.5,.5],[0,0],color="black",lw=6)
ax.text(0,-.21,"I into page",ha="center",bbox=dict(facecolor="white",edgecolor="none"))
ax.text(.9,-.28,"strip width w",fontsize=10,bbox=dict(facecolor="white",edgecolor="none"))
ax.set(xlabel="x/w",ylabel="z/w",aspect="equal",title="Uniform strip current: sheet field nearby, line-current field far away")
fig.savefig("paper-1-strip-field.png",dpi=150,facecolor="white")
