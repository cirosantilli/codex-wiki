"""Original transmission Laue positions; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

One point scatterer per primitive cubic cell, a=0.400 nm. Incident direction
is lab +z; G=(2*pi/a) R(h,k,l). Elasticity gives lambda=-2*a*v_z/|v|²,
v=R(h,k,l), and s_out=z_hat+(lambda/a)*v. Only forward rays landing on
a square detector at z=50 mm are retained. Marker area is NOT intensity.
Run from _media; output is this script's basename.png in the working directory.
"""
from pathlib import Path
import itertools
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize

A = 0.400
BAND = (0.080, 0.160)
DISTANCE = 50.0
HALF_WIDTH = 75.0


def rotation_y(degrees):
    t = np.deg2rad(degrees)
    return np.array([[np.cos(t), 0, np.sin(t)], [0, 1, 0],
                     [-np.sin(t), 0, np.cos(t)]])


def reflections(degrees=0.0):
    """Return (indices, wavelength_nm, outgoing_unit_direction, position_mm)."""
    rotation = rotation_y(degrees)
    # |G| <= 2|k| implies |(h,k,l)| <= 2a/lambda_min, in any orientation.
    bound = int(np.ceil(2 * A / BAND[0]))
    result = []
    for indices in itertools.product(range(-bound, bound + 1), repeat=3):
        v = rotation @ np.array(indices, dtype=float)
        square = float(v @ v)
        if square == 0:
            continue
        wavelength = -2 * A * v[2] / square
        if not BAND[0] - 1e-12 <= wavelength <= BAND[1] + 1e-12:
            continue
        outgoing = np.array([0., 0., 1.]) + wavelength / A * v
        assert abs(outgoing @ outgoing - 1) < 1e-12
        if outgoing[2] <= 1e-12:
            continue
        xy = DISTANCE * outgoing[:2] / outgoing[2]
        if np.max(np.abs(xy)) <= HALF_WIDTH + 1e-10:
            result.append((indices, wavelength, outgoing, xy))
    return result


def draw():
    plt.rcParams.update({'font.size': 11, 'axes.titlesize': 12})
    fig, axes = plt.subplots(1, 2, figsize=(10.6, 5.7), layout='constrained',
                             facecolor='white')
    norm = Normalize(*BAND)
    for ax, tilt in zip(axes, (0.0, 7.0)):
        rows = reflections(tilt)
        xy = np.array([r[3] for r in rows])
        wavelengths = np.array([r[1] for r in rows])
        # Longer wavelengths first: any exact harmonic overlap remains one spot.
        order = np.argsort(wavelengths)[::-1]
        scatter = ax.scatter(xy[order, 0], xy[order, 1], c=wavelengths[order],
                             cmap='viridis', norm=norm, s=32, linewidths=0.4,
                             edgecolors='#243041')
        ax.plot(0, 0, '+', color='#c44e2a', ms=11, mew=1.8)
        ax.set(xlim=(-80, 80), ylim=(-80, 80), aspect='equal',
               xlabel='Plate X (mm)', ylabel='Plate Y (mm)',
               title='[001] along beam' if tilt == 0 else 'Same crystal tilted 7° about lab y')
        ax.set_xticks([-75, -50, -25, 0, 25, 50, 75])
        ax.set_yticks([-75, -50, -25, 0, 25, 50, 75])
        ax.grid(alpha=0.16)
        if tilt == 0:
            ax.annotate(r'$(2,1,-1)$' + '\nλ = 0.1333 nm', (50, 25), (8, 45),
                        fontsize=10, arrowprops={'arrowstyle': '->', 'color': '#243041'})
    bar = fig.colorbar(scatter, ax=axes, shrink=0.79, pad=0.02)
    bar.set_label('Selected wavelength λ (nm)')
    fig.suptitle('Calculated white-beam Laue spots — chosen primitive cubic lattice',
                 fontsize=14)
    fig.supxlabel('a = 0.400 nm  •  λ = 0.080–0.160 nm  •  plate distance = 50 mm\n'
                  'Equal-size position markers; colors label wavelengths, not intensity.\n'
                  '+ direct beam; harmonic reflections can coincide. Not an experimental plate.',
                  fontsize=10)
    fig.savefig(Path(__file__).stem + '.png', dpi=110, facecolor='white', transparent=False)
    plt.close(fig)
    print({f'tilt_{t:g}_reflections': len(reflections(t)) for t in (0.0, 7.0)})


if __name__ == '__main__':
    draw()
