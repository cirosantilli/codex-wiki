"""Original analytic teaching diagram; Python 3.14, numpy, matplotlib.
Run from the desired output directory; writes its basename PNG to cwd.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Dimensionless r_s = c = 1, inward geodesic of unit specific energy.
r0=4.;outside=np.geomspace(3,1e-5,1300)+1
proper=lambda r:2*(r0**1.5-r**1.5)/3
G=lambda r:2*r**1.5/3+2*np.sqrt(r)+np.log((np.sqrt(r)-1)/(np.sqrt(r)+1))
t=G(r0)-G(outside);rstar=lambda r:r+np.log(r-1)
reception=t-rstar(outside)+rstar(r0)
ratio=1-1/np.sqrt(outside)
fig,axs=plt.subplots(1,3,figsize=(12,3.8),layout="constrained")
a=axs[0];rr=np.linspace(r0,.1,1000);tt=proper(rr)
a.plot(tt,rr,color="#326a97",lw=2);a.axhline(1,color="#aa3939",ls="--");a.plot(proper(1),1,"o",color="#aa3939")
a.text(.2,1.25,"horizon",color="#aa3939",fontsize=10)
a.set(xlabel="Particle proper time / (r_s/c)",ylabel="Areal radius / r_s",title="Finite proper-time crossing",ylim=(0,4.1))
b=axs[1];b.plot(reception,outside,color="#326a97",lw=2);b.axhline(1,color="#aa3939",ls="--")
b.set(xlabel="Relative distant reception time / (r_s/c)",ylabel="Emission radius / r_s",title="Outgoing signals are delayed",ylim=(.85,4.1))
c=axs[2];c.semilogy(reception,ratio,color="#326a97",lw=2)
c.set(xlabel="Relative distant reception time / (r_s/c)",ylabel="Received / emitted proper frequency",title="The received signal reddens")
for ax in axs:ax.grid(alpha=.2)
fig.suptitle("Original ideal radial-infall signal example, launched inward from r = 4 r_s with k = 1")
fig.savefig("paper-1-infall-signals.png",dpi=155,facecolor="white")
