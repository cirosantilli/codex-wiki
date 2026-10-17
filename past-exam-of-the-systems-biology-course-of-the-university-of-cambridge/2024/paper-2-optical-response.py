"""Original Gaussian PSF examples, not a fit or copy of an exam image.

Python 3.14, NumPy 2.3.5, matplotlib 3.10.7. Write the output basename
paper-2-optical-response.png in the current working directory.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def gaussian(x, sigma):
    return np.exp(-x*x/(2*sigma*sigma))


def main():
    plt.rcParams.update({'font.size':10,'figure.facecolor':'white'})
    x=np.linspace(-4,4,1601)
    illumination=gaussian(x,1)
    confocal=illumination*gaussian(x,1.1)
    two_photon=gaussian(x,1.8)**2
    fig,axes=plt.subplots(1,2,figsize=(10,3.8),constrained_layout=True)
    axes[0].plot(x,illumination,color='#6b6b6b',ls='--',label=r'Linear generation: $I(x)$')
    axes[0].plot(x,illumination**2,color='#176b9c',label=r'Quadratic generation: $I(x)^2$')
    axes[0].axhline(.5,color='gray',alpha=.35,lw=1)
    axes[0].set(title='Squaring the same illumination narrows it')
    axes[1].plot(x,confocal,color='#176b9c',label=r'Confocal: $h_{ex}h_{det}$')
    axes[1].plot(x,two_photon,color='#c05526',label=r'Two-photon: $h_{ex,2p}^{\,2}$')
    axes[1].set(title='Longer-wavelength excitation starts broader')
    axes[1].text(.03,.97,r'Toy widths: $\sigma_{ex}=1,\ \sigma_{det}=1.1$'+'\n'+r'$\sigma_{ex,2p}=1.8$',transform=axes[1].transAxes,ha='left',va='top',fontsize=9,bbox={'facecolor':'white','alpha':.9,'edgecolor':'none'})
    for ax in axes:
        ax.set(xlabel='Lateral position (arbitrary units)',ylabel='Response / own peak',ylim=(0,1.04))
        ax.legend(loc='lower center',fontsize=9)
        ax.grid(alpha=.15)
    fig.savefig(Path('paper-2-optical-response.png'),dpi=125,facecolor='white')
    plt.close(fig)


if __name__=='__main__':
    main()
