"""Dimensionally continued quartic beta function; Python 3.14.

Root NumPy/Matplotlib dependencies; write the matching PNG to the caller's CWD.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(7.2, 4.1), layout='constrained', facecolor='white')
x = np.linspace(-.22, 1.8, 501)
ax.plot(x, x*(x-1), color='#24547a', lw=2.4)
ax.axhline(0, color='#7c8790', lw=.8)
ax.scatter([0,1], [0,0], color='#243746', s=48, zorder=3)
ax.annotate('Gaussian fixed point', (0,0), (.03,.73),
            arrowprops={'arrowstyle':'->', 'color':'#555'}, fontsize=11)
ax.annotate('interacting fixed point', (1,0), (.77,.88),
            arrowprops={'arrowstyle':'->', 'color':'#555'}, fontsize=11)
for start, end in [(0.75,0.22), (1.2,1.67)]:
    ax.annotate('', (end,-.43), (start,-.43),
                arrowprops={'arrowstyle':'-|>', 'lw':2, 'color':'#b65736'})
ax.text(.81,-.57,'arrows: increasing renormalization scale',ha='center',fontsize=10,color='#96462b')
ax.set(xlim=(-.22,1.8), ylim=(-.67,1.52),
       xlabel=r'$\lambda/\lambda_*,\quad\lambda_*=16\pi^2\epsilon/3$',
       ylabel=r'$\widehat\beta/(\epsilon\lambda_*)$',
       title=r'One-loop quartic flow for $\epsilon=4-d>0$')
ax.set_xticks([0,1], ['0', r'$1$'])
ax.spines[['top','right']].set_visible(False)
fig.savefig('paper-51-quartic-beta.png', dpi=120, facecolor='white')
plt.close(fig)
