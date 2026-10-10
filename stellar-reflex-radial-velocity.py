"""Write stellar-reflex-radial-velocity.png to the current working directory.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Circular two-body toy model with mass ratio 0.001 and RELATIVE speed 100 km/s.
The planet's barycentric speed is 99.9001 km/s; the star's is 99.9001 m/s.
Run from _media with MPLBACKEND=Agg and a writable MPLCONFIGDIR.
"""

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "savefig.facecolor": "white"})
    q = 0.001
    relative_speed = 100_000.0  # m/s; planet relative to star
    star_speed = q * relative_speed / (1 + q)
    star_radius = q / (1 + q)  # relative semi-major axis a = 1
    planet_radius = 1 / (1 + q)
    angle = np.linspace(0, 2 * np.pi, 600)
    time = np.linspace(0, 2, 801)
    fig, (orbit, rv) = plt.subplots(1, 2, figsize=(10, 5.7), facecolor="white",
                                  gridspec_kw={"width_ratios": [1, 1.25]})
    fig.subplots_adjust(left=0.055, right=0.97, top=0.76, bottom=0.20, wspace=0.34)
    fig.suptitle("An unseen planet makes its star move", fontsize=18, y=0.97)
    fig.text(0.5, 0.90, r"Circular orbit: $M_p/M_\star=0.001$, relative speed $V_{\rm rel}=100$ km/s",
             ha="center", fontsize=13)
    fig.text(0.5, 0.845, r"Star speed $V_\star=99.9001$ m/s; planet speed $V_p=99.9001$ km/s",
             ha="center", fontsize=12)

    orbit.plot(planet_radius * np.cos(angle), planet_radius * np.sin(angle),
               color="#2368ac", lw=1.8)
    orbit.plot(star_radius * np.cos(angle), star_radius * np.sin(angle),
               color="#b46b11", lw=2)
    orbit.scatter([0], [0], marker="+", color="black", s=95, zorder=5)
    orbit.scatter([planet_radius], [0], color="#2368ac", s=65, zorder=4)
    orbit.scatter([-star_radius], [0], color="#b46b11", s=40, zorder=3)
    orbit.annotate("Planet", xy=(planet_radius, 0), xytext=(0.57, 0.36),
                   arrowprops={"arrowstyle": "->", "color": "#2368ac"}, color="#2368ac")
    orbit.text(-0.86, -0.40, "Barycentre (+)\nStar orbit tiny here", fontsize=11)
    orbit.annotate("", xy=(0, 0), xytext=(-0.35, -0.28),
                   arrowprops={"arrowstyle": "->", "color": "#555555"})
    orbit.set(aspect="equal", xlim=(-1.23, 1.23), ylim=(-1.23, 1.23))
    orbit.set_title("A. View along orbital normal", fontsize=12, pad=10)
    orbit.axis("off")

    inset = orbit.inset_axes([0.00, 0.59, 0.35, 0.35])
    inset.set_facecolor("white")
    inset.plot(star_radius * np.cos(angle), star_radius * np.sin(angle), color="#b46b11", lw=1.8)
    inset.scatter([0], [0], marker="+", color="black", s=55)
    inset.scatter([-star_radius], [0], color="#b46b11", s=35)
    inset.set(aspect="equal", xlim=(-0.00135, 0.00135), ylim=(-0.00135, 0.00135),
              xticks=[], yticks=[])
    inset.set_title("Star orbit (detail)", fontsize=9, pad=5)
    orbit.text(0.02, 0.52, r"$a_\star/a=0.000999$", transform=orbit.transAxes, fontsize=10)

    colors = ["#2368ac", "#bc5a18", "#777777"]
    for inclination, color, style in zip([90, 30, 0], colors, ["-", "--", ":"]):
        amplitude = star_speed * np.sin(np.deg2rad(inclination))
        rv.plot(time, amplitude * np.sin(2 * np.pi * time), color=color, lw=2.5, ls=style,
                label=rf"$i={inclination}^\circ$: $K={amplitude:.2f}$ m/s")
    rv.set(title=r"B. Line-of-sight signal: $K=V_\star\sin i$",
           xlabel=r"Time / orbital period $t/P$",
           ylabel=r"Stellar velocity $v_r-\gamma$ (m/s)",
           xlim=(0, 2), ylim=(-125, 170), yticks=[-100, -50, 0, 50, 100])
    rv.set_xticks([0, 0.5, 1, 1.5, 2])
    rv.legend(loc="upper right", fontsize=10, framealpha=1)
    rv.grid(alpha=0.20)
    rv.spines[["top", "right"]].set_visible(False)
    fig.text(0.5, 0.09, "Face-on: i = 0° gives no orbital Doppler signal; edge-on: i = 90° gives the full amplitude.",
             ha="center", fontsize=11)
    fig.text(0.5, 0.035, "Calculated toy system; marker sizes are symbolic. The inset magnifies only the star's orbit.",
             ha="center", fontsize=10)
    fig.savefig("stellar-reflex-radial-velocity.png", dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
