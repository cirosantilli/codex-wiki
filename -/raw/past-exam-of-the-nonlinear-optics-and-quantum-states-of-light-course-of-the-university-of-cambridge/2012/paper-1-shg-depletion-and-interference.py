"""Integrate the exam's declared equal-coupling SHG model; original curves."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def propagate(strength, mismatch, pump=1.0, harmonic=0.0, steps=1600):
    state = np.array(np.broadcast_arrays(np.asarray(pump, complex), np.asarray(harmonic, complex)))
    invariant = np.sum(abs(state)**2, axis=0)
    samples = [np.array(state, copy=True)]
    ds = 1/steps

    def derivative(z, values):
        u, v = values
        return np.array([1j*strength*v*u.conj()*np.exp(-1j*mismatch*z),
                         1j*strength*u*u*np.exp(1j*mismatch*z)])

    for index in range(steps):
        z = index*ds
        k1 = derivative(z, state)
        k2 = derivative(z+ds/2, state+ds*k1/2)
        k3 = derivative(z+ds/2, state+ds*k2/2)
        k4 = derivative(z+ds, state+ds*k3)
        state += ds*(k1+2*k2+2*k3+k4)/6
        samples.append(np.array(state, copy=True))
    assert np.max(abs(np.sum(abs(state)**2, axis=0)-invariant)) < 2e-7
    return np.array(samples)


def main():
    fig, axes = plt.subplots(1, 2, figsize=(9.3, 3.7), layout="constrained")
    strength = 1.4
    for mismatch, label in [(0, "0"), (np.pi, r"$\pi$"), (20*np.pi, r"$20\pi$")]:
        values = propagate(strength, mismatch)
        z = np.linspace(0, 1, len(values))
        intensity = abs(values[:, 1])**2
        axes[0].plot(z, intensity, label=fr"$\Delta k L=$ {label}")
        if mismatch == 0:
            assert np.max(abs(intensity-np.tanh(strength*z)**2)) < 1e-8
    axes[0].set(xlabel=r"Position $z/L$", ylabel=r"Harmonic intensity $I_{2\omega}/I_0$",
                title=r"One crystal: $\alpha\sqrt{I_0}L=1.4$", ylim=(0, 1))
    axes[0].legend(fontsize=9, loc="upper left")
    gap_phase = np.linspace(0, 2*np.pi, 361)
    for eta in [.2, .8, 2]:
        first_pump = np.full_like(gap_phase, 1/np.cosh(eta), dtype=complex)
        first_harmonic = 1j*np.tanh(eta)*np.exp(1j*gap_phase)
        out = propagate(eta, 0, first_pump, first_harmonic)
        intensity = abs(out[-1, 1])**2
        assert abs(intensity[0]-np.tanh(2*eta)**2) < 1e-8
        assert intensity[len(gap_phase)//2] < 1e-12
        axes[1].plot(gap_phase/np.pi, intensity, label=fr"$\alpha\sqrt{{I_0}}L={eta:g}$")
    axes[1].set(xlabel=r"Gap phase $\Delta k_g d/\pi$", ylabel=r"Output harmonic intensity / $I_0$",
                title="Two identical crystals, including depletion", ylim=(0, 1.03), xticks=[0, .5, 1, 1.5, 2])
    axes[1].legend(fontsize=9)
    for ax in axes:
        ax.grid(alpha=.18)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=130, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
