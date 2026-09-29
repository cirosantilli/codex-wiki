"""Original analytic teaching diagram; tested with Python 3.14, numpy, matplotlib.
Run from the intended output directory; PNG output is a basename in cwd.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
# Printed scalar-mass model. No absorption trace or source graphic is copied.
hbar=1.054571817e-34;m0=9.11e-31;ev=1.602176634e-19;L=120e-10
A=np.pi**2*hbar**2/(2*m0*L**2*ev)
fig,axs=plt.subplots(1,2,figsize=(11,4.3),layout="constrained")
colors={"hh":"#286b93","lh":"#b35c25","so":"#7c53a0"}
for y,(label,mh,gap) in enumerate([("hh",.53,1.52),("lh",.08,1.52),("so",.15,1.86)]):
 for n in range(1,5):
  edge=gap+A*n*n*(1/.067+1/mh)
  if edge<=2.2:
   axs[0].plot([edge,edge],[y-.17,y+.17],color=colors[label],lw=2)
   axs[0].text(edge,y+.23,f"n={n}\n{edge:.4f}",ha="center",va="bottom",fontsize=9,color=colors[label])
axs[0].set(xlim=(1.51,2.2),ylim=(-.4,2.7),yticks=[0,1,2],yticklabels=["heavy hole","light hole","split off"],xlabel="Calculated photon continuum edge / eV",title="Same-index infinite-well thresholds")
axs[0].grid(axis="x",alpha=.2)
x=np.arange(2);width=.27
R=np.array([13.6*(.067*mh/(.067+mh))/12.8**2 for mh in [.53,.08]])*1000
axs[1].bar(x-width/2,32*R/9,width,label="2D prediction",color="#286b93")
axs[1].bar(x+width/2,.75*R,width,label="3D prediction",color="#bbbbbb")
for j,(low,high) in enumerate([(17,18),(10,11)]):
 axs[1].plot([j-.35,j+.35],[low,low],color="#b35c25",ls="--",lw=1)
 axs[1].plot([j-.35,j+.35],[high,high],color="#b35c25",ls="--",lw=1)
axs[1].plot([],[],color="#b35c25",ls="--",label="Range of listed spacings")
axs[1].set(xticks=x,xticklabels=["heavy hole","light hole"],ylabel="First-to-second peak separation / meV",title="Peak spacing tests dimensionality",ylim=(0,22))
axs[1].legend(fontsize=9);axs[1].grid(axis="y",alpha=.2)
fig.suptitle("Original calculations from the stated well width, masses and permittivity")
fig.savefig("paper-1-interband-thresholds.png",dpi=155,facecolor="white")
