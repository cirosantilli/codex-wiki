"""Hypothetical van der Waals inversion and finite-throttle temperature model.

Python 3.14 / matplotlib 3.10.7 / numpy 2.3.5. Run from _media.
No fitted material parameters or experimental points are used.
r=v_m/b_m, theta=R*b_m*T/a_m, pi=b_m**2*p/a_m, eta=b_m*h_m/a_m.
The caloric assumption is C_V,m/R=3/2, so u_m=C_V,m*T-a_m/v_m.
Only supercritical theta>8/27 is displayed; all endpoints have pi>0.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

C = 1.5
CASES = ((.8, .12, "#176ca4", "Cooling"),
         (2.2, .12, "#9b4327", "Warming"),
         (1.45, .30, "#7950a2", "Warms, then cools"))
OUTLET = .025


def initial_volume(theta, pressure):
    roots = np.roots([pressure, -pressure-theta, 1, -1])
    valid = [z.real for z in roots if abs(z.imag) < 1e-9 and z.real > 1]
    if len(valid) != 1:
        raise ValueError("The plotted supercritical state must have one physical root")
    return valid[0]


def state_on_isenthalp(r, eta):
    theta = (eta + 2/r) / (C + r/(r-1))
    pressure = theta/(r-1) - 1/r**2
    return theta, pressure


def throttle(theta, pressure):
    r1 = initial_volume(theta, pressure)
    eta = C*theta + pressure*r1 - 1/r1
    lo, hi = r1, 250.
    for _ in range(100):
        mid = (lo+hi)/2
        if state_on_isenthalp(mid, eta)[1] > OUTLET:
            lo = mid
        else:
            hi = mid
    r = np.geomspace(r1, (lo+hi)/2, 600)
    t, p = state_on_isenthalp(r, eta)
    return r, t, p, eta


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(10, 5.6), dpi=120)
    r = np.linspace(1.5, 450, 20000)
    inv_t, inv_p = 2*(1-1/r)**2, (2*r-3)/r**2
    # At fixed theta, the inversion pressure is found directly from r.
    ts = np.linspace(.42, 2, 500)
    inverse_r = 1-np.sqrt(ts/2)
    ps = 2*inverse_r-3*inverse_r**2
    ax.fill_betweenx(ts, 0, ps, color="#e6f2fa")
    ax.fill_betweenx(ts, ps, .38, color="#f9ece7")
    ax.axhspan(2, 2.36, color="#f9ece7")
    ax.plot(inv_p, inv_t, "k", linewidth=1.8, label="$\\mu_{JT}=0$")
    ax.text(.055, 1.06, "Cooling\n$\\mu_{JT}>0$", color="#176ca4", ha="center")
    ax.text(.30, 1.97, "Warming\n$\\mu_{JT}<0$", color="#9b4327", ha="center")
    ax.set(xlim=(0, .38), ylim=(.42, 2.36), xlabel="Reduced pressure $\\pi$",
           ylabel="Reduced temperature $\\theta$", title="Inversion curve and endpoint states")
    summary = []
    for t1, p1, color, label in CASES:
        r, t, p, eta = throttle(t1, p1)
        ax.plot(p, t, color=color, linewidth=2)
        ax.plot([p[0], p[-1]], [t[0], t[-1]], "o", color=color, markersize=4)
        j = len(p)//2
        ax.annotate("", xy=(p[j+25], t[j+25]), xytext=(p[j-25], t[j-25]),
                    arrowprops={"arrowstyle": "->", "color": color, "lw": 1.8})
        bx.plot(p1-p, t-t1, color=color, linewidth=2, label=label)
        bx.plot(p1-p[-1], t[-1]-t1, "o", color=color, markersize=4)
        summary.append((t1, p1, float(t[-1]), float(p[-1]), eta))
    ax.legend(loc="lower left", framealpha=1)
    bx.axhline(0, color="#777777", linewidth=1)
    bx.set(xlabel="Pressure drop $\\pi_1-\\pi_2$",
           ylabel="Temperature change $\\theta_2-\\theta_1$",
           title="Finite drops along constant enthalpy")
    bx.legend(loc="lower right", fontsize=10, framealpha=1)
    for a in (ax, bx):
        a.grid(alpha=.22)
    fig.suptitle("Hypothetical van der Waals throttling: cooling is not universal",
                 fontsize=15, weight="bold", y=.98)
    fig.text(.5, .10, "$r=v_m/b_m$,  $\\theta=Rb_mT/a_m$,  $\\pi=b_m^2p/a_m$;  $C_{V,m}=3R/2$",
             ha="center", fontsize=11)
    fig.text(.5, .045, "Model curves only; supercritical states; no experimental measurements or fitted gas.",
             ha="center", fontsize=10, color="#555555")
    fig.subplots_adjust(left=.08, right=.98, bottom=.25, top=.86, wspace=.31)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white")
    plt.close(fig)
    for row in summary:
        print("theta1=%.8f pi1=%.8f theta2=%.8f pi2=%.8f eta=%.8f" % row)


if __name__ == "__main__":
    main()
