"""Original solution illustration. Tested with Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Run from the desired output directory; this script writes only its PNG basename there.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                     "axes.spines.right": False, "figure.facecolor": "white",
                     "axes.facecolor": "white", "savefig.facecolor": "white"})

R=np.array([7.8,7.8,78.]);r,s=.4,.04
J=np.array([[-r/R[0],r/R[0],0],[r/R[1],-(r+s)/R[1],s/R[1]],[0,s/R[2],-s/R[2]]])
S=np.diag(np.sqrt(R))@J@np.diag(1/np.sqrt(R))
lam,Q=np.linalg.eigh(S);lam[abs(lam)<1e-12]=0;weights=Q[0]**2/R[0]
t=np.linspace(0,400,4001)
def response(q,rate=False):
 q=np.maximum(q,0);out=np.zeros_like(q)
 for w,l in zip(weights,lam):
  if l==0:term=q if rate else q*q/2
  else:term=np.expm1(l*q)/l if rate else (np.expm1(l*q)-l*q)/(l*l)
  out+=w*term
 return out
C=.5*(response(t)-2*response(t-100)+response(t-200))
rate=.5*(response(t,True)-2*response(t-100,True)+response(t-200,True))
E=.5*(t-2*np.maximum(t-100,0)+np.maximum(t-200,0))
fig,(ax,bx)=plt.subplots(2,1,figsize=(8,6.1),sharex=True,layout="constrained",height_ratios=[1.5,1])
ax.plot(t,C,lw=2.5,color="#326f9e",label=r"Atmospheric anomaly $C_a$")
ax.axhline(5000/sum(R),color="0.45",ls=":",label="Infinite-time anomaly: 53.4 ppmv")
for year in [200,400]:
 val=np.interp(year,t,C);ax.scatter([year],[val],color="#326f9e",zorder=4)
 ax.annotate(f"Year {year}: {val:.1f} ppmv",(year,val),xytext=((250,300) if year==200 else (year-105,val+32)),arrowprops={"arrowstyle":"->"},fontsize=10)
i=C.argmax();ax.annotate(f"Peak: {C[i]:.1f} ppmv\nat year {t[i]:.0f}",(t[i],C[i]),xytext=(35,293),arrowprops={"arrowstyle":"->"},fontsize=10)
ax.set(ylabel="Concentration anomaly (ppmv)",ylim=(0,340),title="Atmospheric response to a finite emissions pulse")
ax.legend(loc="lower right",frameon=False,fontsize=9)
bx.plot(t,E,color="0.5",ls="--",label="Emissions")
bx.set(ylabel=r"Emissions (GtCO$_2$/yr)",xlabel="Years since emissions begin",xlim=(0,400),ylim=(-21,58))
cx=bx.twinx();cx.spines["right"].set_visible(True)
cx.plot(t,rate,color="#bc4d27",lw=2,label=r"Rate $dC_a/dt$")
cx.axhline(0,color="#bc4d27",lw=.6,alpha=.4)
cx.set(ylabel="Concentration rate (ppmv/yr)",ylim=(-1.5,4.15))
cx.annotate("Maximum rise: 3.27 ppmv/yr",(100,np.interp(100,t,rate)),xytext=(145,3.5),arrowprops={"arrowstyle":"->"},fontsize=9,color="#9a3e20")
bx.legend(loc="upper left",frameon=False,fontsize=9);cx.legend(loc="lower right",frameon=False,fontsize=9)
for axis in (ax,bx):axis.grid(alpha=.15)

fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
            dpi=120, facecolor="white", transparent=False,
            metadata={"Software": "Matplotlib"})
plt.close(fig)
