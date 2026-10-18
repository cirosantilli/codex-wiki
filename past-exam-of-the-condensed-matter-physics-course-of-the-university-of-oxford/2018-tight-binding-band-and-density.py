"""Original tight-binding plots; Python 3.14, NumPy and Matplotlib."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size':12,'axes.spines.top':False,'axes.spines.right':False})
fig,(band,dos)=plt.subplots(1,2,figsize=(10,4.4),layout='constrained',facecolor='white')
x=np.linspace(-1,1,1001);e=-2*np.cos(np.pi*x)
band.plot(x,e,color='#246ba0',lw=2)
band.fill_between(x,-2,e,where=abs(x)<=.5,color='#dae9ef')
band.axhline(0,color='#8f5037',ls='--',label=r'$E_F=\epsilon_0$ (half filling)')
band.scatter([-1,0,1],[2,-2,2],color='#246ba0',s=25)
band.set(xlabel=r'Wavevector $ka/\pi$',ylabel=r'Energy $(E-\epsilon_0)/t$',xticks=[-1,-.5,0,.5,1],yticks=[-2,0,2],xlim=(-1.06,1.06),ylim=(-2.3,2.5),title='One orbital per site; positive hopping')
band.text(0,-1.5,'Occupied at half filling',ha='center',fontsize=10)
band.legend(loc='upper center',fontsize=10)
band.grid(alpha=.2)
egrid=np.linspace(-1.999,1.999,1501);g=2/(np.pi*np.sqrt(4-egrid**2))
dos.plot(egrid,g,color='#277b4a',lw=2)
dos.fill_between(egrid,0,g,where=egrid<=0,color='#deeee1')
for edge in [-2,2]:dos.axvline(edge,color='#777777',ls=':')
dos.set(xlabel=r'Energy $(E-\epsilon_0)/t$',ylabel=r'DOS per atom $t\,g(E)$ (both spins)',xlim=(-2.35,2.35),ylim=(0,2.1),xticks=[-2,0,2],title='Integrable singularities at both edges')
dos.annotate('Diverges',xy=(-1.99,1.9),xytext=(-1.2,1.55),arrowprops={'arrowstyle':'->'},ha='center',fontsize=10)
dos.annotate('Diverges',xy=(1.99,1.9),xytext=(1.2,1.55),arrowprops={'arrowstyle':'->'},ha='center',fontsize=10)
dos.text(0,.8,'Total: two states per atom',ha='center',fontsize=10)
dos.grid(alpha=.2)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white',transparent=False)
