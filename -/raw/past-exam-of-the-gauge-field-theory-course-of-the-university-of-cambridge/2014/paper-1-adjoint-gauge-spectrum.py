"""Original SU(3) adjoint-Higgs spectrum chart; output to cwd."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

generators = np.arange(1, 9)
fig, axes = plt.subplots(1, 2, figsize=(10, 4.8), dpi=100, facecolor="white", sharey=True)
spectra = [[0, 0, 0, 3, 3, 3, 3, 0], [2, 2, 0, 1, 1, 1, 1, 0]]
titles = [r"Vacuum eigenvalues $(v,v,-2v)$", r"Vacuum eigenvalues $(v,-v,0)$"]
subtitles = [r"Unbroken $S(U(2)\times U(1))$", r"Unbroken $U(1)\times U(1)$"]
for ax, masses, title, subtitle in zip(axes, spectra, titles, subtitles):
    masses = np.array(masses)
    ax.bar(generators, masses, color="tab:blue", width=0.65, zorder=3)
    zeros = generators[masses == 0]
    ax.scatter(zeros, np.zeros(len(zeros)), s=42, facecolor="white", edgecolor="tab:red", zorder=5)
    ax.set_xticks(generators, [f"$t^{i}$" for i in generators])
    ax.set(xlabel="Generator labeling the vector field", title=title, ylim=(-0.17, 3.75))
    ax.text(4.5, 3.37, subtitle, ha="center", fontsize=11)
    ax.grid(axis="y", alpha=0.22, zorder=0)
axes[0].set_ylabel(r"Vector-boson mass $m/(g|v|)$")
fig.text(0.5, 0.025, "Open red circles mark massless fields; paired real generators form conjugate charged vectors.",
         ha="center", fontsize=10.5)
fig.subplots_adjust(left=0.085, right=0.985, top=0.88, bottom=0.18, wspace=0.12)
fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, facecolor="white")
