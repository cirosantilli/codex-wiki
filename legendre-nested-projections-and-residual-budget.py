"""Draw original nested polynomial projections and exact residual budgets.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media; writes this script's basename with a .png extension to CWD.
"""

from fractions import Fraction as F
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def inner(p, q):
    return sum((a * b * F(2, i + j + 1)
                for i, a in enumerate(p) for j, b in enumerate(q)
                if (i + j) % 2 == 0), F(0))


polynomials = [[F(1)], [F(0), F(1)], [F(-1, 2), F(0), F(3, 2)],
               [F(0), F(-3, 2), F(0), F(5, 2)]]
f = [F(1)] * 4
norms = [inner(p, p) for p in polynomials]
coefficients = [inner(f, p) / h for p, h in zip(polynomials, norms)]
assert coefficients == [F(4, 3), F(8, 5), F(2, 3), F(2, 5)]
contributions = [c * c * h for c, h in zip(coefficients, norms)]
projections = []
for m in range(4):
    q = [sum((coefficients[n] * polynomials[n][k]
              for n in range(m + 1) if k < len(polynomials[n])), F(0))
         for k in range(4)]
    projections.append(q)
errors = [inner([a - b for a, b in zip(f, q)],
                [a - b for a, b in zip(f, q)]) for q in projections]
assert errors == [F(608, 315), F(352, 1575), F(8, 175), F(0)]
assert errors == [sum(contributions[m + 1:], F(0)) for m in range(4)]

plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                     "axes.spines.right": False, "figure.facecolor": "white",
                     "axes.facecolor": "white", "savefig.facecolor": "white"})
fig, (ax, budget) = plt.subplots(1, 2, figsize=(12.4, 6.2),
                               gridspec_kw={"width_ratios": [1.15, 1]})
fig.subplots_adjust(left=0.06, right=0.88, bottom=0.30, top=0.77, wspace=0.36)
fig.suptitle("Keep one more orthogonal component; remove its exact error budget",
             y=0.96, fontsize=16, weight="bold")
fig.text(0.5, 0.875, r"$f(x)=1+x+x^2+x^3$,  $w=1$ on $[-1,1]$;  "
         r"$q_m=c_0P_0+\cdots+c_mP_m$", ha="center", fontsize=13)
colors = ["#0072B2", "#D55E00", "#009E73", "#8B5AB5"]
x = np.linspace(-1, 1, 701)
ax.plot(x, np.polynomial.polynomial.polyval(x, [float(c) for c in f]),
        color="#263238", linewidth=3.3, label=r"$f=q_3$")
for m, style in zip(range(3), ["--", "-.", ":"]):
    y = np.polynomial.polynomial.polyval(x, [float(c) for c in projections[m]])
    ax.plot(x, y, color=colors[m], linewidth=2.5, linestyle=style,
            label=f"$q_{m}$")
ax.set(xlim=(-1, 1), ylim=(-0.4, 4.25), xlabel="$x$", ylabel="Function value",
       title="Best fits in nested degree spaces")
ax.set_xticks([-1, -0.5, 0, 0.5, 1])
ax.grid(alpha=0.17)
ax.legend(loc="upper left", fontsize=11, framealpha=0.95)

for m in range(4):
    left = 0
    for n in range(m + 1, 4):
        value = float(contributions[n])
        budget.barh(m, value, left=left, height=0.55, color=colors[n],
                    edgecolor="white", linewidth=0.8)
        left += value
    budget.text(1.035, m, f"${errors[m]}$", va="center", ha="left",
                transform=budget.get_yaxis_transform(), fontsize=13)
budget.scatter([0], [3], color="#263238", s=28, zorder=3)
budget.set(xlim=(0, 2.05), ylim=(3.6, -0.7),
           xlabel=r"Squared residual $\int_{-1}^{1}(f-q_m)^2\,dx$",
           title="Omitted components add independently")
budget.set_yticks(range(4), [f"$m={m}$" for m in range(4)])
budget.set_xticks([0, 0.5, 1, 1.5, 2])
budget.grid(axis="x", alpha=0.17)
budget.set_axisbelow(True)
budget.text(1.035, -0.65, "Exact total", ha="left", fontsize=11,
            transform=budget.get_yaxis_transform())
for n, xpos in zip(range(1, 4), [0.1, 0.4, 0.7]):
    fig.text(xpos, 0.12, f"Omit $P_{n}$:  $c_{n}^2h_{n}={contributions[n]}$",
             color=colors[n], fontsize=12)
fig.text(0.5, 0.035, r"Fixed coefficients $(c_0,c_1,c_2,c_3)=(4/3,8/5,2/3,2/5)$; "
         "errors use exact integration, not sampled observations.",
         ha="center", fontsize=11)
fig.savefig(Path(__file__).with_suffix(".png").name, dpi=100, transparent=False)
plt.close(fig)
