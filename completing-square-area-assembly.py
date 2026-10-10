"""Original square-completion area assembly; write PNG to the current directory."""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

plt.rcParams.update({"font.size": 12, "figure.facecolor": "white", "axes.facecolor": "white"})
fig, axes = plt.subplots(1, 2, figsize=(10, 5))
fig.subplots_adjust(left=.04, right=.98, bottom=.19, top=.81, wspace=.24)
for ax, fill in zip(axes, [False, True]):
    ax.add_patch(Rectangle((0, 0), 2, 2, facecolor="#bfdbfe", edgecolor="#2563eb", lw=1.8))
    ax.add_patch(Rectangle((0, 2), 2, 3, facecolor="#d1fae5", edgecolor="#059669", lw=1.8))
    ax.add_patch(Rectangle((2, 0), 3, 2, facecolor="#d1fae5", edgecolor="#059669", lw=1.8))
    ax.add_patch(Rectangle((2, 2), 3, 3, facecolor="#fde68a" if fill else "white", edgecolor="#b45309", lw=2, linestyle="-" if fill else "--"))
    for xx, yy, label in [(1, 1, r"$x^2$"), (1, 3.5, r"$3x$"), (3.5, 1, r"$3x$"), (3.5, 3.5, r"$3^2=9$" if fill else "Missing\ncorner")]:
        ax.text(xx, yy, label, ha="center", va="center", fontsize=14)
    ax.text(1, -.35, r"$x$", ha="center"); ax.text(3.5, -.35, "3", ha="center")
    ax.text(-.32, 1, r"$x$", ha="center", va="center"); ax.text(-.32, 3.5, "3", ha="center", va="center")
    ax.set(xlim=(-.65, 5.3), ylim=(-.65, 5.3), aspect="equal")
    ax.axis("off")
axes[0].set_title(r"Two strips give $x^2+6x$", pad=14)
axes[1].set_title(r"Adding $9$ gives $(x+3)^2$", pad=14)
fig.suptitle("A missing corner explains the squared half-coefficient", fontsize=16)
fig.text(.5, .095, r"$x^2+6x+13=(x+3)^2-9+13=(x+3)^2+4$", ha="center", fontsize=16)
fig.text(.5, .025, "Area layout shown at x = 2; the polynomial identity holds for every real x.", ha="center", fontsize=10)
fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white", transparent=False)
plt.close(fig)
