"""Compare directional values of indefinite, semidefinite and definite matrices.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Write an opaque white PNG with the script's basename in the working directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    theta = np.linspace(0, np.pi, 601)
    real_path = np.column_stack([np.cos(theta), np.sin(theta)])
    h = np.array([[2, 1j], [-1j, 2]])
    eigenbasis = np.array([[1, 1], [1j, -1j]]) / np.sqrt(2)
    complex_path = real_path @ eigenbasis.T
    cases = [
        (np.diag([1., -1.]), real_path, [-1, 1],
         'Self-adjoint, indefinite', r'$D=\mathrm{diag}(1,-1)$',
         r'$q_D=\cos(2\theta)$', '#a44b46'),
        (np.diag([1., 0.]), real_path, [0, 1],
         'Positive semidefinite', r'$P=\mathrm{diag}(1,0)$',
         r'$q_P=\cos^2\theta$', '#326c9d'),
        (h, complex_path, [1, 3],
         'Positive definite', r'$H=[2\ \ i;\ -i\ \ 2]$',
         r'$q_H=\cos^2\theta+3\sin^2\theta$', '#3b7955'),
    ]
    fig, axes = plt.subplots(1, 3, figsize=(11.8, 4.9), dpi=110,
                             sharey=True, facecolor='white')
    fig.subplots_adjust(left=.065, right=.98, bottom=.24, top=.75, wspace=.18)
    for ax, (matrix, path, eigenvalues, title, matrix_label, formula, color) in zip(axes, cases):
        assert np.allclose(matrix.conj().T, matrix)
        assert np.allclose(np.linalg.eigvalsh(matrix), eigenvalues)
        assert np.allclose(np.sum(np.abs(path)**2, axis=1), 1)
        values = np.einsum('ni,ij,nj->n', path.conj(), matrix, path)
        assert np.allclose(values.imag, 0)
        values = values.real
        assert np.isclose(values.min(), min(eigenvalues))
        assert np.isclose(values.max(), max(eigenvalues))
        ax.axhline(0, color='#5c6269', lw=1.3)
        ax.fill_between(theta, values, 0, where=values >= 0,
                        color='#e5f1e8', interpolate=True)
        ax.fill_between(theta, values, 0, where=values <= 0,
                        color='#f5e2df', interpolate=True)
        ax.plot(theta, values, color=color, lw=2.7)
        ax.scatter([0, np.pi/2, np.pi], values[[0, 300, 600]],
                   color=color, s=33, zorder=4)
        for level in eigenvalues:
            ax.axhline(level, color=color, lw=.8, ls=':', alpha=.65)
        ax.set(xlim=(-.07, np.pi + .07), ylim=(-1.35, 3.45),
               xlabel=r'$\theta$', title=title)
        ax.set_xticks([0, np.pi/2, np.pi], [r'$0$', r'$\pi/2$', r'$\pi$'])
        ax.set_yticks([-1, 0, 1, 2, 3])
        ax.grid(axis='x', color='#e2e6eb', lw=.7)
        ax.spines[['top', 'right']].set_visible(False)
        ax.title.set_fontsize(12)
        ax.text(.5, 1.14, matrix_label, transform=ax.transAxes,
                fontsize=13, ha='center', color=color)
        ax.text(.5, -.29, formula, transform=ax.transAxes,
                fontsize=12, ha='center', color=color)
    axes[0].set_ylabel(r'$q_T(x)=\langle Tx,x\rangle,\quad\|x\|=1$', fontsize=12)
    fig.suptitle('Real values do not guarantee positive values', fontsize=17, y=.98)
    fig.text(.5, .045,
             r'$D,P:\ x=(\cos\theta,\sin\theta)\qquad'
             r'H:\ x=\cos\theta\,e_1+\sin\theta\,e_3$',
             fontsize=12, ha='center')
    fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'),
                facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
