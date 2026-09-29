"""Show the local rates of two functions and their composite; output to cwd."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    baseline, changed = 1.0, 1.01
    inner_change = changed**2 - baseline**2
    exact_change = np.sin(changed**2) - np.sin(baseline**2)
    composite_rate = 2 * np.cos(1)
    assert np.isclose(inner_change, 0.0201)
    assert np.isclose(exact_change, 0.010689369475964217)
    step = 1e-6
    numerical_rate = (np.sin((1 + step)**2) - np.sin((1 - step)**2)) / (2 * step)
    assert np.isclose(numerical_rate, composite_rate, atol=1e-9)
    plt.rcParams.update({"font.size": 12, "axes.titlesize": 14})
    fig, axes = plt.subplots(1, 3, figsize=(11.2, 5.4), dpi=120, facecolor="white")
    panels = [
        (lambda x: x**2, 2, changed, "Inner stage", r"$f(x)=x^2$", "Input x", r"$f'(1)=2$"),
        (np.sin, np.cos(1), changed**2, "Outer stage", r"$g(u)=\sin u$", "Intermediate input u", r"$g'(1)=\cos 1$"),
        (lambda x: np.sin(x**2), composite_rate, changed, "Composite", r"$h(x)=\sin(x^2)$", "Original input x", r"$h'(1)=2\cos 1$"),
    ]
    for ax, (function, rate, endpoint, title, formula, xlabel, derivative) in zip(axes, panels):
        inputs = np.linspace(0.97, 1.04, 400)
        output = function(1.0)
        ax.plot(inputs, function(inputs), color="#206a9d", lw=2.8, label="Exact function")
        ax.plot(inputs, output + rate * (inputs - 1), color="#bc7323", lw=2,
                linestyle="--", label="Local tangent")
        ax.scatter([1, endpoint], [output, function(endpoint)], color=["#206a9d", "#b83242"],
                   s=65, zorder=5)
        ax.plot([endpoint, endpoint], [output, function(endpoint)], color="#b83242", lw=2)
        ax.plot([1, endpoint], [output, output], color="#b83242", lw=2)
        ax.annotate(f"Input +{endpoint - 1:.4f}\nOutput +{function(endpoint) - output:.7f}",
                    xy=(endpoint, function(endpoint)), xycoords="data",
                    xytext=(0.04, 0.90), textcoords="axes fraction", fontsize=11,
                    va="top", arrowprops={"arrowstyle": "->", "color": "#b83242"},
                    color="#9b2836", bbox={"facecolor": "white", "edgecolor": "none", "alpha": .9})
        ax.set(xlim=(0.97, 1.04), xlabel=xlabel, ylabel="Output", title=f"{title}\n{formula}")
        ax.text(0.05, 0.055, derivative, transform=ax.transAxes, fontsize=13,
                bbox={"facecolor": "white", "edgecolor": "none", "alpha": .9})
        ax.grid(color="#e5e9eb")
        ax.spines[["top", "right"]].set_visible(False)
        ax.ticklabel_format(useOffset=False)
    fig.suptitle("The chain rule multiplies local rates, not finite changes", fontsize=16, y=.98)
    fig.legend(*axes[0].get_legend_handles_labels(), loc="lower center", ncol=2, frameon=False,
               bbox_to_anchor=(.5, .035))
    fig.subplots_adjust(left=.07, right=.98, bottom=.20, top=.82, wspace=.38)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
