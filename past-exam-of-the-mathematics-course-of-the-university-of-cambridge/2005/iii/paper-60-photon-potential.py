"""Original photon-potential sketch; Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Write the basename PNG to caller CWD, preserving caller MPLCONFIGDIR.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


def main():
    u = np.linspace(0, 1.10, 800)
    potential = u*u*(1-u)
    critical = 2/3
    fig, ax = plt.subplots(figsize=(9, 4.8), dpi=100, facecolor="white")
    fig.subplots_adjust(bottom=.19, top=.90, left=.10, right=.97)
    ax.axvspan(0, .12, color="#d6ebd0", alpha=.9)
    ax.plot(u, potential, color="#566879", lw=2, ls="--", label="Formal first-order potential")
    low = u <= .12
    ax.plot(u[low], potential[low], color="#287135", lw=3)
    ax.axhline(4/27, color="#ac5a26", lw=1.3, ls=":", label=r"Critical constant $K=4/27$")
    ax.plot(critical, 4/27, "o", color="#ac5a26", ms=7)
    ax.annotate(r"$u_c=2/3$"+"\nFormal unstable maximum", xy=(critical,4/27), xytext=(.73,.205), arrowprops={"arrowstyle":"->", "color":"#ac5a26"}, fontsize=11)
    ax.text(.04, .07, r"$u\ll1$", color="#287135", rotation=90, ha="center", fontsize=13)
    ax.set(xlim=(0,1.1), ylim=(-.04,.26), xlabel=r"Inverse-radius variable $u=r_S/r$", ylabel=r"$V(u)=u^2(1-u)$", title="The formal circular orbit lies outside the weak-field regime")
    ax.legend(loc="upper left", frameon=False, fontsize=10)
    ax.spines[["top","right"]].set_visible(False)
    fig.text(.5, .025, "Green shading is an illustrative small-u window, not a sharp validity cutoff.", ha="center", fontsize=10)
    fig.savefig(Path.cwd()/"paper-60-photon-potential.png", facecolor="white", transparent=False)
    plt.close(fig)

if __name__ == "__main__":
    main()
