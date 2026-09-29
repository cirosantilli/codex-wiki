"""Original array geometry and sinc attenuation for an off-axis point source."""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np


def main():
    c = 299792458.
    angle = 10*np.pi/(180*60)
    fig, axes = plt.subplots(1, 2, figsize=(9, 4.1), layout="constrained")
    for x in [0, 6, 12, 18]:
        for y in [0, 6, 12, 18]:
            axes[0].add_patch(Circle((x, y), 2, facecolor="#dcebf5", edgecolor="0.3"))
    axes[0].plot([0, 18], [0, 18], color="tab:red", lw=2)
    axes[0].text(5.4, 10.5, r"$18\sqrt{2}$ m", rotation=45, color="tab:red", fontsize=10)
    axes[0].annotate("", (0, -3), (18, -3), arrowprops={"arrowstyle": "<->"})
    axes[0].text(9, -3.4, "18 m center spacing", ha="center", va="top", fontsize=9)
    axes[0].set(xlim=(-3, 21), ylim=(-5, 21), aspect="equal", xlabel="Position (m)",
                ylabel="Position (m)", title="4 × 4 array, 4 m dishes")
    bandwidth = np.linspace(0, 6, 601)
    for baseline in [18, 18*np.sqrt(2)]:
        attenuation = np.sinc(bandwidth*1e9*baseline*angle/c)
        axes[1].plot(bandwidth, attenuation, label=fr"Projected baseline {baseline:.1f} m")
    axes[1].axhline(.9, color="0.5", ls=":", label="10% loss criterion")
    axes[1].axhline(0, color="0.6", lw=1)
    axes[1].annotate("First null:\nresponse vanishes", (4.0486, 0), (2.8, -.38),
                     arrowprops={"arrowstyle": "->", "color": "0.4"}, fontsize=9)
    axes[1].set(xlabel="Averaged top-hat bandwidth (GHz)", ylabel="Signed fringe attenuation",
                title="10 arcminute offset, maximum projection", ylim=(-.45, 1.08))
    axes[1].legend(fontsize=8.5, loc="upper right")
    axes[1].grid(alpha=.18)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=130, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
