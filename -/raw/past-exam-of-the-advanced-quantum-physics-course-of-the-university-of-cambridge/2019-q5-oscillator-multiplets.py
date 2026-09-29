"""Original total-spin-orbit multiplets; Python 3.14/numpy 2.3.5/matplotlib 3.10.7.

Run from mirrored _media directory. Energies are shifts from 4*hbar*omega_0.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    coupling=np.linspace(-.15,.15,401)
    fig,ax=plt.subplots(figsize=(7,4.4),layout='constrained')
    for slope,label,color,style in [(-2,r'$^3P_0$: 1 state','#c26712','-'),(-1,r'$^3P_1$: 3 states','#9244a0','-'),(0,r'$^1P_1$: 3 states','#177c65','--'),(1,r'$^3P_2$: 5 states','#236bc0','-')]:
        ax.plot(coupling,slope*coupling,color=color,ls=style,lw=2,label=label)
    ax.axvline(0,color='0.7',lw=.8,zorder=0)
    ax.set(xlim=(-.15,.15),ylim=(-.34,.34),xlabel=r'$\lambda\hbar^2/(\hbar\omega_0)$',ylabel=r'$(E-4\hbar\omega_0)/(\hbar\omega_0)$',title=r'Twelve first-excited states under $\lambda\,\mathbf{S}\cdot\mathbf{L}$')
    ax.grid(alpha=.17)
    ax.legend(loc='upper center',ncol=2,fontsize=9)
    fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white')
    plt.close(fig)


if __name__=='__main__':main()
