"""Original noiseless 1D visibility/dirty-image example; no historical data.

Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
No SciPy. Run from _media to write the matching PNG in that directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def model():
    n, length = 1024, .08
    theta = (np.arange(n) - n//2) * length/n
    sky = np.zeros(n)
    offsets, strengths = [-80, 120], [1., .65]
    for offset, strength in zip(offsets, strengths):
        sky[n//2 + offset] = strength
    frequencies = np.fft.fftfreq(n, d=length/n)
    visibility = np.fft.fft(np.fft.ifftshift(sky))
    analytic = sum(strength*np.exp(-2j*np.pi*frequencies*offset*length/n)
                   for offset, strength in zip(offsets, strengths))
    np.testing.assert_allclose(visibility, analytic, atol=2e-13)
    cases = {}
    for name, positive in [
        ("Sparse", np.array([2, 5, 9, 14, 20, 28, 36, 44, 52, 60, 64])),
        ("Denser", np.arange(1, 65)),
    ]:
        sampling = np.zeros(n)
        sampling[positive] = 1
        sampling[-positive] = 1
        normalization = n/sampling.sum()
        beam_complex = np.fft.ifft(sampling)*normalization
        image_complex = np.fft.ifft(sampling*visibility)*normalization
        assert np.max(np.abs(beam_complex.imag)) < 1e-14
        assert np.max(np.abs(image_complex.imag)) < 1e-14
        np.testing.assert_allclose(beam_complex[0], 1., atol=1e-14)
        direct = sum(strength*np.roll(beam_complex.real, offset)
                     for offset, strength in zip(offsets, strengths))
        np.testing.assert_allclose(image_complex.real, direct, atol=1e-13)
        assert abs(image_complex.real.mean()) < 1e-14
        cases[name] = {"k": positive, "sampling": sampling,
                       "beam": np.fft.fftshift(beam_complex.real),
                       "image": np.fft.fftshift(image_complex.real)}
    np.testing.assert_allclose(visibility[32], -1+.65j, atol=1e-13)
    np.testing.assert_allclose(visibility[64], .35, atol=1e-13)
    return theta, frequencies, visibility, cases


def main():
    theta, frequency, visibility, cases = model()
    plt.rcParams.update({"font.size": 10, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, axs = plt.subplots(3, 2, figsize=(10.8, 9.0), layout="constrained", facecolor="white")
    colors = {"Sparse": "#bb5315", "Denser": "#185c9c"}
    u = np.linspace(-800, 800, 2001)
    v = np.exp(2j*np.pi*u*.00625) + .65*np.exp(-2j*np.pi*u*.009375)
    ax = axs[0, 0]
    ax.plot(u, v.real, c="#185c9c", label="Real part")
    ax.plot(u, v.imag, c="#9a3e89", label="Imaginary part", alpha=.85)
    ax.set(title="A. Complex visibility of the chosen sky", xlabel="u (cycles per radian)", ylabel="Visibility (arbitrary units)")
    ax.legend(loc="upper right", ncol=2, fontsize=8)

    ax = axs[0, 1]
    for row, (name, data) in enumerate(cases.items()):
        positions = 12.5*np.r_[-data["k"], data["k"]]
        ax.vlines(positions, row-.23, row+.23, colors=colors[name], lw=1.1)
    ax.axvline(0, c=".5", ls=":", lw=1)
    ax.set(yticks=[0, 1], yticklabels=["Sparse: 22", "Denser: 128"],
           ylim=(-.5, 1.55), xlim=(-850, 850), xlabel="u (cycles per radian)",
           title="B. Unit-weight samples, paired ±u")
    ax.text(0, 1.34, "Zero baseline omitted", ha="center", fontsize=9)

    ax = axs[1, 0]
    for name, data in cases.items():
        ax.plot(theta, data["beam"], color=colors[name], lw=1.25, label=name)
    ax.axhline(0, c=".7", lw=.7)
    ax.set(xlim=(-.025, .025), ylim=(-.65, 1.12), title="C. Dirty beams: each has B(0) = 1",
           xlabel="Angular offset (radians)", ylabel="Unit-peak point response")
    ax.legend(fontsize=9)

    ax = axs[1, 1]
    source_theta, strengths = [-.00625, .009375], [1, .65]
    ax.vlines(source_theta, 0, strengths, color="#222222", lw=2.5)
    ax.scatter(source_theta, strengths, c="#222222", s=25)
    ax.text(-.00625, 1.05, "1.00", ha="center")
    ax.text(.009375, .70, "0.65", ha="center")
    ax.set(xlim=(-.025, .025), ylim=(-.1, 1.23), title="D. True sky: two ideal point sources",
           xlabel="θ (radians)", ylabel="Integrated source strength")

    for ax, (name, data) in zip(axs[2], cases.items()):
        ax.plot(theta, data["image"], c=colors[name], lw=1.4, label="Dirty image")
        ax.vlines(source_theta, 0, strengths, color="#222222", ls="--", lw=1, label="True sources")
        ax.axhline(0, c=".7", lw=.7)
        ax.set(xlim=(-.025, .025), ylim=(-.72, 1.25),
               title=f"{'E' if name == 'Sparse' else 'F'}. {name} sampling: same maximum |u| = 800",
               xlabel="θ (radians)", ylabel="Dirty-image response")
        ax.legend(loc="upper right", fontsize=8)
    for ax in axs.flat:
        ax.grid(alpha=.12)
    fig.suptitle("Two invented sources: sampling changes the image artefacts", fontsize=15, weight="bold")
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=110, facecolor="white")
    plt.close(fig)
    print("FFT visibilities equal analytic visibilities; shifted-beam and real-image checks passed.")


if __name__ == "__main__":
    main()
