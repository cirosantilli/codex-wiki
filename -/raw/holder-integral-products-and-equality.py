"""Original continuous Hölder examples; white PNG output goes to the CWD."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({"font.size": 11, "figure.facecolor": "white", "axes.facecolor": "white"})
t = np.linspace(0, 1, 601)
fig, axes = plt.subplots(1, 2, figsize=(10, 4.9), layout="constrained")
for ax, g, label, text in [(axes[0], 1-t, r"$g(t)=1-t$", r"$\int fg=1/6<25^{-1/3}\approx0.342$"),
                           (axes[1], t*t, r"$g(t)=t^2$", r"$\int fg=1/4=\|f\|_3\|g\|_{3/2}$")]:
    ax.plot(t, t, color="#2563eb", lw=2, label=r"$f(t)=t$")
    ax.plot(t, g, color="#d97706", lw=2, label=label)
    ax.plot(t, t*g, color="#059669", lw=1.5, label=r"$f(t)g(t)$")
    ax.fill_between(t, t*g, color="#a7f3d0", alpha=.65)
    ax.set(xlim=(0, 1), ylim=(0, 1.13), xlabel="t", ylabel="Function value", title=text)
    ax.grid(alpha=.18); ax.spines[["top", "right"]].set_visible(False); ax.legend(loc="upper center", framealpha=.95, fontsize=10)
axes[0].text(.5, .07, "Conjugate-power profiles differ", transform=axes[0].transAxes, ha="center", fontsize=10)
axes[1].text(.5, .07, r"$f^3=g^{3/2}=t^3$", transform=axes[1].transAxes, ha="center", fontsize=12)
fig.suptitle(r"The product area is controlled by complementary norms ($p=3$, $q=3/2$)", fontsize=14)
fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white", transparent=False)
plt.close(fig)
