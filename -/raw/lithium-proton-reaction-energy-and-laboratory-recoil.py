"""Original two-body reaction calculation; Python 3.14, matplotlib 3.10.7.

NIST neutral-atom masses: https://physics.nist.gov/cgi-bin/Compositions/stand_alone.pl?ascii=ascii2
Conversion and electron rest energy: https://www.physics.nist.gov/cuu/pdf/wall_2022.pdf
Subtract electron rest masses; electronic binding corrections are neglected.
Chosen stationary target, T=0.500 MeV, no material losses. Not historical data.
Run from _media to emit this script's basename.png to CWD.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

U_MEV = 931.49410372
ELECTRON_MEV = 0.51099895069
M_H_U = 1.00782503223
M_LI_U = 7.0160034366
M_HE_U = 4.00260325413


def reaction(incident_mev=0.500):
    """Return energies in MeV and momenta times c in MeV."""
    a = M_H_U * U_MEV - ELECTRON_MEV
    b = M_LI_U * U_MEV - 3 * ELECTRON_MEV
    h = M_HE_U * U_MEV - 2 * ELECTRON_MEV
    q = (M_LI_U + M_H_U - 2 * M_HE_U) * U_MEV
    p = np.sqrt(incident_mev * (incident_mev + 2 * a))
    w = np.sqrt((a + b)**2 + 2 * b * incident_mev)
    beta = p / (a + b + incident_mev)
    gamma = (a + b + incident_mev) / w
    e_star = w / 2
    p_star = np.sqrt((e_star - h) * (e_star + h))
    theta = np.linspace(0, np.pi, 361)
    k1 = gamma * (e_star + beta * p_star * np.cos(theta)) - h
    k2 = gamma * (e_star - beta * p_star * np.cos(theta)) - h
    return dict(a=a, b=b, h=h, q=q, p=p, w=w, beta=beta, gamma=gamma,
                e_star=e_star, p_star=p_star, theta=theta, k1=k1, k2=k2)


def main():
    d = reaction()
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    fig, (a, b) = plt.subplots(1, 2, figsize=(10, 6.2), gridspec_kw={"width_ratios": [1, 1.35]})
    fig.patch.set_facecolor("white")
    fig.suptitle("Lithium-7 + proton → two alpha particles", fontsize=16)
    a.bar([0], [d["q"]], width=.55, color="#237da5", label="Reaction Q")
    a.bar([0], [.5], bottom=[d["q"]], width=.55, color="#e7a441", label="Incident proton")
    a.axhline(d["q"] + .5, color="#526575", linestyle=":")
    a.text(.38, d["q"] + .5, f'{d["q"]+.5:.3f} MeV', va="bottom", ha="center")
    a.text(0, 8.6, f'Q\n{d["q"]:.3f}\nMeV', ha="center", color="white", fontsize=11)
    a.text(.38, 20.3, "Added beam energy:\n0.500 MeV", ha="center", fontsize=10)
    a.set(xlim=(-.7, 1.1), ylim=(0, 23), xticks=[], ylabel="Outgoing total kinetic energy (MeV)")
    a.set_title("Mass difference supplies most energy", fontsize=12)
    a.spines[["top", "right", "bottom"]].set_visible(False)
    a.legend(loc="upper center", bbox_to_anchor=(.5, -.22), fontsize=10)

    angle = np.degrees(d["theta"])
    b.plot(angle, d["k1"], color="#237da5", lw=2.5, label="Alpha 1")
    b.plot(angle, d["k2"], color="#a63d35", lw=2.5, label="Alpha 2 (paired event)")
    half = (d["q"] + .5) / 2
    b.axhline(half, color="#526575", ls=":", label="Half of laboratory total")
    b.scatter([90], [half], color="#29475c", zorder=4)
    b.text(90, half + .13, "Equal energies here", ha="center", fontsize=10)
    b.set(xlim=(0, 180), xticks=[0, 45, 90, 135, 180],
          xlabel=r"Center-of-mass emission angle $\theta_*$ (degrees)",
          ylabel="Laboratory kinetic energy (MeV)")
    b.set_title("Center-of-mass symmetry, laboratory asymmetry", fontsize=12)
    b.grid(alpha=.18)
    b.spines[["top", "right"]].set_visible(False)
    b.legend(loc="upper center", bbox_to_anchor=(.5, -.22), fontsize=9)
    fig.text(.5, .025, "Chosen T = 0.500 MeV • stationary target • electronic binding corrections and material losses neglected", ha="center", fontsize=9)
    fig.subplots_adjust(left=.08, right=.98, bottom=.29, top=.81, wspace=.45)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=130, facecolor="white")
    plt.close(fig)
    print({k: float(d[k]) for k in ("q", "beta", "gamma", "e_star", "p_star")})
    print("K endpoints MeV:", float(d["k1"][0]), float(d["k2"][0]), "midpoint:", half)


if __name__ == "__main__":
    main()
