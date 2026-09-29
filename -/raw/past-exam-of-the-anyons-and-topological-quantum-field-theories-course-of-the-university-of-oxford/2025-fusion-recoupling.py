"""Draw the two fusion bases used in the 2025 anyons solution.

Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
Run from the destination directory; writes only 2025-fusion-recoupling.png.
"""
import os
os.environ.setdefault("MPLCONFIGDIR", "/tmp/oxford-2025-anyons-matplotlib")
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

INK = "#17324d"
ACCENT = "#a33638"
fig, ax = plt.subplots(figsize=(10, 4.5), dpi=120, facecolor="white")
ax.set_facecolor("white")
ax.set_xlim(-0.2, 7.5)
ax.set_ylim(-0.8, 3.2)
ax.axis("off")

def edge(p, q, label=None, offset=(0, 0)):
    ax.plot([p[0], q[0]], [p[1], q[1]], color=INK, linewidth=2)
    if label:
        x, y = (p[0]+q[0])/2, (p[1]+q[1])/2
        ax.text(x+offset[0], y+offset[1], label, fontsize=15,
                ha="center", va="center", color=INK,
                bbox={"facecolor": "white", "edgecolor": "none", "pad": 0.8})

def tree_left():
    leaves = [(0.1, 2.3), (0.8, 2.3), (1.7, 2.3), (2.4, 2.3)]
    b, c, root, foot = (0.45, 1.3), (2.05, 1.3), (1.25, 0.25), (1.25, -0.25)
    for p, q, label in [(leaves[0], b, "d"), (leaves[1], b, "j"),
                        (leaves[2], c, "h"), (leaves[3], c, "e")]:
        edge(p, q)
        ax.text(p[0], 2.45, f"${label}$", fontsize=16, ha="center", color=INK)
    edge(b, root, "$b$", (-0.14, 0))
    edge(c, root, "$c$", (0.14, 0))
    edge(root, foot, "$a$", (0.18, 0))
    ax.text(1.25, 2.93, r"$|T_{bc}\rangle$", fontsize=19, ha="center", color=INK)
    ax.text(1.25, -0.65, "The original paired basis", fontsize=12, ha="center", color=INK)

def tree_right():
    leaves = [(4.8, 2.3), (5.5, 2.3), (6.2, 2.3), (6.9, 2.3)]
    x, y, root, foot = (5.85, 1.55), (6.25, 0.8), (5.5, 0.15), (5.5, -0.25)
    edge(leaves[0], root)
    edge(leaves[1], x)
    edge(leaves[2], x)
    edge(leaves[3], y)
    for p, label in zip(leaves, ["d", "j", "h", "e"]):
        ax.text(p[0], 2.45, f"${label}$", fontsize=16, ha="center", color=INK)
    edge(x, y, "$x$", (-0.17, 0))
    edge(y, root, "$y$", (0.17, 0))
    edge(root, foot, "$a$", (0.18, 0))
    ax.text(5.9, 2.93, r"$|X_{xy}\rangle$", fontsize=19, ha="center", color=INK)
    ax.text(5.9, -0.65, r"Full braid: $m_x=R_x^{jh}R_x^{hj}$", fontsize=13, ha="center", color=ACCENT)

tree_left()
tree_right()
ax.annotate("", xy=(4.35, 1.4), xytext=(2.8, 1.4),
            arrowprops={"arrowstyle": "->", "color": ACCENT, "lw": 2})
ax.text(3.58, 1.68, r"$U_{bc;xy}$", color=ACCENT, fontsize=16, ha="center")
ax.text(3.58, 0.95, "Two changes\nof parentheses", color=INK, fontsize=11,
        ha="center", va="center", linespacing=1.5)
fig.tight_layout(pad=0.7)
fig.savefig("2025-fusion-recoupling.png", facecolor="white", transparent=False)
plt.close(fig)
