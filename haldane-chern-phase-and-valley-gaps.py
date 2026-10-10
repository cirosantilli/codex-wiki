"""Original Haldane-model phase diagram and valley gaps.

Run from _media; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
The sign convention is A=i<u|du>, kx,ky positively oriented, lower band.
No experimental data are used. --check performs independent lattice checks.
"""

import argparse
import json
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, BoundaryNorm
import numpy as np


DELTA = np.array([[0.0, 1.0], [np.sqrt(3) / 2, -0.5],
                  [-np.sqrt(3) / 2, -0.5]])
BONDS = np.array([DELTA[2] - DELTA[1], DELTA[0] - DELTA[2],
                  DELTA[1] - DELTA[0]])
CELL = np.array([DELTA[2] - DELTA[0], DELTA[1] - DELTA[0]])
RECIPROCAL = 2 * np.pi * np.linalg.inv(CELL).T


def lattice_d(k, mass, t2, phi):
    """Embedding gauge, bond length=t1=1; analytic k derivatives."""
    kd = np.einsum("...i,ji->...j", k, DELTA)
    kb = np.einsum("...i,ji->...j", k, BONDS)
    d = np.stack([-np.cos(kd).sum(-1), np.sin(kd).sum(-1),
                  mass - 2 * t2 * np.sin(phi) * np.sin(kb).sum(-1)], -1)
    deriv = []
    for axis in (0, 1):
        deriv.append(np.stack([
            (np.sin(kd) * DELTA[:, axis]).sum(-1),
            (np.cos(kd) * DELTA[:, axis]).sum(-1),
            -2 * t2 * np.sin(phi) * (np.cos(kb) * BONDS[:, axis]).sum(-1)
        ], -1))
    return d, deriv[0], deriv[1]


def curvature(k, mass, t2, phi):
    d, dx, dy = lattice_d(k, mass, t2, phi)
    return np.einsum("...i,...i->...", d, np.cross(dx, dy)) / (
        2 * np.linalg.norm(d, axis=-1) ** 3)


def chern_grid(n, mass, t2, phi):
    """Eigenvector link-variable check in a strictly periodic cell gauge.

    Overlaps have phase -A.dk, hence the minus sign before the plaquette sum.
    Exact valley masses reject singular parameters even if the mesh misses K.
    """
    mh = 3 * np.sqrt(3) * t2 * np.sin(phi)
    if min(abs(mass - mh), abs(mass + mh)) < 1e-10:
        raise ValueError("Chern number undefined at a band touching")
    u, v = np.meshgrid(2 * np.pi * np.arange(n) / n,
                       2 * np.pi * np.arange(n) / n, indexing="ij")
    f = 1 + np.exp(1j * u) + np.exp(1j * v)
    dz = mass - 2 * t2 * np.sin(phi) * (np.sin(u - v) - np.sin(u) + np.sin(v))
    h = np.zeros((n, n, 2, 2), dtype=complex)
    h[..., 0, 0], h[..., 1, 1] = dz, -dz
    h[..., 0, 1], h[..., 1, 0] = -f, -f.conj()
    energies, states = np.linalg.eigh(h)
    lower = states[..., 0]
    links = []
    for axis in (0, 1):
        z = np.sum(lower.conj() * np.roll(lower, -1, axis=axis), axis=-1)
        if np.min(abs(z)) < 1e-10:
            raise ValueError("Unresolved mesh: vanishing eigenvector overlap")
        links.append(z / abs(z))
    x, y = links
    loop = x * np.roll(y, -1, axis=0) / (np.roll(x, -1, axis=1) * y)
    return float(-np.angle(loop).sum() / (2 * np.pi)), float(np.min(energies[..., 1] - energies[..., 0]))


