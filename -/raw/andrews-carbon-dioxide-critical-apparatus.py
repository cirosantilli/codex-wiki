"""Functional schematic based on Andrews (1869), pp. 576–583 and Plate LXIII.

Original diagram, not a scale reconstruction or digitization of the historical plate.
Python 3.14; Matplotlib 3.10. Run from _media with MPLBACKEND=Agg.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


BLUE = '#176baa'
GRAY = '#7f8791'


def sample(ax, x, bottom, top, split=None):
    ax.add_patch(Rectangle((x, bottom), .58, top-bottom, facecolor='#fff7e5',
                           edgecolor='#333333', lw=1.5))
    if split is not None:
        ax.add_patch(Rectangle((x+.015, bottom), .55, split-bottom,
                               facecolor='#7dc5e7', edgecolor='none'))
        ax.plot([x+.02, x+.56], [split, split], color=BLUE, lw=2)


def main():
    plt.rcParams.update({'font.size': 10, 'figure.facecolor': 'white'})
    fig, (app, infer) = plt.subplots(1, 2, figsize=(11, 5.5),
                                   gridspec_kw={'width_ratios': [1.25, 1]}, layout='constrained')
    app.set(xlim=(0, 7.1), ylim=(0, 7.7))
    app.axis('off')
    app.set_title('Control and readout: coupled pressure apparatus', fontsize=11, pad=12)
    # Two pressure bodies joined by a water-filled manifold.
    for x in (1.25, 4.75):
        app.add_patch(Rectangle((x-.32, 1.15), 1.22, 1.9, facecolor='#dbeef8',
                                edgecolor='#855c3b', lw=3))
        app.add_patch(Rectangle((x, 2.35), .58, 3.65, facecolor='white',
                                edgecolor='#333333', lw=1.5))
        app.add_patch(Rectangle((x+.02, 2.35), .54, 1.2, facecolor=GRAY, edgecolor='none'))
        app.add_patch(Rectangle((x-.22, 3.25), 1.02, 3, facecolor='#dbeef8',
                                edgecolor=BLUE, alpha=.45))
        app.add_patch(Rectangle((x+.19, .5), .2, 1.45, facecolor='#555555', edgecolor='black'))
        app.plot([x-.05, x+.63], [.5, .5], color='#333333', lw=4)
        app.annotate('', xy=(x+.29, 1.55), xytext=(x+.29, .72),
                     arrowprops={'arrowstyle': '->', 'lw': 1.6, 'color': 'black'})
    app.plot([2.15, 4.43], [1.8, 1.8], color='#855c3b', lw=13, solid_capstyle='butt')
    app.plot([2.15, 4.43], [1.8, 1.8], color='#dbeef8', lw=7, solid_capstyle='butt')
    sample(app, 1.25, 3.55, 6, split=4.35)
    sample(app, 4.75, 3.55, 6)
    app.text(1.54, 6.6, 'CO₂ sample', ha='center', weight='bold')
    app.text(5.04, 6.6, 'Air gauge', ha='center', weight='bold')
    app.text(3.25, .15, 'Steel screws compress the water', ha='center')
    app.text(3.3, 1.04, 'Shared water\npressure circuit', ha='center', fontsize=9)
    app.annotate('Mercury transmits\nthe load', xy=(1.52, 2.8), xytext=(2.7, 2.8),
                 fontsize=9, arrowprops={'arrowstyle': '->', 'color': GRAY})
    app.annotate('Flowing-water jackets\nset temperatures separately', xy=(4.55, 5.4),
                 xytext=(3.5, 7.1), ha='center', fontsize=9,
                 arrowprops={'arrowstyle': '->', 'color': BLUE})
    app.annotate('Optical column readings\n→ calibrated volumes', xy=(1.55, 5),
                 xytext=(2.7, 4.3), fontsize=9,
                 arrowprops={'arrowstyle': '->', 'color': '#333333'})
    infer.set(xlim=(0, 6), ylim=(0, 7.7))
    infer.axis('off')
    infer.set_title('What the observations distinguish', fontsize=11, pad=12)
    sample(infer, .8, 4.1, 6.4, split=5.15)
    infer.text(2.05, 6.1, 'Below Tc', weight='bold')
    infer.text(2.05, 5.65, 'Gas and liquid coexist')
    infer.text(2.05, 5.05, 'Visible meniscus', color=BLUE)
    infer.annotate('', xy=(1.45, 5.15), xytext=(1.95, 5.15),
                   arrowprops={'arrowstyle': '->', 'color': BLUE})
    sample(infer, .8, .95, 3.25)
    infer.add_patch(Rectangle((.815, .95), .55, 2.3, facecolor='#bdddec', edgecolor='none'))
    infer.text(2.05, 2.95, 'Above Tc', weight='bold')
    infer.text(2.05, 2.4, 'One fluid phase')
    infer.text(2.05, 1.85, 'Compression can raise density\nwithout a phase boundary')
    infer.text(3, .12, 'No meniscus alone is insufficient:\na subcritical phase can also run out.',
               ha='center', color='#555555', fontsize=9)
    fig.suptitle('Andrews’s 1869 carbon dioxide experiment — functional schematic', fontsize=13)
    fig.savefig(Path(__file__).stem + '.png', dpi=120, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
