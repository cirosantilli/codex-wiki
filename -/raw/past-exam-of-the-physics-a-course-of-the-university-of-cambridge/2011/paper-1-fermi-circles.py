"""Original pedagogical figure; Python 3.14, numpy 2.3.5, matplotlib 3.10.7.
Run from the destination directory: output is the script's basename PNG in cwd.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 10, "figure.facecolor": "white", "axes.spines.top": False, "axes.spines.right": False})
fig,axs=plt.subplots(1,2,figsize=(8.5,3.8),layout="constrained")
phi=np.linspace(0,2*np.pi,1000)
for ax,z in zip(axs,[1,2]):
 r=np.sqrt(2*np.pi*z)
 ax.plot([-np.pi,np.pi,np.pi,-np.pi,-np.pi],[-np.pi,-np.pi,np.pi,np.pi,-np.pi],'k--',label="First zone")
 ax.fill(r*np.cos(phi),r*np.sin(phi),color="#c7e1f1",alpha=.65)
 ax.plot(r*np.cos(phi),r*np.sin(phi),color="#176493",lw=2,label="Fermi circle")
 ax.axhline(0,c='0.75',lw=.6);ax.axvline(0,c='0.75',lw=.6)
 ax.set(xlim=(-4.1,4.1),ylim=(-4.1,4.1),aspect='equal',xlabel=r'$k_xa$',ylabel=r'$k_ya$',title=f'{"Monovalent" if z==1 else "Divalent"}: z={z}')
 ax.set_xticks([-np.pi,0,np.pi],['−π','0','π']);ax.set_yticks([-np.pi,0,np.pi],['−π','0','π'])
 axs[0].legend(loc='upper right',fontsize=8)
fig.savefig("paper-1-fermi-circles.png", dpi=165, facecolor="white", bbox_inches="tight")
plt.close(fig)
