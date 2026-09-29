"""Original infinite/finite square-well density comparison; Python 3.14, NumPy 2.3, Matplotlib 3.10."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Units L=1 and hbar^2/(2mL^2)=1. A chosen depth, not exam data.
V0 = 80.0
x = np.linspace(-.5, 1.5, 6001)
z = x-.5
inside = np.abs(z) <= .5

def bisect(f, lo, hi):
    for _ in range(90):
        mid = (lo+hi)/2
        if f(lo)*f(mid) <= 0:
            hi = mid
        else:
            lo = mid
    return (lo+hi)/2

fig, axes = plt.subplots(2, 1, figsize=(8.4, 6), sharex=True, layout='constrained')
for n, color in [(1, '#2563eb'), (2, '#d97706')]:
    rho = np.where(inside, 2*np.sin(n*np.pi*x)**2, 0)
    axes[0].plot(x, rho, color=color, lw=2.1, label=f'n = {n}')
    if n == 1:
        k = bisect(lambda k: k*np.tan(k/2)-np.sqrt(V0-k*k), 1e-8, np.pi-1e-8)
        psi = np.where(inside, np.cos(k*z), np.cos(k/2)*np.exp(-np.sqrt(V0-k*k)*(np.abs(z)-.5)))
    else:
        k = bisect(lambda k: -k/np.tan(k/2)-np.sqrt(V0-k*k), np.pi+1e-8, 2*np.pi-1e-8)
        psi = np.where(inside, np.sin(k*z), np.sign(z)*np.sin(k/2)*np.exp(-np.sqrt(V0-k*k)*(np.abs(z)-.5)))
    # Include the exact exterior-tail normalization beyond both walls.
    norm = np.trapezoid(psi[inside]**2, x[inside]) + (np.cos(k/2) if n == 1 else np.sin(k/2))**2/np.sqrt(V0-k*k)
    psi /= np.sqrt(norm)
    axes[1].plot(x, psi**2, color=color, lw=2.1, label=rf'n = {n}, $E={k*k:.2f}$')
    print(f'finite well n={n}: E={k*k:.10f}; plotted probability={np.trapezoid(psi**2,x):.9f}')
axes[0].set_title('Infinite walls: exact zeros at both edges')
axes[1].set_title(r'Finite walls: illustrative $V_0=80\,\hbar^2/(2mL^2)$')
for ax in axes:
    ax.axvspan(-.5, 0, color='#cbd5e1', alpha=.25)
    ax.axvspan(1, 1.5, color='#cbd5e1', alpha=.25)
    for edge in [0, 1]: ax.axvline(edge, color='#475569', lw=1, ls=':')
    ax.set(ylabel=r'$L|\psi(x)|^2$', ylim=(0, 2.25), xlim=(-.4, 1.4))
    ax.legend(loc='upper right', fontsize=9)
    ax.grid(alpha=.15)
axes[1].set_xlabel(r'Position $x/L$')
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name, dpi=150, facecolor='white')
