"""Generate 2023-excitable-pulse.png in the working directory.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
The curves solve the stated equations by fourth-order Runge--Kutta.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def simulate(a=0.25, gamma=0.3, epsilon=0.003, step=0.00015, end=9.0):
    time = np.arange(round(end / step) + 1) * step
    state = np.zeros((len(time), 2, 2))
    state[0, :, 0] = [0.15, 0.4]

    def rhs(y):
        v, w = y[:, 0], y[:, 1]
        return np.column_stack((
            (v * (a - v) * (v - 1) - w) / epsilon,
            gamma * v - w,
        ))

    for i in range(len(time) - 1):
        y = state[i]
        k1 = rhs(y)
        k2 = rhs(y + 0.5 * step * k1)
        k3 = rhs(y + 0.5 * step * k2)
        k4 = rhs(y + step * k3)
        state[i + 1] = y + step * (k1 + 2*k2 + 2*k3 + k4) / 6
    return time, state


def main():
    a, gamma, epsilon = 0.25, 0.3, 0.003
    time, state = simulate(a, gamma, epsilon)
    d = np.sqrt(1 - a + a*a)
    right = (1 + a + d) / 3
    landing = 1 + a - 2*right
    f = lambda v: v * (a-v) * (v-1)
    fig, (plane, trace) = plt.subplots(1, 2, figsize=(10.4, 4.0), layout="constrained")
    fig.set_facecolor("white")
    vv = np.linspace(-0.27, 1.08, 700)
    plane.plot(vv, f(vv), color="black", lw=1.5, label=r"$w=f(v)$")
    plane.plot(vv, gamma*vv, color="0.5", ls="--", lw=1.2, label=r"$w=\gamma v$")
    colors = ("#2274a5", "#c85a17")
    for j, color in enumerate(colors):
        v, w = state[:, j, 0], state[:, j, 1]
        plane.plot(v[::5], w[::5], color=color, lw=1.8,
                   label=rf"$v(0)={v[0]:g}$")
        plane.scatter(v[0], w[0], color=color, s=24, zorder=4)
        trace.plot(time[::5], v[::5], color=color, lw=1.8)
    plane.scatter([0, a, 1, right, landing], [0, 0, 0, f(right), f(right)],
                  s=20, color="black", zorder=5)
    plane.annotate(r"$a$", (a, 0), xytext=(0, -14), textcoords="offset points", ha="center")
    plane.annotate(r"$v_R$", (right, f(right)), xytext=(7, 6), textcoords="offset points")
    plane.annotate(r"$v_J$", (landing, f(right)), xytext=(-17, 7), textcoords="offset points")
    for t0 in (0.008, 0.18, 0.8, 1.8):
        i = np.searchsorted(time, t0)
        jump = 12 if t0 < 0.02 else 120
        plane.annotate("", xy=state[i+jump, 1], xytext=state[i, 1],
                       arrowprops={"arrowstyle": "->", "color": colors[1], "lw": 1.7})
    plane.axhline(0, color="0.8", lw=0.6)
    plane.set(xlim=(-0.27, 1.08), ylim=(-0.025, 0.12), xlabel=r"activation $v$",
              ylabel=r"recovery $w$", title="Threshold and phase-plane excursion")
    plane.legend(fontsize=8, loc="upper center", bbox_to_anchor=(0.5, -0.17), ncol=2)

    pulse = state[:, 1, 0]
    peak = int(np.argmax(pulse))
    falling = np.flatnonzero((np.arange(len(pulse)) > peak) & (pulse < right))[0]
    trough = int(np.argmin(pulse))
    markers = [(0.007, 0.58, "1: fast activation"),
               (float(time[falling])*0.45, 1.04, "2: slow plateau"),
               (float(time[falling])+0.04, 0.45, "3: fast fall"),
               (float(time[trough])+1.1, -0.24, "4: slow recovery")]
    for x, y, label in markers:
        trace.text(x, y, label, fontsize=8, rotation=90 if label.startswith(("1:", "3:")) else 0,
                   va="center" if label.startswith(("1:", "3:")) else "bottom")
    trace.axhline(0, color="0.65", lw=0.8)
    trace.set(xlim=(0, 5), ylim=(-0.3, 1.15), xlabel=r"time $t$", ylabel=r"activation $v(t)$",
              title="A pulse and a subthreshold response")
    fig.suptitle(r"$a=0.25,\quad \gamma=0.30,\quad \varepsilon=0.003,\quad w(0)=0$", fontsize=12)
    fig.savefig(Path.cwd() / "2023-excitable-pulse.png", dpi=145, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
