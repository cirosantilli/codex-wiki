"""Illustrative thin-plate dispersion; tested Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
rho,rhoi,g,h,E,nu=1025.,917.,9.81,3.,5e9,.3
D=E*h**3/(12*(1-nu**2));alpha=rhoi*h/rho;beta=D/rho
k=np.geomspace(.001,.11,3000)
w=np.sqrt((g*k+beta*k**5)/(1+alpha*k))
T=2*np.pi/w;cp=w/k
cg=(g+5*beta*k**4+4*alpha*beta*k**5)/(2*w*(1+alpha*k)**2)
fig,ax=plt.subplots(figsize=(8,4.8),dpi=120,layout="constrained")
ax.plot(T,cp,color="#2764a7",label="Ice: phase velocity")
ax.plot(T,cg,color="#ae4737",label="Ice: group velocity")
t=np.linspace(4,45,400)
ax.plot(t,g*t/(2*np.pi),"--",color="#2764a7",label="Open water: phase velocity")
ax.plot(t,g*t/(4*np.pi),"--",color="#ae4737",label="Open water: group velocity")
j=np.argmin(cg);ax.plot(T[j],cg[j],"o",color="#ae4737")
ax.annotate("Group minimum",(T[j],cg[j]),xytext=(18,25),arrowprops={"arrowstyle":"->"})
ax.set(xlim=(4,45),ylim=(0,85),xlabel="Wave period (s)",ylabel="Velocity (m/s)",title="Flexural-gravity and open-water dispersion")
ax.text(.02,.96,"Illustration: h = 3 m, E = 5 GPa, ν = 0.3\nIce density 917 kg/m³; deep water; no prestress",transform=ax.transAxes,va="top",fontsize=9)
ax.grid(alpha=.2);ax.legend(loc="upper right",fontsize=9)
fig.savefig("paper-72-flexural-gravity.png",facecolor="white",transparent=False)
