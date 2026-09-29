"""Original two-loop response and free ring-down; Python 3.14.

Requires numpy 2.3.5 and matplotlib 3.10.7. Run from _media.
Two identical series loops: L=5mH, C=2nF, TOTAL R=100ohm each.
A 50ohm secondary sense resistor is included in total R. Source 0.1V peak.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 11, 'font.family': 'DejaVu Sans'})
L, C, R, Rs = .005, 2e-9, 100., 50.
w0 = 1 / np.sqrt(L*C)
f0 = w0/(2*np.pi)
Q = w0*L/R
f = np.linspace(35000, 68000, 5000)
w = 2*np.pi*f
Z = R + 1j*(w*L - 1/(w*C))
fig, (a, b) = plt.subplots(2, 1, figsize=(9, 7), dpi=120, facecolor='white')
for k, color in [(.01, '#85949b'), (1/Q, '#176b99'), (.20, '#b75c15')]:
    M = k*L
    H = -1j*w*M*Rs/(Z*Z+(w*M)**2)
    a.plot(f/1000, np.abs(H), color=color, lw=2,
           label=f'k = {k:.4f}'+ (' = 1/Q' if k == 1/Q else ''))
a.axvline(f0/1000, color='#777777', ls=':', lw=1)
a.text(f0/1000+.35, .028, 'f₀ = 50.329 kHz', fontsize=10)
a.set(xlabel='Drive frequency f (kHz)', ylabel='Sense voltage / source voltage',
      title='Coupled resonators: increasing coupling can split the response',
      xlim=(35, 68), ylim=(0, .30))
a.legend(loc='upper right', fontsize=10)
a.grid(alpha=.22)
a.text(.025,.92, 'L = 5 mH, C = 2 nF\nR = 100 Ω total per loop\nRₛ = 50 Ω; Q = 15.811',
       transform=a.transAxes, va='top', fontsize=10,
       bbox={'facecolor':'white','edgecolor':'#dddddd','alpha':.9})
t=np.linspace(0, .0006, 6000)
alpha=R/(2*L)
wd=np.sqrt(w0*w0-alpha*alpha)
decay=np.exp(-alpha*t)
b.plot(t*1e6, np.cos(wd*t)*decay, color='#176b99', lw=1.7, label='Free decay after one excitation')
b.plot(t*1e6, decay, color='#176b99', ls='--', lw=1)
b.plot(t*1e6, -decay, color='#176b99', ls='--', lw=1)
b.plot(t*1e6, np.cos(w0*t), color='#b75c15', alpha=.5, lw=1, label='Maintained sine reference')
b.set(xlabel='Time after excitation (μs)', ylabel='Normalized oscillation',
      title='One damped train is different from a maintained sine',
      xlim=(0, 600), ylim=(-1.15,1.15))
b.legend(loc='upper right', fontsize=10, framealpha=.95)
b.grid(alpha=.22)
b.text(.98,.08,'Amplitude decay time 2L/R = 100 μs', transform=b.transAxes, ha='right', fontsize=10,
       bbox={'facecolor':'white','edgecolor':'none','alpha':.9})
fig.text(.5,.012,'Calculated linear models; no measured points. Free decay below is one isolated loop.',ha='center',fontsize=10)
fig.tight_layout(rect=(0,.04,1,1),h_pad=1.5)
fig.savefig(Path(__file__).stem+'.png',facecolor='white')
