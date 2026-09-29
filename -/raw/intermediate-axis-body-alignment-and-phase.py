"""Independent angular-momentum and attitude integration for torque-free tumbling.

Run in _media; tested with Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
R maps body components into inertial components. Neither L nor R is projected.
"""

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

MOMENTS = np.array([1.0, 2.0, 3.0])


def derivative(state):
    momentum = state[:3]
    rotation = state[3:].reshape(3, 3)
    omega = momentum / MOMENTS
    x, y, z = omega
    cross_matrix = np.array([[0, -z, y], [z, 0, -x], [-y, x, 0]])
    return np.r_[np.cross(momentum, omega), (rotation @ cross_matrix).ravel()]


def solve(step=0.005, stop=50):
    t = np.linspace(0, stop, round(stop / step) + 1)
    states = np.empty((len(t), 12))
    states[0] = np.r_[0.01, 2, 0, np.eye(3).ravel()]
    for j, h in enumerate(np.diff(t)):
        a = derivative(states[j])
        b = derivative(states[j] + h * a / 2)
        c = derivative(states[j] + h * b / 2)
        d = derivative(states[j] + h * c)
        states[j + 1] = states[j] + h * (a + 2 * b + 2 * c + d) / 6
    return t, states


def make_figure():
    t, state = solve()
    momentum = state[:, :3]
    rotation = state[:, 3:].reshape(-1, 3, 3)
    l0 = momentum[0]
    length = np.linalg.norm(l0)
    n = momentum / length
    energy = (momentum**2 / MOMENTS).sum(axis=1) / 2
    l2 = (momentum**2).sum(axis=1)
    fixed_momentum = np.einsum("tij,tj->ti", rotation, momentum)
    orthogonality = np.einsum("tji,tjk->tik", rotation, rotation) - np.eye(3)
    alignment_reconstructed = rotation[:, :, 1] @ (l0 / length)
    sign_changes = np.where(n[:-1, 1] * n[1:, 1] < 0)[0]
    crossings = [float(t[k] - n[k, 1] * (t[k + 1] - t[k]) / (n[k + 1, 1] - n[k, 1])) for k in sign_changes]
    _, fine = solve(step=0.0025)
    checks = {
        "energy_initial": float(energy[0]), "angular_momentum_squared_initial": float(l2[0]),
        "energy_relative_drift": float(np.max(abs(energy / energy[0] - 1))),
        "angular_momentum_squared_relative_drift": float(np.max(abs(l2 / l2[0] - 1))),
        "space_angular_momentum_relative_error": float(np.max(np.linalg.norm(fixed_momentum - l0, axis=1)) / length),
        "rotation_orthogonality_error": float(np.max(abs(orthogonality))),
        "alignment_identity_error": float(np.max(abs(alignment_reconstructed - n[:, 1]))),
        "step_halving_max_difference": float(np.max(abs(state - fine[::2]))),
        "intermediate_axis_zero_crossings": crossings,
        "omega_at_t14": (momentum[2800] / MOMENTS).tolist(),
    }
    assert checks["energy_relative_drift"] < 1e-9
    assert checks["angular_momentum_squared_relative_drift"] < 1e-9
    assert checks["space_angular_momentum_relative_error"] < 1e-8
    assert checks["rotation_orthogonality_error"] < 1e-8
    assert checks["alignment_identity_error"] < 1e-8
    assert checks["step_halving_max_difference"] < 1e-7
    assert len(crossings) >= 2

    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white", "axes.facecolor": "white"})
    fig, (phase, alignment) = plt.subplots(1, 2, figsize=(10, 4.3), layout="constrained", gridspec_kw={"width_ratios": [1, 1.6]})
    phase.plot(n[:, 0], n[:, 2], color="#2171b5", lw=2, label="Numerical orbit")
    x = np.linspace(-0.51, 0.51, 200)
    for s in (-1, 1):
        phase.plot(x, s * np.sqrt(3) * x, "--", color="0.55", lw=1, label="Separatrix projection" if s == 1 else None)
    phase.scatter(n[0, 0], n[0, 2], c="#c52f24", s=35, zorder=5)
    phase.set(xlabel=r"$L_1/|L|$", ylabel=r"$L_3/|L|$", title="Body-frame momentum projection", xlim=(-0.54, 0.54), ylim=(-0.94, 0.94), aspect="equal")
    phase.legend(fontsize=8, loc="upper left")
    neck = phase.inset_axes([0.12, 0.13, 0.56, 0.27])
    neck.plot(n[:, 0], n[:, 2], color="#2171b5", lw=1.5)
    small_x = np.linspace(0, 0.014, 100)
    for s in (-1, 1):
        neck.plot(small_x, s * np.sqrt(3) * small_x, "--", color="0.55", lw=0.8)
    neck.scatter(n[0, 0], 0, c="#c52f24", s=12, zorder=5)
    neck.set(xlim=(0, 0.014), ylim=(-0.016, 0.016), title="Off separatrix")
    neck.title.set_fontsize(8)
    neck.tick_params(labelsize=7)
    neck.set_xticks([0, 0.01])
    neck.set_yticks([-0.01, 0, 0.01])
    alignment.plot(t, n[:, 1], color="#c52f24", lw=2)
    alignment.axhline(0, color="0.6", lw=0.8)
    for crossing in crossings:
        alignment.axvline(crossing, color="0.6", ls=":", lw=1)
    alignment.set(xlabel="Normalized time t", ylabel=r"$c_2=\hat e_2\cdot\hat L=L_2/|L|$", title="The intermediate body axis reverses", ylim=(-1.12, 1.12))
    for a in (phase, alignment):
        a.grid(alpha=0.2)
    fig.suptitle(r"Torque-free tumbling: $(I_1,I_2,I_3)=(1,2,3)$, $\omega(0)=(0.01,1,0)$", fontsize=13)
    fig.savefig(Path(__file__).stem + ".png", dpi=130, facecolor="white")
    plt.close(fig)
    print(json.dumps(checks, indent=2))


if __name__ == "__main__":
    make_figure()
