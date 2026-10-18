"""Original exact piecewise exponential relay trajectory, threshold h=1/2."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
h = .5
v = np.array([0., 1., 0.])
u = np.array([1., 1., 0.])
t = 0.
ts, values = [t], [v.copy()]
while t < 18:
    crossings = np.full(3, np.inf)
    for i in range(3):
        if u[i] == 1 and v[i] < h - 1e-12:
            crossings[i] = np.log((1 - v[i]) / (1 - h))
        elif u[i] == 0 and v[i] > h + 1e-12:
            crossings[i] = np.log(v[i] / h)
    j = int(np.argmin(crossings))
    duration = min(float(crossings[j]), 18 - t)
    if not np.isfinite(duration):
        duration = 18 - t
    local = np.linspace(0, duration, max(3, int(duration * 100)))
    segment = u[None, :] + (v - u)[None, :] * np.exp(-local[:, None])
    ts.extend(t + local[1:]); values.extend(segment[1:])
    v = segment[-1].copy()
    t += duration
    if t >= 18:
        break
    v[j] = h
    u[(j + 1) % 3] = 1 - u[(j + 1) % 3]
values = np.array(values)
fig, ax = plt.subplots(figsize=(10, 4.5), layout='constrained', facecolor='white')
for i, label in enumerate(['X', 'Y', 'Z']):
    ax.plot(ts, values[:, i], lw=2, label=label)
ax.axhline(h, color='.4', ls='--', lw=1, label='threshold h = 1/2 (stipulated)')
ax.set(xlim=(0, 18), ylim=(-.02, 1.05), xlabel=r'Common removal time units, $\alpha t$', ylabel='Concentration / unrepressed steady level', title='Original relay model: X represses Y, Y represses Z, Z represses X')
ax.legend(ncol=4, loc='upper right', frameon=False)
fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name, dpi=120, facecolor='white', metadata={'Software': 'matplotlib'})
