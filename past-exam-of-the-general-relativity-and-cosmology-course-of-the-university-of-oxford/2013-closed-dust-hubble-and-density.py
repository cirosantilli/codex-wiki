"""Original closed-dust curves for Oxford 2013 GR Q3. Output PNG to CWD."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white", "axes.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(10, 4), layout="constrained")
    for left, right, color in [(.02, np.pi-.002, "#0072B2"), (np.pi+.002, 2*np.pi-.02, "#D55E00")]:
        theta = np.linspace(left, right, 2500)
        proper_time = (theta-np.sin(theta))/(2*np.pi)
        omega = 1/np.cos(theta/2)**2
        h_lifetime = np.pi*np.cos(theta/2)/np.sin(theta/2)**3
        label = "expansion" if left < np.pi else "contraction"
        axes[0].plot(proper_time, h_lifetime, color=color, label=label)
        axes[1].plot(proper_time, omega, color=color, label=label)
    axes[0].axhline(0, color="0.4", linewidth=1)
    axes[0].scatter([.5], [0], color="black", s=25, zorder=5)
    axes[0].set_yscale("symlog", linthresh=3)
    axes[0].set_ylim(-1e4, 1e4)
    axes[0].set_yticks([-1e4, -1e3, -1e2, -10, 0, 10, 1e2, 1e3, 1e4])
    axes[0].set(ylabel=r"$H\,t_{\rm life}$", title="Hubble parameter changes sign")
    axes[1].set_yscale("log")
    axes[1].set_ylim(.9, 1e4)
    axes[1].axhline(1, color="0.4", linestyle=":", linewidth=1)
    axes[1].set(ylabel=r"$\Omega_M=\rho_M/\rho_c$", title="Finite density, divergent density ratio")
    for ax in axes:
        ax.axvline(.5, color="0.5", linestyle="--", linewidth=1)
        ax.set(xlabel=r"cosmic time / total lifetime, $t/t_{\rm life}$", xlim=(0, 1))
        ax.legend(loc="lower left", fontsize=10)
        ax.grid(alpha=.2)
    fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
