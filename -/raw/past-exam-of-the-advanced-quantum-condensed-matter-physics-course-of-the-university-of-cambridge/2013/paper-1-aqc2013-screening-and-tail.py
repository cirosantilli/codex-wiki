"""Original Lindhard function and asymptotic Friedel-tail illustration.
Python3.14/NumPy2.3/Matplotlib3.10. Write PNG basename in cwd.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def F(x):
    x=np.asarray(x,dtype=float)
    y=np.empty_like(x)
    a=np.abs(x)<1e-5;b=np.abs(x-1)<1e-12;c=~(a|b)
    y[a]=1-x[a]**2/3
    y[b]=0.5
    y[c]=0.5+(1-x[c]**2)/(4*x[c])*np.log(np.abs((1+x[c])/(1-x[c])))
    return y
plt.rcParams.update({"font.size":11,"figure.facecolor":"white","axes.facecolor":"white"})
fig,axes=plt.subplots(1,2,figsize=(9,3.4),layout="constrained")
x=np.sort(np.r_[np.linspace(0,3,1500),1])
axes[0].plot(x,F(x),lw=2)
axes[0].axvline(1,color="0.5",ls="--",lw=1)
axes[0].plot([1],[0.5],"o",color="#b33c28",ms=4)
axes[0].set(xlabel=r"$q/(2k_F)$",ylabel=r"$F$",title="Nonlocal screening function",ylim=(0,1.08))
r=np.linspace(4,22,1200)
rho=np.cos(2*r)/r**3
axes[1].plot(r,1000*rho,lw=1.8,color="#155e80")
axes[1].plot(r,1000/r**3,color="0.65",ls="--",lw=1)
axes[1].plot(r,-1000/r**3,color="0.65",ls="--",lw=1)
axes[1].axhline(0,color="0.7",lw=0.7)
axes[1].set(xlabel=r"$k_Fr$",ylabel="Arbitrary density units",title=r"Asymptotic tail: $C\cos(2k_Fr)/r^3$")
fig.savefig("paper-1-aqc2013-screening-and-tail.png",dpi=140,facecolor="white",bbox_inches="tight")
