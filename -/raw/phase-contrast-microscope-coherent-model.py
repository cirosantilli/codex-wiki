"""Original zero-mode phase-contrast calculation; PNG is written to the CWD.

Periodic, lossless, coherent specimen; only the zero Fourier coefficient is
changed. This is not an annular-instrument simulation or historical data.
Tested with Python 3.14, matplotlib 3.10 and numpy 2.3.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def model(n=256, alpha=.5):
    x = np.arange(n)/n
    xx, yy = np.meshgrid(x, x)
    phase = .06*(np.cos(2*np.pi*xx)+.4*np.cos(2*np.pi*yy))
    field = np.exp(1j*phase)
    c0 = field.mean()
    image = lambda theta: abs(field+(alpha*np.exp(1j*theta)-1)*c0)**2
    return x, phase, field, c0, image


def main():
    alpha = .5
    x, phase, field, c0, image = model(alpha=alpha)
    bright = abs(field)**2
    plus, minus = image(np.pi/2), image(-np.pi/2)
    assert np.max(abs(bright-1)) < 1e-14
    assert np.max(abs(phase)) <= .084000000001
    expected_mean = 1-(1-alpha**2)*abs(c0)**2
    assert abs(plus.mean()-expected_mean) < 1e-14
    assert abs(minus.mean()-expected_mean) < 1e-14
    plt.rcParams.update({"font.size": 10, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig = plt.figure(figsize=(12.6, 7.9), facecolor="white")
    gs = fig.add_gridspec(2, 4, left=.06, right=.93, bottom=.12, top=.83,
                         height_ratios=[1, 1.02], hspace=.62, wspace=.50)
    axes = [fig.add_subplot(gs[0, j]) for j in range(4)]
    pm = axes[0].imshow(phase, origin="lower", extent=(0, 1, 0, 1),
                        cmap="RdBu_r", vmin=-.084, vmax=.084)
    fig.colorbar(pm, ax=axes[0], fraction=.046, pad=.03)
    axes[0].set_title("Chosen phase (rad)")
    for ax, data, title in zip(axes[1:], [bright, plus/alpha**2, minus/alpha**2],
                               ["Ideal bright field", r"Reference $\theta=+\pi/2$", r"Reference $\theta=-\pi/2$"]):
        im = ax.imshow(data, origin="lower", extent=(0, 1, 0, 1),
                       cmap="gray", vmin=.6, vmax=1.4)
        ax.set_title(title)
    fig.colorbar(im, ax=axes[1:], fraction=.019, pad=.025, label="Relative intensity")
    for j, ax in enumerate(axes):
        ax.set(xlabel="x (periods)", ylabel="y (periods)" if j == 0 else "",
               xticks=[0, .5, 1], yticks=[0, .5, 1])

    cut = fig.add_subplot(gs[1, :2])
    cut.plot(x, plus[0]/alpha**2, color="#265b9a", label=r"Exact $\theta=+\pi/2$")
    cut.plot(x, 1+2*phase[0]/alpha, "--", color="#d38324", label=r"First order $1+2\phi/a$")
    cut.plot(x, minus[0]/alpha**2, color="#7c3e82", label=r"Exact $\theta=-\pi/2$")
    cut.axhline(1, color=".45", lw=1, label="Ideal bright field")
    cut.set(xlabel="x along y = 0 (periods)", ylabel="Relative intensity", xlim=(0, 1), ylim=(.6, 1.42))
    cut.set_title("Image line cut: the same phase pattern, opposite contrast")
    cut.legend(fontsize=9, loc="lower center", ncol=2)

    response = fig.add_subplot(gs[1, 2:])
    theta = np.linspace(-np.pi, np.pi, 401)
    exact = abs(field[0, 0]+(alpha*np.exp(1j*theta)-1)*c0)**2/alpha**2
    response.plot(theta, exact, color="#265b9a", label="Exact, pattern maximum")
    response.plot(theta, 1+2*.084*np.sin(theta)/alpha, "--", color="#d38324", label="First order")
    response.axhline(1, color=".65", lw=.8)
    response.set(xlabel=r"Reference shift $\theta$", ylabel="Relative intensity", xlim=(-np.pi, np.pi), ylim=(.6, 1.42))
    response.set_xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
                        [r"$-\pi$", r"$-\pi/2$", "0", r"$\pi/2$", r"$\pi$"])
    response.set_title("A quarter-cycle shift gives the largest linear response")
    response.legend(fontsize=9, loc="lower center")
    fig.suptitle("Turning phase variations into brightness", fontsize=18, y=.97)
    fig.text(.5, .915, r"$\phi=0.06[\cos(2\pi x)+0.4\cos(2\pi y)]$,  $a=0.5$,  $E=e^{i\phi}+(ae^{i\theta}-1)\langle e^{i\phi}\rangle$",
             ha="center", fontsize=12)
    fig.text(.5, .875, "Original coherent zero-mode model; synthetic pattern, no absorption in the specimen and no measured data",
             ha="center", color=".3", fontsize=10)
    fig.text(.5, .035, "Brightness is normalized to the empty-field intensity: 1 for bright field, a² = 0.25 with the reference plate.",
             ha="center", fontsize=10)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=110, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
