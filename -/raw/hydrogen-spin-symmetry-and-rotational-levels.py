"""Original hydrogen exchange-symmetry diagram; Python 3.14, matplotlib 3.10.7.
Run from _media; writes this script's basename.png to the current directory.
"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

plt.rcParams.update({'font.size': 11, 'figure.facecolor': 'white', 'axes.facecolor': 'white'})
fig = plt.figure(figsize=(10, 6.2), layout='constrained')
gs = fig.add_gridspec(1, 2, width_ratios=[1.1, 1])
a = fig.add_subplot(gs[0]); a.set_axis_off()
a.text(0, .98, 'Exchange the two protons', fontsize=16, weight='bold', va='top')
a.text(0, .87, 'Electronic ground state + vibrational ground state\nare symmetric under proton exchange.', va='top', linespacing=1.5)
a.text(0, .72, 'Total proton wavefunction must change sign.', weight='bold')
for y, color, title, line1, line2 in [
    (.39, '#176b98', 'Parahydrogen', r'$I_{\mathrm{n}}=0$: one antisymmetric spin state', r'$(-1)^J=+1$: even $J$'),
    (.08, '#b45220', 'Orthohydrogen', r'$I_{\mathrm{n}}=1$: three symmetric spin states', r'$(-1)^J=-1$: odd $J$')]:
    a.add_patch(FancyBboxPatch((.025, y), .925, .26, boxstyle='round,pad=0.015', fc='white', ec=color, lw=1.8))
    a.text(.05, y+.205, title, color=color, weight='bold', fontsize=14)
    a.text(.05, y+.13, line1, fontsize=11)
    a.text(.05, y+.055, line2, fontsize=12)
b = fig.add_subplot(gs[1]); b.set_xlim(-.1, 2.7); b.set_ylim(-1.8, 15.3)
b.set_ylabel(r'Rotational energy $E/(k_{\mathrm{B}}\theta_r)=J(J+1)$')
b.set_xticks([.45, 1.95], ['Para\neven $J$', 'Ortho\nodd $J$']); b.set_yticks([0,2,6,12])
b.spines[['top','right']].set_visible(False)
for j in range(4):
    x, color = (.45, '#176b98') if j%2==0 else (1.95, '#b45220')
    e=j*(j+1); g=(2*j+1)*(1 if j%2==0 else 3)
    b.hlines(e, x-.38, x+.38, color=color, lw=3)
    b.text(x, e+.32, f'J = {j};  g = {g}', ha='center', color=color)
b.annotate('', xy=(1.13, 2), xytext=(1.13, 0), arrowprops={'arrowstyle':'<->', 'color':'#444444'})
b.text(1.2, .85, r'$2k_{\mathrm{B}}\theta_r$', fontsize=11)
b.text(1.1, 14.4, r'$g=(2I_{\mathrm{n}}+1)(2J+1)$', ha='center', fontsize=13)
fig.suptitle('Hydrogen spin symmetry selects alternating rotor levels', fontsize=17, weight='bold')
fig.supxlabel('Field-free rigid-rotor model; no hyperfine splitting. Lines show energies, not measured spectra.', fontsize=9)
fig.savefig(Path(__file__).stem+'.png', dpi=150, facecolor='white', transparent=False)
