"""Original dimensionless one-family seesaw. Python3.14 NumPy Matplotlib."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
r=np.geomspace(.01,1e6,1000)
heavy=(r+np.sqrt(r*r+4))/2
light=2/(r+np.sqrt(r*r+4))
fig,ax=plt.subplots(figsize=(8,4.5),layout="constrained")
ax.loglog(r,heavy,lw=2,color="#274e82",label="Exact heavy physical mass")
ax.loglog(r,light,lw=2,color="#bc5429",label="Exact light physical mass")
ax.loglog(r[r>3],r[r>3],":",color=".3",label=r"Asymptotes: $M_R$ and $m_D^2/M_R$")
ax.loglog(r[r>3],1/r[r>3],":",color=".3")
ax.set(xlabel=r"$M_R/m_D$",ylabel=r"Physical mass / $m_D$",title=r"Type-I seesaw: $M_L=0$, fixed but unspecified Dirac mass")
ax.text(.04,.06,r"Exact product: $m_{\rm light}m_{\rm heavy}=m_D^2$",transform=ax.transAxes,fontsize=11)
ax.legend(fontsize=10);ax.grid(which="major",alpha=.2)
fig.savefig("paper-1-seesaw-scales.png",dpi=150,facecolor="white")
