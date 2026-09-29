"""One original figure; Python3.14/numpy/matplotlib, output in current directory."""
import numpy as np
import matplotlib.pyplot as plt
v = np.linspace(-2.4, 2.4, 1000)
x = np.linspace(0, 1, 6001)
fig, axes = plt.subplots(1, 2, figsize=(9.4, 3.4), facecolor='white', layout='constrained')
axes[0].plot(v, (v**4/16-1)**4, color='#245b91')
axes[0].scatter([-2, 2], [0, 0], color='#b23b34', zorder=3)
axes[0].set(xlim=(-2.4,2.4), ylim=(-.05,1.4), xlabel='Slope v', ylabel='Derivative penalty / 16⁴', title='Two zero-energy slopes')
for n in [1,4,12]:
    y=2*np.abs((n*x+.5)%1-.5)/n
    axes[1].plot(x,y,label=f'N = {n}')
axes[1].set(xlim=(0,1),ylim=(-.02,1.08),xlabel='x',ylabel='u_N(x)',title='Amplitude vanishes; slopes stay ±2')
axes[1].legend(frameon=False)
for ax in axes:
    ax.grid(alpha=.2)
    ax.spines[['top','right']].set_visible(False)
fig.savefig('2009-oscillating-minimizing-sequence.png', dpi=150, facecolor='white')
