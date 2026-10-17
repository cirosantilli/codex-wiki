"""Original cubic-quartic model curves; Python 3.14, NumPy, Matplotlib."""
import numpy as np
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 3, figsize=(10.5, 6.5), layout="constrained")
cases = [(.5, [1.7, np.sqrt(2), .8]), (1.2, [3., 1.2, .8])]
for row, (gamma, temperatures) in enumerate(cases):
    B = np.sqrt(gamma/2)
    for col, T in enumerate(temperatures):
        ax = axes[row, col]
        A = T*T-1
        discriminant = (3*B*T)**2-4*A
        roots = []
        if discriminant >= 0:
            roots = [(3*B*T-np.sqrt(discriminant))/2, (3*B*T+np.sqrt(discriminant))/2]
            roots = [r for r in roots if r>1e-10]
        xmax = 1.18*max(roots) if roots else 2.
        x = np.linspace(0, xmax, 1100)
        free = lambda q: A*q*q/2-B*T*q**3+q**4/4
        ax.plot(x, free(x), color="#175b98", lw=2)
        ax.axhline(0, color=".5", lw=.8)
        ax.scatter([0], [0], s=25, color="#333333", zorder=5)
        for r in roots:
            curvature = A-6*B*T*r+3*r*r
            ax.scatter([r], [free(r)], marker="o" if curvature>0 else "x", s=34, color="#b65a25", zorder=5)
        if row==0 and col==1:
            ax.text(.05, .92, "Equal minima; finite barrier", transform=ax.transAxes, va="top", fontsize=8)
        elif row==1 and col<2:
            ax.text(.05, .92, "0 metastable; nonzero global", transform=ax.transAxes, va="top", fontsize=8)
        elif col==2:
            ax.text(.05, .92, "0 unstable; nonzero global", transform=ax.transAxes, va="top", fontsize=8)
        else:
            ax.text(.05, .92, "Only the zero minimum", transform=ax.transAxes, va="top", fontsize=8)
        ax.set_title(rf"$\gamma={gamma:g},\quad T/T_0={T:.3g}$", fontsize=11)
        ax.set(xlabel=r"Order parameter $\phi$ (chosen units)", ylabel=r"$F(\phi)-F(0)$ (chosen units)", xlim=(0, xmax))
        ax.grid(alpha=.15)
fig.suptitle(r"Illustrative $c=\lambda=T_0=1$, $B=\sqrt{\gamma/2}$; circles: minima, crosses: barriers", fontsize=11)
fig.savefig("paper-1-landau-potentials.png", dpi=150, facecolor="white")
