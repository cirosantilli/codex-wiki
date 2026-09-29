"""Original exam-solution figure; Python 3.14.4, numpy 2.3.5, matplotlib 3.10.7.
Writes an opaque PNG with the same basename to the current working directory.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
fig,ax=plt.subplots(1,2,figsize=(9,3.9),dpi=100,facecolor="white")
a=np.linspace(0,5,1000)
ax[0].fill_between(a,0,a,where=a>1,color="#dce8f2",label="Stable homogeneous state")
ax[0].plot(a,a,color="#333333");ax[0].axvline(1,color="#555555",ls="--")
ax[0].text(2.3,1.25,"a > 1, 0 < b < a",fontsize=10)
ax[0].set(title="Homogeneous stability",xlim=(0,5),ylim=(0,5),xlabel="a",ylabel="b")
d=4.;b=4*d*a*a/(d+a)**2
ax[1].fill_between(a,0,a,where=a>1,color="#dce8f2",label="Homogeneous stability")
ax[1].fill_between(a,b,a,where=(a>1)&(a<d),color="#d2915f",alpha=.85,label="Turing instability")
ax[1].plot(a,a,color="#333333",label="b = a")
ax[1].plot(a,b,color="#964b22",label="b = 4da²/(d+a)²")
ax[1].axvline(1,color="#555555",ls="--");ax[1].axvline(d,color="#555555",ls=":")
ax[1].set(title="Diffusion threshold (d = 4)",xlim=(0,5),ylim=(0,5),xlabel="a",ylabel="b")
ax[1].legend(fontsize=8,loc="upper left")
for p in ax:p.grid(alpha=.12)
fig.subplots_adjust(left=.06,right=.985,top=.89,bottom=.16,wspace=.25)

fig.savefig(Path.cwd()/(Path(__file__).stem+".png"),facecolor="white",transparent=False)
plt.close(fig)
