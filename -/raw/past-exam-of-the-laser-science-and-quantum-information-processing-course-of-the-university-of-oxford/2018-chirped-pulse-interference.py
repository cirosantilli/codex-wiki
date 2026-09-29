"""Original temporal interferometer profiles; Python 3.14, NumPy/Matplotlib."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size':12,'axes.spines.top':False,'axes.spines.right':False})
a=2*np.log(2);b=300.;omega=2000*np.pi
field=lambda t:np.exp(-a*t*t)*np.exp(-1j*(omega*t+b*t*t))
fig,axes=plt.subplots(1,2,figsize=(10,4.3),layout='constrained',facecolor='white')
t=np.linspace(-1.3,1.3,16001);d=.05
exact=abs((field(t)+field(t-d))/2)**2
approx=np.exp(-2*a*t*t)*np.cos(b*d*(t-d/2)+omega*d/2)**2
axes[0].plot(t,exact,color='#222222',lw=1.8,label='Exact delayed fields')
axes[0].plot(t,approx,'--',color='#3179b7',lw=1.1,label='Small-delay approximation')
axes[0].set(xlabel=r'Time $t/\tau$',ylabel=r'Output intensity $I/I_0$',title=r'Overlapping chirped pulses: $d=0.05\tau$',xlim=(-1.3,1.3),ylim=(0,1.08))
axes[0].legend(fontsize=9)
t=np.linspace(-1.3,4.1,20001);d=2.8
axes[1].plot(t,abs((field(t)+field(t-d))/2)**2,color='#9e4538',lw=2)
axes[1].axhline(.25,color='#777777',ls=':',lw=1)
axes[1].set(xlabel=r'Time $t/\tau$',ylabel=r'Output intensity $I/I_0$',title=r'Widely separated replicas: $d=2.8\tau$',xlim=(-1.3,4.1),ylim=(0,.32))
axes[1].text(1.4,.27,'Each replica has one quarter\nof the input pulse energy',ha='center',fontsize=10)
for ax in axes:ax.grid(alpha=.18)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white',transparent=False)
