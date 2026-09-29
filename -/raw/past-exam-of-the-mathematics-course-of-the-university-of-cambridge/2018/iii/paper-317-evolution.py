"""Original qualitative 5-solar-mass HR track; Python 3.14, matplotlib 3.10.7.
Coordinates illustrate phases, not a stellar-model calculation. Output goes to CWD.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(10, 6), dpi=100, facecolor='white')
ax.set_facecolor('white')
ax.axvspan(3.72, 3.85, color='#f4d885', alpha=.55)
ax.text(3.785, 4.35, 'Cepheid strip\n(approximate)', ha='center', va='top', fontsize=10)
# Qualitative points, chosen independently to separate the evolutionary phases.
pts=np.array([[4.18,2.72],[4.12,3.08],[4.15,3.14],[4.03,3.12],[3.64,3.35],
 [3.65,3.17],[3.76,3.05],[3.94,3.18],[3.83,3.40],[3.64,3.50],[3.58,3.82],[3.55,4.15]])
ax.plot(pts[:,0],pts[:,1],color='#285d98',lw=2.3)
for i in [0,3,5,7,8,10]:
 a,b=pts[i],pts[i+1]
 ax.annotate('',xy=a+.62*(b-a),xytext=a+.34*(b-a),arrowprops=dict(arrowstyle='->',color='#285d98',lw=1.8))
labels=[(0,'ZAMS\nage 0',(-18,-43)),(2,'H exhaustion\n80–100 Myr',(-15,30)),
 (4,'First giant branch\nfirst dredge-up',(34,-5)),(5,'Quiet He ignition\nage ~100 Myr',(43,-52)),
 (7,'Core He burning\nblue loop: 16–22 Myr',(-52,-58)),
 (9,'He exhaustion\nage 100–120 Myr',(41,5)),(10,'Early AGB\nsecond dredge-up',(42,-4)),
 (11,'TP-AGB\nthermal pulses / third dredge-up',(20,20))]
for i,text,off in labels:
 ax.plot(*pts[i],'o',color='#285d98',ms=4)
 ax.annotate(text,pts[i],xytext=off,textcoords='offset points',fontsize=10,ha='center',arrowprops=dict(arrowstyle='-',color='#7a7a7a',lw=.7))
ax.annotate('Hertzsprung gap\nrapid redward crossing',xy=(3.97,3.15),xytext=(4.02,2.45),fontsize=10,ha='center',arrowprops=dict(arrowstyle='-',color='#777'))
ax.annotate('',xy=(4.30,4.13),xytext=(3.58,4.13),arrowprops=dict(arrowstyle='->',color='#705088',lw=1.6))
ax.text(4.10,4.18,'Envelope ejection → hot remnant\n→ C/O white dwarf',fontsize=10,ha='center',va='bottom')
ax.text(4.20,2.28,'Schematic positions; ages and loop extent depend on composition and mixing.',fontsize=10,ha='left')
ax.set(xlim=(4.35,3.35),ylim=(2.2,4.48),xlabel=r'$\log_{10}(T_{\rm eff}/\mathrm{K})$  (hotter ←)',ylabel=r'$\log_{10}(L/L_\odot)$')
ax.set_title('Evolution of an initially 5-solar-mass star',fontsize=15)
ax.grid(alpha=.16)
fig.subplots_adjust(left=.10,right=.98,bottom=.12,top=.91)
fig.savefig(Path.cwd()/'paper-317-evolution.png',facecolor='white',transparent=False)
plt.close(fig)
