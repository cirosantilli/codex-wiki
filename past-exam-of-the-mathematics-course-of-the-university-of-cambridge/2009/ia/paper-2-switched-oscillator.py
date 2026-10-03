"""Draw an original periodic velocity-switched oscillator; PNG to CWD.

Tested with Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    k, omega, force = 0.2, 1.0, 1.0
    p = np.sqrt(omega**2 - k**2)
    half = np.pi / p
    r = np.exp(-k * half)
    xmax = force / (omega**2 * (1-r))
    xmin = -r * xmax
    tau = np.linspace(0, half, 500)
    factor = np.exp(-k*tau) * (np.cos(p*tau) + k/p*np.sin(p*tau))
    derivative = -omega**2/p * np.exp(-k*tau) * np.sin(p*tau)
    x1, v1 = xmax*factor, xmax*derivative
    x2 = force/omega**2 + (xmin-force/omega**2)*factor
    v2 = (xmin-force/omega**2)*derivative
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.8), dpi=100)
    fig.set_facecolor("white")
    axes[0].plot(tau, x1, color="#176a9e", lw=2, label="Velocity < 0: force off")
    axes[0].plot(half+tau, x2, color="#bc5138", lw=2, label="Velocity > 0: force on")
    axes[0].axhline(0, color="#aaaaaa", lw=0.8)
    axes[0].axvline(half, color="#aaaaaa", lw=0.8, ls="--")
    axes[0].set(xticks=[0, half, 2*half],
                xticklabels=["0", "π/p", "2π/p"],
                xlabel="Time", ylabel="Position x", title="One repeating cycle")
    axes[0].legend(fontsize=9, loc="lower right")
    axes[1].plot(x1, v1, color="#176a9e", lw=2)
    axes[1].plot(x2, v2, color="#bc5138", lw=2)
    for xs, vs, color in ((x1,v1,"#176a9e"),(x2,v2,"#bc5138")):
        i = len(xs)//2
        axes[1].annotate("", (xs[i+20],vs[i+20]),(xs[i-20],vs[i-20]),
                         arrowprops={"arrowstyle":"-|>","color":color,"lw":2})
    axes[1].axhline(0, color="#aaaaaa", lw=0.8)
    axes[1].scatter([xmin,xmax],[0,0],color="black",s=25,zorder=3)
    axes[1].annotate("Force turns on", (xmin,0), xytext=(8,12),
                     textcoords="offset points", fontsize=9)
    axes[1].annotate("Force turns off", (xmax,0), xytext=(-8,-20),
                     textcoords="offset points", ha="right", fontsize=9)
    axes[1].set(xlabel="Position x",ylabel="Velocity dx/dt",
                title="Closed phase-plane orbit")
    fig.suptitle("Velocity-switched forcing: k = 0.2, ω = 1, a = 1",fontsize=12)
    fig.tight_layout()
    fig.savefig(Path.cwd() / "paper-2-switched-oscillator.png",
                facecolor="white",transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
