"""Original torsion-balance schematic; illustrative geometry, not measured data.

Tested with Python 3.14.4, matplotlib 3.10.7, numpy 2.3.5.
Run from _media: MPLCONFIGDIR=/tmp/codex-wiki-matplotlib python3 ../torsion-balance-readout.py
Writes the matching opaque white PNG basename to the current working directory.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Circle, Rectangle
import numpy as np

BLUE = '#245a91'
ORANGE = '#b74b16'
GREEN = '#197149'
GRAY = '#6b7280'


def arrow(ax, start, end, color):
    ax.annotate('', xy=end, xytext=start, arrowprops={'arrowstyle': '-|>', 'color': color, 'lw': 2.1, 'mutation_scale': 14})


def rotor(ax, beta):
    v = np.array([np.cos(beta), np.sin(beta)])
    ax.plot([-v[0], v[0]], [-v[1], v[1]], color=BLUE, lw=4)
    for sign in (-1, 1):
        ax.add_patch(Circle(sign*v, .075, facecolor=BLUE, edgecolor=BLUE))
    ax.add_patch(Circle((0, 0), .045, facecolor='black'))
    ax.plot([-1.25, 1.35], [0, 0], '--', color=GRAY, lw=1.1, zorder=0)
    tangent = np.array([-v[1], v[0]])
    for sign in (-1, 1):
        start = sign*v
        arrow(ax, start, start+sign*.58*tangent, ORANGE)
    return v


def main():
    plt.rcParams.update({'font.size': 11, 'figure.facecolor': 'white', 'axes.facecolor': 'white'})
    fig, axes = plt.subplots(1, 3, figsize=(11.4, 4.7))
    fig.subplots_adjust(left=.025, right=.98, top=.77, bottom=.14, wspace=.24)
    fig.suptitle('Torsion balance: convert a weak torque into a twist', fontsize=17, y=.97)
    fig.text(.5, .88, 'Original ideal schematic • angles exaggerated • no measured data', ha='center', color=GRAY)
    for ax in axes:
        ax.set_aspect('equal')
        ax.axis('off')
        ax.set_xlim(-1.55, 1.55)
        ax.set_ylim(-.9, 2.05)
    ax = axes[0]
    ax.set_title('Suspension (side view)', pad=10)
    ax.add_patch(Rectangle((-.35, 1.7), .70, .12, color=GRAY))
    ax.plot([0, 0], [.1, 1.7], color=GREEN, lw=2.3)
    ax.plot([-1, 1], [.1, .1], color=BLUE, lw=4)
    ax.add_patch(Circle((-1, .1), .075, color=BLUE))
    ax.add_patch(Circle((1, .1), .075, color=BLUE))
    ax.text(.1, 1.68, 'top attachment', va='top', fontsize=10)
    ax.text(.16, .95, 'thin elastic fiber', color=GREEN, fontsize=10)
    ax.text(0, -.12, 'suspended body', color=BLUE, ha='center', fontsize=10)
    arrow(ax, (-1.24, 1.02), (-1.24, 1.52), GRAY)
    ax.text(-1.13, 1.25, 'vertical\nrotation axis', fontsize=9, va='center')
    ax.text(0, -.63, 'Weight is supported;\naxial torque twists the fiber.', ha='center', fontsize=10)

    ax = axes[1]
    ax.set_title('Deflection (top view)', pad=10)
    beta = np.deg2rad(25)
    v = rotor(ax, beta)
    ax.add_patch(Arc((0, 0), .94, .94, theta1=0, theta2=25, color=GREEN, lw=1.8))
    ax.text(.65, .13, r'$\beta=\theta$', color=GREEN)
    ax.text(1.05, .96, r'$F$', color=ORANGE, fontsize=13)
    ax.text(-1.19, -.74, r'$F$', color=ORANGE, fontsize=13)
    ax.text(-.12, .35, r'$a$', color=BLUE)
    ax.text(0, 1.55, r'Top fixed: $\alpha=0$', ha='center')
    ax.text(0, 1.12, r'Applied $\tau=\kappa\beta>0$', color=ORANGE, ha='center')
    ax.text(0, -.79, r'Fiber torque $=-\kappa\beta$', color=GREEN, ha='center')

    ax = axes[2]
    ax.set_title('Null readout (top view)', pad=10)
    rotor(ax, 0)
    ax.text(1.08, .60, r'$F$', color=ORANGE, fontsize=13)
    ax.text(-1.2, -.72, r'$F$', color=ORANGE, fontsize=13)
    ax.text(0, .88, r'Body held at $\beta=0$', ha='center', color=BLUE)
    # The dial is shown separately above the body, not as another physical rod.
    center = np.array([0., 1.56])
    ax.add_patch(Circle(center, .29, fill=False, edgecolor=GRAY, lw=1.1))
    ax.plot([0, .25], [1.56, 1.56], '--', color=GRAY, lw=1)
    end = center+.25*np.array([np.cos(-beta), np.sin(-beta)])
    ax.plot([center[0], end[0]], [center[1], end[1]], color=GREEN, lw=2)
    ax.add_patch(Arc(center, .41, .41, theta1=-25, theta2=0, color=GREEN, lw=1.6))
    ax.text(.4, 1.53, r'$\alpha<0$', color=GREEN, va='center')
    ax.text(-.39, 1.88, 'top dial', color=GRAY, fontsize=9)
    ax.text(0, -.79, r'Twist $\theta=\beta-\alpha=-\alpha$', color=GREEN, ha='center')
    fig.text(.5, .035, r'Positive torque is counterclockwise; at equilibrium $\tau_{\mathrm{ext}}=\kappa(\beta-\alpha)$.', ha='center', fontsize=11)
    fig.savefig(Path(__file__).with_suffix('.png').name, dpi=110, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
