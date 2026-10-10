"""Generate hubble-law-and-redshift.png in the current directory.

Use: make _media/hubble-law-and-redshift.png
Tested with Python 3.14.4, Matplotlib 3.10.7, NumPy 2.3.5.
H0 = 70 km/s/Mpc is stipulated, not fitted or a measured consensus value.
The left panel calculates instantaneous recession rates and low-z estimates;
the right panel independently illustrates wavelength doubling, not velocity.
"""

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "savefig.facecolor": "white"})
    hubble, c = 70.0, 299792.458
    distances = np.array([10.0, 100.0, 200.0])
    rates = hubble * distances
    approx_z = rates / c
    fig, (left, right) = plt.subplots(1, 2, figsize=(10.8, 5.4), facecolor="white")
    fig.subplots_adjust(left=0.085, right=0.975, bottom=0.19, top=0.79, wspace=0.35)
    fig.suptitle("Expansion rates and wavelength stretching", fontsize=19, y=0.975)
    fig.text(0.5, 0.906, "Computed illustrations: no observed galaxy catalogue", ha="center", fontsize=12)
    left.set_title(r"Local example: stipulated $H_0=70$ km/s/Mpc", fontsize=12, pad=14)
    line_distance = np.linspace(0, 220, 221)
    left.plot(line_distance, hubble * line_distance, color="#286b96", lw=2.5)
    left.scatter(distances, rates, s=55, color="#bf5928", zorder=4)
    for distance, rate, z, offset in zip(distances, rates, approx_z,
                                        ((14, 12), (10, -44), (-100, -45))):
        left.annotate(f"{rate:,.0f} km/s\n" + rf"$z\approx {z:.6f}$",
                      xy=(distance, rate), xytext=offset, textcoords="offset points",
                      fontsize=11, color="#833e1c",
                      bbox={"facecolor": "white", "edgecolor": "none", "pad": 2})
    left.set(xlim=(0, 225), ylim=(0, 16600), xticks=[0, 50, 100, 150, 200],
             yticks=[0, 4000, 8000, 12000, 16000],
             xlabel="Present proper distance d (Mpc)",
             ylabel=r"Instantaneous recession rate $H_0d$ (km/s)")
    left.grid(alpha=0.2)
    left.spines[["top", "right"]].set_visible(False)
    left.text(0.03, 0.95, r"$z\approx H_0d/c$ only at low redshift", transform=left.transAxes,
              va="top", fontsize=11)

    right.set_title(r"Scale factor doubles: $a_e=0.5\ \to\ a_0=1$", fontsize=12, pad=14)
    position = np.linspace(0, 2300, 1600)
    for baseline, wavelength, color, label in (
            (2.1, 500, "#286b96", r"Emitted: $\lambda_e=500$ nm"),
            (0.6, 1000, "#bf5928", r"Received: $\lambda_0=1000$ nm")):
        right.axhline(baseline, color="#ccd3da", lw=0.8)
        right.plot(position, baseline + 0.3 * np.cos(2 * np.pi * position / wavelength),
                   lw=2.5, color=color)
        right.text(0, baseline + 0.52, label, fontsize=12, color=color)
        # Consecutive crests have exactly the labelled wavelength separation.
        right.annotate("", xy=(1500 if wavelength == 500 else 2000, baseline - 0.52),
                       xytext=(1000, baseline - 0.52),
                       arrowprops={"arrowstyle": "<->", "color": color, "lw": 1.6})
        right.text(1250 if wavelength == 500 else 1500, baseline - 0.74,
                   f"{wavelength} nm", ha="center", color=color, fontsize=11)
    right.set(xlim=(-50, 2350), ylim=(-0.6, 3.1))
    right.axis("off")
    right.text(0.5, -0.10, r"$1+z=\lambda_0/\lambda_e=2$, so $z=1$",
               transform=right.transAxes, ha="center", fontsize=13)
    fig.text(0.5, 0.055, "Left: redshift estimates are approximate. Right: wavelength diagram is schematic; z = 1 is not a speed.",
             ha="center", fontsize=11)
    fig.savefig("hubble-law-and-redshift.png", dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
