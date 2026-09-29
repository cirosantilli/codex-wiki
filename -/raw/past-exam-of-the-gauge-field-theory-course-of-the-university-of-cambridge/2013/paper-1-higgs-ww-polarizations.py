"""Tree-level on-shell partial widths divided by their common mass-cubic factor."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    ratio = np.linspace(2, 12, 700)
    x = 1/ratio**2
    beta = np.sqrt(1-4*x)
    longitudinal = beta*(1-2*x)**2
    transverse = beta*8*x*x
    total = beta*(1-4*x+12*x*x)
    assert np.max(np.abs(total-longitudinal-transverse)) < 1e-14
    fig, ax = plt.subplots(figsize=(8, 4.5), layout="constrained")
    ax.plot(ratio, total, color="black", lw=2, label="All polarizations")
    ax.plot(ratio, longitudinal, color="tab:blue", lw=2, label="Longitudinal pair")
    ax.plot(ratio, transverse, color="tab:orange", lw=2, label="Transverse sum")
    ax.set(xlabel=r"$m_H/m_W$", ylabel=r"$\Gamma\,/\,[G_Fm_H^3/(8\pi\sqrt{2})]$",
           title="On-shell W-pair decay: threshold and polarization contributions", xlim=(1.8, 12), ylim=(-.02, 1.05))
    ax.axvline(2, ls="--", color="0.6", lw=1)
    ax.legend(loc="lower right"); ax.grid(alpha=.2)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=130, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
