"""Original triplet-Higgs vertices; Python 3.14, root NumPy/Matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


def leg(ax, end, label, vector=False):
    end = np.array(end, dtype=float)
    if vector:
        t = np.linspace(0, 1, 201)
        n = np.array([-end[1], end[0]])/np.linalg.norm(end)
        z = end[:, None]*t+n[:, None]*.033*np.sin(14*np.pi*t)
        ax.plot(*z, color='black', lw=1.4)
    else:
        ax.plot([0, end[0]], [0, end[1]], color='black', lw=1.5, ls='--')
    ax.text(*(1.16*end), label, ha='center', va='center', fontsize=14)


def vertex(ax, labels, vectors, rule, title):
    if len(labels) == 3:
        ends = [(-.65, .50), (.65, .50), (0, -.66)]
    else:
        ends = [(-.60, .50), (.60, .50), (-.60, -.50), (.60, -.50)]
    for end, label, vector in zip(ends, labels, vectors):
        leg(ax, end, label, vector)
    ax.plot(0, 0, 'ko', ms=4)
    ax.set(xlim=(-1.05, 1.05), ylim=(-1.28, 1.12), aspect='equal')
    ax.axis('off')
    ax.text(0, .96, title, ha='center', fontsize=14)
    ax.text(0, -1.03, rule, ha='center', fontsize=13)


def main():
    fig = plt.figure(figsize=(11.52, 8.2), dpi=100, facecolor='white')
    grid = fig.add_gridspec(2, 12, left=.035, right=.965, top=.86, bottom=.04, hspace=.38)
    top = [fig.add_subplot(grid[0, 3*i:3*i+3]) for i in range(4)]
    bottom = [fig.add_subplot(grid[1, 4*i:4*i+4]) for i in range(3)]
    vertex(top[0], [r'$h$']*3, [False]*3, r'$-3i\lambda v$', 'Scalar cubic')
    vertex(top[1], [r'$h$']*4, [False]*4, r'$-3i\lambda$', 'Scalar quartic')
    vertex(top[2], [r'$W^+_\mu$', r'$W^-_\nu$', r'$h$'], [True, True, False], r'$2ie^2v\,g_{\mu\nu}$', 'One scalar, two vectors')
    vertex(top[3], [r'$h$', r'$h$', r'$W^+_\mu$', r'$W^-_\nu$'], [False, False, True, True], r'$2ie^2g_{\mu\nu}$', 'Two scalars, two vectors')
    vertex(bottom[0], [r'$\phi_b(p)$', r'$\phi_c(q)$', r'$A^a_\mu$'], [False, False, True], r'$e\epsilon^{abc}(q-p)_\mu$', 'Unbroken: derivative vertex')
    vertex(bottom[1], [r'$\phi_c$', r'$\phi_d$', r'$A^a_\mu$', r'$A^b_\nu$'], [False, False, True, True], r'$ie^2(2\delta^{ab}\delta^{cd}-\delta^{ac}\delta^{bd}$'+'\n'+r'$-\delta^{ad}\delta^{bc})g_{\mu\nu}$', 'Unbroken: contact vertex')
    vertex(bottom[2], [r'$\phi_a$', r'$\phi_b$', r'$\phi_c$', r'$\phi_d$'], [False]*4, r'$-i\lambda(\delta^{ab}\delta^{cd}+\delta^{ac}\delta^{bd}$'+'\n'+r'$+\delta^{ad}\delta^{bc})$', 'Unbroken: scalar quartic')
    fig.text(.5, .968, 'Physical scalar interactions of a real triplet Higgs model', ha='center', fontsize=19)
    fig.text(.5, .925, r'Broken phase: $\Phi=(0,0,v+h)$, $v>0$', ha='center', fontsize=16)
    fig.text(.5, .468, r'Unbroken phase: $\Phi=(\phi_1,\phi_2,\phi_3)$, $v=0$; all momenta incoming', ha='center', fontsize=15)
    fig.savefig(Path.cwd()/'paper-53-scalar-vertices.png', facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
