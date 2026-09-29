"""Original lin-perpendicular-lin geometry and idealised energy cycle.

Python 3.14; NumPy 2.3.5; Matplotlib 3.10.7. Run from _media.
The potentials and completed hilltop cycles are explanatory, not trajectories
sampled from a particular atom's stochastic scattering dynamics.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    fig = plt.figure(figsize=(10, 7.2), layout="constrained")
    grid = fig.add_gridspec(3, 1, height_ratios=[1, 2.1, .8])
    top, ax, budget = [fig.add_subplot(grid[i]) for i in range(3)]
    fig.suptitle("Sisyphus cooling: climb, pump, climb again", fontsize=17)
    top.set(xlim=(-.045, .545), ylim=(-1.1, 1.35))
    top.axis("off")
    top.text(.25, 1.04, r"$\mathbf{E}(z)=E_0(\hat{\mathbf{x}}e^{ikz}+i\hat{\mathbf{y}}e^{-ikz})$   (complex amplitude)", ha="center")
    top.annotate(r"$+z$: linear $x$", (.17, .50), (-.02, .50), arrowprops={"arrowstyle": "->", "color": "#185fa5"}, color="#185fa5")
    top.annotate(r"$-z$: linear $y$", (.33, .50), (.52, .50), arrowprops={"arrowstyle": "->", "color": "#b24b13"}, color="#b24b13", ha="right")
    phi = np.linspace(0, 2*np.pi, 150)
    for q in np.arange(5)/8:
        ex, ey = np.exp(2j*np.pi*q), 1j*np.exp(-2j*np.pi*q)
        xx = np.real(ex*np.exp(-1j*phi))
        yy = np.real(ey*np.exp(-1j*phi))
        top.plot(q+.013*xx, -.19+.29*yy, color="#244657", lw=2)
        label = [r"$\sigma^+$", "linear", r"$\sigma^-$", "linear", r"$\sigma^+$"][round(q*8)]
        top.text(q, -.75, label, ha="center")
    top.text(.25, -1.04, r"$\sigma^\pm\equiv(\hat{\mathbf{x}}\pm i\hat{\mathbf{y}})/\sqrt{2}$; constant total intensity", ha="center", fontsize=10)

    z = np.linspace(0, .5, 600)
    up = -1-.5*np.cos(4*np.pi*z)
    um = -1+.5*np.cos(4*np.pi*z)
    ax.plot(z, up, color="#185fa5", lw=2.5, label=r"$U_+$: $m=+1/2$")
    ax.plot(z, um, color="#b24b13", lw=2.5, label=r"$U_-$: $m=-1/2$")
    ax.plot(z[z <= .25], up[z <= .25], color="#185fa5", lw=5, alpha=.3)
    ax.plot(z[z >= .25], um[z >= .25], color="#b24b13", lw=5, alpha=.3)
    for q, color in [(.25, "#185fa5"), (.5, "#b24b13")]:
        ax.annotate("", (q, -1.5), (q, -.5), arrowprops={"arrowstyle": "-|>", "lw": 2.5, "color": "#7c3994", "linestyle": "--"})
        ax.scatter([q], [-.5], color=color, zorder=5)
    for q, curve, color in [(.13, up, "#185fa5"), (.38, um, "#b24b13")]:
        zi = np.array([q-.025, q+.025])
        ui = -1+(-.5 if q < .25 else .5)*np.cos(4*np.pi*zi)
        ax.annotate("", (zi[1], ui[1]), (zi[0], ui[0]), arrowprops={"arrowstyle": "->", "lw": 2.5, "color": color})
    ax.text(.126, -1.68, r"climb: $\Delta K=-U_0$", ha="center", fontsize=10)
    ax.text(.377, -1.68, r"climb: $\Delta K=-U_0$", ha="center", fontsize=10)
    ax.annotate("optical pumping\nnear the opposite hilltop", (.25, -.95), (.20, -.12), ha="center", fontsize=10, arrowprops={"arrowstyle": "->", "color": "#7c3994"})
    ax.set(xlim=(-.025, .525), ylim=(-1.8, .23), xlabel=r"Position $z/\lambda$", ylabel=r"Ground-state potential $U/U_0$")
    ax.set_xticks(np.arange(5)/8, ["0", "1/8", "1/4", "3/8", "1/2"])
    ax.legend(loc="upper right", fontsize=10)
    ax.grid(alpha=.15)
    budget.axis("off")
    budget.text(.5, .82, "One ideal hilltop cycle (neglect recoil):", ha="center", weight="bold")
    budget.text(.5, .43, r"Climb: $\Delta K=-U_0$, $\Delta U=+U_0$     Pump: $\Delta U=-U_0$", ha="center")
    budget.text(.5, .08, r"Radiation gains $U_0$: $\hbar(\omega_{\rm out}-\omega_L)=U_0$; recoil adds heating.", ha="center")
    out = Path(__file__).stem+".png"
    fig.savefig(out, dpi=130, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
