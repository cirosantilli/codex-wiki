"""Original illustrative burst-model paths; Python 3.14, numpy and matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
rng = np.random.default_rng(201501)
fig = plt.figure(figsize=(11, 9), facecolor='white', layout='constrained')
grid = fig.add_gridspec(3, 2)
for row, (mean, burst) in enumerate([(10000, 3), (10000, 400), (100, 3)]):
    ax = fig.add_subplot(grid[row, 0])
    t, n = 0., 0
    ts, ns = [0.], [0.]
    arrival = mean / burst
    while t < 8:
        rate = arrival + n
        t += rng.exponential(1 / rate)
        if rng.random() < arrival / rate:
            n += int(rng.geometric(1 / (1 + burst)) - 1)
        else:
            n -= 1
        if t <= 8:
            ts.append(t)
            ns.append(n)
    ax.step(ts, np.array(ns) / mean, where='post', lw=.8, color='#176b87')
    tt = np.linspace(0, 8, 400)
    ax.plot(tt, 1 - np.exp(-tt), '--', color='#c05229', label='mean')
    ax.axhline(1, color='.6', lw=.7)
    ax.set(xlim=(0, 8), ylim=(0, 2), xlabel=r'$\alpha_P t$', ylabel=r'$N/\overline{N}$', title=f'burst b={burst}; stationary mean {mean:,} molecules')
    ax.legend(frameon=False, loc='lower right')
for row, intrinsic, title in [(0, .02, 'Intrinsic noise much smaller'), (1, .24, 'Comparable intrinsic and extrinsic noise')]:
    ax = fig.add_subplot(grid[row, 1])
    shared = rng.normal(0, .24, 350)
    cyan = 1 + shared + rng.normal(0, intrinsic, 350)
    yellow = 1 + shared + rng.normal(0, intrinsic, 350)
    ax.scatter(cyan, yellow, s=9, alpha=.45, color='#176b87')
    ax.plot([0, 2], [0, 2], '--', color='.4', lw=1)
    ax.set(xlim=(0, 2), ylim=(0, 2), xlabel='Cyan / mean cyan', ylabel='Yellow / mean yellow', title=title)
ax = fig.add_subplot(grid[2, 1]); ax.axis('off')
ax.text(.02, .9, 'Original model illustrations\n\nLeft: geometric bursts + individual loss.\nCell volume stipulated as 1 μm³.\nHigh concentration: mean 10,000.\nLow concentration: mean 100.\n\nRight: shared plus independent variation.\nNo experimental data are shown.', va='top', fontsize=12)
fig.suptitle('Expression fluctuations: copies, bursts, and paired reporters', fontsize=16)
fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name, dpi=120, facecolor='white', metadata={'Software': 'matplotlib'})
