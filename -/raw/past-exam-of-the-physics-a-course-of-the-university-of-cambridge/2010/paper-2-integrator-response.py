"""Original finite-gain integrator plot; Python 3.14, numpy, matplotlib; cwd PNG."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

A = 100.
u = np.geomspace(1e-4, 1e3, 1000)  # u=omega*R*C, no component values invented.
transfer = -A/(1+1j*(1+A)*u)
phase = np.pi-np.arctan((1+A)*u)
assert np.allclose(np.exp(1j*phase), transfer/abs(transfer))
plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
fig, (ax, bx) = plt.subplots(2, 1, figsize=(8.1, 5.4), sharex=True)
ax.loglog(u, abs(transfer), color="#175baa", lw=2.4, label="Finite gain A=100")
ax.loglog(u, 1/u, color="#d97706", ls="--", lw=1.5, label="Ideal integrator")
ax.axhline(A, color=".55", ls=":", lw=1)
ax.set(ylim=(4e-4, 4e3), ylabel=r"$|V_{\rm out}/V_{\rm in}|$")
ax.legend(frameon=False)
bx.semilogx(u, phase*180/np.pi, color="#175baa", lw=2.4)
bx.axhline(90, color="#d97706", ls="--")
bx.set(ylim=(80, 190), yticks=[90, 135, 180], ylabel="Phase (degrees)",
       xlabel=r"$\omega RC$")
for plot in [ax, bx]:
    plot.axvline(1/(1+A), color="#b91c1c", ls=":")
    plot.grid(alpha=.18)
bx.text(.012, 163, r"Corner: $\omega RC=1/101$", color="#b91c1c")
fig.suptitle(r"Finite constant gain: $e^{i\omega t}$ convention")
fig.tight_layout()
fig.savefig("paper-2-integrator-response.png", dpi=160, facecolor="white")
