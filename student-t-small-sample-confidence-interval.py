"""Original chosen-data illustration of a normal mean t interval; PNG in CWD.

Assumes iid normal sampling with unknown population standard deviation.
The five displayed values are chosen for arithmetic, not real measurements.
Tested with Python 3.14, matplotlib 3.10.7. Uses no SciPy.
"""
from math import sqrt
from pathlib import Path
from statistics import NormalDist, mean, variance

import matplotlib.pyplot as plt


def t4_cdf(t):
    a = t / sqrt(4 + t * t)
    return 0.5 + 0.75 * a - 0.25 * a ** 3


def t4_quantile(p):
    if not 0 < p < 1:
        raise ValueError("probability must lie strictly between zero and one")
    lo, hi = -1.0, 1.0
    while t4_cdf(lo) > p:
        lo *= 2
    while t4_cdf(hi) < p:
        hi *= 2
    for _ in range(100):
        mid = (lo + hi) / 2
        if t4_cdf(mid) < p:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def main():
    chosen = [8, 9, 10, 11, 12]
    n = len(chosen)
    average = mean(chosen)
    s2 = variance(chosen)
    se = sqrt(s2 / n)
    critical = t4_quantile(0.975)
    t_margin = critical * se
    z_margin = NormalDist().inv_cdf(0.975) * se
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False})
    fig, axes = plt.subplots(2, 1, figsize=(10, 5.6), sharex=True, height_ratios=[1, 1.65], layout="constrained", facecolor="white")
    upper, lower = axes
    upper.scatter(chosen, [0] * n, s=85, color="#444444", zorder=3)
    for value in chosen:
        upper.annotate(str(value), (value, 0), xytext=(0, 14), textcoords="offset points", ha="center")
    upper.set_yticks([0], ["Chosen values"])
    upper.set_ylim(-0.45, 0.65)
    upper.set_title(r"$n=5,\quad\bar{x}=10,\quad s^2=2.5,\quad s/\sqrt{n}=\sqrt{0.5}$", fontsize=13)
    for y, margin, color, label, style in [(1, t_margin, "#245c9c", "95% t interval (df = 4)", "-"), (0, z_margin, "#b14628", "Normal critical value\nwith estimated SE", "--")]:
        left, right = average - margin, average + margin
        lower.plot([left, right], [y, y], color=color, lw=4, ls=style, solid_capstyle="butt")
        lower.scatter([left, right], [y, y], color=color, marker="|", s=240, linewidths=2)
        lower.scatter([average], [y], color=color, s=50, zorder=4)
        lower.annotate(f"[{left:.6f}, {right:.6f}]", (average, y), xytext=(0, 14), textcoords="offset points", ha="center", color=color)
    lower.set_yticks([1, 0], ["95% t interval (df = 4)", "Normal critical value\nwith estimated SE"])
    lower.set_ylim(-0.65, 1.7)
    lower.set_xlim(7.5, 12.5)
    lower.set_xticks([8, 9, 10, 11, 12])
    lower.axvline(average, color="#999999", lw=1, ls=":", zorder=0)
    lower.grid(axis="x", alpha=0.2)
    lower.set_xlabel("Population mean being estimated (same units as chosen values)")
    lower.text(0.5, 0.01, f"t margin = {t_margin:.6f}; normal margin = {z_margin:.6f} (too small)", transform=lower.transAxes, ha="center", fontsize=10)
    fig.suptitle("Small normal sample: unknown spread requires a wider interval", fontsize=15)
    fig.supxlabel("Chosen arithmetic example; exact 95% coverage assumes iid normal sampling with unknown σ.", fontsize=10)
    fig.savefig(Path(__file__).stem + ".png", dpi=100, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
