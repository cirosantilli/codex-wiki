"""Original teaching diagram. Tested with Python 3.14, numpy, matplotlib.
Run in the desired output directory; PNG is written as a basename in cwd.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

fig,axs=plt.subplots(2,3,figsize=(10,7),layout="constrained")
branches=[]
for lam,title in [(4,"Repulsive B > 0; lambda = 4"),(.25,"Weak attraction; lambda = 1/4")]:
 th=np.linspace(-np.arccos(.2)/np.sqrt(lam),np.arccos(.2)/np.sqrt(lam),2500);r=1/np.cos(np.sqrt(lam)*th);branches.append((title,th,r))
th=np.linspace((.2-1)/.3,22,3500);branches.append(("Critical attraction; lambda = 0",th,1/(1+.3*th)))
th=np.linspace(np.arcsinh(.2),8,2500);branches.append(("Strong attraction; energy > 0",th,1/np.sinh(th)))
th=np.linspace(-np.log(5),7,2500);branches.append(("Strong attraction; energy = 0",th,np.exp(-th)))
th=np.linspace(-8,8,3500);branches.append(("Strong attraction; energy < 0",th,2/np.cosh(th)))
for ax,(title,th,r) in zip(axs.flat,branches):
 ax.plot(r*np.cos(th),r*np.sin(th),color="#326a97",lw=1.6);ax.plot(0,0,"o",color="#aa3939",ms=4)
 if "Critical" in title:
  ang=np.linspace(0,2*np.pi,300);ax.plot(np.cos(ang),np.sin(ang),ls="--",color="#8a8a8a",lw=1);ax.text(-4.7,4,"dashed: marginal circle",fontsize=8)
 if "Strong" in title:ax.text(-4.7,-4.5,"spiralling ends reach the centre",fontsize=8)
 ax.axhline(0,color="#cccccc",lw=.5);ax.axvline(0,color="#cccccc",lw=.5)
 ax.set(xlim=(-5,5),ylim=(-5,5),aspect="equal",title=title,xticks=[],yticks=[])
fig.suptitle("Inverse-cube force: original positive-radius orbit branches (arbitrary length scale)")
fig.savefig("paper-1-inverse-cube-orbits.png",dpi=155,facecolor="white")
