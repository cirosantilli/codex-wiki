"""Original chosen cubic I-V and quasistatic load-line dynamics, not device data.

Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7. Run from _media.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


def current(x):
    return x**3 - 6*x**2 + 10*x


def slope(x):
    return 3*x**2 - 12*x + 10


def trajectory(x0, r, xs):
    # tau = t I0 / (C V0). RK4, dimensionless time, no SciPy.
    t = np.linspace(0, 8, 4001)
    x = np.empty_like(t)
    x[0] = x0
    dt = t[1]-t[0]
    def f(y):
        return (xs-y)/r-current(y)
    for k in range(len(t)-1):
        a = f(x[k])
        b = f(x[k]+dt*a/2)
        c = f(x[k]+dt*b/2)
        d = f(x[k]+dt*c)
        x[k+1] = x[k]+dt*(a+2*b+2*c+d)/6
    return t, x


def main():
    plt.rcParams.update({'font.size': 11, 'figure.facecolor': 'white',
                         'axes.facecolor': 'white'})
    fig, axes = plt.subplots(2, 2, figsize=(11, 7.8), gridspec_kw={'height_ratios': [1.3, 1]})
    x = np.linspace(0, 3.6, 1801)
    ndr = (slope(x) < 0)
    cases = [(1., 6., [1., 2., 3.], r'$R=100\,\Omega,\ V_s=0.60\,\mathrm{V}$'),
             (.25, 3., [2.], r'$R=25\,\Omega,\ V_s=0.30\,\mathrm{V}$')]
    for col, (r, xs, roots, title) in enumerate(cases):
        ax = axes[0, col]
        ax.plot(.1*x, current(x), color='#1d5e99', lw=2.5, label='chosen device $I(V)$')
        ax.plot(.1*x[ndr], current(x)[ndr], color='#ba502c', lw=3, label='$dI/dV<0$ segment')
        ax.plot(.1*x, (xs-x)/r, '--', color='#574779', lw=1.8, label='supply line $(V_s-V)/R$')
        for root in roots:
            stable = 1/r+slope(root) > 0
            ax.plot(.1*root, current(root), 'o', ms=8, mec='#168253' if stable else '#bb2525',
                    mfc='#168253' if stable else 'white', mew=2, zorder=5)
            ax.annotate('stable' if stable else 'unstable', (.1*root, current(root)),
                        xytext=(-15, 17 if stable else -25), textcoords='offset points',
                        fontsize=10, color='#168253' if stable else '#bb2525')
        ax.set(xlim=(0, .36), ylim=(0, 7), xlabel='Junction voltage $V$ (V)',
               ylabel='Current $I$ (mA)', title=title)
        ax.grid(alpha=.18)
        if col == 0:
            ax.legend(loc='upper right', fontsize=9, framealpha=.95)
        ax = axes[1, col]
        for x0, color in [(1.9, '#1d5e99'), (2.1, '#b76619')]:
            t, y = trajectory(x0, r, xs)
            ax.plot(t, .1*y, color=color, lw=2, label=f'$V(0)={.1*x0:.2f}$ V')
        for root in roots:
            ax.axhline(.1*root, color='#999999', ls=':', lw=1)
        ax.set(xlim=(0, 8), ylim=(.08, .32), xlabel=r'Time $t$ ($\mu$s)',
               ylabel='Junction voltage $V$ (V)')
        ax.grid(alpha=.18)
        ax.legend(loc='lower right' if col == 0 else 'upper right', fontsize=9)
        ax.set_title('Two attracting states' if col == 0 else 'Negative-slope point is stable', fontsize=12)
    fig.suptitle('A toy tunnel-diode curve: supply resistance determines local stability', fontsize=15, y=.99)
    fig.text(.5, .92, r'$I=I_0(x^3-6x^2+10x),\ x=V/V_0;\quad V_0=0.10$ V, $I_0=1.0$ mA, $C=10$ nF',
             ha='center', fontsize=12)
    fig.text(.5, .024, r'$C\dot V=(V_s-V)/R-I(V)$; stable when $1/R+I^{\prime}(V)>0$. All values chosen; no measured curve or device fit.',
             ha='center', fontsize=10)
    fig.tight_layout(rect=(0, .05, 1, .91), h_pad=2.1, w_pad=2.4)
    fig.savefig(Path.cwd() / (Path(__file__).stem+'.png'), dpi=120, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
