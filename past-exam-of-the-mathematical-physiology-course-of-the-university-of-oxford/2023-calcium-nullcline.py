"""Generate 2023-calcium-nullcline.png in the working directory.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
All roots use bisection; only NumPy and Matplotlib are required.
The orange cycle is the singular limiting cycle, not a finite-epsilon orbit.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

DELTA = 0.001
GAMMA = 0.01


def nullcline(u):
    u = np.asarray(u)
    low, high = np.zeros_like(u, dtype=float), np.full_like(u, 1 / DELTA, dtype=float)
    a, b = u*u / (1+u*u), u**4 / (1+u**4)
    for _ in range(65):
        middle = (low+high) / 2
        positive = a - b*middle**2/(1+middle**2) - DELTA*middle > 0
        low = np.where(positive, middle, low)
        high = np.where(positive, high, middle)
    return (low+high) / 2


def slope(u):
    v = nullcline(u)
    fu = 2*u/(1+u*u)**2 - 4*u**3/(1+u**4)**2 * v*v/(1+v*v)
    fv = -2*v/(1+v*v)**2 * u**4/(1+u**4) - DELTA
    return -fu/fv


def bisect(fn, low, high):
    assert fn(low) * fn(high) < 0
    sign = fn(low) > 0
    for _ in range(65):
        middle = (low+high) / 2
        if (fn(middle) > 0) == sign:
            low = middle
        else:
            high = middle
    return (low+high) / 2


def main():
    minus = bisect(lambda u: slope(u)+1/GAMMA, 0.59, 0.8)
    plus = bisect(lambda u: slope(u)+1/GAMMA, 0.95, 1.2)
    zm, zp = minus+GAMMA*nullcline(minus), plus+GAMMA*nullcline(plus)
    right = bisect(lambda u: u+GAMMA*nullcline(u)-zm, 1.2, 3)
    left = bisect(lambda u: u+GAMMA*nullcline(u)-zp, 0.05, 0.5)
    mu = (minus+plus) / 2
    fig, ax = plt.subplots(figsize=(8.4, 4.7), layout="constrained")
    fig.set_facecolor("white")
    uu = np.linspace(0, 2.3, 1800)
    ax.plot(uu, nullcline(uu), color="0.65", lw=2, label=r"$v=g(u)$")
    middle = uu[(uu >= minus) & (uu <= plus)]
    ax.plot(middle, nullcline(middle), color="#a92935", lw=2.7,
            label=r"repelling: $g'(u)<-1/\gamma$")
    orange = "#c85a17"
    ul = np.linspace(left, minus, 300)
    ur = np.linspace(right, plus, 450)
    ax.plot(ul, nullcline(ul), color=orange, lw=2.3, label="limiting relaxation cycle")
    ax.plot(ur, nullcline(ur), color=orange, lw=2.3)
    ax.plot([minus, right], [nullcline(minus), nullcline(right)], color=orange, lw=1.7, ls="--")
    ax.plot([plus, left], [nullcline(plus), nullcline(left)], color=orange, lw=1.7, ls="--")
    arrows = [((0.43, nullcline(0.43)), (0.45, nullcline(0.45))),
              ((1.65, nullcline(1.65)), (1.58, nullcline(1.58))),
              ((1.25, (zm-1.25)/GAMMA), (1.36, (zm-1.36)/GAMMA)),
              ((0.7, (zp-0.7)/GAMMA), (0.6, (zp-0.6)/GAMMA))]
    for start, end in arrows:
        ax.annotate("", xy=end, xytext=start,
                    arrowprops={"arrowstyle": "->", "color": orange, "lw": 2})
    for u, label, offset in [(minus, r"$\mu_-$", (-22, 12)), (plus, r"$\mu_+$", (10, 16))]:
        ax.scatter(u, nullcline(u), color="black", s=28, zorder=5)
        ax.plot([u, u], [0, nullcline(u)], ls=":", color="0.4", lw=1)
        ax.annotate(label, (u, nullcline(u)), xytext=offset,
                    textcoords="offset points", fontsize=12)
    ax.axvline(mu, color="#2274a5", lw=1, ls="-.")
    ax.scatter(mu, nullcline(mu), marker="x", s=55, lw=2, color="#2274a5", zorder=5)
    ax.annotate(r"repelling equilibrium at $u=\mu$", (mu, nullcline(mu)),
                xytext=(1.25, 125), arrowprops={"arrowstyle": "->", "color": "#2274a5"},
                color="#2274a5", fontsize=10)
    ax.text(1.48, 49, r"fast jumps: $u+\gamma v=$ constant" + "\n" + r"slope $-1/\gamma=-100$",
            fontsize=10, ha="center")
    ax.set(xlim=(0, 2.3), ylim=(-4, 170), xlabel=r"cytosolic calcium $u$",
           ylabel=r"store calcium $v$",
           title=r"$\delta=0.001,\quad \gamma=0.01,\quad \mu_-\approx0.62970,\quad\mu_+\approx1.01157$")
    ax.legend(loc="upper right", fontsize=9)
    fig.savefig(Path.cwd() / "2023-calcium-nullcline.png", dpi=145, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
