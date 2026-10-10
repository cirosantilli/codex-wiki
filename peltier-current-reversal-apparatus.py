"""Explain Peltier apparatus and current orientation; no measured values.

Run from _media; emits this script's basename.png to the working directory.
Tested: Python 3.14.4, Matplotlib 3.10.7, NumPy 2.3.5. No extra dependencies.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def main():
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11})
    fig, (a, b) = plt.subplots(1, 2, figsize=(11, 6.4), dpi=120,
                             gridspec_kw={'width_ratios': [1.2, 1]})
    fig.patch.set_facecolor('white')
    for ax in (a, b):
        ax.set(xlim=(0, 10), ylim=(0, 12))
        ax.set_facecolor('white')
        ax.axis('off')

    def box(ax, x, y, w, h, label, color='#eeeeee', size=11):
        ax.add_patch(Rectangle((x, y), w, h, facecolor=color,
                              edgecolor='#374151', lw=1.3))
        ax.text(x+w/2, y+h/2, label, ha='center', va='center', fontsize=size)

    def arrow(ax, start, end, color='#303030', dashed=False):
        ax.annotate('', end, start, arrowprops={'arrowstyle': '-|>',
                    'color': color, 'lw': 1.8, 'linestyle': '--' if dashed else '-'})

    a.text(5, 11.5, 'External thermal assembly', ha='center', weight='bold', fontsize=15)
    a.text(5, 10.85, 'Qualitative CTU arrangement', ha='center', color='#555555')
    box(a, 1.5, 8.7, 5.8, .4, 'Insulating cap', '#f3f4f6', 10)
    box(a, 1.5, 7.1, 5.8, 1.6, 'Water in brass container', '#e8f4fc')
    box(a, 1.5, 6.5, 5.8, .6, 'Copper block', '#f2d4b6', 10)
    box(a, 1.5, 5.45, 5.8, 1.05, 'Thermoelectric cell', '#ece8f7')
    box(a, 1.5, 4.85, 5.8, .6, 'Copper block', '#f2d4b6', 10)
    box(a, 1.5, 3.7, 5.8, 1.15, 'Water-cooled exchanger', '#e8f4fc')
    arrow(a, (.3, 4.1), (1.5, 4.1), '#177eab')
    arrow(a, (7.3, 4.1), (8.4, 4.1), '#177eab')
    a.text(4.4, 3.35, 'External water circuit', ha='center', fontsize=10)
    for y, label in ((6.8, '$T_c$'), (5.13, '$T_h$')):
        a.plot([6.9, 8.3], [y, y], color='#333333')
        a.plot(6.9, y, 'o', ms=4, color='#333333')
        a.text(8.45, y, label, va='center', fontsize=13)
    a.text(8.5, 7.4, 'Thermal\nreadouts', ha='center', fontsize=10)
    a.text(5, 2.8, 'Controlled ±I; measure actual I and U', ha='center', fontsize=11)
    arrow(a, (.9, 6), (1.5, 6), '#713f9a')
    a.plot([.9, .9, 4], [6, 2.4, 2.4], color='#713f9a', lw=1.5)
    a.plot([7.3, 9.35, 9.35, 6], [6, 6, 2.4, 2.4], color='#713f9a', lw=1.5)
    box(a, 3.5, 1.65, 3, .95, 'Supply + meters', '#ffffff', 10)
    arrow(a, (.6, 8), (1.5, 8), '#8b6c23', True)
    a.text(.45, 9.6, 'Ambient\nleak', ha='left', color='#8b6c23', fontsize=10)
    arrow(a, (7.65, 4.7), (7.65, 7.5), '#8b6c23', True)
    a.text(8, 8.8, 'Bypass\nleak', color='#8b6c23', fontsize=10)
    a.text(5, .85, 'Sensor positions schematic; type unspecified.\nDashed leak controls are proposed additions.', ha='center', va='center', fontsize=10)

    b.text(5, 11.5, 'Idealized pair inside a cooler', ha='center', weight='bold', fontsize=15)
    b.text(5, 10.85, 'Positive conventional current: n → p at c', ha='center', fontsize=11)
    box(b, 1.8, 8.5, 6.4, .7, '', '#cfe9f7')
    b.text(5, 8.62, 'Cold bridge, $T_c$', ha='center', va='center', fontsize=11)
    box(b, 2, 4.8, 2, 3.7, 'n\n$S_n$', '#dcebf9', 14)
    box(b, 6, 4.8, 2, 3.7, 'p\n$S_p>S_n$', '#fae2d3', 14)
    box(b, 1.8, 4.2, 2.4, .6, '', '#e8b88d')
    box(b, 5.8, 4.2, 2.4, .6, '', '#e8b88d')
    b.text(5, 3.65, 'Separate hot contacts, both at $T_h$', ha='center', fontsize=10)
    for start, end in (((3, 7), (3, 8)), ((4.25, 8.85), (5.75, 8.85)), ((7, 8), (7, 7))):
        arrow(b, start, end, '#713f9a')
    b.plot([3, 3, 4], [4.2, 2.1, 2.1], color='#713f9a', lw=1.5)
    b.plot([7, 7, 6], [4.2, 2.1, 2.1], color='#713f9a', lw=1.5)
    box(b, 4, 1.65, 2, .9, 'DC source', '#ffffff', 10)
    b.text(3.6, 2.45, '+', fontsize=14, color='#713f9a')
    b.text(6.1, 2.45, '−', fontsize=14, color='#713f9a')
    arrow(b, (5, 10.2), (5, 9.3), '#177eab')
    b.text(5.2, 9.8, '$Q_c$ absorbed', color='#177eab', fontsize=11)
    for x in (2.4, 7.6):
        arrow(b, (x, 4.2), (x, 3.1), '#ba4c21')
    b.text(5, 2.9, '$Q_h$ rejected (sum)', color='#ba4c21', ha='center', fontsize=11)
    b.text(5, .85, 'Reverse I: junction heat reverses.\nJoule heating does not.', ha='center', va='center', fontsize=11)
    fig.subplots_adjust(left=.015, right=.985, bottom=.02, top=.99, wspace=.10)
    fig.savefig(Path(__file__).stem+'.png', facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
