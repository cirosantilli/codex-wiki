"""Original illustrative light-shift cycle. Save PNG basename in cwd."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
z=np.linspace(0,1,700)
u=-1-.5*np.cos(4*np.pi*z);v=-1+.5*np.cos(4*np.pi*z)
fig,ax=plt.subplots(figsize=(9,4),layout="constrained")
ax.plot(z,u,color="#274e82",label="Sublevel A")
ax.plot(z,v,color="#bc5429",label="Sublevel B")
for start,end,branch in [(0,.25,u),(.25,.5,v),(.5,.75,u),(.75,1,v)]:
 pos=(start+end)/2
 delta=.018
 def value(q):
  return -1+(-.5 if branch is u else .5)*np.cos(4*np.pi*q)
 ax.annotate("",xy=(pos+delta,value(pos+delta)),xytext=(pos-delta,value(pos-delta)),arrowprops={"arrowstyle":"-|>","lw":2,"color":"black"})
for q in [.25,.5,.75]:
 ax.annotate("",xy=(q,-1.47),xytext=(q,-.53),arrowprops={"arrowstyle":"-|>","color":"#288969","lw":2})
ax.text(.51,-.27,"Optical pumping dissipates the gained energy",ha="center",color="#186b4e",fontsize=11)
ax.set(xlabel=r"Position $z/\lambda$",ylabel=r"Light-shift energy / $U_0$",ylim=(-1.7,-.1),title="Motion climbs each occupied potential branch")
ax.legend(loc="lower right");ax.grid(alpha=.15)
fig.savefig("paper-1-sisyphus-cycle.png",dpi=150,facecolor="white")
