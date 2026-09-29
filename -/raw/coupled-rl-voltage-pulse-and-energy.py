"""Closed-return coupled RL model: exactly specified currents and energy budget."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

L = .1  # H, each self-inductance
M = .06  # H, positive mutual inductance in the stated current convention
R = 10.  # ohm, each loop resistance
V = 1.  # V, applied to loop 1 during the pulse
DURATION = .12  # s; the primary circuit stays closed when the drive becomes zero


def step_currents(time):
    t = np.maximum(np.asarray(time), 0.)
    plus = np.exp(-t / ((L + M) / R))
    minus = np.exp(-t / ((L - M) / R))
    return V / (2 * R) * np.array([2 - plus - minus, minus - plus])


def pulse_currents(time):
    return step_currents(time) - step_currents(np.asarray(time) - DURATION)


def energy_budget(time):
    t_on = np.clip(np.asarray(time), 0., DURATION)
    t_after = np.maximum(np.asarray(time) - DURATION, 0.)
    tau_p, tau_m = (L + M) / R, (L - M) / R
    supplied = V**2 / R * (t_on - .5 * tau_p * (-np.expm1(-t_on / tau_p))
                          - .5 * tau_m * (-np.expm1(-t_on / tau_m)))
    def integral_squared_step(t, tau):
        return t - 2 * tau * (-np.expm1(-t / tau)) + .5 * tau * (-np.expm1(-2 * t / tau))
    heat = V**2 / (2 * R) * (integral_squared_step(t_on, tau_p)
                             + integral_squared_step(t_on, tau_m))
    s_end = V / R * (-np.expm1(-DURATION / tau_p))
    d_end = V / R * (-np.expm1(-DURATION / tau_m))
    heat += R / 4 * (s_end**2 * tau_p * (-np.expm1(-2 * t_after / tau_p))
                    + d_end**2 * tau_m * (-np.expm1(-2 * t_after / tau_m)))
    i1, i2 = pulse_currents(time)
    stored = .5 * L * (i1**2 + i2**2) + M * i1 * i2
    return supplied, heat, stored


def main():
    t = np.linspace(-.01, .25, 4001)
    i1, i2 = pulse_currents(t)
    supplied, heat, stored = energy_budget(t)
    fig, axes = plt.subplots(2, 2, figsize=(10.5, 6.6), layout="constrained")
    a, b, c, d = axes.ravel()
    a.plot(t * 1000, np.where((t >= 0) & (t < DURATION), V, 0), color="#555555")
    a.set(title="Voltage pulse; primary return stays closed", xlabel="Time (ms)", ylabel="Drive (V)", ylim=(-.08, 1.15))
    b.plot(t * 1000, i1 * 1000, label="Primary current", color="#d55e00")
    b.plot(t * 1000, i2 * 1000, label="Secondary current", color="#0072b2")
    b.set(title="Receiver responds during changes", xlabel="Time (ms)", ylabel="Current (mA)")
    b.legend(fontsize=9)
    short = np.linspace(0, .045, 1000)
    secondary = step_currents(short)[1]
    tp, tm = (L + M) / R, (L - M) / R
    peak_time = tp * tm / (tp - tm) * np.log(tp / tm)
    c.plot(short * 1000, secondary * 1000, color="#0072b2")
    c.scatter([peak_time * 1000], [step_currents(peak_time)[1] * 1000], color="#333333", zorder=4)
    c.set(title="Step response has two decay times", xlabel="Time after voltage step (ms)", ylabel="Secondary current (mA)")
    c.text(.95, .12, r"$\tau_+=16$ ms, $\tau_-=4$ ms", transform=c.transAxes, ha="right", fontsize=10)
    d.plot(t * 1000, stored * 1000, label="Stored magnetic energy", color="#009e73", lw=2.7)
    d.plot(t * 1000, (supplied - heat) * 1000, "--", label="Source work minus heat", color="#cc79a7", lw=1.6)
    d.set(title="Independent energy expressions agree", xlabel="Time (ms)", ylabel="Energy (mJ)")
    d.legend(fontsize=9)
    for ax in axes.ravel():
        ax.grid(alpha=.2)
        ax.axhline(0, color="#555555", lw=.6)
    fig.suptitle(r"Chosen linear model: $L_1=L_2=0.1$ H, $M=0.06$ H, $R_1=R_2=10\,\Omega$", fontsize=13)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=140, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
