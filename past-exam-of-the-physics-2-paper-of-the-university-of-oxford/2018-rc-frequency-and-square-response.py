"""Original solution illustration; output the matching PNG into the cwd."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import patches
plt.rcParams.update({"font.size":12,"figure.facecolor":"white"})

fig=plt.figure(figsize=(10.5,9.3),layout="constrained")
grid=fig.add_gridspec(4,2)
w=np.logspace(-2,2,600)
ax=fig.add_subplot(grid[0,0]);ax.semilogx(w,1/np.sqrt(1+w*w),lw=2,color="#286d88")
ax.scatter([1],[1/np.sqrt(2)],s=20,color="#a3304c")
ax.set(xlabel=r"$\omega RC$",ylabel="Amplitude ratio",title="Low-pass frequency response",ylim=(0,1.1));ax.grid(alpha=.2)
ax=fig.add_subplot(grid[0,1]);ax.semilogx(w,-np.arctan(w)*180/np.pi,lw=2,color="#286d88")
ax.set(xlabel=r"$\omega RC$",ylabel="Phase (degrees)",yticks=[-90,-45,0],ylim=(-95,5));ax.grid(alpha=.2)
phase=np.linspace(0,3,1801)
for row,value in enumerate([.1,10,1],1):
    T=2*np.pi/value;t=phase*T;local=t%T;M=np.tanh(T/4)
    vi=np.where(local<T/2,1.,-1.)
    vo=np.where(local<T/2,1-(1+M)*np.exp(-local),-1+(1+M)*np.exp(-(local-T/2)))
    ax=fig.add_subplot(grid[row,:]);ax.plot(phase,vi,color="#999999",lw=1.1,drawstyle="steps-post",label="Input")
    ax.plot(phase,vo,color="#286d88",lw=2.2,label="Output")
    ax.set(xlim=(0,3),ylim=(-1.18,1.18),ylabel=r"$V/V_0$",title=rf"$\omega RC={value:g}$; output extrema $\pm{M:.3f}V_0$")
    ax.grid(alpha=.15)
    if row==1:ax.legend(loc="upper right",ncol=2,fontsize=10)
    if row==3:ax.set_xlabel("Time / input period")

fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=120,facecolor="white")
