"""Original exact-sum rotor comparison; Python 3.14, numpy 2.3.5, matplotlib 3.10.7.
Run from _media; writes this script's basename.png to the current directory.
Temperature is dimensionless: t = T/theta_r. No measured constants or data.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


def rotor_models(t, jmax=100):
    """Return equilibrium ortho fraction, C_eq/kB, C_frozen/kB, and pure-para C/kB.
    Subtract each sector's lowest energy before exponentiating, retaining its
    physical offset in mean energies. Frozen composition is x_ortho=3/4.
    """
    j = np.arange(jmax+1)
    e = j*(j+1)
    means, variances, logq = [], [], []
    for parity in [0, 1]:
        en = e[j%2 == parity]
        g = 2*j[j%2 == parity]+1
        weights = g*np.exp(-(en-en[0])/t)
        z = weights.sum()
        p = weights/z
        mean = np.dot(p, en)
        means.append(mean)
        variances.append(np.dot(p, (en-mean)**2))
        logq.append(np.log(z)-en[0]/t)
    f = 1/(1+np.exp(logq[0]-logq[1])/3)
    within = (1-f)*variances[0]+f*variances[1]
    between = f*(1-f)*(means[1]-means[0])**2
    return f, (within+between)/t**2, (.25*variances[0]+.75*variances[1])/t**2, variances[0]/t**2


def main():
    plt.rcParams.update({'font.size':11, 'figure.facecolor':'white', 'axes.facecolor':'white'})
    t = np.geomspace(.12, 20, 750)
    values = np.array([rotor_models(x) for x in t])
    fig, axes = plt.subplots(2, 1, figsize=(9, 7), sharex=True, layout='constrained', gridspec_kw={'height_ratios':[1,1.6]})
    a, b = axes
    a.plot(t, values[:,0], color='#176b98', lw=2.5, label='Conversion maintains equilibrium')
    a.axhline(.75, color='#b45220', ls='--', lw=2, label='Frozen normal hydrogen: 3/4 ortho')
    a.set_ylabel('Ortho fraction'); a.set_ylim(-.035,.88); a.set_yticks([0,.25,.5,.75]); a.legend(loc='lower right', fontsize=10)
    b.plot(t, values[:,1], color='#176b98', lw=2.5, label='Equilibrium composition')
    b.plot(t, values[:,2], color='#b45220', ls='--', lw=2.5, label='Frozen 3:1 ortho/para composition')
    b.plot(t, values[:,3], color='#567a3e', ls=':', lw=2, label='Pure para (even J only)')
    b.axhline(1, color='#888888', lw=.8)
    b.set_ylabel(r'Rotational heat capacity per molecule $c_{\rm rot}/k_{\rm B}$')
    b.set_xlabel(r'Dimensionless temperature $t=T/\theta_r$')
    b.set_ylim(-.05,2.3); b.legend(loc='upper right', fontsize=10)
    b.annotate('Conversion contributes\nto equilibrium heat capacity', xy=(.52,1.9), xytext=(.13,1.1), arrowprops={'arrowstyle':'->','color':'#333333'}, fontsize=10)
    for ax in axes:
        ax.set_xscale('log'); ax.set_xlim(.12,20); ax.grid(alpha=.18); ax.spines[['top','right']].set_visible(False)
    fig.suptitle('The same rotor levels, two different thermal constraints', fontsize=16, weight='bold')
    fig.supxlabel('Ideal independent rotors; electronic and vibrational excitation omitted. Exact sums through J = 100.', fontsize=10)
    fig.savefig(Path(__file__).stem+'.png', dpi=150, facecolor='white', transparent=False)


if __name__ == '__main__':
    main()
