"""Generate paper-141-lens.png in CWD; Python 3.14, matplotlib 3.10.7, numpy 2.3.5."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots(figsize=(6.6, 3.6), dpi=100)
x0 = .13
t = np.linspace(0, 1, 2001)
x, y = (5*t+.02) % 1, (3*t+.08) % 1
jump = (np.abs(np.diff(x)) > .5) | (np.abs(np.diff(y)) > .5)
x[1:][jump] = np.nan; y[1:][jump] = np.nan
ax.plot(x, y, color='#bc3131', lw=2, label=r'$\beta=5\mu+3\lambda$')
ax.plot([x0,x0], [0,1], color='#2368ad', lw=2, label=r'$\alpha=\lambda$')
for k in range(5):
 tt=(x0-.02+k)/5
 ax.plot(x0, (3*tt+.08)%1, 'ko', ms=4)
ax.plot([0,1,1,0,0],[0,0,1,1,0], 'k-', lw=1)
ax.set_aspect('equal'); ax.set_xlim(-.12,1.12); ax.set_ylim(-.12,1.12)
ax.set_xticks([0,1]);ax.set_yticks([0,1]);ax.set_xlabel(r'$\mu$');ax.set_ylabel(r'$\lambda$')
ax.spines[['top','right','bottom','left']].set_visible(False)
ax.legend(loc='center left', bbox_to_anchor=(1.04,.5), frameon=False)
ax.set_title('Heegaard torus: opposite edges identified', fontsize=12)
fig.subplots_adjust(left=.1,right=.66,bottom=.16,top=.86)
fig.savefig('paper-141-lens.png',facecolor='white')
