"""Fixed-sphere Rayleigh response; write an opaque PNG to the current directory.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Assume a fixed, real, nondispersive refractive index and ka << 1 throughout.
The normalized response is independent of the chosen sphere radius and index.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    wavelength_nm = np.linspace(350.0, 750.0, 801)
    response = (650.0 / wavelength_nm) ** 4
    blue_response = (650.0 / 450.0) ** 4
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    fig, ax = plt.subplots(figsize=(9.0, 5.4), dpi=100)
    ax.plot(wavelength_nm, response, color="#34495e", linewidth=2.5)
    for wavelength, value, color in [
        (450.0, blue_response, "#2166ac"), (650.0, 1.0, "#b2182b")
    ]:
        ax.vlines(wavelength, 0, value, color=color, linestyles="--", linewidth=1.4)
        ax.scatter([wavelength], [value], color=color, s=70, zorder=3)
    ax.annotate("Blue: 450 nm\nRelative response = 4.353", (450, blue_response),
                xytext=(478, 7.0), color="#2166ac", fontsize=12,
                arrowprops={"arrowstyle": "->", "color": "#2166ac"})
    ax.annotate("Red: 650 nm\nRelative response = 1", (650, 1),
                xytext=(566, 3.2), color="#b2182b", fontsize=12,
                arrowprops={"arrowstyle": "->", "color": "#b2182b"})
    ax.set(xlim=(350, 750), ylim=(0, 13),
           xlabel=r"Wavelength $\lambda$ (nm)",
           ylabel=r"Relative cross-section $\sigma(\lambda)/\sigma(650\,\mathrm{nm})$")
    ax.set_xticks(np.arange(350, 751, 50))
    ax.grid(alpha=0.23)
    ax.set_title(r"Rayleigh scattering: $(650\,\mathrm{nm}/\lambda)^4$",
                 fontsize=16, pad=13)
    fig.text(0.5, 0.035,
             "Fixed small sphere; fixed real refractive index; ka ≪ 1 at every wavelength",
             ha="center", fontsize=11)
    fig.subplots_adjust(left=0.105, right=0.975, top=0.87, bottom=0.18)
    fig.savefig(Path.cwd() / "rayleigh-wavelength-scaling.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
