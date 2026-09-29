"""Original comparison of cooled and insulated triangular-temperature diffusion."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,1,700)
fig,axes=plt.subplots(1,2,figsize=(9,4.2),layout="constrained",sharey=True)
times=[0,.005,.03,.15]
colors=["#333333","#b6712b","#267ca5","#648b42"]
for ax,title in zip(axes,["Cooled ends: final temperature 0","Insulated ends: final temperature 1/4"]):
    ax.plot(x,np.minimum(x,1-x),color=colors[0],lw=1.8,label="Initial profile")
    ax.set(title=title,xlabel="Position x/L",xlim=(0,1),ylim=(-.015,.535));ax.grid(alpha=.15)
for time,color in zip(times[1:],colors[1:]):
    n=np.arange(1,201)[:,None]
    cooled=4/np.pi**2*np.sum(np.sin(n*np.pi/2)/n**2*np.sin(n*np.pi*x[None,:])*np.exp(-n**2*np.pi**2*time),axis=0)
    j=np.arange(80)[:,None];odd=2*j+1
    insulated=.25-2/np.pi**2*np.sum(np.cos(2*odd*np.pi*x[None,:])/odd**2*np.exp(-(2*odd*np.pi)**2*time),axis=0)
    for ax,values in zip(axes,[cooled,insulated]):ax.plot(x,values,color=color,lw=1.6,label=fr"$\nu t/L^2={time}$")
axes[0].set_ylabel("Temperature θ/L")
axes[1].axhline(.25,color="#666666",ls=":",lw=.9)
axes[1].legend(loc="upper right",fontsize=9)
fig.savefig(Path(__file__).with_suffix(".png").name,dpi=120,facecolor="white")
plt.close(fig)
