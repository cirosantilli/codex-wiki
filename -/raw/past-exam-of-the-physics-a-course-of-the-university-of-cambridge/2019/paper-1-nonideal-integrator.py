"""Original amplifier model and Bode curves; Python 3.14, NumPy 2.3, Matplotlib 3.10."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

fig = plt.figure(figsize=(10, 8), layout='constrained')
gs = fig.add_gridspec(3, 2, height_ratios=[1.1, 1, 1])
circuit = fig.add_subplot(gs[0, :])
mag = fig.add_subplot(gs[1, :])
phase = fig.add_subplot(gs[2, :], sharex=mag)
circuit.set(xlim=(-.3, 10.2), ylim=(-1.95, 3.1))
circuit.axis('off')

def wire(x, y): circuit.plot(x, y, color='#334155', lw=1.5)
def resistor(x0, x1, y, label):
    w = (x1-x0)*.6
    left = (x0+x1-w)/2
    wire([x0, left], [y, y]); wire([left+w, x1], [y, y])
    circuit.add_patch(Rectangle((left, y-.16), w, .32, fill=False, lw=1.5, edgecolor='#334155'))
    circuit.text((x0+x1)/2, y+.28, label, ha='center', fontsize=11)

resistor(.5, 2.8, .5, 'R')
wire([0, .5], [.5, .5]); circuit.text(0, .15, r'$V_{\rm in}$', ha='center', fontsize=12)
wire([2.8, 4], [.5, .5]); circuit.plot(3.2, .5, 'o', color='#334155', ms=4)
circuit.text(3.25, .12, 'v', fontsize=12)
circuit.add_patch(Rectangle((4, -.7), 2.1, 2.1, facecolor='#e0f2fe', edgecolor='#334155', lw=1.5))
circuit.text(4.12, .5, '−', va='center', fontsize=13)
circuit.text(4.12, -.3, '+', va='center', fontsize=13)
circuit.text(5.1, .55, r'$A(s)$', ha='center', fontsize=14)
circuit.text(5.1, -.03, r'$u=-A(s)v$', ha='center', fontsize=11)
wire([3.7, 4], [-.3, -.3]); wire([3.7, 3.7], [-.3, -1])
for j, w in enumerate([.35, .24, .12]): wire([3.7-w, 3.7+w], [-1-j*.12, -1-j*.12])
wire([6.1, 6.5], [.5, .5]); circuit.text(6.3, .8, 'u', fontsize=11)
resistor(6.5, 8.1, .5, r'$r_o$')
wire([8.1, 9.5], [.5, .5]); circuit.text(9.5, .1, r'$y=V_{\rm out}$', ha='center', fontsize=12)
wire([3.2, 3.2, 5.1], [.5, 2.2, 2.2]); wire([5.3, 8.9, 8.9], [2.2, 2.2, .5])
wire([5.1, 5.1], [1.85, 2.55]); wire([5.3, 5.3], [1.85, 2.55]); circuit.text(5.2, 2.68, 'C', ha='center', fontsize=12)
circuit.plot(8.9, .5, 'o', color='#334155', ms=4)
circuit.text(.1, -1.7, 'Infinite input impedance; unloaded output; finite gain and series output resistance', fontsize=10)
circuit.set_title('A specified linear non-ideal amplifier model', fontsize=12)

x = np.logspace(-6, 5, 2000) # x = omega RC
s = 1j*x
A0 = 1e4
pole = .01 # omega_a RC
A = A0/(1+s/pole)
for ratio, ls, label in [(0, '-', r'$r_o=0$'), (.01, '--', r'$r_o/R=0.01$')]:
    H = (s*ratio-A)/(1+s*(ratio+1+A))
    mag.semilogx(x, 20*np.log10(np.abs(H)), lw=2, ls=ls, label=label)
    phase.semilogx(x, np.angle(H, deg=True), lw=2, ls=ls, label=label)
for ax in [mag, phase]:
    for corner in [1/A0, A0*pole]: ax.axvline(corner, color='#64748b', ls=':', lw=1)
    ax.grid(alpha=.2, which='major')
    ax.set_xlim(x[0], x[-1])
mag.set(ylabel='Gain magnitude (dB)', title=r'Illustration: $A_0=10^4$, $\omega_aRC=0.01$')
mag.legend(loc='upper right')
mag.text(2e-6, 52, 'finite DC gain', fontsize=9)
mag.text(.035, 14, 'integrating', fontsize=9)
mag.text(1e3, -128, 'extra pole\n(when ro = 0)', fontsize=9)
phase.set(xlabel=r'Angular frequency $\omega RC$', ylabel='Phase (degrees)', ylim=(-5, 190), yticks=[0, 45, 90, 135, 180])
phase.text(1/A0, 18, r'$\omega_lRC\simeq10^{-4}$', ha='left', fontsize=9)
phase.text(A0*pole, 155, r'$\omega_hRC\simeq100$', ha='right', fontsize=9)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name, dpi=150, facecolor='white')
