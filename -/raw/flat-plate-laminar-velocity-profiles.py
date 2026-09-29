"""Generate flat-plate-laminar-velocity-profiles.png in the working directory.

Tested with Python 3.14, matplotlib 3.10.7, numpy 2.3.5.
The numerical model uses f''' + f f''/2 = 0 and a Töpfer rescaling.
"""
from pathlib import Path
import json
import matplotlib.pyplot as plt
import numpy as np


def blasius_profile(step=0.002, end=10.0):
    """Integrate a unit-curvature IVP with RK4, then enforce f'(infinity)=1."""
    eta_raw = np.linspace(0, end, round(end / step) + 1)
    h = eta_raw[1] - eta_raw[0]
    states = np.zeros((len(eta_raw), 3))
    states[0, 2] = 1.0

    def rhs(z):
        return np.array([z[1], z[2], -0.5 * z[0] * z[2]])

    for i in range(len(eta_raw) - 1):
        z = states[i]
        a = rhs(z)
        b = rhs(z + h * a / 2)
        c = rhs(z + h * b / 2)
        d = rhs(z + h * c)
        states[i + 1] = z + h * (a + 2 * b + 2 * c + d) / 6
    scale = states[-1, 1] ** -0.5
    eta = eta_raw / scale
    states *= np.array([scale, scale**2, scale**3])
    return eta, states


def model_constants(eta, states):
    speed = states[:, 1]
    return {
        "wall_curvature": float(states[0, 2]),
        "eta99": float(np.interp(0.99, speed, eta)),
        "displacement_coefficient": float(np.trapezoid(1 - speed, eta)),
        "momentum_coefficient": float(np.trapezoid(speed * (1 - speed), eta)),
        "far_speed": float(speed[-1]),
        "min_speed_increment": float(np.min(np.diff(speed))),
    }


def main():
    eta, states = blasius_profile()
    data = model_constants(eta, states)
    U, nu = 10.0, 1.5e-5
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white"})
    fig, (ax, norm) = plt.subplots(1, 2, figsize=(10.6, 5.0),
                                  gridspec_kw={"width_ratios": [1.65, 1]}, layout="constrained")
    fig.suptitle("Laminar boundary layer on a stationary flat plate", fontsize=15)
    x = np.linspace(0.002, 0.57, 400)
    length = np.sqrt(nu * x / U) * 1000
    ax.plot(x, data["eta99"] * length, "--", color="#1f6f9b", lw=2,
            label=r"99% thickness $\delta_{99}$")
    ax.plot(x, data["displacement_coefficient"] * length, color="#a25a23", lw=2,
            label=r"Displacement thickness $\delta^*$")
    ax.plot(x, data["momentum_coefficient"] * length, color="#437741", lw=2,
            label=r"Momentum thickness $\theta$")
    for station, color in [(0.10, "#64429a"), (0.25, "#b84145"), (0.45, "#313d48")]:
        keep = eta <= 6.5
        y = eta[keep] * np.sqrt(nu * station / U) * 1000
        velocity = states[keep, 1]
        ax.plot(station + 0.055 * velocity, y, color=color, lw=2)
        ax.plot([station, station], [0, y[-1]], ":", color=color, lw=0.8)
        for level in [0.8, 2, 3.7]:
            if level <= y[-1]:
                vel = float(np.interp(level, y, velocity))
                ax.annotate("", (station + 0.055 * vel, level), (station, level),
                            arrowprops={"arrowstyle": "->", "color": color, "lw": 0.9})
        ax.text(station, -0.43, f"{station:.2f} m", ha="center", fontsize=10, color=color)
    ax.axhline(0, color="#222222", lw=3)
    ax.text(0.015, 6.1, r"$U=10$ m/s, $\nu=1.5\times10^{-5}$ m$^2$/s", fontsize=11)
    ax.text(0.015, 5.5, "Profiles shifted from their stations; arrows show u/U", fontsize=9)
    ax.set(xlim=(0, 0.60), ylim=(-0.8, 6.6), xlabel="Downstream distance x (m)",
           ylabel="Normal distance y (mm)")
    ax.legend(loc="upper left", bbox_to_anchor=(0.0, 0.78), fontsize=9, framealpha=1)
    ax.grid(alpha=0.17)
    keep = eta <= 7
    norm.fill_betweenx(eta[keep], states[keep, 1], 1, color="#d5e6f1", label=r"Deficit $1-u/U$")
    norm.plot(states[keep, 1], eta[keep], color="#1f6f9b", lw=2.5, label=r"Blasius profile $f'(\eta)$")
    norm.axhline(data["eta99"], color="#1f6f9b", ls="--", lw=1)
    norm.axvline(1, color="gray", ls=":", lw=1)
    norm.scatter([0.99], [data["eta99"]], color="#1f6f9b", zorder=5)
    norm.text(0.05, data["eta99"] + 0.15, r"$u/U=0.99$ at $\eta=4.910$", fontsize=10)
    norm.text(0.35, 0.3, "No slip: u = 0", fontsize=10)
    norm.set(xlim=(0, 1.13), ylim=(0, 7), xlabel="Normalized velocity u/U",
             ylabel=r"$\eta=y\sqrt{U/(\nu x)}$")
    norm.legend(loc="upper left", fontsize=9)
    norm.grid(alpha=0.17)
    fig.savefig(Path(__file__).stem + ".png", dpi=130, facecolor="white", transparent=False)
    plt.close(fig)
    print(json.dumps(data, sort_keys=True))


if __name__ == "__main__":
    main()
