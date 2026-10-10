"""Original stipulated heat balance; run from _media to create matching CWD PNG.

Tested with Python 3.14.4, Matplotlib 3.10.7 and NumPy 2.3.5.
All powers and temperatures are chosen model values, not device measurements.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def main():
    dark, light, absorptance = 2.0, 1.005, 0.995
    absorbed = dark - light
    incident = absorbed / absorptance
    escaped = incident - absorbed
    conductance, temperature, reference = 5.0, 5.4, 5.0
    assert abs(incident - 1.0) < 1e-12
    assert abs(conductance * (temperature - reference) - dark) < 1e-12
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
    fig, (ax, note) = plt.subplots(1, 2, figsize=(9.6, 5.1), dpi=120,
                                  facecolor="white", gridspec_kw={"width_ratios": [1.5, 1]})
    fig.subplots_adjust(left=0.085, right=0.975, top=0.79, bottom=0.14, wspace=0.28)
    orange, blue, green, ink = "#c76c1c", "#186d9b", "#197b61", "#243745"
    fig.suptitle("Dark / light balance at fixed receiver temperature", fontsize=16, color=ink, y=0.97)
    fig.text(0.5, 0.89, "STIPULATED MODEL — not measured device performance",
             ha="center", fontsize=11, color="#5a6b78")
    ax.bar([0, 1], [dark, light], width=0.56, color=orange)
    ax.bar(1, absorbed, bottom=light, width=0.56, color=blue)
    ax.text(0, dark / 2, "Heater\n2.000 mW", ha="center", va="center", color="white", fontsize=12)
    ax.text(1, light / 2, "Heater\n1.005 mW", ha="center", va="center", color="white", fontsize=12)
    ax.text(1, light + absorbed / 2, "Absorbed light\n0.995 mW", ha="center", va="center", color="white", fontsize=11)
    ax.axhline(dark, color=green, lw=1.6, linestyle="--")
    ax.text(-0.48, 2.11, "Outward heat flow: 2.000 mW in either state", fontsize=10, color=green)
    ax.set(xticks=[0, 1], xticklabels=["Dark\nbeam blocked", "Light\nbeam admitted"],
           ylabel="Power deposited in receiver (mW)", ylim=(0, 2.32), xlim=(-0.65, 1.65))
    ax.set_yticks([0, 0.5, 1, 1.5, 2])
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(axis="y", color="#e5eaed", linewidth=0.7)
    ax.set_axisbelow(True)
    note.axis("off")
    note.set(xlim=(0, 1), ylim=(0, 1))
    note.text(0.0, 0.97, "Same thermal operating point", color=ink, weight="bold")
    note.text(0.0, 0.84, r"$T=5.4\ \mathrm{K},\quad T_b=5.0\ \mathrm{K}$", color=ink)
    note.text(0.0, 0.74, r"$G=5\ \mathrm{mW\,K^{-1}}$", color=ink)
    note.text(0.0, 0.62, "Incident light: 1.000 mW\nAbsorptance: 0.995", color=blue, linespacing=1.7)
    note.text(0.0, 0.44, f"Absorbed: {absorbed:.3f} mW\nEscapes: {escaped:.3f} mW (not heat)",
              color=blue, linespacing=1.7)
    note.text(0.0, 0.23, r"$P_{\mathrm{in}}=\dfrac{2.000-1.005}{0.995}=1.000\ \mathrm{mW}$", color=ink, fontsize=12)
    note.text(0.0, 0.04, "Zero parasitic-input change;\nperfect thermal equivalence stipulated.",
              color="#5a6b78", fontsize=10)
    destination = Path.cwd() / (Path(__file__).stem + ".png")
    fig.savefig(destination, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
