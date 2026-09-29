"""Original Laue apparatus schematic and calculated reciprocal-space slice.

Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7. Apparatus roles follow Friedrich,
Knipping and Laue (1912), pp.311–318; layout is deliberately not a reconstruction.
Bottom: chosen primitive cubic lattice, k_out=k_in+G, angular convention 2*pi/a.
Run from _media, emitting this script's basename.png to the working directory.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle


def arrow(ax, start, end, color, **kwargs):
    ax.annotate('', xy=end, xytext=start,
                arrowprops={'arrowstyle': '-|>', 'lw': 2, 'color': color, **kwargs})


def draw():
    plt.rcParams.update({'font.size': 11})
    fig = plt.figure(figsize=(10.2, 8.2), layout='constrained', facecolor='white')
    grid = fig.add_gridspec(2, 2, height_ratios=[1, 1.2])
    top = fig.add_subplot(grid[0, :])
    top.set(xlim=(-5, 6.8), ylim=(-2.35, 2.2))
    top.axis('off')
    top.set_title('Transmission Laue geometry: apparatus roles, schematic dimensions', fontsize=13)
    top.add_patch(Rectangle((-4.8, -0.45), 1.1, .9, fc='#e6edf5', ec='#284b63'))
    top.text(-4.25, 0, 'X-ray\ntube', ha='center', va='center')
    for z in (-2.9, -2.0, -1.1):
        for y in (-1.0, 0.12):
            top.add_patch(Rectangle((z, y), .14, .88, fc='#64748b'))
    top.text(-2.0, 1.28, 'Lead apertures\nrestrict beam / stray radiation', ha='center', fontsize=10)
    arrow(top, (-3.7, 0), (-.2, 0), '#b94825')
    top.text(-2.0, -1.27, 'Broad spectrum; propagation +z', ha='center', fontsize=10)
    top.add_patch(Rectangle((-.13, -.46), .26, .92, angle=0, fc='#a9dacc', ec='#15745e'))
    top.add_patch(Circle((0, -.68), .19, fill=False, ec='#15745e'))
    top.text(.25, -1.35, 'Single crystal\non goniometer', ha='center')
    top.plot([5.0, 5.0], [-1.5, 1.5], color='#27374b', lw=5)
    top.text(5.0, 1.69, 'Photographic plate', ha='center')
    arrow(top, (.18, 0), (4.95, 0), '#b94825')
    for endpoint in (1.1, -.9):
        arrow(top, (.12, 0), (4.94, endpoint), '#267f8e')
        top.plot(5, endpoint, 'o', color='#267f8e', ms=7)
    top.plot(5, 0, '+', color='#b94825', ms=10, mew=2)
    top.text(5.25, 0, 'Direct\nbeam', va='center', fontsize=10)
    top.text(2.4, 1.05, 'Diffracted directions\n→ separate spots', ha='center', color='#216575')
    top.annotate('', xy=(5, -1.85), xytext=(0, -1.85),
                 arrowprops={'arrowstyle': '<->', 'color': '#526074'})
    top.text(2.5, -2.12, 'Plate distance L; position X = L sₓ / s_z', ha='center', fontsize=10)

    left = fig.add_subplot(grid[1, 0])
    right = fig.add_subplot(grid[1, 1])
    # G coordinates in units 2*pi/a; center is -k_in, all spheres pass through O.
    for ax, wavelength, label in ((left, .160, 'This wavelength satisfies (2,0,−1)'),
                                  (right, .100, 'Another wavelength selects other points')):
        radius = .4 / wavelength
        xx, zz = np.meshgrid(np.arange(-4, 5), np.arange(-8, 2))
        ax.scatter(xx, zz, s=14, c='#a3adb9', zorder=2)
        ax.add_patch(Circle((0, -radius), radius, fill=False, ec='#287c8e', lw=2))
        ax.plot(0, -radius, 'x', color='#287c8e')
        ax.plot(0, 0, 'o', color='#26374b', ms=6)
        ax.plot(2, -1, 'o', ms=8, mfc='#e87935', mec='#713f12', zorder=4)
        arrow(ax, (0, -radius), (0, 0), '#b94825')
        arrow(ax, (0, 0), (2, -1), '#e87935')
        if wavelength == .160:
            arrow(ax, (0, -radius), (2, -1), '#287c8e')
            ax.text(.22, -2.4, r'$\mathbf{k}_{out}$', fontsize=10)
        else:
            ax.text(.2, -4.6, 'Orange point\noff this sphere', fontsize=10)
        ax.text(-1.5, -.65, r'$\mathbf{k}_{in}$', fontsize=10)
        ax.text(1.1, -.35, r'$\mathbf{G}$', color='#96440a', fontsize=11)
        ax.set(xlim=(-4.5, 4.5), ylim=(-8.5, 1), aspect='equal',
               xlabel=r'$G_x$ (units $2\pi/a$)', ylabel=r'$G_z$ (units $2\pi/a$)',
               title=f'λ = {wavelength:.3f} nm\n{label}')
        ax.tick_params(labelsize=9)
        ax.set_xticks([-4, -2, 0, 2, 4])
        ax.set_yticks([-8, -6, -4, -2, 0])
    fig.suptitle('A fixed crystal selects different wavelengths into different directions', fontsize=15)
    fig.supxlabel('Reciprocal-space slice: Gᵧ = 0, a = 0.400 nm; sphere center −kᵢₙ, radius |kᵢₙ|.\n'
                  'White beam supplies a continuous family of radii. Original schematic and calculated slice.', fontsize=10)
    fig.savefig(Path(__file__).stem + '.png', dpi=110, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    draw()
