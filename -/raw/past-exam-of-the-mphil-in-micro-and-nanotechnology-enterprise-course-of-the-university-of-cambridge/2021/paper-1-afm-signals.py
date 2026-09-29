"""Original schematic signals; illustrative lag and friction, not measured data."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-55,210,2200); left=0.;right=150.
z=-30*np.minimum(np.clip((x-left)/(30*np.tan(np.deg2rad(25))),0,1),np.clip((right-x)/(30*np.tan(np.deg2rad(15))),0,1))
def lag(y,dx,length):
 out=np.empty_like(y);out[0]=y[0];a=1-np.exp(-dx/length)
 for j in range(1,len(y)):out[j]=out[j-1]+a*(y[j]-out[j-1])
 return out
trace=lag(z,x[1]-x[0],23);retrace=lag(z[::-1],x[1]-x[0],23)[::-1]
mu=np.where((x>14)&(x<142),2.0,0.85)
slope=1.25*np.exp(-((x-6)/6)**2)-1.25*np.exp(-((x-146)/6)**2)
fig,axs=plt.subplots(3,1,figsize=(8,7.6),sharex=True,layout='constrained')
axs[0].plot(x,z,color='#245c9f',label='accessible tip-convolved profile')
axs[0].plot([-55,0,0,150,150,210],[0,0,-30,-30,0,0],':',color='.6',label='ideal geometric surface')
axs[0].annotate('30 nm step',(85,-30),(85,-7),ha='center',arrowprops={'arrowstyle':'->'})
axs[0].set(ylabel='Height (nm)',ylim=(-36,6),title='Optimized feedback: trace and retrace coincide')
axs[0].legend(fontsize=8,loc='lower left')
axs[1].plot(x,z,':',color='.5');axs[1].plot(x,trace,label='trace →');axs[1].plot(x,retrace,label='← retrace');axs[1].legend(fontsize=9)
axs[1].set(ylabel='Height (nm)',ylim=(-36,6),title='Low gain: illustrative spatial lag of 23 nm')
axs[2].plot(x,slope+mu,label='trace');axs[2].plot(x,slope-mu,label='retrace');axs[2].plot(x,slope,':',color='.4',label='slope contribution')
axs[2].set(ylabel='Lateral signal (arb.)',xlabel='Laboratory scan position (nm)',title='Optimized load control: wider friction loop on perovskite')
axs[2].legend(fontsize=8,ncol=3,loc='lower center')
for ax in axs:ax.grid(alpha=.18);ax.axvspan(14,142,color='#f7e4bd',alpha=.24)
fig.savefig(Path(__file__).with_suffix('.png').name,dpi=140,facecolor='white');plt.close(fig)
