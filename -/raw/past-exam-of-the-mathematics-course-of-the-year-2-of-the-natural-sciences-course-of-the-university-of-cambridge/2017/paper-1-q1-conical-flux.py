"""Original open-cone diagram. Save the white PNG in the working directory."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    fig = plt.figure(figsize=(6.5, 5.0))
    fig.subplots_adjust(left=0.04, right=0.94, bottom=0.07, top=0.88)
    ax = fig.add_subplot(111, projection='3d')
    theta, z = np.meshgrid(np.linspace(0, 2*np.pi, 55), np.linspace(0, 1, 20))
    radius = np.sqrt(2)*z
    ax.plot_surface(radius*np.cos(theta), radius*np.sin(theta), z,
                    color='#77aadd', alpha=0.48, linewidth=0, shade=True)
    ring = np.linspace(0, 2*np.pi, 240)
    ax.plot(np.sqrt(2)*np.cos(ring), np.sqrt(2)*np.sin(ring), np.ones_like(ring),
            ls='--', color='#555555', lw=1.4)
    ax.plot([0, 0], [0, 0], [0, 1], ':', color='#777777', lw=1)
    ax.scatter([0], [0], [0], color='#111111', s=15)
    # A lateral normal has an outward radial and a downward axial component.
    azimuth = -np.pi/2
    zz = 0.57
    point = np.array([np.sqrt(2)*zz*np.cos(azimuth), np.sqrt(2)*zz*np.sin(azimuth), zz])
    normal = np.array([np.cos(azimuth), np.sin(azimuth), -np.sqrt(2)])/np.sqrt(3)
    ax.quiver(*point, *normal, length=0.45, color='#aa3344', linewidth=2, arrow_length_ratio=0.22)
    label = point+0.55*normal
    ax.text(*label, r'$\mathbf{n}_{\rm out}$', color='#aa3344', fontsize=11)
    ax.text2D(0.5, 0.90, r'Open rim: radius $\sqrt{2}h$', transform=ax.transAxes, ha='center', fontsize=10)
    ax.set(xlabel=r'$x/h$', ylabel=r'$y/h$', zlabel=r'$z/h$',
           title='Lateral cone; the top disk is not part of the surface',
           xlim=(-1.65, 1.65), ylim=(-1.65, 1.65), zlim=(0, 1.25))
    ax.set_zticks([0, 1], ['0', '1'])
    ax.set_box_aspect((1, 1, 0.75))
    ax.view_init(elev=23, azim=-56)
    for axis in [ax.xaxis, ax.yaxis, ax.zaxis]:
        axis.pane.set_facecolor('white')
        axis.pane.set_alpha(0.2)
    ax.set_title('Lateral cone; the top disk is not part of the surface', fontsize=11)
    ax.grid(False)
    fig.savefig(Path.cwd() / 'paper-1-q1-conical-flux.png', dpi=150, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
