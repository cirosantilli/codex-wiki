from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


output = Path(Path(__file__).stem + ".png")
c = np.linspace(0.0, np.pi, 1001)
f_plus = np.cos(c) * np.sinh(c) + np.sin(c) * np.cosh(c)
f_minus = np.cos(c) * np.sinh(c) - np.sin(c) * np.cosh(c)

lo, hi = np.pi / 2.0, np.pi
for _ in range(80):
    mid = (lo + hi) / 2.0
    value = np.cos(mid) * np.sinh(mid) + np.sin(mid) * np.cosh(mid)
    if value > 0.0:
        lo = mid
    else:
        hi = mid
root = (lo + hi) / 2.0

fig, ax = plt.subplots(figsize=(7.2, 4.4))
ax.axhline(0.0, color="black", linewidth=0.8)
ax.plot(c, f_plus, label=r"$\cos c\,\sinh c+\sin c\,\cosh c$")
ax.plot(c, f_minus, label=r"$\cos c\,\sinh c-\sin c\,\cosh c$")
ax.plot([root], [0.0], "o", color="black")
ax.annotate(
    rf"$c\approx {root:.3f}$",
    xy=(root, 0.0),
    xytext=(root - 0.75, 4.0),
    arrowprops={"arrowstyle": "->", "color": "black"},
)
ax.set_xlim(0.0, np.pi)
ax.set_xlabel(r"$c$")
ax.set_ylabel("characteristic function")
ax.set_xticks([0.0, np.pi / 2.0, np.pi], [r"$0$", r"$\pi/2$", r"$\pi$"])
ax.legend(loc="lower left")
ax.set_title(r"The $+$ condition has the unique root in $(0,\pi)$")
fig.tight_layout()
fig.savefig(output, dpi=100, facecolor="white")
