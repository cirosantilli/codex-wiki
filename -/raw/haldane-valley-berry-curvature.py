"""Original lattice Berry-curvature comparison, no experimental data.

Run from _media; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Bond length=t1=1, embedding gauge and lower-band A=i<u|du> convention.
"""

from pathlib import Path
import importlib.util
import sys

sys.dont_write_bytecode = True
import matplotlib.pyplot as plt
from matplotlib.colors import TwoSlopeNorm
import numpy as np

spec = importlib.util.spec_from_file_location(
    "haldane_model", Path(__file__).with_name("haldane-chern-phase-and-valley-gaps.py"))
model = importlib.util.module_from_spec(spec)
spec.loader.exec_module(model)


def draw():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white", "axes.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(10.2, 4.5), layout="constrained")
    n = 341
    s, t = np.meshgrid(np.linspace(-.5, .5, n), np.linspace(-.5, .5, n), indexing="ij")
    k = s[..., None] * model.RECIPROCAL[0] + t[..., None] * model.RECIPROCAL[1]
    mu = 3 * np.sqrt(3) * .08
    cases = [(0, .08, np.pi / 2), (mu, 0, 0)]
    values = [model.curvature(k, *case) for case in cases]
    vmax = max(float(np.max(abs(value))) for value in values)
    norm = TwoSlopeNorm(vmin=-vmax, vcenter=0, vmax=vmax)
    for ax, z, title in zip(axes, values, [
        "Opposite valley masses: $C=-1$\n" + r"$M=0$, $t_2=0.08$, $\phi=\pi/2$",
        "Equal valley masses: $C=0$\n" + r"$M=3\sqrt{3}(0.08)$, $t_2=0$"
    ]):
        im = ax.pcolormesh(s, t, z, cmap="RdBu_r", norm=norm, shading="auto", rasterized=True)
        for tau, label in [(1, "$K_+$"), (-1, "$K_-$")]:
            sx, sy = -tau / 3, tau / 3
            ax.scatter(sx, sy, s=110, facecolor="none", edgecolor="black", lw=1)
            ax.annotate(label, (sx, sy), xytext=(9, 0), textcoords="offset points", va="center")
        ax.set(xlabel=r"$s_1$ in $\mathbf{k}=s_1\mathbf{g}_1+s_2\mathbf{g}_2$", ylabel=r"$s_2$", title=title, aspect="equal", xticks=[-.5, 0, .5], yticks=[-.5, 0, .5])
    fig.colorbar(im, ax=axes, shrink=.81, label=r"Lower-band Berry curvature $\Omega_-(\mathbf{k})/a^2$")
    fig.suptitle("Equal valley-gap magnitudes do not fix topology", fontsize=14)
    fig.supxlabel(r"Original lattice calculation, $a=t_1=1$; both cases have valley gaps $6\sqrt{3}(0.08)\simeq0.831$", fontsize=10)
    fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    draw()
