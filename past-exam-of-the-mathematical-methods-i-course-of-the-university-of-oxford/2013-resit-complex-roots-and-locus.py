"""Original complex-plane root and argument-locus diagrams, not exam artwork."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(11, 5), layout='constrained', facecolor='white')
for ax in axes:
    ax.axhline(0, color='.65', lw=.8)
    ax.axvline(0, color='.65', lw=.8)
    ax.set(aspect='equal', xlabel='Real part', ylabel='Imaginary part')
t = np.linspace(0, 2*np.pi, 400)
axes[0].plot(3*np.cos(t), 3*np.sin(t), '--', color='.65')
z = 3*np.exp(1j*(np.pi/6+2*np.pi*np.arange(3)/3))
axes[0].scatter(z.real, z.imag, color='#176b87', s=45, zorder=4)
for value, label, offset in zip(z, ['3√3/2 + 3i/2', '−3√3/2 + 3i/2', '−3i'], [(0,12),(0,12),(15,0)]):
    axes[0].annotate(label, xy=(value.real,value.imag), xytext=offset, textcoords='offset points', ha='center', fontsize=11)
axes[0].set(xlim=(-3.8,3.8), ylim=(-3.7,3.6), title='Cube roots of 27i: three equally spaced points')
x = np.linspace(.001,3,400)
axes[1].plot(x,np.sqrt(1+x*x),color='#176b87',lw=2.5)
axes[1].plot(-x,-np.sqrt(1+x*x),color='#176b87',lw=2.5)
axes[1].plot(-x,np.sqrt(1+x*x),'--',color='.8',lw=1)
axes[1].plot(x,-np.sqrt(1+x*x),'--',color='.8',lw=1)
axes[1].scatter([0,0],[1,-1],facecolors='white',edgecolors='#c05229',s=65,zorder=5)
axes[1].text(-2.9,2.9,'Dashed halves excluded',fontsize=10)
axes[1].text(.2,-.5,'Open vertices:\nargument undefined',fontsize=10)
axes[1].set(xlim=(-3.4,3.4),ylim=(-3.6,3.6),title=r'$\arg(z^2+1)=\pi/2$: $y^2-x^2=1$, $xy>0$')
fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name, dpi=120, facecolor='white', metadata={'Software':'matplotlib'})
