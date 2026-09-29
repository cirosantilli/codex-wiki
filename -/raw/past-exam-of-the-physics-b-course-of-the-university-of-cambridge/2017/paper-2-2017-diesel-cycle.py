"""Original dimensionless Diesel cycle, Python 3.14; pyproject dependencies.
Writes PNG basename in cwd.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(6.3, 4.4), facecolor='white', layout='constrained')
gamma = 1.4
v1, v2, v3, p1 = 1., .2, .4, 1.
p2 = p1*(v1/v2)**gamma
p4 = p2*(v3/v1)**gamma
v = np.linspace(v2, v1, 350)
ax.plot(v, p1*(v1/v)**gamma, color='#176a98', lw=2)
w = np.linspace(v3, v1, 350)
ax.plot(w, p2*(v3/w)**gamma, color='#176a98', lw=2)
ax.plot([v2, v3], [p2, p2], color='#bd6720', lw=2)
ax.plot([v1, v1], [p4, p1], color='#377e45', lw=2)
for xa, xb, func in [(.68, .52, lambda q: p1/q**gamma), (.57, .72, lambda q: p2*(v3/q)**gamma)]:
    ax.annotate('', xy=(xb, func(xb)), xytext=(xa, func(xa)), arrowprops=dict(arrowstyle='-|>', lw=1.7, color='#176a98'))
ax.annotate('', xy=(.35, p2), xytext=(.25, p2), arrowprops=dict(arrowstyle='-|>', color='#bd6720', lw=1.6))
ax.annotate('', xy=(1, 1.35), xytext=(1, 2.1), arrowprops=dict(arrowstyle='-|>', color='#377e45', lw=1.6))
for xx, yy, label in [(v1,p1,'1'),(v2,p2,'2'),(v3,p2,'3'),(v1,p4,'4')]:
    ax.plot(xx, yy, 'ko', ms=4)
    ax.annotate(label, (xx, yy), xytext=(7, 7), textcoords='offset points')
ax.text(.30, p2+1.05, 'Constant pressure: heat in', ha='center', fontsize=10)
ax.text(1.05, 1.8, 'Heat out', rotation=90, fontsize=10)
ax.set(xlabel='$V/V_1$', ylabel='$p/p_1$', xlim=(.1, 1.16), ylim=(0, 11.5), xticks=[v2,v3,v1], xticklabels=['$V_2/V_1$','$V_3/V_1$','1'], title='Ideal Diesel cycle: illustrative volume ratios')
ax.spines[['top','right']].set_visible(False)
fig.savefig(Path(__file__).with_suffix('.png').name, dpi=160, facecolor='white')
plt.close(fig)
