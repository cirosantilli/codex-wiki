"""Original local Fermi-surface illustration; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Run from _media; the output is this script's basename with a .png suffix.
All curves are stipulated teaching models, not helium-3 data. Momentum is p,
not wavevector. E_u = p_F**2 / m; m_star / m = 2; Z = 0.65.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white"})
    fig, (occ, energy) = plt.subplots(1, 2, figsize=(10.4, 4.7), layout="constrained")
    x = np.linspace(-0.25, 0.25, 1201)
    z = 0.65
    xi = x / 2
    thermal = 1 / (1 + np.exp(xi / 0.015))
    occ.plot(x, thermal, color="#bb5a17", lw=2.5,
             label=r"Quasiparticles, $k_B T/E_u=0.015$")
    for side in [x[x < 0], x[x > 0]]:
        step = (side < 0).astype(float)
        occ.plot(side, step, color="#215e9c", lw=2.3,
                 label=r"Quasiparticles, $T=0$" if side[0] < 0 else None)
        n_particle = z * step + (1 - z) * (0.5 - 0.2 * np.tanh(2 * side))
        occ.plot(side, n_particle, color="#278576", lw=2.4, ls="--",
                 label=r"Particles, $T=0$: schematic $Z=0.65$" if side[0] < 0 else None)
    occ.annotate("", xy=(0, (1 + z) / 2), xytext=(0, (1 - z) / 2),
                 arrowprops={"arrowstyle": "<->", "color": "#278576", "lw": 1.8})
    occ.text(0.009, 0.58, r"Jump $Z$", color="#176b5e")
    occ.set(xlim=(-0.25, 0.25), ylim=(-0.025, 1.08), ylabel="Occupation per spin state",
            xlabel=r"$(p-p_F)/p_F$", title="A. Quasiparticle and particle occupations differ")
    occ.legend(loc="upper right", fontsize=8.3, bbox_to_anchor=(1, -0.18), frameon=False)
    energy.axvspan(-0.03, 0.03, color="#f4ce9e", alpha=0.55)
    energy.axhline(0, color="#9b9b9b", lw=0.8)
    energy.axvline(0, color="#9b9b9b", lw=0.8)
    energy.plot(x, x, color="#777777", lw=2, ls="--", label=r"Reference: $m^*=m$")
    energy.plot(x, xi, color="#215e9c", lw=2.6, label=r"Quasiparticles: $m^*=2m$")
    energy.scatter([-0.03, 0.03], [-0.015, 0.015], color="#bb5a17", zorder=4, s=24)
    energy.text(-0.235, 0.19, r"$\xi_p \simeq v_F(p-p_F)$" + "\n" + r"$v_F=p_F/m^*$")
    energy.text(0.04, -0.17, "Shaded shell:\n" + r"$|\xi_p|\leq k_B T$", color="#9b4a12")
    energy.set(xlim=(-0.25, 0.25), ylim=(-0.26, 0.26), ylabel=r"$(\epsilon_p-\mu)/E_u$",
               xlabel=r"$(p-p_F)/p_F$", title="B. A heavier excitation has a gentler slope")
    energy.legend(loc="upper right", fontsize=9, bbox_to_anchor=(1, -0.18), frameon=False)
    fig.suptitle(r"Low-energy Fermi liquid: $E_u=p_F^2/m$, $m^*/m=2$" + "\n"
                 "Local illustrative models; neither a global momentum distribution nor a helium fit",
                 fontsize=12.5)
    fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
