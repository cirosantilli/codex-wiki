"""Original weak-field schematic. Python 3.14; NumPy and Matplotlib."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
fig, ax = plt.subplots(figsize=(9, 4), layout="constrained")
x = np.linspace(-5, 5, 700)
b, bend = 1.5, 0.11
y = b - bend * (x + np.sqrt(x*x + b*b))
ax.plot(x, y, color="#1767a2", lw=2.5, label="bent ray (exaggerated)")
ax.add_patch(Circle((0, 0), .38, color="#edba45"))
ax.text(0, -.58, "mass", ha="center")
xo = 5.
yo = y[-1]
slope = -bend * (1 + xo / np.sqrt(xo*xo + b*b))
ax.plot(x, yo + slope * (x-xo), "--", color="#b24545",
        label="backward extrapolation at observer")
ax.plot([-5, 5], [b, b], ":", color=".5", label="undeflected reference")
ax.plot(xo, yo, "o", color="black")
ax.text(xo, yo-.28, "observer", ha="right")
for xx in [-3., 2.7]:
    yy = b - bend * (xx + np.sqrt(xx*xx+b*b))
    xx1 = xx + .55
    yy1 = b - bend * (xx1 + np.sqrt(xx1*xx1+b*b))
    ax.annotate("", (xx1, yy1), (xx, yy),
                arrowprops={"arrowstyle": "->", "lw": 2, "color": "#1767a2"})
ax.annotate("", (-1, b), (-1, 0),
            arrowprops={"arrowstyle": "<->", "color": ".35"})
ax.text(-.85, .75, r"$b$")
ax.text(-4.9, 2.9, "apparent stellar direction\nlies farther from the mass",
        color="#b24545", va="top")
ax.set(xlim=(-5.4, 5.4), ylim=(-1.6, 3.15), aspect="equal")
ax.axis("off")
ax.legend(loc="lower left", ncol=2, frameon=False, fontsize=9)
fig.savefig("paper-1-light-deflection.png", dpi=155, facecolor="white")
