"""Original calculated torsion calibration curves, not measured data.

Tested with Python 3.14.4, matplotlib 3.10.7, numpy 2.3.5.
Run from _media: MPLCONFIGDIR=/tmp/codex-wiki-matplotlib python3 ../torsion-balance-calibration.py
Writes the matching opaque white PNG basename to the current working directory.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({'font.size': 11, 'figure.facecolor': 'white', 'axes.facecolor': 'white'})
    kappa, inertia, gamma = 1e-8, 2e-6, .020
    omega0 = np.sqrt(kappa/inertia)
    omegad = np.sqrt(omega0**2-gamma**2)
    period0, periodd = 2*np.pi/omega0, 2*np.pi/omegad
    delta = gamma*periodd
    # Choose phase so t=0 and every integer damped period are true positive maxima.
    phase = -np.arctan(gamma/omegad)
    amplitude = .020/np.cos(phase)
    t = np.linspace(0, 3.1*periodd, 1600)
    theta = amplitude*np.exp(-gamma*t)*np.cos(omegad*t+phase)
    envelope = amplitude*np.exp(-gamma*t)
    fig, axes = plt.subplots(1, 2, figsize=(10.6, 4.9))
    fig.subplots_adjust(left=.085, right=.98, bottom=.25, top=.76, wspace=.32)
    fig.suptitle('Two ways to calibrate a torsion constant', fontsize=17, y=.97)
    fig.text(.5, .87, r'Toy model, not measured data: $\kappa=10^{-8}$ N m/rad', ha='center', color='#555555')
    blue, orange, gray = '#245a91', '#b74b16', '#6b7280'
    ax = axes[0]
    ax.set_title('Static: slope of known torque vs twist', fontsize=12)
    angles = np.linspace(-.022, .022, 100)
    ax.plot(angles*1e3, kappa*angles/1e-10, color=blue, lw=2)
    pts = np.array([-.020, -.010, 0, .010, .020])
    ax.scatter(pts*1e3, kappa*pts/1e-10, color=blue, s=35, zorder=3)
    ax.axhline(0, color=gray, lw=.7)
    ax.axvline(0, color=gray, lw=.7)
    ax.set_xlabel(r'Twist $\theta$ (mrad)')
    ax.set_ylabel(r'Applied torque ($10^{-10}$ N m)')
    ax.set_xlim(-24, 24)
    ax.set_ylim(-2.45, 2.45)
    ax.annotate(r'20 mrad $\to 2\times10^{-10}$ N m', xy=(20, 2), xytext=(-20, 1.2), fontsize=10,
                arrowprops={'arrowstyle': '->', 'color': gray})
    ax.grid(alpha=.17)
    ax = axes[1]
    ax.set_title('Dynamic: period plus viscous decay', fontsize=12)
    ax.plot(t, 20*np.cos(omega0*t), '--', color=gray, alpha=.6, lw=1, label='no damping')
    ax.plot(t, theta*1e3, color=orange, lw=2, label='viscous damping')
    for sign in (-1, 1):
        ax.plot(t, sign*envelope*1e3, ':', color=orange, lw=1)
    peaks_t = np.array([0., periodd, 2*periodd])
    peaks = .020*np.exp(-gamma*peaks_t)
    ax.scatter(peaks_t, peaks*1e3, color=orange, s=25, zorder=4)
    ax.annotate('', xy=(periodd, 16), xytext=(0, 16), arrowprops={'arrowstyle': '<->', 'color': orange})
    ax.text(periodd/2, 17.7, r'$T_d=92.64$ s', ha='center', color=orange, fontsize=10)
    ax.text(122, -17, r'$\delta=\ln(p_n/p_{n+1})=1.853$', fontsize=10, color=orange)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Twist (mrad)')
    ax.set_xlim(-5, t[-1])
    ax.set_ylim(-24, 25)
    ax.legend(loc='upper right', fontsize=9, frameon=False)
    ax.grid(alpha=.17)
    fig.text(.26, .12, r'Same slope for both signs; zero intercept is assumed.', ha='center', fontsize=10)
    fig.text(.76, .12, r'$I=2\times10^{-6}$ kg m$^2$, $\gamma=0.020$ s$^{-1}$', ha='center', fontsize=10)
    fig.text(.5, .035, r'Period alone gives $0.92\kappa$; $\kappa=I(4\pi^2+\delta^2)/T_d^2$ recovers the input.', ha='center', fontsize=11)
    fig.savefig(Path(__file__).with_suffix('.png').name, dpi=110, facecolor='white', transparent=False)
    plt.close(fig)
    print(f'T0={period0:.9f} s; Td={periodd:.9f} s; delta={delta:.9f}; naive={inertia*omegad**2:.12g}; corrected={inertia*(omegad**2+gamma**2):.12g}')


if __name__ == '__main__':
    main()