def checks():
    results = []
    for mass, t2, phi in [(0, .08, np.pi / 2), (0, .08, -np.pi / 2),
                          (.7, .08, np.pi / 2), (-.7, .08, np.pi / 2),
                          (.4, 0, 0), (.12, .08, .7), (.5, .08, .7)]:
        mh = 3 * np.sqrt(3) * t2 * np.sin(phi)
        expected = (np.sign(mass - mh) - np.sign(mass + mh)) / 2
        row = {"M": mass, "t2": t2, "phi": phi, "mass_formula_C": float(expected), "grids": []}
        for n in (31, 61, 121):
            c, gap = chern_grid(n, mass, t2, phi)
            assert abs(c - expected) < 1e-10
            row["grids"].append({"n": n, "C": c, "sampled_direct_gap": gap})
        n = 240
        s, t = np.meshgrid((np.arange(n) + .5) / n,
                           (np.arange(n) + .5) / n, indexing="ij")
        k = s[..., None] * RECIPROCAL[0] + t[..., None] * RECIPROCAL[1]
        integrated = curvature(k, mass, t2, phi).mean() * np.linalg.det(RECIPROCAL) / (2 * np.pi)
        assert abs(integrated - expected) < 2e-6
        row["analytic_curvature_integral"] = float(integrated)
        results.append(row)
    kplus = np.array([4 * np.pi / (3 * np.sqrt(3)), 0.])
    for tau in (-1, 1):
        d, dx, dy = lattice_d(tau * kplus, .12, .08, .7)
        assert np.linalg.norm(d[:2]) < 1e-14
        assert abs(d[2] - (.12 - tau * 3 * np.sqrt(3) * .08 * np.sin(.7))) < 1e-14
        np.testing.assert_allclose(dx[:2], [tau * 1.5, 0], atol=1e-14)
        np.testing.assert_allclose(dy[:2], [0, 1.5], atol=1e-14)
    singular = []
    for mass, phi in [(0, 0), (3 * np.sqrt(3) * .08, np.pi / 2),
                      (-3 * np.sqrt(3) * .08, np.pi / 2)]:
        try:
            chern_grid(31, mass, .08, phi)
        except ValueError:
            singular.append({"M": mass, "phi": phi, "excluded": True})
        else:
            raise AssertionError("A singular point was assigned a Chern number")
    return {"cases": results, "singular_points": singular,
            "valley_linearizations": "passed", "orientation_determinant": float(np.linalg.det(RECIPROCAL))}


def draw():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white", "axes.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(10.4, 4.4), layout="constrained", gridspec_kw={"width_ratios": [1.35, 1]})
    phi = np.linspace(-np.pi, np.pi, 1001)
    y = np.linspace(-1.5, 1.5, 601)
    p, m = np.meshgrid(phi, y)
    c = (np.sign(m - np.sin(p)) - np.sign(m + np.sin(p))) / 2
    c = np.ma.masked_where(np.minimum(abs(m - np.sin(p)), abs(m + np.sin(p))) < .012, c)
    cmap = ListedColormap(["#336ca4", "#eeeeea", "#c95842"])
    axes[0].pcolormesh(phi, y, c, cmap=cmap, norm=BoundaryNorm([-1.5, -.5, .5, 1.5], 3), shading="auto", rasterized=True)
    axes[0].plot(phi, np.sin(phi), "k", lw=1.2)
    axes[0].plot(phi, -np.sin(phi), "k", lw=1.2)
    for x, yy, label, color in [(-np.pi / 2, 0, "$C=+1$", "white"), (np.pi / 2, 0, "$C=-1$", "white"), (0, 1.23, "$C=0$", "black"), (0, -1.23, "$C=0$", "black")]:
        axes[0].text(x, yy, label, color=color, ha="center", va="center", fontsize=13)
    axes[0].set(xticks=[-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi], xticklabels=[r"$-\pi$", r"$-\pi/2$", "$0$", r"$\pi/2$", r"$\pi$"], xlabel=r"Hopping phase $\phi$", ylabel=r"$M/(3\sqrt{3}t_2)$", title="Lower-band Chern number")
    axes[0].text(.5, -.26, "Black curves: band touching; C undefined", transform=axes[0].transAxes, ha="center", fontsize=10)
    x = np.linspace(-1.5, 1.5, 601)
    axes[1].axvspan(-1, 1, color="#e9eff7")
    axes[1].plot(x, abs(x - 1), color="#2475a9", lw=2.2, label=r"$\Delta_+=2|m_+|$")
    axes[1].plot(x, abs(x + 1), color="#bc5540", lw=2.2, label=r"$\Delta_-=2|m_-|$")
    axes[1].scatter([-1, 1], [0, 0], color="black", s=28, zorder=5)
    axes[1].set(xlim=(-1.5, 1.5), ylim=(-.05, 2.65), xlabel=r"$M/(3\sqrt{3}t_2)$", ylabel=r"Valley gap / $(6\sqrt{3}t_2)$", title=r"Valley gaps at $\phi=\pi/2$")
    axes[1].legend(loc="upper center", frameon=True)
    axes[1].text(0, .20, "$C=-1$", ha="center", color="#234965")
    axes[1].grid(alpha=.18)
    fig.suptitle(r"Haldane model: different gapped phases, $t_2/t_1=0.08$", fontsize=14)
    fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if args.check:
        print(json.dumps(checks(), indent=2))
    else:
        draw()
