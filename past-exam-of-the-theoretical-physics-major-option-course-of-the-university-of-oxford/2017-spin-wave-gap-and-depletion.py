"""Original spectra and field-regulated zero-point spin depletion; Python 3.14."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size':12,'figure.facecolor':'white','axes.facecolor':'white'})
fig,axs=plt.subplots(1,2,figsize=(11.5,4.8),layout='constrained')
k=np.linspace(-np.pi,np.pi,1201)
for ratio,color in [(0.,'#767676'),(.1,'#2577ae'),(1.,'#b95b2e')]:
    omega=np.sqrt((ratio+2)*(ratio+4*np.sin(k/2)**2))
    axs[0].plot(k/np.pi,omega,label=rf'$|h|/J={ratio:g}$',lw=2.2,color=color,ls='--' if ratio==0 else '-')
axs[0].set(xlim=(-1,1),ylim=(0,3.98),xlabel=r'$k/\pi$',ylabel=r'$\epsilon(k)/(JS)$',title='A field opens a gap in the planar chain')
axs[0].legend(frameon=False)
axs[0].grid(alpha=.2)
# k=pi*t^2 resolves the integrable, field-regulated peak near zero momentum.
t=np.linspace(0,1,20001)
positive_k=np.pi*t*t
ratios=np.logspace(-6,1,201)
deltas=[]
for ratio in ratios:
    alpha=ratio+2-np.cos(positive_k)
    omega=np.sqrt((ratio+2)*(ratio+4*np.sin(positive_k/2)**2))
    # Stable alternative to subtracting two nearly equal values at large fields.
    delta=np.cos(positive_k)**2/(2*omega*(alpha+omega))
    deltas.append(np.trapezoid(delta*(2*np.pi*t),t)/np.pi)
axs[1].semilogx(ratios,deltas,lw=2.4,color='#2577ae')
axs[1].set(xlim=(1e-6,10),ylim=(0,None),xlabel=r'$|h|/J$',ylabel=r'$\delta S$ per site',title='Zero-point depletion grows as the field closes')
axs[1].grid(alpha=.2,which='both')
axs[1].text(.38,.92,r'$\langle S^x\rangle=\mathrm{sgn}(h)(S-\delta S)$'+'\n'+r'Validity requires $\delta S\ll S$',transform=axs[1].transAxes,va='top',fontsize=11)
fig.suptitle('Linear spin waves: thermodynamic-limit spectrum and depletion\nThe exact uniform mode at zero field requires separate collective-coordinate treatment',fontsize=13)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=110,facecolor='white',transparent=False)
