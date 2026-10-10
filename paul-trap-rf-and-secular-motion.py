"""Original dimensionless small-q example, using numpy and velocity Verlet.

Python 3.14, numpy 2.3.5, matplotlib 3.10.7. No SciPy.
Run from _media. Prints convergence and independent Floquet checks as JSON.
"""
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


Q_MATHIEU = .10
CYCLES = 80


def verlet(q, steps_per_cycle, cycles=CYCLES, x0=None, v0=0.):
    """Integrate x_ss = (q/2) cos(s) x, s=Omega*t, a=0."""
    h = 2*np.pi/steps_per_cycle
    s = np.arange(cycles*steps_per_cycle + 1)*h
    x = np.empty_like(s)
    x[0] = 1-q/2 if x0 is None else x0
    v = v0
    force = .5*q*np.cos(s)*1.0
    acc = force[0]*x[0]
    for n in range(len(s)-1):
        x[n+1] = x[n]+h*v+.5*h*h*acc
        acc_next = force[n+1]*x[n+1]
        v += .5*h*(acc+acc_next)
        acc = acc_next
    return s, x, v


def monodromy(q, steps=3200):
    """Fundamental matrix after one RF period; independent RK4 evolution."""
    h = 2*np.pi/steps
    matrix = np.eye(2)

    def rhs(s, y):
        return np.array([[0., 1.], [.5*q*np.cos(s), 0.]]) @ y

    for n in range(steps):
        s = n*h
        k1 = rhs(s, matrix)
        k2 = rhs(s+h/2, matrix+h*k1/2)
        k3 = rhs(s+h/2, matrix+h*k2/2)
        k4 = rhs(s+h, matrix+h*k3)
        matrix += h*(k1+2*k2+2*k3+k4)/6
    return matrix


def checks():
    runs = {n: verlet(Q_MATHIEU, n) for n in (400, 800, 1600, 3200)}
    diffs = [float(np.max(np.abs(runs[n][1]-runs[2*n][1][::2])))
             for n in (400, 800, 1600)]
    ratio = diffs[0]/diffs[1]
    assert 3.8 < ratio < 4.2
    assert 3.8 < diffs[1]/diffs[2] < 4.2
    assert diffs[-1] < 2e-5
    s, x, _ = runs[3200]
    w = Q_MATHIEU/(2*np.sqrt(2))
    secular = np.cos(w*s)
    reconstructed = secular*(1-.5*Q_MATHIEU*np.cos(s))
    assert abs(x[0]-reconstructed[0]) < 1e-15
    # A direct independent RK4 trajectory at every fine-grid point.
    h = s[1]-s[0]
    state = np.array([1-Q_MATHIEU/2, 0.])
    rk4_error = 0.
    def rhs(t, y):
        return np.array([y[1], .5*Q_MATHIEU*np.cos(t)*y[0]])
    for n in range(len(s)-1):
        k1 = rhs(s[n], state)
        k2 = rhs(s[n]+h/2, state+h*k1/2)
        k3 = rhs(s[n]+h/2, state+h*k2/2)
        k4 = rhs(s[n]+h, state+h*k3)
        state += h*(k1+2*k2+2*k3+k4)/6
        rk4_error = max(rk4_error, abs(state[0]-x[n+1]))
    assert rk4_error < 1e-5
    # Check both radial and axial equations for this 3D quadrupole.
    modes = {}
    for q in (Q_MATHIEU, -2*Q_MATHIEU):
        matrix = monodromy(q)
        trace = float(np.trace(matrix))
        assert abs(np.linalg.det(matrix)-1) < 1e-10
        assert abs(trace) < 2
        modes[str(q)] = {"trace": trace, "determinant": float(np.linalg.det(matrix)),
                         "frequency_over_Omega": float(np.arccos(trace/2)/(2*np.pi))}
    return runs[3200], secular, reconstructed, {
        "q_radial": Q_MATHIEU, "q_axial": -2*Q_MATHIEU, "a_all": 0,
        "cycles": CYCLES, "steps_per_cycle": [400, 800, 1600, 3200],
        "successive_max_position_differences": diffs,
        "convergence_ratio": ratio,
        "fine_rk4_max_difference": float(rk4_error),
        "max_secular_reconstruction_error": float(np.max(np.abs(x-reconstructed))),
        "approx_frequency_over_Omega": float(w),
        "chosen_point_floquet_checks": modes,
    }


def main():
    (s, x, _), secular, reconstruction, report = checks()
    cycles = s/(2*np.pi)
    fig, axes = plt.subplots(2, 1, figsize=(9, 6.7), facecolor="white",
                             gridspec_kw={"height_ratios": [1.4, 1]})
    ax = axes[0]
    ax.plot(cycles, x, color="#176a97", lw=1.0, label="Full RF trajectory (velocity Verlet)")
    ax.plot(cycles, secular, color="#b44736", lw=1.5, ls="--", label="Leading secular motion X")
    ax.set(xlim=(0, CYCLES), ylim=(-1.15, 1.15), ylabel=r"$x/X_0$",
           xlabel=r"RF cycles $\Omega t/(2\pi)$")
    ax.legend(loc="upper right", fontsize=10)
    ax.grid(alpha=.2)
    ax = axes[1]
    ax.plot(cycles, x, color="#176a97", lw=1.8, label="Full RF trajectory")
    ax.plot(cycles, secular, color="#b44736", ls="--", lw=1.5, label="Secular motion")
    ax.plot(cycles, reconstruction, color="#25835b", ls=":", lw=2,
            label=r"$X[1-(q/2)\cos\Omega t]$")
    ax.set(xlim=(0, 6), ylim=(.15, 1.08), ylabel=r"$x/X_0$",
           xlabel="First six RF cycles: the fast ripple is resolved")
    ax.grid(alpha=.2)
    ax.legend(loc="lower left", fontsize=10)
    fig.suptitle(r"Chosen Paul-trap example: $a_x=0$, $q_x=0.10$, $q_z=-0.20$", fontsize=15)
    fig.text(.5, .025, r"$\omega_x/\Omega\simeq q_x/(2\sqrt{2})=0.03536$; initial $x/X_0=0.95$, $\dot{x}=0$",
             ha="center", fontsize=11)
    fig.subplots_adjust(left=.09, right=.98, top=.92, bottom=.12, hspace=.42)
    fig.savefig(Path(__file__).stem+".png", dpi=130, facecolor="white")
    plt.close(fig)
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
