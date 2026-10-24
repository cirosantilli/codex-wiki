"""Generate 2017-exponential-coupling.png in the current directory."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    rng = np.random.default_rng(20170615)
    n = np.arange(36)
    uniforms = rng.uniform(size=len(n)-1)
    inputs = rng.exponential(size=len(n)-1)
    initial = rng.exponential()

    def trajectory(start):
        path = [start]
        for uniform, fresh in zip(uniforms, inputs):
            path.append(uniform*(path[-1]+fresh))
        return np.asarray(path)

    fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.5), dpi=100, facecolor="white")
    for start, color in [(-2, "#2563eb"), (2, "#15803d"), (8, "#b91c1c")]:
        axes[0].plot(n, trajectory(start), lw=1.4, color=color, label=rf"$Z_0={start}$")
    axes[0].plot(n, trajectory(initial), lw=1.6, color="#111827", ls="--", label=r"Stationary $X_0\sim\mathrm{Exp}(1)$")
    axes[0].set_title("Shared inputs erase the starting value", fontsize=11)
    axes[0].set_ylabel("State")
    axes[0].legend(fontsize=8)
    error = abs(8-initial)*np.r_[1, np.cumprod(uniforms)]
    mean_error = (7+2*np.exp(-8))*2.0**(-n)
    axes[1].semilogy(n, error, lw=1.8, color="#b91c1c", label="One path difference (product formula)")
    axes[1].semilogy(n, mean_error, lw=1.8, color="#111827", ls="--", label=r"Mean difference: $(7+2e^{-8})2^{-n}$")
    axes[1].set_title(r"Synchronous error for $Z_0=8$", fontsize=11)
    axes[1].set_ylabel("Absolute difference (logarithmic scale)")
    axes[1].legend(fontsize=8, loc="lower left")
    for ax in axes:
        ax.set_xlabel("Step n")
        ax.grid(alpha=0.2)
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle("An invariant exponential law and contraction under common random inputs", fontsize=13, y=0.96)
    fig.subplots_adjust(left=0.06, right=0.98, bottom=0.14, top=0.82, wspace=0.27)
    fig.savefig("2017-exponential-coupling.png", dpi=100, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
