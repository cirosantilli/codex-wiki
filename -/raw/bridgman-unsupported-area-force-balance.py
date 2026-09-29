"""Original functional seal diagram. Tested with Python 3.14 / matplotlib 3.10.7.
Run from _media; the output goes to the current working directory.
No dimensions or construction specifications are implied.
"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch


def arrow(ax, a, b, color, label=None):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle='-|>', mutation_scale=17,
                                linewidth=2, color=color))
    if label:
        ax.text((a[0]+b[0])/2, (a[1]+b[1])/2, label, fontsize=12)


def main():
    plt.rcParams.update({'font.size': 11, 'figure.facecolor': 'white'})
    fig, (ax, free) = plt.subplots(1, 2, figsize=(11, 6), dpi=110,
                                  gridspec_kw={'width_ratios': [1.45, 1]})
    fig.suptitle('Unsupported-area seal: one force, two supporting areas', fontsize=16)
    blue, orange = '#1675aa', '#bb5a17'
    ax.set(xlim=(0, 6.3), ylim=(0, 5.3))
    ax.axis('off')
    ax.set_title('Functional section (not to scale)', pad=12)
    ax.add_patch(Rectangle((1.1, .55), 3.8, 1.15, fc='#e3f3ff', ec=blue))
    ax.text(3, .88, 'Chamber fluid\npressure p relative to exterior', ha='center')
    for x in (.65, 4.9):
        ax.add_patch(Rectangle((x, .55), .45, 3.4, fc='#d2d6da', ec='#555'))
    ax.add_patch(Rectangle((1.1, 1.7), 3.8, .4, fc='#a6b7c6', ec='#374d5e'))
    ax.add_patch(Rectangle((2.6, 2.1), .8, 2.0, fc='#a6b7c6', ec='#374d5e'))
    for x, width in ((1.1, 1.5), (3.4, 1.5)):
        ax.add_patch(Rectangle((x, 2.1), width, .37, fc='#f9d5b4', ec=orange))
        ax.add_patch(Rectangle((x, 2.47), width, .45, fc='#d2d6da', ec='#555'))
    for x in (1.6, 2.15, 3.85, 4.4):
        arrow(ax, (x, 1.12), (x, 1.69), blue)
        arrow(ax, (x, 2.8), (x, 2.12), orange)
    ax.annotate('Closure plug', (3, 1.9), (5.2, 1.55), ha='left',
                arrowprops={'arrowstyle': '-', 'color': '#555'})
    ax.annotate('Annular packing\ncontact area $A_{\\rm seal}$', (4.4, 2.28),
                (4.45, 3.5), ha='center', arrowprops={'arrowstyle': '-'})
    ax.annotate('Retaining support', (1.8, 2.7), (.1, 4.2),
                arrowprops={'arrowstyle': '-'})
    ax.annotate('Stem: projected $A_u$\nno packing contact here', (3, 3.25),
                (2.4, 4.62), ha='center', arrowprops={'arrowstyle': '-'})
    ax.annotate('', (1.1, .3), (4.9, .3), arrowprops={'arrowstyle': '|-|', 'color': blue})
    ax.text(3, .01, 'Full pressure-loaded projected area $A_p$', ha='center', color=blue)
    free.set(xlim=(0, 5), ylim=(0, 5.3))
    free.axis('off')
    free.set_title('Closure plug: axial force balance', pad=12)
    free.add_patch(Rectangle((1.4, 2.2), 2.2, .8, fc='#a6b7c6', ec='#374d5e'))
    free.text(2.5, 2.6, 'Plug', ha='center', va='center')
    arrow(free, (2.5, .9), (2.5, 2.2), blue)
    arrow(free, (2.5, 4.25), (2.5, 3.0), orange)
    free.text(2.75, 1.35, '$p A_p$', color=blue, fontsize=17)
    free.text(2.75, 3.7, '$q A_{\\rm seal}$', color=orange, fontsize=17)
    free.text(2.5, .35, '$p A_p=q A_{\\rm seal}$', ha='center', fontsize=16)
    free.text(2.5, 4.75, '$A_p=A_{\\rm seal}+A_u$', ha='center', fontsize=15)
    fig.text(.5, .035, 'Ideal model: no friction or other axial reactions; q is mean axial packing stress.\nLocal sealing also depends on confinement, deformation and material strength.',
             ha='center', fontsize=11)
    fig.subplots_adjust(left=.04, right=.97, bottom=.16, top=.85, wspace=.15)
    fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
