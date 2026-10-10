"""Draw a quadratic Fenchel-Young gap; save basename.png to cwd.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    p = 2.0
    sample = -1.0
    x = np.linspace(-2.0, 3.8, 1001)
    f = x**2 / 2
    support = p * x - p**2 / 2
    gap = f + p**2 / 2 - p * x
    assert np.allclose(gap, (x - p)**2 / 2)
    assert np.allclose(gap, f - support)
    assert np.all(gap >= -1e-12)
    sample_f = sample**2 / 2
    sample_support = p * sample - p**2 / 2
    sample_gap = sample_f - sample_support
    assert sample_f == 0.5 and sample_support == -4 and sample_gap == 4.5
    assert p**2 / 2 - (p * p - p**2 / 2) == 0

    plt.rcParams.update({"font.size": 11})
    fig, (ax, residual) = plt.subplots(
        1, 2, figsize=(9.1, 4.5), layout="constrained", facecolor="white"
    )
    ax.plot(x, f, color="#244e78", lw=2.8, label=r"$f(x)=x^2/2$")
    ax.plot(x, support, color="#cc6b20", lw=2.1,
            label=r"$\ell_2(x)=2x-2$")
    ax.annotate("", (sample, sample_f), (sample, sample_support),
                arrowprops={"arrowstyle": "<->", "color": "#a53656", "lw": 2.2})
    ax.scatter([sample, sample, p], [sample_f, sample_support, p**2 / 2],
               color=["#244e78", "#cc6b20", "#287d70"], s=48, zorder=5)
    ax.text(-0.8, -2.2, "$G_f(-1,2)=9/2$\nVertical distance = 4.5",
            color="#a53656", fontsize=10,
            bbox={"facecolor": "white", "edgecolor": "none", "pad": 3})
    ax.annotate("Equality at x = p = 2", (p, p**2 / 2),
                xytext=(0.0, 4.4), fontsize=10,
                arrowprops={"arrowstyle": "->", "color": "#287d70"},
                bbox={"facecolor": "white", "edgecolor": "none", "pad": 2})
    ax.set(xlim=(-2, 3.8), ylim=(-6.7, 7.6), xlabel="Input x",
           ylabel="Function / line value", title="Fix the slope p = 2")
    ax.legend(loc="upper left", fontsize=10, framealpha=1)

    residual.plot(x, gap, color="#a53656", lw=2.8,
                  label=r"$G_f(x,2)=(x-2)^2/2$")
    residual.plot([sample, sample], [0, sample_gap],
                  color="#a53656", ls="--", lw=1.2)
    residual.scatter([sample, p], [sample_gap, 0],
                     color=["#a53656", "#287d70"], s=48, zorder=5)
    residual.annotate("(-1, 4.5)", (sample, sample_gap),
                      xytext=(12, 10), textcoords="offset points", color="#a53656")
    residual.annotate("(2, 0): exact match", (p, 0),
                      xytext=(-82, 18), textcoords="offset points", color="#287d70")
    residual.set(xlim=(-2, 3.8), ylim=(-0.45, 8.7), xlabel="Input x",
                 ylabel="Gap", title="Subtract the line from the function")
    residual.legend(loc="upper right", fontsize=10, framealpha=1)
    for panel in (ax, residual):
        panel.set_facecolor("white")
        panel.axhline(0, color="#b4bcc3", lw=0.7, zorder=0)
        panel.axvline(0, color="#b4bcc3", lw=0.7, zorder=0)
        panel.grid(color="#e5e8eb", lw=0.7)
        panel.spines[["top", "right"]].set_visible(False)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"),
                dpi=120, facecolor="white", transparent=False)
    plt.close(fig)
    print("Verified gap identities on 1001 inputs; G(-1,2)=4.5, G(2,2)=0.")


if __name__ == "__main__":
    main()
