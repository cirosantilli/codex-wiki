"""Original normal-mode schematic; write the PNG to the current directory."""
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch
import numpy as np


def main():
    fig, axes = plt.subplots(1, 3, figsize=(10.2, 3.6), facecolor='white')
    directions = np.pi / 2 + np.arange(3) * 2 * np.pi / 3
    names = ['Horizontal translation', 'Vertical translation', 'Rotation about the centre']
    shifts = [np.array([0.20, 0.0]), np.array([0.0, 0.20]), np.array([0.0, 0.0])]
    for index, (ax, name, shift) in enumerate(zip(axes, names, shifts)):
        angle = 0.26 if index == 2 else 0
        ax.add_patch(Circle((0, 0), 0.53, fill=False, ec='0.5', ls='--', lw=1.3))
        ax.add_patch(Circle(shift, 0.53, fc='#dcecf9', ec='#265b87', lw=1.8, alpha=0.85))
        for phi in directions:
            anchor = 1.28 * np.array([np.cos(phi), np.sin(phi)])
            contact = shift + 0.53 * np.array([np.cos(phi + angle), np.sin(phi + angle)])
            delta = anchor - contact
            tangent = np.array([-delta[1], delta[0]]) / np.linalg.norm(delta)
            t = np.linspace(0, 1, 160)
            wiggle = 0.042 * np.sin(12 * np.pi * t) * np.sin(np.pi * t)
            spring = contact[:, None] + delta[:, None] * t + tangent[:, None] * wiggle
            ax.plot(*spring, color='0.3', lw=1.3)
            ax.plot(*anchor, 'ks', ms=5)
            ax.plot(*contact, 'o', color='#265b87', ms=4)
        if index < 2:
            vector = np.array([0.7, 0]) if index == 0 else np.array([0, 0.7])
            ax.add_patch(FancyArrowPatch(-vector / 2, vector / 2,
                                         arrowstyle='<->', mutation_scale=15,
                                         color='#bd4f26', lw=2.2))
        else:
            ax.add_patch(FancyArrowPatch((0.27, 0.03), (-0.22, 0.15),
                                         connectionstyle='arc3,rad=0.7',
                                         arrowstyle='<->', mutation_scale=14,
                                         color='#bd4f26', lw=2.2))
            ax.plot([0, 0.4 * np.cos(angle)], [0, 0.4 * np.sin(angle)], color='#265b87', lw=2)
        ax.set_title(name, fontsize=11)
        ax.text(0, -1.30, 'Same frequency' if index < 2 else 'Separate frequency',
                ha='center', fontsize=10)
        ax.set_aspect('equal')
        ax.set(xlim=(-1.42, 1.42), ylim=(-1.45, 1.55))
        ax.axis('off')
    fig.subplots_adjust(left=0.025, right=0.975, bottom=0.03, top=0.88, wspace=0.12)
    fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), dpi=120,
                facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
