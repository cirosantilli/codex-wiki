"""Original local bond-potential comparison; Python 3.14, NumPy/Matplotlib."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size':12,'axes.spines.top':False,'axes.spines.right':False})
fig,ax=plt.subplots(figsize=(7.3,4.5),layout='constrained',facecolor='white')
x=np.linspace(-.7,1.2,1001)
ax.plot(x,np.expm1(-x)**2,color='#222222',lw=2,label='Exact Morse bond')
ax.plot(x,x*x,'--',color='#2a70a5',label='Harmonic approximation')
local=np.linspace(-.45,.45,501)
ax.plot(local,local**2-local**3,':',color='#b34631',lw=2,label='Through cubic order (local)')
energy=.1
left=-np.log(1+np.sqrt(energy));right=-np.log(1-np.sqrt(energy))
ax.plot([left,right],[energy,energy],color='#488452',lw=2)
ax.scatter([left,right],[energy,energy],color='#488452',s=25)
ax.annotate('Stretching reaches farther',xy=(right,energy),xytext=(.45,.27),arrowprops={'arrowstyle':'->'},fontsize=11)
ax.axvline(0,color='#888888',lw=.7)
ax.set(xlabel=r'Bond displacement $(r-a)/\xi$',ylabel=r'Energy above minimum $(V+D)/D$',xlim=(-.65,1.15),ylim=(0,1.05),title='Anharmonic asymmetry produces positive expansion')
ax.legend(loc='upper right',fontsize=10)
ax.grid(alpha=.2)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white',transparent=False)
