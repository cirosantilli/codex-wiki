"""Plot the cutoff-identification potential; Python 3.14, numpy, matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size':12,'axes.spines.top':False,'axes.spines.right':False})
x=np.linspace(-3,3,801)
r=np.abs(x)
v=(r*np.sqrt(1+r*r)*(2*r*r+1)-np.arcsinh(r))/2
fig,axs=plt.subplots(1,2,figsize=(10,4.2),layout='constrained',facecolor='white')
axs[0].plot(x,v,color='#126782',lw=2.5,label='Exact potential')
axs[0].plot(x,x**4,color='#ab5425',ls='--',lw=1.8,label='Large-field quartic')
axs[0].set(xlabel=r'$\varphi/m$',ylabel=r'$16\pi^2 V/m^4$',title='Even potential; unique minimum at zero')
axs[0].legend(loc='upper center',fontsize=10)
z=np.linspace(-.5,.5,501);r=np.abs(z)
w=(r*np.sqrt(1+r*r)*(2*r*r+1)-np.arcsinh(r))/2
axs[1].plot(z,w,color='#126782',lw=2.5,label='Exact potential')
axs[1].plot(z,4*np.abs(z)**3/3,color='#7b4490',ls='--',lw=1.8,label=r'Small-field $4|\varphi/m|^3/3$')
axs[1].set(xlabel=r'$\varphi/m$',ylabel=r'$16\pi^2 V/m^4$',title='Massive case: cubic behavior near zero')
axs[1].legend(loc='upper center',fontsize=10)
for ax in axs:
 ax.set_facecolor('white');ax.grid(alpha=.18);ax.axhline(0,color='black',lw=.6)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white',transparent=False,metadata={'Software':'Matplotlib'})
plt.close(fig)
