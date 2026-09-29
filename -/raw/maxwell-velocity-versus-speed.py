"""Compare a signed Maxwell velocity component with the three-dimensional speed.

Writes an opaque white PNG with this script's basename in the working directory.
Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    # Quadrature checks the component and speed laws, including their moments.
    w_check = np.linspace(-12.0, 12.0, 24001)
    phi_check = np.exp(-w_check**2 / 2) / np.sqrt(2 * np.pi)
    u_check = np.linspace(0.0, 12.0, 24001)
    h_check = np.sqrt(2 / np.pi) * u_check**2 * np.exp(-u_check**2 / 2)
    assert np.isclose(np.trapezoid(phi_check, w_check), 1.0, atol=1e-10, rtol=0)
    assert np.isclose(np.trapezoid(w_check * phi_check, w_check), 0.0,
                      atol=1e-10, rtol=0)
    assert np.isclose(np.trapezoid(w_check**2 * phi_check, w_check), 1.0,
                      atol=1e-10, rtol=0)
    expected = [1.0, np.sqrt(8 / np.pi), 3.0]
    for order, value in enumerate(expected):
        assert np.isclose(np.trapezoid(u_check**order * h_check, u_check),
                          value, atol=1e-10, rtol=0)
    vector_density = np.exp(-u_check**2 / 2) / (2 * np.pi)**1.5
    assert np.allclose(4 * np.pi * u_check**2 * vector_density, h_check)

    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white",
                         "axes.spines.top": False, "axes.spines.right": False})
    fig, axes = plt.subplots(1, 2, figsize=(9.0, 4.8), dpi=130)
    fig.subplots_adjust(left=0.08, right=0.97, bottom=0.25, top=0.72, wspace=0.27)
    fig.suptitle("Velocity component and speed have different peaks", y=0.98,
                 fontsize=15)
    fig.text(0.5, 0.90, r"Gas rest frame; $s=\sqrt{k_B T/m}$; each density has area 1",
             ha="center", fontsize=12)
    blue, orange = "#236a9e", "#bd5b25"
    w = np.linspace(-4.0, 4.0, 801)
    phi = np.exp(-w**2 / 2) / np.sqrt(2 * np.pi)
    left, right = axes
    left.plot(w, phi, color=blue, lw=2.6)
    left.fill_between(w, phi, color=blue, alpha=0.10)
    left.axvline(0, color=blue, ls="--", lw=1.0)
    left.scatter([0], [1 / np.sqrt(2 * np.pi)], color=blue, zorder=3)
    left.set(title=r"Signed component: $\phi(w)=e^{-w^2/2}/\sqrt{2\pi}$",
             xlabel=r"Component $w=v_x/s$", ylabel="Probability density",
             xlim=(-4, 4), ylim=(0, 0.49))
    left.text(0.5, 0.92, "Peak and mean: 0", ha="center", color=blue,
              transform=left.transAxes)
    u = np.linspace(0.0, 4.5, 901)
    h = np.sqrt(2 / np.pi) * u**2 * np.exp(-u**2 / 2)
    right.plot(u, h, color=orange, lw=2.6)
    right.fill_between(u, h, color=orange, alpha=0.10)
    peak = np.sqrt(2.0)
    peak_density = np.sqrt(2 / np.pi) * peak**2 * np.exp(-peak**2 / 2)
    right.axvline(peak, color=orange, ls="--", lw=1.0)
    right.scatter([peak], [peak_density], color=orange, zorder=3)
    right.set(title=r"Speed: $h(u)=\sqrt{2/\pi}\,u^2e^{-u^2/2}$",
              xlabel=r"Speed $u=v/s$", xlim=(0, 4.5), ylim=(0, 0.70))
    right.text(0.5, 0.92, r"Peak: $\sqrt{2}\approx1.414$", ha="center",
               color=orange, transform=right.transAxes)
    for ax in axes:
        ax.grid(axis="y", alpha=0.18)
    fig.text(0.5, 0.105, r"Speed groups all directions: shell volume $4\pi v^2\,dv$",
             ha="center", fontsize=12)
    fig.text(0.5, 0.045, "The vector density peaks at zero; multiplying by shell volume moves the speed peak.",
             ha="center", fontsize=10.5)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
