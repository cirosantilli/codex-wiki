"""Photon potential and actual printed-time null directions. Python 3.14."""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({"font.size": 10, "figure.facecolor": "white"})
fig, (ax, cones) = plt.subplots(1, 2, figsize=(10, 4), layout="constrained")
r = np.linspace(1.85, 14, 900)
potential = (1-2/r)/r**2
ax.plot(r, potential, color="#1767a2", lw=2.3)
ax.axvline(2, color=".4", ls=":", label="horizon")
ax.axvline(3, color="#b24545", ls="--", lw=1)
ax.plot(3, 1/27, "o", color="#b24545")
ax.annotate("unstable maximum", (3, 1/27), (5.7, .043),
            arrowprops={"arrowstyle": "->"}, fontsize=10)
for bb, name, col in [(6.8, r"$b>b_{\rm crit}$", "#38955a"),
                       (4.6, r"$b<b_{\rm crit}$", "#c18b17")]:
    ax.axhline(1/bb**2, ls="--", lw=1.2, color=col)
    ax.text(10.3, 1/bb**2+.0013, name, fontsize=9, color=col)
ax.set(xlabel=r"$r/\mu$", ylabel=r"$\mu^2V_{\rm eff}$",
       xlim=(1.85, 14), ylim=(-.027, .055), title="Photon radial potential")
ax.grid(alpha=.17)
cones.axvspan(.7, 2, color=".94")
cones.axvline(2, color=".35", ls=":")
for rr in [1.25, 2., 3., 4.7]:
    for tt in [.25, 1.7]:
        for slope, color in [(-1., "#1767a2"),
                             ((1-2/rr)/(1+2/rr), "#b24545")]:
            dr = slope / np.sqrt(1+slope*slope) * .75
            dt = 1 / np.sqrt(1+slope*slope) * .75
            cones.annotate("", (rr+dr, tt+dt), (rr, tt),
                           arrowprops={"arrowstyle": "->", "lw": 1.7,
                                       "color": color})
        cones.plot(rr, tt, ".", color="black", ms=3)
cones.text(2.08, 2.8, "horizon", fontsize=9)
cones.text(.8, 3.25, r"ingoing $dr/(c\,dt')=-1$", color="#1767a2")
cones.text(.8, 3.55, r"outgoing $dr/(c\,dt')=(r-2\mu)/(r+2\mu)$",
           color="#b24545", fontsize=9)
cones.set(xlabel=r"$r/\mu$", ylabel=r"$ct'/\mu$",
          xlim=(.7, 5.45), ylim=(0, 3.9),
          title=r"Future radial null directions ($t'\ne v$)")
cones.grid(alpha=.17)
fig.savefig("paper-1-photon-potential.png", dpi=155, facecolor="white")
