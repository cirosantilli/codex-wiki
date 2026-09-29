"""Original conditional magnetic curves and physical-sign Poisson-Boltzmann solutions."""
import numpy as np
import matplotlib.pyplot as plt
fig,axs=plt.subplots(2,2,figsize=(11,8),layout="constrained")
ax=axs[0,0];h=np.linspace(-4,4,800)
ax.plot(h,np.tanh(h),label="equilibrated illustrative response")
for hc,style,label in [(.5,"--","blocked"),(1.,"-.", "one interacting example")]:
 ax.plot(h,np.tanh(1.7*(h-hc)),style,label=label)
 ax.plot(h,np.tanh(1.7*(h+hc)),style,color=ax.lines[-1].get_color())
ax.set(xlabel="field (chosen units)",ylabel="normalized magnetization",title="A  Conditional loop changes");ax.legend(fontsize=8)
ax.text(-3.8,-.15,"no unique interaction trend",fontsize=9)
ax=axs[0,1];n=np.linspace(.05,5,400)
ax.plot(n,n**-.5);ax.set(xlabel="bulk density / reference density",ylabel="Debye length / reference length",title="B  Screening length ∝ density⁻¹ᐟ²")
x=np.linspace(0,6,600)
for ax,u0,title in [(axs[1,0],.2,"C  Weak positive surface potential"),(axs[1,1],3,"D  Strong positive surface potential")]:
 u=4*np.arctanh(np.tanh(u0/4)*np.exp(-x))
 ax.plot(x,np.exp(u),label="counterions (negative)")
 ax.plot(x,np.exp(-u),label="co-ions (positive)")
 ax.axhline(1,color="gray",ls=":");ax.set(xlabel="distance / Debye length",ylabel="number density / bulk density",title=title)
 ax.legend(fontsize=9)
fig.savefig("paper-2-magnetism-and-screening.png",dpi=150,facecolor="white")

