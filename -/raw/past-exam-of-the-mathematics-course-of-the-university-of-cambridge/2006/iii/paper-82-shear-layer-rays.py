"""Original acoustic-ray sketch; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Writes paper-82-shear-layer-rays.png to caller CWD; honors MPLCONFIGDIR.
Units: omega = c0 = 1; mean flow U(y) = 0.6 (1 - exp(-y)).
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def primitive(values, grid):
    return np.r_[0, np.cumsum((values[:-1] + values[1:]) * np.diff(grid) / 2)]


def flow(y):
    return 0.6 * (1 - np.exp(-y))


def ray(beta, y):
    kx = np.cos(np.deg2rad(beta))
    intrinsic = 1 - flow(y) * kx
    ky = np.sqrt(intrinsic**2 - kx**2)
    return primitive((flow(y) * intrinsic + kx) / ky, y)


fig, ax = plt.subplots(figsize=(7.8, 5.3), facecolor='white')
y = np.linspace(0, 3, 1200)
for beta, color, label in [(65, '#1864ab', 'Downstream ray escapes'),
                            (145, '#2b8a3e', 'Upstream wave normal at launch'),
                            (90, '#862e9c', 'Wall-normal wave normal; ray drifts')]:
    x = ray(beta, y)
    ax.plot(x, y, color=color, lw=2.1, label=label)
    j = 650
    ax.annotate('', xy=(x[j+30], y[j+30]), xytext=(x[j-30], y[j-30]),
                arrowprops=dict(arrowstyle='->', color=color, lw=2.1))

kx = np.cos(np.deg2rad(35))
uturn = 1 / kx - 1
yturn = -np.log(1 - uturn / .6)
t = np.linspace(0, np.pi/2 - 1e-5, 1000)
yt = yturn * np.sin(t)**2
intrinsic = 1 - flow(yt) * kx
ky = np.sqrt(intrinsic**2 - kx**2)
dx_dt = (flow(yt) * intrinsic + kx) / ky * 2*yturn*np.sin(t)*np.cos(t)
xt = primitive(dx_dt, t)
ax.plot(xt, yt, color='#d95f02', lw=2.2, label='Shallow downstream ray turns')
ax.plot(2*xt[-1] - xt[::-1], yt[::-1], color='#d95f02', lw=2.2)
ax.scatter([xt[-1]], [yturn], color='#d95f02', s=28, zorder=5)
ax.annotate('Turning: $k_y=0$', xy=(xt[-1], yturn), xytext=(1.4, .95),
            color='#d95f02', fontsize=10,
            arrowprops=dict(arrowstyle='->', color='#d95f02'))
ax.annotate('', xy=(2*xt[-1]-xt[600], yt[600]),
            xytext=(2*xt[-1]-xt[680], yt[680]),
            arrowprops=dict(arrowstyle='->', color='#d95f02', lw=2.2))

for height in [.3, .8, 1.4, 2.1, 2.8]:
    ax.annotate('', xy=(4.35 + flow(height), height), xytext=(4.35, height),
                arrowprops=dict(arrowstyle='->', color='#a6aeb5', lw=1.5))
ax.text(4.05, 3.05, 'Mean flow', fontsize=10, color='#68737d')
ax.axhline(0, color='#343a40', lw=3)
ax.scatter([0], [0], color='#343a40', s=35, zorder=6)
ax.text(-.25, -.2, 'Wall source', fontsize=10)
ax.set(xlim=(-1.8, 5), ylim=(-.25, 3.25), xlabel='Distance along the wall',
       ylabel='Height above the wall', title='Acoustic rays through a wall shear layer')
ax.legend(loc='upper center', bbox_to_anchor=(.5, -.2), ncol=2, fontsize=8.5, frameon=True, facecolor='white', framealpha=1)
ax.spines[['top', 'right']].set_visible(False)
fig.tight_layout()
fig.savefig('paper-82-shear-layer-rays.png', dpi=120, facecolor='white', transparent=False)
plt.close(fig)
