"""Original pointwise logarithmic-integrand comparison; output to cwd."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(1,np.e,900);log=np.log(x)
fig,ax=plt.subplots(figsize=(6.8,4.0),layout="constrained")
for y,label,color in [(log**2,r"$(\ln x)^2$; area $e-2$","#568e40"),(log,r"$\ln x$; area 1","#2874a3"),(2*log,r"$\ln(x^2)=2\ln x$; area 2","#b75a2a")]:
    ax.plot(x,y,color=color,lw=2,label=label)
ax.set(xlim=(1,np.e),ylim=(0,2.05),xlabel="x",ylabel="Integrand",title="On 1 < x < e, squaring lowers ln x and doubling raises it")
ax.set_xticks([1,1.5,2,np.e],labels=["1","1.5","2","e"])
ax.grid(alpha=.18);ax.legend(loc="upper left",fontsize=10)
fig.savefig(Path(__file__).with_suffix(".png").name,dpi=120,facecolor="white")
plt.close(fig)
