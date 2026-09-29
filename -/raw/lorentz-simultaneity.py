"""Draw lorentz-simultaneity.png in cwd with an opaque white background.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Two coordinate descriptions of the same three rod-endpoint events.
All coordinates are lengths in metres, with time plotted as ct.
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


BLUE = "#1766a6"
ORANGE = "#bd580b"
GREEN = "#217144"


def main():
    beta, rest_length = 0.6, 10.0
    gamma = 1 / np.sqrt(1 - beta**2)
    lab_length = rest_length / gamma
    # Rows are (ct, x), so the matrix acts directly on spacetime coordinates.
    boost = gamma * np.array([[1, -beta], [-beta, 1]])
    metric = np.diag([-1.0, 1.0])
    lab_events = np.array([[0, 0], [0, lab_length],
                           [gamma * beta * rest_length, gamma * rest_length]])
    rod_events = lab_events @ boost.T
    np.testing.assert_allclose(rod_events, [[0, 0], [-6, 10], [0, 10]], atol=1e-13)
    np.testing.assert_allclose(lab_events, [[0, 0], [0, 8], [7.5, 12.5]])
    np.testing.assert_allclose(boost.T @ metric @ boost, metric, atol=1e-14)
    np.testing.assert_allclose(lab_events[1:, 1] - beta * lab_events[1:, 0], lab_length)
    for endpoint in (1, 2):
        original = lab_events[endpoint] @ metric @ lab_events[endpoint]
        transformed = rod_events[endpoint] @ metric @ rod_events[endpoint]
        np.testing.assert_allclose(original, transformed, atol=1e-12)
    np.testing.assert_allclose(lab_length, 8)

    plt.rcParams.update({"font.size": 12, "axes.titlesize": 15})
    fig, axes = plt.subplots(1, 2, figsize=(11.4, 6.6), facecolor="white")
    fig.subplots_adjust(left=0.07, right=0.98, bottom=0.30, top=0.83, wspace=0.23)
    fig.suptitle("A 10 m rod moving at 0.6c: simultaneity selects the endpoint events",
                 fontsize=17, y=0.966)
    lab, rod = axes
    lab.set_title("Laboratory S: measured length 8 m")
    rod.set_title("Rod rest frame S′: rest length 10 m")
    lab.set(xlim=(-3, 16), ylim=(-4, 10), xlabel="x (m)", ylabel="ct (m)")
    rod.set(xlim=(-3, 13), ylim=(-8, 4), xlabel="x′ (m)", ylabel="ct′ (m)")
    ct = np.linspace(-4, 10, 200)
    lab.plot(beta * ct, ct, color=BLUE, lw=2.5)
    lab.plot(beta * ct + lab_length, ct, color=BLUE, lw=2.5)
    rod.axvline(0, color=BLUE, lw=2.5)
    rod.axvline(rest_length, color=BLUE, lw=2.5)

    for ax, events in zip(axes, (lab_events, rod_events)):
        ax.set_aspect("equal")
        ax.set_facecolor("white")
        ax.grid(alpha=0.16)
        ax.spines[["top", "right"]].set_visible(False)
        ax.plot(events[[0, 1], 1], events[[0, 1], 0], color=ORANGE, lw=3)
        ax.plot(events[[0, 2], 1], events[[0, 2], 0], color=GREEN, lw=3)
        ax.scatter(events[:, 1], events[:, 0], s=42, color="#26323a", zorder=5)

    lab.annotate("A (0, 0)", (0, 0), xytext=(-20, -24), textcoords="offset points")
    lab.annotate("B (8, 0)", (8, 0), xytext=(8, -18), textcoords="offset points")
    lab.annotate("C (12.5, 7.5)", (12.5, 7.5), xytext=(-27, 16), textcoords="offset points")
    lab.text(3.5, -2.2, "t = 0: L = 8 m", color=ORANGE, ha="center")
    lab.text(6.2, 5.2, "t′ = 0", color=GREEN, rotation=31, ha="center")
    rod.annotate("A (0, 0)", (0, 0), xytext=(-20, 14), textcoords="offset points")
    rod.annotate("B (10, −6)", (10, -6), xytext=(-50, -23), textcoords="offset points")
    rod.annotate("C (10, 0)", (10, 0), xytext=(-50, 14), textcoords="offset points")
    rod.text(5, 2.1, "t′ = 0: L₀ = 10 m", color=GREEN, ha="center")
    rod.text(5, -4.7, "t = 0", color=ORANGE, rotation=-31, ha="center")
    for ax in axes:
        ax.tick_params(labelsize=10)

    fig.text(0.5, 0.16, "Blue: rear and front world lines    Orange: lab simultaneity    Green: rod simultaneity",
             ha="center", fontsize=11)
    fig.text(0.5, 0.097, "A–B measures the moving rod in S; A–C measures the resting rod in S′.",
             ha="center", fontsize=13)
    fig.text(0.5, 0.043, "Event labels give (ct, x) or (ct′, x′), in metres. Colored slices are not signal paths.",
             ha="center", fontsize=11, color="#555555")
    fig.savefig("lorentz-simultaneity.png", dpi=110, facecolor="white", transparent=False)
    plt.close(fig)
    print("Verified gamma=1.25; rest length 10 m, lab length 8 m; events B′=(-6,10), C=(7.5,12.5);")
    print("both front events lie on one world line, and the boost preserves diag(-1,1).")


if __name__ == "__main__":
    main()
