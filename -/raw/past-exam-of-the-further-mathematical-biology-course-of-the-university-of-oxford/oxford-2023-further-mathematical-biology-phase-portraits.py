"""Generate representative phase portraits in cwd; Python 3.14, NumPy, Matplotlib."""
import os
os.environ.setdefault('MPLCONFIGDIR', '/tmp/oxford-2023-fmb-matplotlib')
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

alpha = 0.2
cases = [(0.5, .05, -.1, 'One stable node'),
         (.4, .5, .112, 'One stable focus'),
         (.4, .15, .112, 'One unstable focus; sustained oscillation'),
         (.2, .2, .032, 'Two sinks and a saddle'),
         (.2, .04, .035, 'One source, one saddle, one sink'),
         (.25, .1, .052, 'Two sources and a saddle')]
fig, axes = plt.subplots(2, 3, figsize=(12, 7), layout='constrained')
vv = np.linspace(-.45, 1.25, 61)
ww = np.linspace(-.18, .56, 57)
V, W = np.meshgrid(vv, ww)
curve_v = np.linspace(-.45, 1.25, 700)
def f(v):
    return v*(alpha-v)*(v-1)
for ix, (ax, (k, gamma, current, title)) in enumerate(zip(axes.flat, cases)):
    beta = k*gamma
    U, Z = f(V)-W+current, beta*V-gamma*W
    ax.streamplot(vv, ww, U, Z, color='0.81', density=.8, linewidth=.6,
                  arrowsize=.6, integration_direction='both')
    ax.plot(curve_v, f(curve_v)+current, color='#2463a4', lw=1.4)
    ax.plot(curve_v, k*curve_v, color='#cb6a23', lw=1.4)
    roots = np.roots([1, -1-alpha, alpha+k, -current])
    roots = np.sort(roots.real[np.abs(roots.imag)<1e-9])
    for root in roots:
        p = -3*root**2+2*(1+alpha)*root-alpha
        det = gamma*(k-p)
        if det < 0:
            ax.scatter(root, k*root, marker='x', s=50, color='black', zorder=6)
        else:
            ax.scatter(root, k*root, marker='o', s=40, edgecolor='black',
                       facecolor='black' if p<gamma else 'white', zorder=6)
    seeds = np.array([[-.2, -.02], [.9, .27], [.42, .02]])
    if ix == 2:
        seeds = np.array([[.401, k*.4], [.9, .3], [-.15, -.05]])
    if ix == 5:
        seeds = np.array([[roots[0]+.002, k*roots[0]],
                          [roots[-1]-.002, k*roots[-1]], [-.2, -.02]])
    def rhs(state):
        v, w = state[:, 0], state[:, 1]
        return np.column_stack((f(v)-w+current, beta*v-gamma*w))
    dt = .04
    state = seeds.copy()
    track = np.empty((12001, len(seeds), 2))
    track[0] = state
    for j in range(12000):
        a = rhs(state)
        b = rhs(state+dt*a/2)
        c = rhs(state+dt*b/2)
        d = rhs(state+dt*c)
        state = state+dt*(a+2*b+2*c+d)/6
        track[j+1] = state
    for j, color in enumerate(['#29794c', '#89428c', '#b63a43']):
        ax.plot(track[:, j, 0], track[:, j, 1], color=color, lw=.9, alpha=.8)
        ax.scatter(*track[0, j], color=color, s=9, zorder=5)
    ax.set(xlim=(-.45, 1.25), ylim=(-.18, .56), xlabel='v', ylabel='w',
           title=title+'\n'+rf'$k={k:g},\ \gamma={gamma:g},\ I={current:g}$')
    ax.tick_params(labelsize=8)
    ax.title.set_fontsize(9)
legend = [Line2D([], [], color='#2463a4', label='v nullcline'),
          Line2D([], [], color='#cb6a23', label='w nullcline'),
          Line2D([], [], color='black', marker='o', ls='', label='sink'),
          Line2D([], [], color='black', marker='o', mfc='white', ls='', label='source'),
          Line2D([], [], color='black', marker='x', ls='', label='saddle')]
fig.legend(handles=legend, loc='outside lower center', ncol=5, fontsize=9)
fig.suptitle(r'FitzHugh–Nagumo phase portraits ($\alpha=0.2$); colored curves are trajectories', fontsize=12)
fig.savefig('oxford-2023-further-mathematical-biology-phase-portraits.png', dpi=145, facecolor='white')
