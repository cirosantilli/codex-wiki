"""Python3.14, numpy2.3, matplotlib3.10; write one PNG in the working directory."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
fig,axs=plt.subplots(1,2,figsize=(8.6,3.7),layout='constrained',facecolor='white')
t=np.linspace(.001,np.pi-.001,600)
paths=[.0+1j*np.geomspace(.0001,10000,800),-1.1+1.1*np.exp(1j*t),.7+1.8*np.exp(1j*t)]
colors=['#1665ad','#cb601a','#288444']
for z,c in zip(paths,colors):
 axs[0].plot(z.real,z.imag,color=c,lw=2)
 w=(z-1j)/(z+1j)
 axs[1].plot(w.real,w.imag,color=c,lw=2)
axs[0].axhline(0,color='black',lw=1)
axs[0].set(xlim=(-2.5,2.7),ylim=(-.08,3.2),xlabel='x',ylabel='y',title='Upper half-plane')
phi=np.linspace(0,2*np.pi,600)
axs[1].plot(np.cos(phi),np.sin(phi),color='black',lw=1)
axs[1].set(xlim=(-1.1,1.1),ylim=(-1.1,1.1),xlabel='Re w',ylabel='Im w',title='Disc: w = (z − i)/(z + i)')
for ax in axs:
 ax.set_aspect('equal');ax.set_facecolor('white');ax.spines[['top','right']].set_visible(False)
fig.savefig(Path(__file__).with_suffix('.png').name,dpi=145,facecolor='white')
