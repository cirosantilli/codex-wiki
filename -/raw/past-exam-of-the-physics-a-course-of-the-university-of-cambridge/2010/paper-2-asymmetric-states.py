"""Original illustrative asymmetric-well states; Python 3.14, numpy, matplotlib.

No source image/data are used. PNG output is a basename in the current directory.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def model(n=700):
    length = 5.
    x = np.linspace(0, length, n+2)[1:-1]
    dx = length/(n+1)
    potential = np.where(x < 2, 0., np.where(x < 3, 30., 12.))
    matrix = (np.diag(2/dx**2 + potential)
              + np.diag(np.full(n-1, -1/dx**2), 1)
              + np.diag(np.full(n-1, -1/dx**2), -1))
    energy, states = np.linalg.eigh(matrix)
    return x, energy[:3], states[:, :3]


def main():
    x, energy, state = model()
    assert energy[0] < energy[1] < 12 < energy[2] < 30
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    fig, axes = plt.subplots(3, 1, figsize=(8.1, 6), sharex=True)
    colors = ["#175baa", "#bb4f14", "#136f63"]
    for i, (ax, color) in enumerate(zip(axes, colors)):
        psi = state[:, i]
        if psi[np.argmax(abs(psi))] < 0:
            psi = -psi
        psi = psi/max(abs(psi))
        xx = np.r_[0, x, 5]
        yy = np.r_[0, psi, 0]
        ax.axvspan(2, 3, color="#cbd5e1", alpha=.6)
        if i < 2:
            ax.axvspan(3, 5, color="#e2e8f0", alpha=.7)
        ax.plot(xx, yy, color=color, lw=2.2)
        ax.axhline(0, color=".6", lw=.6)
        for wall in [0, 5]:
            ax.axvline(wall, color=".3", lw=1.5)
        sig = np.sign(psi[abs(psi) > 1e-7])
        assert np.count_nonzero(sig[1:] != sig[:-1]) == i
        ax.text(.03, .83, f"State {i}: {i} interior node" + ("s" if i != 1 else ""),
                transform=ax.transAxes)
        ax.set(ylim=(-1.2, 1.45), yticks=[-1, 0, 1], ylabel=r"$\psi$ (scaled)")
        ax.grid(axis="x", alpha=.13)
        if i == 2:
            zoom = ax.inset_axes([.13, .06, .37, .48])
            selected = x <= 2
            zoom.plot(x[selected], psi[selected], color=color, lw=1.5)
            zoom.axhline(0, color=".5", lw=.6)
            zoom.set_xlim(0, 2)
            zoom.set_ylim(-.012, .012)
            zoom.set_xticks([0, 1, 2])
            zoom.set_yticks([])
            zoom.tick_params(labelsize=8)
            zoom.set_title("Left well (magnified)", fontsize=9, pad=2)
    axes[0].text(2.5, .55, "Barrier", ha="center", fontsize=10)
    axes[0].text(4, .55, "Forbidden", ha="center", fontsize=10)
    axes[2].text(4, .7, "Right well allowed", ha="center", fontsize=10)
    axes[-1].set(xlabel="Position (arbitrary units)", xlim=(-.05, 5.05))
    fig.suptitle("An original asymmetric-well model: zero, one and two nodes")
    fig.tight_layout()
    fig.savefig("paper-2-asymmetric-states.png", dpi=160, facecolor="white")
    print({"illustrative_energies": energy.tolist(), "right_floor": 12.,
           "barrier_height": 30., "outer_boundary": "Dirichlet"})


if __name__ == "__main__":
    main()
