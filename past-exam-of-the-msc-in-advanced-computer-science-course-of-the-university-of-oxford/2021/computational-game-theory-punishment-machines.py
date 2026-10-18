"""Original solution diagram. Python 3.14; NumPy 2.3.5; Matplotlib 3.10.7.
Run from the directory where the PNG should be written.
"""
from pathlib import Path
import io
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, Ellipse
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11, "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white", "savefig.transparent": False})

fig, axes = plt.subplots(2, 2, figsize=(11.5, 6.8), layout="constrained")
for row, target in enumerate([("T", "L"), ("M", "C")]):
    for player in range(2):
        ax = axes[row, player]
        ax.set(xlim=(-1.2, 5.5), ylim=(-1.6, 2.0))
        ax.axis("off")
        own = target[player]
        punish = ("B", "R")[player]
        pair = "(" + ",".join(target) + ")"
        ax.set_title(f"Target {pair}: player {player+1}", fontsize=12)
        for x, label, color in [(0, f"Follow\noutput {own}", "#dcecf6"), (4.1, f"Punish\noutput {punish}", "#f4e0df")]:
            ax.add_patch(Circle((x, 0), 0.68, facecolor=color, edgecolor="#222222", lw=1.5))
            ax.text(x, 0, label, ha="center", va="center")
        ax.annotate("", xy=(-0.68, 0), xytext=(-1.12, 0), arrowprops={"arrowstyle": "->", "lw": 1.5})
        ax.annotate("", xy=(3.42, 0), xytext=(0.68, 0), arrowprops={"arrowstyle": "->", "lw": 1.5})
        ax.text(2.05, -0.35, f"observed pair != {pair}", ha="center", fontsize=10)
        for x, label in [(0, f"observed pair = {pair}"), (4.1, "any observed pair")]:
            ax.add_patch(FancyArrowPatch((x-0.43, 0.52), (x+0.43, 0.52), connectionstyle="arc3,rad=-1.65", arrowstyle="->", mutation_scale=12, lw=1.3))
            ax.text(x, 1.4, label, ha="center", fontsize=9)
fig.suptitle("Initial state: Follow. Read the completed joint action after each round.", fontsize=13)

buf = io.BytesIO()
fig.savefig(buf, format="png", dpi=160, facecolor="white", transparent=False, metadata={"Software": "Matplotlib"})
output = Path(Path(__file__).with_suffix(".png").name)
temporary = output.with_suffix(".png.tmp")
temporary.write_bytes(buf.getvalue())
os.replace(temporary, output)
plt.close(fig)
