"""Original finite pulses and echoes; no exam figure is traced. Python 3.14, NumPy, Matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'figure.facecolor':'white','savefig.facecolor':'white'})
fig,axs=plt.subplots(3,1,figsize=(10,7),layout='constrained');x=np.linspace(-3.2,2.2,4001);w=.4
# Compact smooth profile: quoted width is its full support.
def pulse(center,width,amplitude):
 u=(x-center)/width;return amplitude*np.where(np.abs(u)<=.5,np.cos(np.pi*u)**2,0)
for ax,time,title in zip(axs,[.025,.065,.125],['After the first junction encounter','After reflection from the fixed wall','After return to the junction']):
 heavy=pulse(-20*time,w,1/3)
 if time<.05:light=pulse(40*time,2*w,4/3)
 elif time<.1:light=pulse(2-40*(time-.05),2*w,-4/3)
 else:
  light=pulse(40*(time-.1),2*w,4/9);heavy+=pulse(-20*(time-.1),w,-8/9)
 ax.plot(x,np.where(x<=0,heavy,np.nan),lw=2,label='heavy string, speed 20 m/s');ax.plot(x,np.where((x>=0)&(x<=2),light,np.nan),lw=2,label='light string, speed 40 m/s');ax.axvline(0,color='.4',ls='--',lw=1);ax.axvspan(2,2.2,color='.7',alpha=.4);ax.axhline(0,color='.75',lw=.8)
 ax.set(xlim=(-3.2,2.2),ylim=(-1.6,1.6),ylabel=r'$y/A_i$',title=f'{title}: t = {time:g} s');ax.legend(fontsize=8,loc='lower left',ncol=2)
axs[-1].set_xlabel('distance from the junction / metres');fig.suptitle('Incident heavy-string pulse: amplitude 1 and width 0.4 m',fontsize=12)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white',transparent=False);plt.close(fig)
