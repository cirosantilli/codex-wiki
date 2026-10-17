"""Original rest-frame ray geometry and Fresnel calculation; Python 3.14."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc

fig, (ray, plot) = plt.subplots(1, 2, figsize=(10.0, 4.7), layout="constrained")
n = 1.5
beta = n/np.sqrt(1+n*n)
ci = np.sqrt(1-beta*beta)
st = beta/n
ct = np.sqrt(1-st*st)
ray.axhspan(-1.6, 0, color="#dce9f3")
ray.axhline(0, color="0.25", lw=1.5)
ray.plot([0, 0], [-1.5, 1.5], "--", color=".6", lw=1)
ray.annotate("", xy=(0, 0), xytext=(1.65*beta, 1.65*ci), arrowprops=dict(arrowstyle="->", color="C0", lw=2.3))
ray.annotate("", xy=(-1.65*beta, 1.65*ci), xytext=(0, 0), arrowprops=dict(arrowstyle="->", color="C1", lw=2.3))
ray.annotate("", xy=(-1.35*st, -1.35*ct), xytext=(0, 0), arrowprops=dict(arrowstyle="->", color="C2", lw=2.3))
ray.text(.65, 1.05, "Incident", color="C0", fontsize=10)
ray.text(-1.58, 1.05, "Reflected: s only", color="C1", fontsize=10)
ray.text(-1.53, -1.38, "Transmitted", color="C2", fontsize=10)
ray.add_patch(Arc((0, 0), 1.0, 1.0, theta1=np.rad2deg(np.arccos(beta)), theta2=90, lw=1))
ray.text(.3, .5, r"$i_B$", fontsize=12)
ray.text(.35, -.42, "Illustrative n = 1.5\nSlab at rest in this frame", fontsize=9)
ray.text(-1.58, .2, r"$s\parallel y$: out of this plane", fontsize=9)
ray.set(xlabel=r"$x'$", ylabel=r"$z'$", title="Brewster geometry in slab frame", xlim=(-1.75, 1.75), ylim=(-1.55, 1.55), aspect="equal")
ray.set_xticks([])
ray.set_yticks([])
speeds = np.linspace(0, .995, 1600)
for index in [1.3, 1.5, 2.0]:
    cosi = np.sqrt(1-speeds**2)
    cost = np.sqrt(1-(speeds/index)**2)
    rs = (cosi-index*cost)/(cosi+index*cost)
    rp = (index*cosi-cost)/(index*cosi+cost)
    degree = np.abs(rs*rs-rp*rp)/(rs*rs+rp*rp)
    plot.plot(speeds, degree, lw=2, label=f"n = {index}")
plot.scatter([beta], [1], color="C1", zorder=5)
plot.annotate(r"$\beta_B=1.5/\sqrt{1+1.5^2}=0.832$", xy=(beta, 1), xytext=(.06, .86), fontsize=9, arrowprops=dict(arrowstyle="->"))
plot.set(xlabel=r"Tangential speed $|v|/c$", ylabel="Reflected degree of linear polarization", xlim=(0, 1), ylim=(0, 1.08), title="Unpolarized normal incidence in laboratory")
plot.grid(alpha=.17)
plot.legend(loc="lower right", fontsize=9)
fig.savefig("paper-1-moving-dielectric.png", dpi=150, facecolor="white")
