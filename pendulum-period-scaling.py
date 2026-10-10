"""Generate pendulum-period-scaling.png in cwd.

Tested with Python 3.14.4, numpy 2.3.5, matplotlib 3.10.7.
Small-angle periods are analytic. Finite-amplitude periods use Gaussian
quadrature of the exact ideal-pendulum elliptic integral, not simulated data.
"""

from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def period_ratio(theta):
    nodes,weights=np.polynomial.legendre.leggauss(256)
    phi=(nodes+1)*np.pi/4
    k=np.sin(np.asarray(theta)[...,None]/2)
    integral=np.sum(weights*(np.pi/4)/np.sqrt(1-k*k*np.sin(phi)**2),axis=-1)
    return 2*integral/np.pi


def main():
    g=9.81
    length=np.linspace(.1,4.2,400)
    degrees=np.linspace(0,150,400)
    ratio=period_ratio(np.deg2rad(degrees))
    assert np.isclose(period_ratio(0),1,atol=1e-14)
    assert np.isclose(period_ratio(np.pi/2),1.1803405990160962,atol=1e-12)
    fig,axes=plt.subplots(1,2,figsize=(10.5,4.9),dpi=120,facecolor='white')
    axes[0].plot(length,2*np.pi*np.sqrt(length/g),color='#2878ad',lw=2.3)
    for ell in (1,4):
        t=2*np.pi*np.sqrt(ell/g)
        axes[0].scatter(ell,t,c='#c05a2a',s=50,zorder=4)
        axes[0].annotate(f'{ell} m: {t:.3f} s',(ell,t),xytext=(-5,-25) if ell==4 else (10,9),
                         textcoords='offset points',ha='right' if ell==4 else 'left',fontsize=11)
    axes[0].set(xlim=(0,4.4),ylim=(0,4.7),xlabel='Length ℓ (m)',ylabel='Small-angle period (s)',
                title=r'Length scaling: $T_0=2\pi\sqrt{\ell/g}$')
    axes[1].plot(degrees,ratio,color='#24805e',lw=2.3,label='Exact ideal-pendulum period ratio')
    axes[1].axhline(1,color='#2878ad',lw=1.4,ls='--',label='Small-angle approximation')
    for deg in (10,60,90,120):
        r=float(period_ratio(np.deg2rad(deg)))
        axes[1].scatter(deg,r,s=30,c='#c05a2a',zorder=4)
        axes[1].annotate(f'{deg}°: {r:.4f}',(deg,r),xytext=(5,8),textcoords='offset points',fontsize=10)
    axes[1].set(xlim=(0,155),ylim=(.96,1.8),xlabel='Initial amplitude θ₀ (degrees)',ylabel=r'$T/T_0$',
                title='Amplitude reveals the approximation limit')
    axes[1].legend(loc='upper left',fontsize=9)
    for ax in axes:
        ax.set_facecolor('white');ax.grid(alpha=.16)
        ax.spines['top'].set_visible(False);ax.spines['right'].set_visible(False)
    fig.suptitle('One ideal model predicts scaling and its small-angle correction',fontsize=15)
    fig.text(.5,.026,'Assume a point mass, massless fixed-length support, no drag, and '+r'$g=9.81\ \mathrm{m/s^2}$'+'.\n'
             'Right: exact periods from 256-point quadrature; these curves are not experimental measurements.',ha='center',fontsize=9)
    fig.tight_layout(rect=(0,.085,1,.925))
    fig.savefig(Path.cwd()/'pendulum-period-scaling.png',facecolor='white',transparent=False)
    plt.close(fig)
    for deg in (10,60,90,120):
        print(f'Amplitude {deg} degrees: T/T0={float(period_ratio(np.deg2rad(deg))):.10f}')
    print(f'Lengths 1m and4m: {2*np.pi/np.sqrt(g):.10f}s, {4*np.pi/np.sqrt(g):.10f}s')


if __name__=='__main__':
    main()
