"""Plot A.T u = f and its coercivity bound; Python 3.14 / matplotlib 3.10.7 / NumPy 2.3.5."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white", "axes.facecolor": "white"})
    matrix = np.array([[2., 1.], [-1., 3.]])
    angle = np.linspace(0, 2*np.pi, 721)
    loads = np.vstack((np.cos(angle), np.sin(angle)))
    responses = np.linalg.solve(matrix.T, loads)
    alpha = np.linalg.eigvalsh((matrix+matrix.T)/2)[0]
    assert alpha == 2
    assert np.max(np.linalg.norm(responses, axis=0)) <= 1/alpha
    assert np.allclose(matrix.T @ responses, loads, atol=1e-14)
    fig, (ellipse, growth) = plt.subplots(1, 2, figsize=(10.3, 4.7), layout="constrained")
    ellipse.plot(np.cos(angle)/alpha, np.sin(angle)/alpha, "--", color="#b45309", lw=2, label=r"Bound: $\|u\|_2\leq 1/2$")
    ellipse.fill(responses[0], responses[1], color="#dbeafe", alpha=1)
    ellipse.plot(responses[0], responses[1], color="#1d4ed8", lw=2, label=r"$u=(A^T)^{-1}f$, $\|f\|_2=1$")
    colors = ["#15803d", "#7e22ce"]
    for i, color in enumerate(colors):
        response = np.linalg.solve(matrix.T, np.eye(2)[:, i])
        ellipse.scatter(*response, color=color, s=45, zorder=4)
        ellipse.annotate(fr"$f=e_{i+1}$", response, xytext=(9, 5), textcoords="offset points", color=color)
    ellipse.axhline(0, color="#9ca3af", lw=0.7); ellipse.axvline(0, color="#9ca3af", lw=0.7)
    ellipse.set(xlabel=r"$u_1$", ylabel=r"$u_2$", aspect="equal", xlim=(-.62, .62), ylim=(-.62, .62), title="Unit-load responses inside the bound")
    ellipse.legend(loc="upper center", fontsize=9)
    magnitude = np.linspace(0, 4, 101)
    growth.plot(magnitude, magnitude/alpha, "--", color="#b45309", lw=2, label=r"Coercivity bound: $t/2$")
    largest = 1/np.linalg.svd(matrix, compute_uv=False)[-1]
    growth.plot(magnitude, largest*magnitude, color="#1d4ed8", lw=2, label="Largest response over load directions")
    for i, color in enumerate(colors):
        gain = np.linalg.norm(np.linalg.solve(matrix.T, np.eye(2)[:, i]))
        growth.plot(magnitude, gain*magnitude, color=color, lw=1.8, label=fr"Load $f=te_{i+1}$")
    growth.set(xlabel=r"Load norm $t=\|f\|_2$", ylabel=r"Response norm $\|u\|_2$", xlim=(0, 4), ylim=(0, 2.1), title="Fixed form: response scales with load")
    growth.grid(alpha=.2); growth.legend(loc="upper left", fontsize=9)
    fig.suptitle(r"$A=[[2,1],[-1,3]]$: solve $A^Tu=f$, with $\alpha=2$", fontsize=15)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=110, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
