"""Original functional schematic of the inspected NIST FTMW experiment.

Sources: Chu et al., NISTIR 6816 (2002), printed pp.25–27, Fig.2;
Lovas et al., J.Res.NIST 117 (2012), printed pp.282–283, Fig.20.
Layout and explanatory grouping original; not a copy of either figure.
Python 3.14 / matplotlib 3.10.7. Run from _media.
"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Arc


def main():
    fig, ax = plt.subplots(figsize=(11, 7.3))
    fig.patch.set_facecolor('white')
    ax.set(xlim=(0, 11), ylim=(0, 7.3))
    ax.axis('off')
    blue, orange, green = '#2166ac', '#b35806', '#28734a'

    def box(x, y, w, h, label, color=blue, fontsize=11):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.08',
                                   facecolor='white', edgecolor=color, lw=1.6))
        ax.text(x+w/2, y+h/2, label, ha='center', va='center', fontsize=fontsize, color=color)

    def arrow(start, end, color=blue, dashed=False):
        ax.annotate('', xy=end, xytext=start,
                    arrowprops=dict(arrowstyle='->', color=color, lw=1.8,
                                    linestyle='--' if dashed else '-'))

    ax.text(5.5, 7.02, 'NIST cavity FTMW: sample → coherent signal → assigned lines',
            ha='center', fontsize=15, weight='bold')
    ax.text(5.5, 6.65, 'Original functional schematic of documented apparatus; not to scale',
            ha='center', fontsize=11)
    box(.2, 4.65, 2.2, 1.15, 'Documented sample\n1% OCS in argon\nPulsed nozzle', green)
    box(3.05, 4.05, 4.1, 2, '', green)
    ax.text(5.1, 5.82, 'Pumped vacuum chamber', ha='center', fontsize=11, color=green)
    ax.text(5.1, 4.25, 'Coaxial molecular beam', ha='center', fontsize=11, color=green)
    arrow((2.48, 5.12), (3.98, 5.12), green)
    ax.add_patch(Arc((4.07, 5.12), .55, 1.05, theta1=-70, theta2=70, color=blue, lw=3))
    ax.add_patch(Arc((6.13, 5.12), .55, 1.05, theta1=110, theta2=250, color=blue, lw=3))
    arrow((4.35, 5.12), (5.84, 5.12), green)
    ax.text(5.1, 5.53, 'Two facing cavity mirrors', ha='center', fontsize=10, color=blue)
    ax.text(5.1, 4.6, 'Motorized mirror tunes resonance', ha='center', fontsize=10)
    box(.25, 2.45, 2.1, 1.05, 'Microwave\nsynthesizer', blue)
    box(3.05, 2.45, 2, 1.05, 'Sideband + gating\nExcitation pulse', blue)
    arrow((2.45, 3), (2.96, 3))
    arrow((4.05, 3.57), (4.05, 3.95))
    box(7.9, 4.65, 2.8, 1.15, 'Receiver / mixer\nTime-dependent field\nafter excitation', orange)
    arrow((7.23, 5.12), (7.8, 5.12), orange)
    box(7.9, 2.45, 2.8, 1.05, 'Digitizer → Fourier transform\nLine centers (doublets)', orange, 10)
    arrow((9.3, 4.57), (9.3, 3.59), orange)
    box(5.75, 2.45, 1.45, 1.05, 'Shared source\nto mixer', blue, 10)
    arrow((2.05, 3.55), (6.42, 3.55), blue, True)
    arrow((6.42, 3.55), (6.42, 3.51), blue, True)
    arrow((7.28, 3), (7.64, 3), blue, True)
    arrow((7.64, 3), (7.64, 4.86), blue, True)
    arrow((7.64, 4.86), (7.81, 4.86), blue, True)
    ax.text(.25, 1.92, 'Frequency reference: 10 MHz → 30 MHz offset; common-source mixing', fontsize=10, color=blue)
    box(.25, .36, 5.25, 1.05, 'Controls reported in validation study\nBlind nitrogen mixture; single-component standards\nNozzle off/on; carrier-gas change', green, 10)
    box(6.05, .36, 4.65, 1.05, 'Inference and limits\nSeveral assigned lines → species evidence\nSignal → concentration needs response calibration', orange, 10)
    ax.text(5.5, -.01, 'Chu et al., NISTIR 6816, pp.25–27 (2002); Lovas et al., J.Res.NIST 117, pp.282–283 (2012)',
            ha='center', fontsize=9)
    fig.subplots_adjust(left=.015, right=.985, top=.99, bottom=.035)
    fig.savefig(Path(__file__).stem + '.png', dpi=110, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
