"""Original functional Homestake diagram; Python 3.14, matplotlib 3.10, NumPy 2.3.

Run from _media; writes homestake-chemical-neutrino-readout.png to CWD.
Illustrative curves use dimensionless half-life units, not experimental data.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def main():
    plt.rcParams.update({'font.size': 11, 'font.family': 'DejaVu Sans'})
    fig = plt.figure(figsize=(10, 6.3), facecolor='white')
    fig.suptitle('Homestake: chemical memory, then delayed pulses', fontsize=17, y=.97)
    ax = fig.add_axes([.025, .53, .95, .36])
    ax.set(xlim=(0, 10), ylim=(0, 3)); ax.axis('off')
    boxes = [(0.15, '1  Capture', 'Chlorine target\nin liquid'),
             (3.6, '2  Extract', 'Helium sweep\nArgon trap + purification'),
             (7.05, '3  Count', 'Small proportional counter\nElectron-capture pulses')]
    for x, title, label in boxes:
        ax.add_patch(FancyBboxPatch((x, .6), 2.8, 1.85, boxstyle='round,pad=0.1',
                                   facecolor='#edf4fa', edgecolor='#22577a', linewidth=1.7))
        ax.text(x+1.4, 2.05, title, ha='center', weight='bold', color='#173e59')
        ax.text(x+1.4, 1.3, label, ha='center', va='center', fontsize=11)
    for x in (3.0, 6.45):
        ax.annotate('', xy=(x+.5, 1.5), xytext=(x, 1.5),
                    arrowprops={'arrowstyle':'->', 'lw':2, 'color':'#22577a'})
    ax.text(1.55, .1, r'$\nu_e+{}^{37}\mathrm{Cl}\to{}^{37}\mathrm{Ar}+e^-$', ha='center', fontsize=12)
    ax.text(5, .1, 'Stable argon: recovery check', ha='center', fontsize=10)
    ax.text(8.45, .1, 'Background counting: pulse check', ha='center', fontsize=10)
    plot = fig.add_axes([.11, .13, .52, .33])
    t = np.linspace(0, 3, 301)
    signal = 2.0**(-t)
    background = .12
    plot.plot(t, signal+background, color='#22577a', lw=2.5, label='Signal + background')
    plot.plot(t, signal, color='#c05a19', lw=2, label='Signal alone')
    plot.axhline(background, color='#707070', ls='--', lw=1.5, label='Constant background')
    plot.set(xlim=(0, 3), ylim=(0, 1.2), xlabel='Time after counting starts / half-life',
             ylabel='Expected pulse rate\n(arbitrary units)', xticks=[0, 1, 2, 3])
    plot.spines[['top', 'right']].set_visible(False)
    plot.grid(alpha=.17); plot.legend(fontsize=9, loc='upper right', frameon=False)
    fig.text(.70, .37, 'Illustrative counting model', weight='bold', fontsize=11)
    fig.text(.70, .22, 'After one half-life:\nsignal rate halves;\nconstant background persists.', fontsize=11, linespacing=1.6)
    fig.text(.5, .025, 'Functional schematic; not to scale. Curves are not measured data.', ha='center', fontsize=10, color='#4a4a4a')
    fig.savefig(Path.cwd() / (Path(__file__).stem+'.png'), dpi=110, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
