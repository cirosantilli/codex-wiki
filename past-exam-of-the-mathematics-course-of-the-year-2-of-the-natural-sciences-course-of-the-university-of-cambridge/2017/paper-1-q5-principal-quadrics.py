"""Original principal-axis quadric examples. Save PNG to cwd."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    fig = plt.figure(figsize=(12, 4.8))
    fig.subplots_adjust(left=0.01, right=0.98, bottom=0.12, top=0.88, wspace=0.16)
    theta = np.linspace(0, 2*np.pi, 64)
    phi = np.linspace(0, np.pi, 35)
    th, ph = np.meshgrid(theta, phi)
    longitudinal, tt = np.meshgrid(np.linspace(-1.55, 1.55, 42), theta)
    examples = [
        (np.cos(th)*np.sin(ph), np.sin(th)*np.sin(ph)/np.sqrt(3), np.cos(ph),
         '#4477aa', r'$a=1$: ellipsoid'),
        (longitudinal, np.cos(tt)/2, np.sin(tt),
         '#228833', r'$a=2$: elliptic cylinder'),
        (longitudinal, np.sqrt(1+longitudinal**2)*np.cos(tt)/np.sqrt(5),
         np.sqrt(1+longitudinal**2)*np.sin(tt), '#aa5577', r'$a=3$: one-sheet hyperboloid'),
    ]
    for index, (xx, yy, zz, color, title) in enumerate(examples, 1):
        ax = fig.add_subplot(1, 3, index, projection='3d')
        ax.plot_surface(xx, yy, zz, color=color, alpha=0.8, linewidth=0, shade=True)
        ax.set(xlabel=r'$X$', ylabel=r'$Y$', title=title,
               xlim=(-1.65, 1.65), ylim=(-1.0, 1.0), zlim=(-1.9, 1.9))
        ax.text2D(0.94, 0.52, r'$Z$', transform=ax.transAxes, fontsize=11)
        ax.set_title(title, fontsize=11)
        ax.xaxis.labelpad = 1
        ax.yaxis.labelpad = 1
        ax.tick_params(labelsize=9, pad=1)
        ax.set_xticks([-1, 0, 1])
        ax.set_yticks([-1, 0, 1])
        ax.set_zticks([-1, 0, 1])
        ax.set_box_aspect((1.0, 0.65, 1.1))
        ax.view_init(elev=19, azim=-55)
        for axis in [ax.xaxis, ax.yaxis, ax.zaxis]:
            axis.pane.set_facecolor('white')
            axis.pane.set_alpha(0.2)
        ax.grid(False)
    fig.savefig(Path.cwd() / 'paper-1-q5-principal-quadrics.png', dpi=150, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
