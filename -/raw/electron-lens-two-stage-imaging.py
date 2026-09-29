"""Original ideal electron-lens relay; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

Run from _media. Emits the matching PNG to the current directory.
The invented geometry omits magnetic image rotation and aberrations.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle
import numpy as np


def main():
    plt.rcParams.update({'font.size': 11, 'font.family': 'DejaVu Sans'})
    fig, ax = plt.subplots(figsize=(10.8, 6.1), dpi=110, facecolor='white')
    fig.subplots_adjust(left=.035, right=.985, bottom=.17, top=.84)
    obj, lens1, intermediate, lens2, screen = 0., 40., 120., 170., 320.
    object_height = .10  # mm; plotted transverse distances are magnified separately.
    mid_height, end_height = -2*object_height, 6*object_height
    ax.add_patch(Rectangle((-30, -.44), 365, 1.24, fill=False,
                           linestyle=(0, (5, 4)), edgecolor='#83919c', linewidth=1.3))
    ax.plot([-27, 332], [0, 0], color='#a2abb3', linestyle=':', linewidth=1)
    for x, height, label in [(lens1, .30, 'First magnetic lens'),
                             (lens2, .39, 'Second magnetic lens')]:
        ax.add_patch(Rectangle((x-6, -height), 12, 2*height,
                               facecolor='#d5e5f1', edgecolor='#527e9c', linewidth=1.5))
        ax.text(x, .87, label, ha='center', fontsize=11,
                bbox={'facecolor':'white', 'edgecolor':'none', 'pad':1})
    for y_at_lens, color in zip([-.12, .025, .16], ['#c0582c', '#176c9e', '#307d46']):
        # Thin-lens refraction in a frame neglecting magnetic image rotation.
        slope_in = (y_at_lens-object_height)/(lens1-obj)
        slope_mid = slope_in-y_at_lens/(80/3)
        y_at_second = y_at_lens+slope_mid*(lens2-lens1)
        slope_out = slope_mid-y_at_second/37.5
        xx = np.array([obj, lens1, intermediate, lens2, screen])
        yy = np.array([object_height, y_at_lens,
                       y_at_lens+slope_mid*(intermediate-lens1), y_at_second,
                       y_at_second+slope_out*(screen-lens2)])
        ax.plot(xx, yy, color=color, linewidth=1.7)
    for x, y, label, label_y in [(obj, object_height, 'Object', -.34),
                                (intermediate, mid_height, 'Intermediate image', -.34),
                                (screen, end_height, 'Screen image', -.34)]:
        ax.add_patch(FancyArrowPatch((x, 0), (x, y), arrowstyle='-|>',
                                    mutation_scale=13, linewidth=2.2, color='#202a32'))
        ax.plot(x, y, 'o', markersize=4, color='#202a32')
        ax.text(x, label_y, label, ha='center', va='top', fontsize=10.5,
                bbox={'facecolor':'white', 'edgecolor':'none', 'pad':1})
    ax.plot([screen, screen], [-.28, .70], color='#647b43', linewidth=5, alpha=.4)
    ax.text(screen-2, .74, 'Fluorescent screen\n(spatial readout)', ha='right', va='top', fontsize=10)
    ax.annotate('Electron source\n(upstream)', xy=(-19, .02), xytext=(-22, .55),
                ha='left', fontsize=10, arrowprops={'arrowstyle':'->','color':'#4c5964'})
    ax.plot([245, 245], [-.44, -.61], color='#83919c', linewidth=1.5)
    ax.text(245, -.65, 'To vacuum pump', ha='center', fontsize=10, color='#4c5964')
    ax.text(80, .69, r'$m_1=-2$', ha='center', color='#334f64', fontsize=13)
    ax.text(236, .23, r'$m_2=-3$', ha='center', color='#334f64', fontsize=13)
    ax.set(xlim=(-38, 343), ylim=(-.75, 1.0))
    ax.axis('off')
    fig.suptitle('Two electron lenses preserve a point-to-point image', y=.96, fontsize=17)
    fig.text(.5, .885, 'Invented thin-lens geometry; smooth magnetic bending and rotation omitted',
             ha='center', fontsize=11, color='#4c5964')
    fig.text(.5, .10, r'$u_1=40,\ v_1=80,\ u_2=50,\ v_2=150\ \mathrm{mm}$'
             r'     $\Rightarrow\ m=+6$', ha='center', fontsize=12)
    fig.text(.5, .045, 'Diagram uses different horizontal and vertical scales. No historical measurements.',
             ha='center', fontsize=10, color='#4c5964')
    fig.savefig(Path(__file__).stem+'.png', facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
