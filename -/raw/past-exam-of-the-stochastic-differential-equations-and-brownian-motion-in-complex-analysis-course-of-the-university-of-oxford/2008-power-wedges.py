"""Original power-map domains. Python3.14, NumPy, Matplotlib. Output CWD."""
import matplotlib
matplotlib.use("Agg")
import numpy as np
import matplotlib.pyplot as plt
fig,axes=plt.subplots(2,3,figsize=(9,6),facecolor="white")
for ax,a in zip(axes.flat,[0,.25,.5,1,1.5,2]):
 ax.axhline(0,color=".8",lw=.7);ax.axvline(0,color=".8",lw=.7)
 if a:
  th=np.linspace(0,a*np.pi,300);r=1.7
  ax.fill(np.r_[0,r*np.cos(th),0],np.r_[0,r*np.sin(th),0],color="#d8eef7")
  ax.plot([0,r],[0,0],color=".3",lw=2)
  ax.plot([0,r*np.cos(a*np.pi)],[0,r*np.sin(a*np.pi)],color=".3",lw=2)
  z=np.exp(1j*a*np.pi/2);ax.scatter([z.real],[z.imag],color="#b2182b",s=30,zorder=4)
  ax.text(z.real+.09,z.imag+.08,r"$i^\alpha$",fontsize=10)
 else:
  ax.scatter([1],[0],s=40,color="#b2182b",zorder=4)
  ax.text(-1.5,.7,"constant map:\nimage is {1}",fontsize=11)
 ax.set(xlim=(-1.8,1.8),ylim=(-1.8,1.8),aspect="equal",xticks=[],yticks=[],
        title=r"$\alpha="+str(a)+"$")
 ax.spines[["top","right","bottom","left"]].set_visible(False)
fig.suptitle(r"Images of the upper half-plane under $z^\alpha$",fontsize=14)
fig.tight_layout()
fig.savefig("2008-power-wedges.png",dpi=150,facecolor="white")
