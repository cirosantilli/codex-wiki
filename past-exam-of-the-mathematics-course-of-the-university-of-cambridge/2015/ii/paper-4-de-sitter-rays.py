"""Draw radial null paths; PNG output goes only to the current directory."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(10, 6), dpi=100, facecolor='white')
r = np.linspace(0, .99, 700)
for u in np.arange(-1.5, 2.1, .5):
    ax.plot(r, u+r, color='#0072b2', linewidth=1.5)
for C in np.arange(.0, 4.6, .65):
    ax.plot(r, C+r-2*np.arctanh(r), color='#d55e00', linewidth=1.5)
ax.axvline(1,color='#333333',linestyle='--',label='Horizon r/a = 1')
ax.plot([],[],color='#0072b2',label='Outgoing: constant u')
ax.plot([],[],color='#d55e00',label='Ingoing: u/a = C − 2 artanh(r/a)')
ax.set(xlim=(0,1.06),ylim=(-.8,1.5),xlabel='r/a',ylabel='Plotting height (u+r)/a',title='Radial null rays in de Sitter space')
ax.set_aspect('equal',adjustable='box')
ax.legend(loc='upper left',bbox_to_anchor=(1.04,1.0),frameon=False)
ax.grid(alpha=.2)
fig.subplots_adjust(left=.10,right=.59,bottom=.12,top=.9)
fig.text(.63,.32,'Equal coordinate scale makes\nconstant-u rays rise at 45°.\n\nThe vertical coordinate is a\ntilted retarded-time grid,\nnot static time t.',fontsize=11)
fig.savefig('paper-4-de-sitter-rays.png',facecolor='white',transparent=False)
