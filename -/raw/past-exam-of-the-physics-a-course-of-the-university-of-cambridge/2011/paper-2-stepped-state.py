"""Original matched fourth eigenstate; Python 3.14, NumPy, Matplotlib.

Dimensionless illustrative model, not reconstructed source-image data.
Output is a basename in the current working directory.
"""
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def propagate(v, energy, potential, length):
    q = energy - potential
    if abs(q) < 1e-12:
        return np.array([v[0] + length * v[1], v[1]])
    if q > 0:
        k = np.sqrt(q)
        c, s = np.cos(k * length), np.sin(k * length)
        return np.array([c * v[0] + s * v[1] / k,
                         -k * s * v[0] + c * v[1]])
    k = np.sqrt(-q)
    c, s = np.cosh(k * length), np.sinh(k * length)
    return np.array([c * v[0] + s * v[1] / k,
                     k * s * v[0] + c * v[1]])


def boundary(energy, odd):
    v = np.array([0., 1.]) if odd else np.array([1., 0.])
    v = propagate(v, energy, 0., 1.)
    v = propagate(v, energy, 5., 1.)
    return v[1] + np.sqrt(18. - energy) * v[0]


def levels():
    roots = []
    for odd in (False, True):
        grid = np.linspace(.00001, 17.99999, 3001)
        for lo, hi in zip(grid[:-1], grid[1:]):
            if boundary(lo, odd) * boundary(hi, odd) < 0:
                for _ in range(50):
                    mid = (lo + hi) / 2
                    if boundary(lo, odd) * boundary(mid, odd) <= 0:
                        hi = mid
                    else:
                        lo = mid
                roots.append(((lo + hi) / 2, odd))
    return sorted(roots)


def state(x, energy, odd):
    q = abs(x)
    start = np.array([0., 1.]) if odd else np.array([1., 0.])
    at_one = propagate(start, energy, 0., 1.)
    at_two = propagate(at_one, energy, 5., 1.)
    if q <= 1:
        val = propagate(start, energy, 0., q)[0]
    elif q <= 2:
        val = propagate(at_one, energy, 5., q - 1)[0]
    else:
        val = at_two[0] * np.exp(-np.sqrt(18. - energy) * (q - 2))
    return -val if odd and x < 0 else val


def main():
    spectrum = levels()
    energy, odd = spectrum[3]
    assert odd and 5 < energy < 18
    x = np.linspace(-3.5, 3.5, 2801)
    psi = np.array([state(t, energy, odd) for t in x])
    psi /= np.max(abs(psi))
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    fig, (ax, bx) = plt.subplots(2, 1, figsize=(8.2, 5.7), sharex=True,
                               gridspec_kw={"height_ratios": [1, 1.6]})
    xx = [-3.5, -2, -2, -1, -1, 1, 1, 2, 2, 3.5]
    vv = [18, 18, 5, 5, 0, 0, 5, 5, 18, 18]
    ax.plot(xx, vv, color="#64748b", lw=2)
    ax.axhline(energy, color="#d97706", ls="--", label="Fourth energy")
    ax.set_ylabel("Illustrative potential")
    ax.set_yticks([0, 5, 18])
    ax.legend(loc="upper center", frameon=False)
    bx.plot(x, psi, color="#175baa", lw=2.2)
    bx.axhline(0, color=".5", lw=.7)
    for a, b in [(-3.5, -2), (2, 3.5)]:
        bx.axvspan(a, b, color="#e2e8f0", alpha=.8)
    for a in [-2, -1, 1, 2]:
        bx.axvline(a, color=".6", ls=":", lw=.8)
    zeros = []
    for i in np.where(psi[:-1] * psi[1:] < 0)[0]:
        zeros.append(x[i] - psi[i] * (x[i+1]-x[i])/(psi[i+1]-psi[i]))
    zeros.append(0.)
    bx.scatter(zeros, np.zeros(len(zeros)), color="#b91c1c", zorder=4, s=28)
    bx.text(0, 1.12, "Odd parity; three nodes", ha="center")
    bx.set_ylim(-1.25, 1.35)
    bx.set_ylabel(r"$\psi$ (arbitrary scale)")
    bx.set_xlabel("Position (arbitrary length units)")
    bx.set_yticks([-1, 0, 1])
    bx.text(-2.75, -.95, "Decaying tail", ha="center", fontsize=9)
    bx.text(2.75, .95, "Decaying tail", ha="center", fontsize=9)
    fig.suptitle("A matched bound state in an illustrative stepped well")
    fig.tight_layout()
    fig.savefig("paper-2-stepped-state.png", dpi=160, facecolor="white")
    print(json.dumps({"levels": spectrum, "fourth_energy": energy,
                      "odd": odd, "nodes": zeros,
                      "boundary_residual": boundary(energy, odd)}))


if __name__ == "__main__":
    main()
