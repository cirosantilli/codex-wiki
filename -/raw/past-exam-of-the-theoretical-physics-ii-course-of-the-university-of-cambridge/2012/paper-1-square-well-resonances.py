"""Original exact/approximate S-wave comparison. Python 3.14, NumPy/Matplotlib."""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({"font.size": 10, "figure.facecolor": "white"})
ratio = 4e-4
k = np.sqrt(ratio)
inner_k = np.sqrt(1+ratio)
q = np.linspace(.035, 8.5, 35000)
phase = np.arctan2(k*np.sin(inner_k*q), inner_k*np.cos(inner_k*q))-k*q
exact = np.sin(phase)**2
approximation = ratio*np.sin(q)**2/(ratio*np.sin(q)**2+np.cos(q)**2)
fig, (ax, zoom) = plt.subplots(1, 2, figsize=(10, 4.4), layout="constrained",
                              gridspec_kw={"width_ratios": [1.65, 1]})
ax.semilogy(q, exact, color="#1767a2", lw=1.8, label="exact S wave")
ax.semilogy(q, approximation, "--", color="#b65435", lw=1.5,
            label="near-threshold approximation")
for threshold in np.pi*(np.arange(3)+.5):
    ax.axvline(threshold, color=".55", ls=":", lw=.9)
ax.plot([np.pi, 2*np.pi], [1.6e-10]*2, "v", color="#b65435", ms=6)
ax.annotate(r"formal zeros: $q=n\pi$", (np.pi, 1.6e-10), (1.1, 1.5e-8),
            arrowprops={"arrowstyle": "->", "color": "#b65435"},
            color="#b65435", fontsize=9)
root = 4.493409457909064
ax.axvline(root, color="#7657a6", ls=":", lw=.8)
ax.text(4.8, 5e-8, r"true zero-energy zeros:"+"\n"+r"$\tan q=q$",
        fontsize=9, color="#7657a6")
ax.set(xlabel=r"$q=a\sqrt{2mV_0}/\hbar$",
       ylabel=r"$\sigma_0/(4\pi/k^2)$",
       xlim=(0, 8.5), ylim=(1e-10, 2),
       title=r"Low energy: $E/V_0=4\times10^{-4}$")
ax.grid(alpha=.18)
ax.legend(loc="lower right", frameon=False, fontsize=9)
selected = abs(q-np.pi/2)<.09
zoom.plot(q[selected], exact[selected], color="#1767a2", lw=2)
zoom.plot(q[selected], approximation[selected], "--", color="#b65435", lw=1.5)
zoom.axvline(np.pi/2, color=".5", ls=":", lw=1)
zoom.axhline(1, color=".6", ls=":", lw=1)
zoom.text(np.pi/2+.002, .14, "zero-energy\nthreshold", fontsize=9)
zoom.set(xlabel=r"$q$", ylabel=r"$\sigma_0/(4\pi/k^2)$",
         ylim=(0, 1.07), title="First peak approaches unitarity")
zoom.grid(alpha=.18)
fig.savefig("paper-1-square-well-resonances.png", dpi=155, facecolor="white")
