"""Original nondispersive Cherenkov construction. Python 3.14, NumPy 2.3.5,
Matplotlib 3.10.7. Run from _media; output is this script's basename.png.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Circle


def main():
    beta, n = 0.9, 1.5
    r = 1 / (beta * n)  # distance unit = v*Delta t
    theta = np.arccos(r)
    q = np.array([r*r, r*np.sqrt(1-r*r)])
    p = np.array([1.0, 0.0])
    fig, ax = plt.subplots(figsize=(9.6, 5.3), dpi=130, facecolor='white')
    for center in np.linspace(0, 0.85, 6):
        ax.add_patch(Circle((center, 0), r*(1-center), fill=False,
                            color='#8eacc3', lw=1.2))
    for sign in [1, -1]:
        ax.plot([1, 0.12], [0, sign*0.88*r/np.sqrt(1-r*r)],
                color='#007c83', lw=2.4)
    ax.annotate('', (1.32, 0), (-0.85, 0),
                arrowprops=dict(arrowstyle='->', lw=1.5, color='#333333'))
    ax.annotate('', q, (0, 0),
                arrowprops=dict(arrowstyle='->', lw=2.5, color='#c45121'))
    ax.plot([q[0], 1], [q[1], 0], color='#007c83', lw=2.4)
    ax.add_patch(Arc((0, 0), .50, .50, theta1=0,
                     theta2=np.degrees(theta), color='#c45121', lw=1.8))
    eta = 90-np.degrees(theta)
    ax.add_patch(Arc((1, 0), .43, .43, theta1=180-eta,
                     theta2=180, color='#007c83', lw=1.5))
    # Right-angle marker at the tangency point.
    a = -q/np.linalg.norm(q)*.055
    b = (p-q)/np.linalg.norm(p-q)*.055
    marker = np.array([q+a, q+a+b, q+b])
    ax.plot(marker[:, 0], marker[:, 1], color='#444444', lw=1)
    ax.scatter([0, 1, q[0]], [0, 0, q[1]], color='#333333', s=23, zorder=5)
    ax.text(-.03, -.12, 'O: earlier position', ha='center', fontsize=10)
    ax.text(1.05, -.12, 'P: charge now', ha='left', fontsize=10)
    ax.text(q[0]+.025, q[1]+.03, 'Q: tangency', fontsize=10)
    ax.text(.23, .08, r'$\theta$', color='#c45121', fontsize=14)
    ax.text(.73, .075, r'$\eta$', color='#007c83', fontsize=14)
    ax.text(.08, .39, r'wave normal $\mathbf{k}$', color='#c45121',
            rotation=np.degrees(theta), fontsize=11)
    ax.text(-.66, .86, 'Tangent envelope\n(cone in 3D)', color='#007c83', fontsize=11)
    ax.text(.50, -.25, r'$OP=v\,\Delta t,\quad OQ=(c/n)\,\Delta t$',
            ha='center', fontsize=12)
    ax.text(.50, -1.18,
            r'$\cos\theta=OQ/OP=1/(\beta n)$'+'\n'
            + rf'Chosen $\beta=0.90$, $n=1.50$: $\theta={np.degrees(theta):.2f}^\circ$, '
            + rf'$\eta={eta:.2f}^\circ$', ha='center', fontsize=12)
    ax.set_title('A charge outruns phase fronts in a transparent medium', fontsize=15, pad=15)
    ax.text(.50, 1.13, 'Original constant-index construction; circles are phase fronts, not particle paths',
            ha='center', fontsize=10, color='#444444')
    ax.set_aspect('equal')
    ax.set_xlim(-.85, 1.65)
    ax.set_ylim(-1.36, 1.20)
    ax.axis('off')
    fig.tight_layout()
    fig.savefig(Path(__file__).stem+'.png', facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
