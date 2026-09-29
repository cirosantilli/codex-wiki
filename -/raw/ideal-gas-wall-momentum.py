"""Illustrate the signs and counting in an ideal gas wall collision.

Writes ideal-gas-wall-momentum.png to the current working directory.
This original schematic is a model, not a real experimental setup.
Tested with Python 3.14.4 and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle


def arrow(ax, start, end, color, width=2, style="-|>"):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle=style,
                                mutation_scale=17, linewidth=width, color=color))


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    fig = plt.figure(figsize=(10, 5.5), dpi=120)
    fig.suptitle("Gas pressure is momentum delivered to a wall", fontsize=16, y=0.965)
    fig.text(0.5, 0.895,
             "Schematic ideal gas model — not a real experimental setup",
             ha="center", fontsize=11, color="#555555")
    blue, green, red = "#226a9a", "#267849", "#b64231"
    ax = fig.add_axes((0.04, 0.285, 0.52, 0.56))
    ax.set(xlim=(0, 6.0), ylim=(0, 3.9))
    ax.axis("off")
    ax.add_patch(Rectangle((0.5, 0.85), 4, 2.45, fill=False,
                           linewidth=1.6, edgecolor="#666666"))
    ax.plot([4.5, 4.5], [0.85, 3.3], color="#333333", lw=4)
    ax.text(4.5, 3.5, r"Right wall: area $A$", ha="center")
    ax.text(0.65, 3.03, "One particle, before and after the bounce", fontsize=10)
    ax.scatter([1.55], [2.45], color=blue, s=55, zorder=3)
    arrow(ax, (1.65, 2.45), (4.47, 2.45), blue)
    ax.text(2.8, 2.62, r"Incoming: $v_x=+v$, $p_x=+mv$", color=blue,
            ha="center", fontsize=10)
    arrow(ax, (4.47, 1.4), (1.65, 1.4), green)
    ax.scatter([1.55], [1.4], color=green, s=55, zorder=3)
    ax.text(2.8, 1.08, r"Outgoing: $v_x=-v$, $p_x=-mv$", color=green,
            ha="center", fontsize=10)
    arrow(ax, (4.5, 1.95), (5.85, 1.95), red, width=2.5)
    ax.text(5.13, 2.09, r"$J_{\rm wall}=+2mv$", color=red,
            ha="center", fontsize=10)
    arrow(ax, (0.5, 0.55), (4.5, 0.55), "#555555", width=1.1, style="<->")
    ax.text(2.5, 0.30, r"Length $L$; volume $V=AL$", ha="center", fontsize=10)
    arrow(ax, (4.85, 0.55), (5.75, 0.55), "#333333", width=1.3)
    ax.text(5.30, 0.28, r"$+x$", ha="center")

    fig.text(0.59, 0.775, "Particle loses normal momentum", fontsize=12, color=green)
    fig.text(0.59, 0.723, r"$\Delta p_{x,\rm particle}=(-mv)-(+mv)=-2mv$", fontsize=12)
    fig.text(0.59, 0.646, "Wall receives the opposite impulse", fontsize=12, color=red)
    fig.text(0.59, 0.595, r"$J_{x,\rm wall}=+2mv$  (outward)", fontsize=13, color=red)
    fig.text(0.59, 0.514, "Return to the same wall: normal distance 2L", fontsize=11)
    fig.text(0.59, 0.456, r"Hit rate $=|v_x|/(2L)$", fontsize=13)
    fig.text(0.59, 0.378, r"$\overline{F}_{\perp,1}=(2m|v_x|)\frac{|v_x|}{2L}"
             r"=\frac{mv_x^2}{L}$", fontsize=14)
    fig.text(0.59, 0.306, r"$P_1=\overline{F}_{\perp,1}/A=mv_x^2/V$", fontsize=13)

    fig.text(0.5, 0.205,
             r"Many equal-mass particles, isotropic velocities:  "
             r"$P=\frac{Nm\langle v_x^2\rangle}{V}=\frac{Nm\langle v^2\rangle}{3V}$",
             ha="center", fontsize=14)
    fig.text(0.5, 0.112,
             r"Classical equipartition:  $\frac{1}{2}m\langle v^2\rangle="
             r"\frac{3}{2}k_BT$     $\Longrightarrow$     $PV=Nk_BT$",
             ha="center", fontsize=14)
    fig.text(0.5, 0.035,
             "Round-trip counting neglects intervening particle collisions; equilibrium momentum flux gives the same result.",
             ha="center", fontsize=9.5, color="#555555")
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
