"""Original explanatory diagram; Python 3.14, numpy, matplotlib.
Outputs its basename PNG to the current working directory.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
H=1.;a1=1.;a2=1.6;ic=np.arcsin(a1/a2);leg=H*np.tan(ic);X=6.;xmin=2*leg;xc=2*H*np.sqrt((a2+a1)/(a2-a1))
fig,axs=plt.subplots(1,2,figsize=(11,4.1),layout="constrained");ax=axs[0]
ax.axhspan(0,H,color="#edf3f5");ax.axhspan(H,2.05,color="#e3e3e3");ax.axhline(0,color="k",lw=1);ax.axhline(H,color="k",lw=1)
ax.plot([0,X],[0,0],color="#286b93",lw=2,label="direct P")
ax.plot([0,X/2,X],[0,H,0],color="#b35c25",ls="--",lw=2,label="PP reflection")
ax.plot([0,leg,X-leg,X],[0,H,H,0],color="#7c53a0",lw=2,label="critical P head wave")
ax.plot([0,X],[0,0],"ko",ms=5);ax.text(0,-.1,"source",ha="left",fontsize=9);ax.text(X,-.1,"receiver",ha="right",fontsize=9)
ax.text(.12,.3,"upper layer: alpha₁",fontsize=10);ax.text(.12,1.75,"faster half-space: alpha₂",fontsize=10);ax.text(X+.08,H,"H",va="center")
ax.set(xlim=(-.1,6.6),ylim=(2.05,-.3),xlabel="Horizontal offset / H",ylabel="Depth / H",title="P-ray geometry (conversion phases discussed in text)");ax.legend(fontsize=8,loc="lower right")
ax=axs[1];xx=np.linspace(0,8,1000);direct=xx/a1;reflection=np.sqrt(xx*xx+4*H*H)/a1;head=xx/a2+2*H*np.cos(ic)/a1
ax.plot(xx,direct,label="direct",color="#286b93");ax.plot(xx,reflection,"--",label="reflection",color="#b35c25");ax.plot(xx[xx>=xmin],head[xx>=xmin],label="head",color="#7c53a0")
ax.axvline(xc,color="#777777",ls=":");ax.text(xc+.12,1.,"first-arrival\ncrossover",fontsize=9)
ax.set(xlabel="Offset / H",ylabel="Travel time / (H/alpha₁)",title="Illustrative alpha₂/alpha₁ = 1.6",ylim=(0,9));ax.grid(alpha=.2);ax.legend(fontsize=9)
fig.suptitle("Original ideal two-layer sketches; H = alpha₁ = 1 are normalization choices")
fig.savefig("paper-1-seismic-phases.png",dpi=150,facecolor="white")
