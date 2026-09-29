"""Generate chromatic-aberration-focal-split.png in the working directory.

Run from _media with Python 3.14.4, matplotlib 3.10.7, numpy 2.3.5.
Original paraxial ray diagram; synthetic dispersion, not measured glass.
All rays use Phi(q) = 5 * (1 + q/60) D, q = -0.5, 0, +0.5.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import numpy as np


def main():
    phi_d, abbe, height = 5.0, 60.0, 0.008
    colours = [(-0.5, "Red", "#bd383b", "--"),
               (0.0, "Reference", "#37764a", ":"),
               (0.5, "Blue", "#2166b1", "-")]
    foci = {name: 1 / (phi_d * (1 + q / abbe))
            for q, name, _, _ in colours}
    assert np.allclose([foci["Red"], foci["Reference"], foci["Blue"]],
                       [24 / 119, 1 / 5, 24 / 121], rtol=0, atol=1e-15)
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.facecolor": "white", "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, (ax, zoom) = plt.subplots(1, 2, figsize=(10.8, 5.4), dpi=110,
                                   gridspec_kw={"width_ratios": [1.15, 1]})
    fig.subplots_adjust(left=.075, right=.975, bottom=.25, top=.78, wspace=.32)
    incoming = np.linspace(-0.04, 0, 40)
    outgoing = np.linspace(0, .216, 300)
    detail = np.linspace(.1974, .2026, 200)
    for axis in (ax, zoom):
        axis.axhline(0, color="0.4", lw=1)
        axis.grid(alpha=.16)
    ax.add_patch(Ellipse((0, 0), 5, 19, facecolor="#e7f0f8",
                         edgecolor="#63829a", lw=1.5))
    for sign in (-1, 1):
        ax.plot(incoming * 1000, np.full_like(incoming, sign * height * 1000),
                color="0.45", lw=1.8)
        ax.annotate("", xy=(-10, sign * height * 1000),
                    xytext=(-29, sign * height * 1000),
                    arrowprops={"arrowstyle": "->", "color": "0.45", "lw": 1.8})
    for q, name, colour, style in colours:
        focal = foci[name]
        for sign in (-1, 1):
            ray = lambda x: sign * height * (1 - x / focal)
            assert abs(ray(focal)) < 1e-15
            ax.plot(outgoing * 1000, ray(outgoing) * 1000,
                    color=colour, linestyle=style, lw=1.8)
            zoom.plot(detail * 1000, ray(detail) * 1e6,
                      color=colour, linestyle=style, lw=2,
                      label=name if sign == 1 else None)
            ax.annotate("", xy=(100, ray(.1) * 1000),
                        xytext=(75, ray(.075) * 1000),
                        arrowprops={"arrowstyle": "->", "color": colour, "lw": 1.3})
        ax.scatter(focal * 1000, 0, s=25, color=colour, zorder=6)
        zoom.scatter(focal * 1000, 0, s=40, color=colour, zorder=6)
        # Two upper labels and one lower label keep the three foci legible.
        label_y = -144 if name == "Reference" else 134
        label_x = {"Blue": 198.2, "Reference": 200.0, "Red": 201.8}[name]
        zoom.annotate(f"{name}\n{focal * 1000:.3f} mm",
                      xy=(focal * 1000, 0), xytext=(label_x, label_y),
                      ha="center", va="center", color=colour, fontsize=10,
                      bbox={"facecolor": "white", "edgecolor": "none", "pad": 2},
                      arrowprops={"arrowstyle": "->", "color": colour, "lw": 1.2},
                      zorder=8)
    ax.text(4, 9.6, "Lens at x = 0", fontsize=10, color="#456b84")
    ax.text(80, -8.3, "Optical axis", fontsize=10, color="0.35")
    ax.set(xlim=(-42, 220), ylim=(-10.6, 11.2),
           xticks=[0, 50, 100, 150, 200], xlabel="Position x (mm)",
           ylabel="Ray height (mm)", title="Parallel rays converge at different distances")
    zoom.set(xlim=(197.4, 202.6), ylim=(-190, 190),
             xticks=[198, 199, 200, 201, 202], xlabel="Position x (mm)",
             ylabel="Ray height (µm)", title="Enlarged view of the three foci")
    fig.suptitle("Chromatic aberration: blue focuses before red", fontsize=16, y=.965)
    fig.text(.5, .867, r"Single lens: $\Phi_d = 5$ D, $V_d = 60$;  $\Phi(q)=5(1+q/60)$ D", ha="center", fontsize=12)
    handles, labels = zoom.get_legend_handles_labels()
    fig.legend(handles, labels, loc="lower center", bbox_to_anchor=(.5, .11),
               ncol=3, frameon=False)
    fig.text(.5, .074, "Toy dispersion, not measured glass. q = −0.5 red, 0 reference, +0.5 blue.",
             ha="center", fontsize=10)
    fig.text(.5, .027, "Ideal thin lens in air. Vertical scales enlarged; arrows show propagation to the right.",
             ha="center", fontsize=10)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
