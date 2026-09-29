"""Original covariance ellipses; Python 3.14, NumPy 2.3, Matplotlib 3.10.
Run in the mirrored media directory; writes a basename in the current directory.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

plt.rcParams.update({"font.size": 11, "figure.facecolor": "white", "axes.facecolor": "white"})
fig, axes = plt.subplots(1, 2, figsize=(8, 3.6), layout="constrained")
r = 0.75
for ax, squeezed in zip(axes, (False, True)):
    sx, sp = (np.exp(-r)/2, np.exp(r)/2) if squeezed else (0.5, 0.5)
    ax.add_patch(Ellipse((0, 0), 2*sx, 2*sp, facecolor="#d7e8f7", edgecolor="#155a91", lw=2))
    ax.axhline(0, color="0.75", lw=0.7)
    ax.axvline(0, color="0.75", lw=0.7)
    ax.annotate("", (sx, 0), (0, 0), arrowprops={"arrowstyle":"<->", "color":"#155a91"})
    ax.annotate("", (0, sp), (0, 0), arrowprops={"arrowstyle":"<->", "color":"#b13c2e"})
    ax.set(xlim=(-1.3, 1.3), ylim=(-1.3, 1.3), xlabel=r"$X-\langle X\rangle$", ylabel=r"$P-\langle P\rangle$")
    ax.set_aspect("equal")
    ax.set_title("Squeezed state" if squeezed else "Coherent state")
    ax.text(0.5, -0.29, r"$\Delta X=e^{-r}/2,\quad\Delta P=e^r/2$" if squeezed else r"$\Delta X=\Delta P=1/2$", transform=ax.transAxes, ha="center")
fig.suptitle("One-standard-deviation covariance contours")
fig.savefig("paper-1-aqp2013-quadrature-noise.png", dpi=140, facecolor="white", bbox_inches="tight")
