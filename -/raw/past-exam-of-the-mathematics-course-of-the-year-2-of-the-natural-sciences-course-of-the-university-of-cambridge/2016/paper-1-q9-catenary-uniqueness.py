"""Original catenary graphical proof; Python 3.14, NumPy, Matplotlib. PNG to cwd."""
import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

q = 1.5
lo, hi = 0.01, 3.0
for _ in range(70):
    mid = (lo + hi) / 2
    if np.sinh(mid) / mid < q:
        lo = mid
    else:
        hi = mid
root = (lo + hi) / 2
k = 1 / root
fig, axes = plt.subplots(1, 2, figsize=(9.4, 3.9), layout="constrained", facecolor="white")
u = np.linspace(0, 2.5, 800)
axes[0].plot(u, np.sinh(u), lw=2, color="#1565a8", label=r"$\sinh u$")
axes[0].plot(u, q * u, lw=2, color="#c35419", label=r"$(L/a)u$, example $L/a=1.5$")
axes[0].scatter([root], [q * root], color="black", zorder=4)
axes[0].plot([root, root], [0, q * root], "--", color="0.5", lw=1)
axes[0].scatter([0], [0], facecolor="white", edgecolor="black", s=45, zorder=4)
axes[0].annotate("u = 0 excluded", (0, 0), (0.22, 0.8), arrowprops={"arrowstyle": "->", "lw": 0.8}, fontsize=9)
axes[0].set(xlim=(-0.04, 2.5), ylim=(-0.1, 6.3), xlabel=r"$u=a/k$", ylabel="Intersection height", title="One positive intersection")
axes[0].legend(fontsize=9, loc="upper left")
x = np.linspace(-1, 1, 600)
y = k * (np.cosh(x / k) - np.cosh(1 / k))
axes[1].plot(x, y, color="#1565a8", lw=2)
axes[1].scatter([-1, 1], [0, 0], color="black", s=35)
axes[1].axhline(0, color="0.6", lw=0.8, ls="--")
axes[1].set(xlim=(-1.15, 1.15), xlabel=r"$x/a$", ylabel=r"$(y-b)/a$", title=rf"Example chain: $k/a={k:.3f}$, $L/a=1.5$")
for ax in axes:
    ax.grid(alpha=0.17)
fig.savefig("paper-1-q9-catenary-uniqueness.png", dpi=165, facecolor="white")
plt.close(fig)
