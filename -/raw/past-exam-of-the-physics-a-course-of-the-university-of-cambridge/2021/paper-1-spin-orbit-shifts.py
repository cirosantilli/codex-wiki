"""Original dimensionless spin-orbit shifts; Python 3.14/numpy 2.3.5/matplotlib 3.10.7.

Run from mirrored _media directory. E_*=hbar^2*omega_*^2/(4*m*c^2).
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    w=np.linspace(0,1.2,401)
    fig,ax=plt.subplots(figsize=(6.5,4.1),layout='constrained')
    ax.plot(w,w*w,color='#236bc0',lw=2.3,label=r'$l=1,\ j=3/2$ (four states)')
    ax.plot(w,np.zeros_like(w),color='#177c65',ls='--',lw=2,label=r'$l=0,\ j=1/2$ (two states)')
    ax.plot(w,-2*w*w,color='#c26712',lw=2.3,label=r'$l=1,\ j=1/2$ (two states)')
    ax.set(xlim=(0,1.2),ylim=(-3.1,1.7),xlabel=r'$\omega/\omega_*$',ylabel=r'$\Delta E/E_*$',title='Spin-orbit corrections in an isotropic harmonic trap')
    ax.grid(alpha=.18)
    ax.legend(loc='lower left',fontsize=9)
    fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white')
    plt.close(fig)


if __name__=='__main__':main()
