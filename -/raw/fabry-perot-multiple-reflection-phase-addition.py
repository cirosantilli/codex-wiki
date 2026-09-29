"""Original ideal ray geometry and coherent amplitudes; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

Run from _media to emit this script's matching opaque PNG into the working directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def arrow(ax, a, b, color, lw=1.8):
    ax.annotate("", xy=b, xytext=a,
                arrowprops=dict(arrowstyle="->", color=color, lw=lw,
                                shrinkA=0, shrinkB=0, mutation_scale=12))


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "savefig.facecolor": "white"})
    fig = plt.figure(figsize=(11.5, 6.5), facecolor="white")
    gs = fig.add_gridspec(2, 2, width_ratios=(1.15, 1), hspace=.68, wspace=.30)
    geometry = fig.add_subplot(gs[:, 0])
    theta = np.deg2rad(25)
    d, y0 = 1.5, .4
    slope = np.tan(theta)
    direction = np.array([np.cos(theta), np.sin(theta)])
    colors = ["#1565a8", "#b45309", "#15805d", "#8b4b9f", "#ba3945"]
    geometry.axvspan(-.065, .065, color="#c6d2db")
    geometry.axvspan(d-.065, d+.065, color="#c6d2db")
    geometry.text(0, 4.85, "Mirror 1", ha="center", weight="bold")
    geometry.text(d, 4.85, "Mirror 2", ha="center", weight="bold")
    arrow(geometry, (-.72, y0-.72*slope), (0, y0), colors[0])
    geometry.text(-.70, -.25, "Incident\nplane wave", color=colors[0])
    vertices = [np.array([0., y0])]
    for j in range(5):
        vertices.append(np.array([d if j % 2 == 0 else 0., y0+(j+1)*d*slope]))
        arrow(geometry, vertices[-2], vertices[-1], colors[0])
    # A common plane perpendicular to the emerging direction: k_hat dot x = C.
    cplane = 4.30
    ends = []
    for j in range(3):
        start = np.array([d, y0+(2*j+1)*d*slope])
        end = start+(cplane-np.dot(direction, start))*direction
        ends.append(end)
        arrow(geometry, start, end, colors[j])
        geometry.text(*(start+.28*direction+np.array([0., -.16])),
                      rf"$E_{j}$", color=colors[j], fontsize=13)
    tangent = np.array([-direction[1], direction[0]])
    plane = np.array([ends[0]-.38*tangent, ends[-1]+.40*tangent])
    geometry.plot(plane[:, 0], plane[:, 1], "--", color="#54616c", lw=1.5)
    geometry.text(3.53, 4.42, "Common outgoing\nwavefront", ha="center", fontsize=10)
    geometry.plot([0, .75], [y0, y0], ":", color="#54616c")
    arc = np.linspace(0, theta, 50)
    geometry.plot(.52*np.cos(arc), y0+.52*np.sin(arc), color="#54616c")
    geometry.text(.64, y0+.08, r"$\theta$", fontsize=14)
    geometry.annotate("", (0, -.30), (d, -.30),
                      arrowprops=dict(arrowstyle="<->", color="#333333"))
    geometry.text(d/2, -.56, r"Mirror spacing $d$", ha="center")
    geometry.text(.95, 5.30, "Extra round trip: two internal reflections", ha="center", fontsize=11)
    geometry.set(xlim=(-.85, 4.45), ylim=(-.85, 5.55), aspect="equal")
    geometry.axis("off")
    geometry.set_title("Ray paths and phase comparison", pad=20, weight="bold")
    for row, delta in enumerate([0., np.pi/2]):
        ax = fig.add_subplot(gs[row, 1])
        terms = .25*.75**np.arange(5)*np.exp(1j*np.arange(5)*delta)
        points = np.r_[0j, np.cumsum(terms)]
        exact = .25/(1-.75*np.exp(1j*delta))
        for j in range(5):
            a, b = points[j], points[j+1]
            arrow(ax, (a.real, a.imag), (b.real, b.imag), colors[j], 2.5)
            if row == 0:
                ax.text((a.real+b.real)/2, .032, str(j), ha="center", fontsize=10, color=colors[j])
            else:
                offset = [(0, -.025), (.025, 0), (0, .025), (-.025, 0), (0, -.025)][j]
                ax.text((a.real+b.real)/2+offset[0], (a.imag+b.imag)/2+offset[1],
                        str(j), ha="center", va="center", color=colors[j])
        ax.scatter([exact.real], [exact.imag], marker="*", s=135, color="#111111", zorder=5)
        ax.axhline(0, color="#b7c0c8", lw=.8)
        ax.axvline(0, color="#b7c0c8", lw=.8)
        ax.set_xlabel(r"Real part of $E_{\rm out}/E_{\rm in}$")
        ax.set_ylabel("Imaginary part")
        if row == 0:
            ax.set(xlim=(-.03, 1.08), ylim=(-.05, .09), yticks=[0])
            ax.set_title(r"$R=0.75,\ \delta=0$: all terms reinforce", fontsize=11)
            ax.text(.99, -.034, "Infinite sum = 1", ha="right", fontsize=10)
        else:
            ax.set(xlim=(-.02, .32), ylim=(-.04, .28), aspect="equal")
            ax.set_title(r"$R=0.75,\ \delta=\pi/2$: directions rotate", fontsize=11)
            ax.text(.005, .25, "Infinite sum = 0.16 + 0.12i", fontsize=10)
    fig.subplots_adjust(left=.035, right=.975, bottom=.14, top=.86)
    fig.suptitle("Fabry–Pérot transmission: add amplitudes before squaring", fontsize=16, y=.965)
    fig.text(.5, .035, r"Terms $E_j/E_{\rm in}=(1-R)R^j e^{ij\delta}$; arrows 0–4 shown, stars mark the infinite sums.",
             ha="center", fontsize=11)
    fig.savefig(Path.cwd()/(Path(__file__).stem+".png"), dpi=100, transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
