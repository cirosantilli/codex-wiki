"""Original multivariate-method sketches.

Tested with root Python 3.14, NumPy 2.3 and Matplotlib 3.10.
Write only paper-30-multivariate-sketches.png in the caller's CWD.
The caller's MPLCONFIGDIR is respected; no cache directory is hardcoded.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse


def main():
    rng = np.random.default_rng(200130)
    fig, axes = plt.subplots(2, 2, figsize=(10, 7), constrained_layout=True)
    fig.patch.set_facecolor('white')
    blue, red = '#2878b5', '#c9574b'
    angle = np.pi / 5
    rot = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
    points = rng.normal(size=(90, 2)) @ np.diag([1.35, .30]) @ rot.T
    points -= points.mean(axis=0)
    values, vectors = np.linalg.eigh(np.cov(points.T))
    ax = axes[0, 0]
    ax.scatter(*points.T, s=13, color=blue, alpha=.65)
    for j, (length, vector, color) in enumerate(zip(np.sqrt(values[::-1]), vectors.T[::-1], [red, '#569342']), 1):
        ends = np.array([-2, 2])[:, None] * length * vector
        ax.plot(*ends.T, color=color, lw=2.2, label=f'PC{j}')
    ax.set_title('Principal components: covariance axes')
    ax.set_aspect('equal', adjustable='datalim')
    ax.legend(fontsize=9, loc='upper left')
    ax.set_xlabel('centered measurement 1'); ax.set_ylabel('centered measurement 2')

    original = np.array([[-2., -1.], [2., -1.], [2., 1.], [-2., 1.]])
    squared = np.sum((original[:, None] - original[None, :]) ** 2, axis=2)
    J = np.eye(4) - np.ones((4, 4)) / 4
    B = -.5 * J @ squared @ J
    val, vec = np.linalg.eigh(B)
    coords = vec[:, -2:][:, ::-1] * np.sqrt(val[-2:][::-1])
    recovered = np.sum((coords[:, None] - coords[None, :]) ** 2, axis=2)
    assert np.allclose(recovered, squared)
    ax = axes[0, 1]
    order = [0, 1, 2, 3, 0]
    ax.plot(*coords[order].T, color=blue, lw=1.8)
    ax.plot(*coords[[0, 2]].T, color='#777777', ls='--', lw=1)
    ax.scatter(*coords.T, s=36, color=blue)
    for name, (x, y) in zip('ABCD', coords):
        ax.annotate(name, (x, y), xytext=(6, 6), textcoords='offset points')
    ax.set_title('Classical scaling: recover distance geometry')
    ax.set_aspect('equal', adjustable='box'); ax.margins(.3)
    ax.set_xlabel('coordinate 1'); ax.set_ylabel('coordinate 2')

    ax = axes[1, 0]
    # Complete linkage for scalar positions A=0, B=.25, C=3, D=3.4.
    # The first two merges have heights .25 and .4; the final height is 3.4.
    def merge(left, right, lower_left, lower_right, height):
        ax.plot([left, left, right, right], [lower_left, height, height, lower_right], color=blue, lw=2)
        return (left + right) / 2
    left = merge(0, 1, 0, 0, .25)
    right = merge(2, 3, 0, 0, .4)
    merge(left, right, .25, .4, 3.4)
    ax.axhline(1.5, color=red, ls='--', label='two-cluster cut')
    ax.set_xticks(range(4), ['A', 'B', 'C', 'D'])
    ax.set_ylim(0, 3.8); ax.set_xlim(-.4, 3.4)
    ax.set_title('Complete linkage: a nested hierarchy')
    ax.set_ylabel('merge dissimilarity'); ax.legend(fontsize=9)

    ax = axes[1, 1]
    cov = np.array([[.6, .54], [.54, .6]])
    ev, evec = np.linalg.eigh(cov)
    major = evec[:, 1]
    tilt = np.degrees(np.arctan2(major[1], major[0]))
    centers = np.array([[-.55, .55], [.55, -.55]])
    for name, center, color in zip(['group 1', 'group 2'], centers, [blue, red]):
        sample = rng.multivariate_normal(center, cov, size=50)
        ax.scatter(*sample.T, color=color, s=12, alpha=.5)
        ax.add_patch(Ellipse(center, 4*np.sqrt(ev[1]), 4*np.sqrt(ev[0]), angle=tilt,
                             edgecolor=color, facecolor='none', lw=1.8))
        ax.scatter(*center, color=color, marker='X', s=90, label=name+' mean')
    ax.plot(*centers.T, color='#333333', lw=1.3, ls='--')
    ax.set_title('MANOVA: separation relative to covariance')
    ax.set_aspect('equal', adjustable='datalim')
    ax.set_xlabel('response 1'); ax.set_ylabel('response 2'); ax.legend(fontsize=8)
    for ax in axes.flat:
        ax.set_facecolor('white'); ax.spines[['top', 'right']].set_visible(False)
        ax.grid(alpha=.15)
    output = Path('paper-30-multivariate-sketches.png')
    fig.savefig(output, dpi=140, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
