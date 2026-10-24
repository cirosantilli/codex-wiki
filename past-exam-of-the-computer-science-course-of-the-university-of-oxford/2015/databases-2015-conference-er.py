#!/usr/bin/env python3
"""Render the conference design; writes a deterministic opaque PNG in cwd.

Tested with the repository Python 3.14 environment and existing Matplotlib.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle

OUTPUT = 'databases-2015-conference-er.png'


def main():
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11,
                         'savefig.facecolor': 'white', 'figure.facecolor': 'white'})
    fig, ax = plt.subplots(figsize=(14, 9), dpi=110)
    fig.subplots_adjust(left=.02, right=.98, bottom=.02, top=.98)
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 9)
    ax.axis('off')
    edge = '#28475b'

    def box(x, y, w, h, title, attributes, shade='#edf5fa'):
        ax.add_patch(Rectangle((x, y), w, h, ec=edge, fc=shade, lw=1.6, zorder=3))
        ax.plot([x, x+w], [y+h-.47]*2, color=edge, lw=1, zorder=4)
        ax.text(x+w/2, y+h-.235, title, ha='center', va='center', weight='bold', zorder=5)
        ax.text(x+.15, y+h-.64, '\n'.join(attributes), va='top', linespacing=1.45,
                fontsize=10.5, zorder=5)

    def line(points, label=None, at=None):
        xs, ys = zip(*points)
        ax.plot(xs, ys, color=edge, lw=1.5, zorder=1)
        if label:
            ax.text(*at, label, ha='center', va='center', fontsize=10.5,
                    bbox={'facecolor':'white', 'edgecolor':'none', 'pad':1.5}, zorder=6)

    def card(x, y, text, ha='center'):
        ax.text(x, y, text, ha=ha, va='center', fontsize=10, color='#123f5a',
                bbox={'facecolor':'white', 'edgecolor':'none', 'pad':.5}, zorder=6)

    ax.text(7, 8.76, 'Conference bookings and event locations', ha='center',
            weight='bold', fontsize=16)
    box(.2, 6.2, 3.35, 2.1, 'Customer',
        ['PK: customerid', 'name', 'contactPhone', 'billingAddress'])
    box(5.15, 6.2, 3.2, 2.1, 'Conference', ['PK: conferenceid'])
    box(10.05, 6.2, 3.7, 2.1, 'Event',
        ['Local identifier: eventNo', 'startTime (timestamp)', 'endTime (timestamp)',
         'Full key: conferenceid + eventNo'])
    line([(3.55, 7.25), (5.15, 7.25)], 'books', (4.35, 7.6))
    card(3.73, 7.02, '1')
    card(4.88, 7.02, '0..*')
    line([(8.35, 7.25), (10.05, 7.25)], 'contains', (9.2, 7.6))
    card(8.53, 7.02, '1')
    card(9.78, 7.02, '1..*')

    # EER convention: total specialization (double line), disjoint (d).
    line([(6.69, 6.2), (6.69, 5.56)])
    line([(6.81, 6.2), (6.81, 5.56)])
    ax.add_patch(Circle((6.75, 5.3), .27, ec=edge, fc='white', lw=1.5, zorder=4))
    ax.text(6.75, 5.3, 'd', ha='center', va='center', weight='bold', zorder=5)
    line([(6.54, 5.12), (4.4, 4.5)])
    line([(6.96, 5.12), (8.7, 4.5)])
    box(2.5, 3.1, 3.8, 1.4, 'SingleDay',
        ['Inherited PK: conferenceid', 'heldDate'], '#f0f6e9')
    box(6.95, 3.1, 3.5, 1.4, 'MultiDay',
        ['Inherited PK: conferenceid', 'Events may span dates'], '#f0f6e9')
    ax.text(2.8, 2.55, 'All events share one room.\nEvery timestamp is on heldDate.',
            ha='center', va='center', fontsize=10, color='#31532a')

    box(10.05, .8, 3.7, 1.9, 'Venue (room)', ['PK: venueid', 'name', 'capacity'])
    box(5.15, .8, 3.2, 1.9, 'Building', ['PK: buildingid'])
    line([(11.9, 6.2), (11.9, 2.7)], 'held at', (11.9, 4.55))
    card(12.23, 5.93, '0..*')
    card(12.12, 2.99, '1')
    line([(8.35, 1.75), (10.05, 1.75)], 'contains', (9.2, 2.1))
    card(8.53, 1.5, '1')
    card(9.78, 1.5, '0..*')
    ax.text(.25, 1.65, 'PK = primary key\nEndpoint labels count that entity.\nEvery conference has one customer\nand at least one event.',
            va='center', fontsize=10.5, linespacing=1.55)
    ax.text(7, .25, 'Total, disjoint specialization: each conference is exactly one of SingleDay and MultiDay.',
            ha='center', va='center', fontsize=10.5)
    fig.savefig(Path.cwd()/OUTPUT, dpi=110, metadata={'Software':'codex-wiki figure generator'})
    plt.close(fig)


if __name__ == '__main__':
    main()
