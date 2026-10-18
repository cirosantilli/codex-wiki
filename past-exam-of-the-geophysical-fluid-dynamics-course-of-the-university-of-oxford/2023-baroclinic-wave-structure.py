"""Original Eady wave contours; Python 3.14, NumPy 2.3, Matplotlib 3.10."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    # Choose the growing Eady mode whose boundary streamfunction phases differ by pi/2.
    # With alpha = coth(q), the rigid-boundary eigencondition is
    # q = tanh(q)*(1+tanh(q)**2)/(1+tanh(q)**4), q = K D.
    low, high = 0.6, 1.0
    for _ in range(60):
        q = (low + high)/2
        t = np.tanh(q)
        if q - t*(1+t*t)/(1+t**4) > 0:
            high = q
        else:
            low = q
    q = (low+high)/2
    alpha = 1/np.tanh(q)
    x = np.linspace(-0.5, 0.5, 501)
    z = np.linspace(-1, 1, 301)
    X, Z = np.meshgrid(x, z)
    C, S = np.cosh(q*Z), np.sinh(q*Z)
    psi = C*np.cos(2*np.pi*X) - alpha*S*np.sin(2*np.pi*X)
    buoyancy = S*np.cos(2*np.pi*X) - alpha*C*np.sin(2*np.pi*X)
    ridges = (-np.arctan(alpha*np.tanh(q*z))/(2*np.pi),
              -np.arctan2(alpha*np.cosh(q*z), np.sinh(q*z))/(2*np.pi))
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    fig, axes = plt.subplots(1, 2, figsize=(10.5, 5), layout="constrained")
    fig.set_facecolor("white")
    for ax, field, ridge, title in zip(
        axes, (psi, buoyancy), ridges,
        (r"Streamfunction $\psi'/A$: westward tilt", r"Buoyancy $b'/(f_0AK)$: eastward tilt"),
    ):
        bound = np.max(np.abs(field))
        ax.contourf(X, Z, field, levels=np.linspace(-bound, bound, 21), cmap="RdBu_r")
        ax.contour(X, Z, field, levels=[0], colors="#666666", linewidths=0.8)
        ax.plot(ridge, z, "k--", lw=2.2, label="Positive crest")
        for side in (-1, 1):
            ax.axhline(side, color="black", lw=2.2)
        ax.set(xlim=(-0.5, 0.5), ylim=(-1.02, 1.02), xlabel=r"Eastward position $x/\lambda_x$",
               ylabel=r"Height $z/D$", title=title, yticks=[-1, 0, 1])
        ax.legend(loc="upper right", framealpha=0.95)
    fig.suptitle(r"Growing Eady mode: $KD\simeq0.803$, $\alpha\tanh(KD)=1$" + "\nRed positive; blue negative; boundaries at z/D = ±1", fontsize=13)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                dpi=140, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
