"""Original functional SHG diagram; emit PNG to CWD using Python 3.14/matplotlib."""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

plt.rcParams.update({'font.size': 11, 'font.family': 'DejaVu Sans'})
fig = plt.figure(figsize=(10.8, 6.1), dpi=100, facecolor='white')
ax = fig.add_axes((0, 0, 1, 1))
ax.set(xlim=(0, 10.8), ylim=(0, 6.1))
ax.axis('off')
red, violet, ink = '#ba3434', '#7044b5', '#243447'
ax.text(.4, 5.72, 'Second-harmonic generation: source, material, readout', fontsize=17, weight='bold', color=ink)
ax.text(.4, 5.33, 'Functional arrangement • not to scale • no historical data reproduced', fontsize=11, color='#52616b')
blocks = [(.35, 1.24, 'Ruby\nlaser', '#fbe8e5'), (2.0, 1.18, 'Red\nfilter', '#fbe8e5'),
          (3.6, 1.10, 'Focusing\noptics', '#edf2f6'), (5.12, 1.12, 'Quartz\nsample', '#e4f4f1'),
          (6.66, 1.5, 'Quartz-prism\nspectrograph', '#f0eafa'), (8.58, 1.85, 'Photographic\nplate', '#edf2f6')]
y, h = 4.0, .84
for x, w, label, color in blocks:
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.03', facecolor=color, edgecolor=ink, linewidth=1.2))
    ax.text(x+w/2, y+h/2, label, ha='center', va='center', color=ink)
for (x, w, *_), (nx, *_rest) in zip(blocks[:-1], blocks[1:]):
    col = red if x < 5 else violet
    ax.add_patch(FancyArrowPatch((x+w+.05, y+h/2), (nx-.07, y+h/2), arrowstyle='-|>', mutation_scale=14, lw=2, color=col))
ax.text(2.58, 3.72, 'Suppress flash background\nbefore conversion', ha='center', va='top', fontsize=10, color=red)
ax.text(5.68, 3.72, r'$\omega\ \rightarrow\ \omega,\ 2\omega$', ha='center', va='top', color=violet)
ax.text(9.5, 3.72, 'Readout position\nlabels frequency', ha='center', va='top', fontsize=10, color=ink)
ax.plot([.4, 10.4], [3.05, 3.05], color='#c9d0d7', lw=1)
ax.text(.45, 2.65, 'Ideal photon energy balance', fontsize=14, weight='bold', color=ink)
for cy in (1.88, 1.18):
    xx = np.linspace(.5, 2.5, 250)
    ax.plot(xx, cy+.12*np.sin(2*np.pi*2*(xx-.5)), color=red, lw=1.8)
    ax.text(.5, cy+.20, r'$h\nu$', color=red)
    ax.add_patch(FancyArrowPatch((2.65, cy), (3.4, 1.53), arrowstyle='->', mutation_scale=15, lw=1.4, color=ink))
xx = np.linspace(3.6, 5.5, 300)
ax.plot(xx, 1.53+.12*np.sin(2*np.pi*4*(xx-3.6)), color=violet, lw=1.8)
ax.text(4.55, 2.00, r'$h(2\nu)=2h\nu$', ha='center', color=violet)
ax.text(.5, .52, 'Two input photons → one harmonic photon\nWaves illustrate frequency, not individual photon paths.', color=ink, fontsize=10)
ax.text(6.25, 2.65, 'Illustrative spectral readout', fontsize=14, weight='bold', color=ink)
ax.plot([6.4, 10.2], [1.25, 1.25], color=ink)
for x, color, label in [(6.9, violet, 'Harmonic'), (9.65, red, 'Fundamental')]:
    ax.plot([x, x], [1.02, 1.88], color=color, lw=3)
    ax.text(x, 2.05, label, ha='center', color=color, fontsize=10)
    ax.text(x, .79, r'$2\nu$' if x < 8 else r'$\nu$', ha='center', color=color)
ax.text(8.3, .25, 'Position schematic; no signal heights or yields implied.', ha='center', fontsize=9, color='#52616b')
fig.savefig(Path(__file__).stem+'.png', dpi=100, facecolor='white', transparent=False)
plt.close(fig)
