"""Original invariant-mass domains computed from the supplied meson masses."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size':12,'figure.facecolor':'white','axes.facecolor':'white'})
fig,axes=plt.subplots(1,2,figsize=(11.8,5.4),layout='constrained')
m=.139
for ax,M,label,color in zip(axes,[1.870,.494],[r'$D^+\to\pi^+\pi^+\pi^-$',r'$K^+\to\pi^+\pi^+\pi^-$'],['#d4e6f2','#f3dfd1']):
    s=np.linspace(4*m*m,(M-m)**2,12001)
    centre=2*m*m+(M*M-m*m-s)/2
    width=np.sqrt(np.maximum(((M*M-m*m-s)**2-4*m*m*s)*(s*s-4*s*m*m),0))/(2*s)
    lo,hi=centre-width,centre+width
    ax.fill_between(s,lo,hi,color=color)
    ax.plot(s,lo,color='#2a4c66',lw=1.7);ax.plot(s,hi,color='#2a4c66',lw=1.7)
    span=s[-1]-s[0];pad=.035*span
    ax.set(xlim=(s[0]-pad,s[-1]+pad),ylim=(s[0]-pad,s[-1]+pad),xlabel=r'$s_{13}=m^2(\pi_1^+\pi^-)$ [GeV$^2$]',ylabel=r'$s_{23}=m^2(\pi_2^+\pi^-)$ [GeV$^2$]',aspect='equal')
    area=np.trapezoid(hi-lo,s)
    ax.set_title(label+'\n'+rf'Area $={area:.4g}$ GeV$^4$',fontsize=13)
    ax.grid(alpha=.18)
    if M>1:
        for mass,c,ls,name in [(.775,'#2876a4','--',r'$\rho^0$'),(.980,'#a75c28',':',r'$f_0(980)$')]:
            ax.axvline(mass**2,color=c,ls=ls,lw=1.6,label=name)
            ax.axhline(mass**2,color=c,ls=ls,lw=1.6)
        ax.legend(loc='upper right',framealpha=.95,fontsize=11)
    else:
        ax.text(.5,.50,r'$m(\pi^+\pi^-)\leq0.355$ GeV'+'\n'+r'No on-shell $\rho^0$ band',transform=ax.transAxes,ha='center',va='center',fontsize=11)
fig.suptitle('Calculated kinematic domains: different axis scales\nThe charm Dalitz area is about 3150 times larger; dashed lines mark possible bands, not intensities',fontsize=13)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=110,facecolor='white',transparent=False)
