"""Original tree-level teaching curves; Python 3.14, numpy 2.3.5, mpl 3.10.7.

High energy relative to electron mass, contact limit relative to Z mass.
Run from _media; no SciPy, data fitting, or measured mixing angle.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


s2 = 0.25
g_l, g_r = -0.5+s2, s2
y = np.linspace(0.0, 1.0, 501)
left = np.full_like(y, g_l**2)
right = g_r**2*(1-y)**2
neutrino = left+right
antineutrino = g_r**2+g_l**2*(1-y)**2
assert np.allclose(neutrino, antineutrino)
assert np.isclose(np.trapezoid(neutrino, y), g_l**2+g_r**2/3, rtol=1e-6)

fig, axes=plt.subplots(1, 2, figsize=(10.5, 5.5), layout="constrained", facecolor="white")
ax=axes[0]
ax.plot(y, neutrino, color="#174e7a", lw=3, label=r"$\nu_\mu$: total")
ax.plot(y, left, color="#27835c", lw=2, label=r"$g_L^2$")
ax.plot(y, right, color="#ae542e", lw=2, label=r"$g_R^2(1-y)^2$")
ax.plot(y, antineutrino, color="#8054ad", lw=2, ls=(0, (4, 4)), label=r"$\bar\nu_\mu$: same here")
ax.set(xlim=(0, 1), ylim=(0, .145), xlabel=r"Recoil fraction $y=T_e/E_\nu$", ylabel=r"$\left(d\sigma/dy\right)/K$", title=r"Chosen $s_W^2=1/4$: $g_L=-1/4$, $g_R=1/4$")
ax.legend(loc="upper right", fontsize=10)
ax=axes[1]
for s2, color in [(0.15, "#17679c"), (0.25, "#8054ad"), (0.35, "#b24137")]:
    g_l, g_r=-.5+s2, s2
    ax.plot(y, g_l**2+g_r**2*(1-y)**2, color=color, lw=2.5, label=fr"$s_W^2={s2:.2f}$")
ax.set(xlim=(0, 1), ylim=(0, .16), xlabel=r"Recoil fraction $y=T_e/E_\nu$", ylabel=r"$\left(d\sigma_{\nu}/dy\right)/K$", title="Changing the chosen mixing parameter")
ax.legend(fontsize=11)
for ax in axes:
    ax.grid(alpha=.20)
    ax.spines[["top", "right"]].set_visible(False)
fig.suptitle("Muon-neutrino–electron elastic scattering", fontsize=18, fontweight="bold")
fig.supxlabel("Tree-level contact limit; electron initially at rest; neglect terms of order mₑ/Eν\n"
              r"$K = 2G_F^2 m_e E_\nu/\pi$ in natural units. All mixing values are toys, not measurements.", fontsize=11)
fig.savefig(Path(__file__).stem+".png", dpi=100, facecolor="white", transparent=False)
