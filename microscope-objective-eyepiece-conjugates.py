"""Draw an original finite-conjugate thin-lens microscope; Python 3.14.

Run from _media; output is the generator basename with a .png suffix.
Heights are enlarged by the same factor for both image and object.
"""
from pathlib import Path

import matplotlib.pyplot as plt


def main():
    plt.rcParams.update({'font.size': 11, 'font.family': 'DejaVu Sans'})
    fig, ax = plt.subplots(figsize=(11, 5.6), dpi=100, facecolor='white')
    ax.set_facecolor('white')
    ax.set_xlim(-24, 118)
    ax.set_ylim(-12, 13)
    ax.axis('off')
    fig.suptitle('A real intermediate image, then relaxed-eye viewing', fontsize=16, y=0.96)
    ax.axhline(0, color='#737373', linewidth=1)
    ax.text(113, 0.5, 'Optical\naxis', ha='center', fontsize=10)
    for x, label, focal in [(0, 'Objective', 10), (85, 'Eyepiece', 25)]:
        ax.annotate('', xy=(x, 8.6), xytext=(x, -8.6),
                    arrowprops={'arrowstyle': '<->', 'lw': 2, 'color': '#34495e'})
        ax.text(x, 10.6, label, ha='center', fontsize=12, fontweight='bold')
        ax.text(x, 9.1, f'f = {focal} mm', ha='center')
    for x in [-10, 10, 60]:
        ax.plot(x, 0, 'o', color='#34495e', markersize=4)
    ax.annotate('', xy=(-12, 1), xytext=(-12, 0),
                arrowprops={'arrowstyle': '-|>', 'lw': 2.5, 'color': '#207a47'})
    ax.text(-15, 3.5, 'Object', ha='center', color='#207a47', fontweight='bold')
    ax.axvline(60, ymin=0.14, ymax=0.64, color='#207a47', linestyle=':', lw=1.5)
    ax.annotate('', xy=(60, -5), xytext=(60, 0),
                arrowprops={'arrowstyle': '-|>', 'lw': 2.5, 'color': '#207a47'})
    ax.text(59, 5.9, 'Real intermediate image\n5 times taller, inverted',
            ha='center', color='#207a47', fontsize=11)
    # Two independent paraxial rays from the same object point.
    # Thin-lens slope update is t_out = t_in - y/f.
    for intercept, color in [(1.0, '#c34737'), (0.0, '#2868ac')]:
        slope_in = (intercept - 1) / 12
        slope_obj = slope_in - intercept / 10
        y_image = intercept + slope_obj * 60
        y_eye = intercept + slope_obj * 85
        slope_eye = slope_obj - y_eye / 25
        ax.plot([-12, 0, 60, 85, 112],
                [1, intercept, y_image, y_eye, y_eye + slope_eye * 27],
                color=color, linewidth=2)
        ax.annotate('', xy=(108, y_eye + slope_eye * 23),
                    xytext=(101, y_eye + slope_eye * 16),
                    arrowprops={'arrowstyle': '->', 'color': color, 'lw': 2})
    ax.text(103, -9.2, 'Parallel rays from\none image point', ha='center', fontsize=10)
    for left, right, y, label in [(-12, 0, -10.6, '12 mm'),
                                  (0, 60, -10.6, '60 mm'),
                                  (60, 85, -10.6, '25 mm')]:
        ax.annotate('', xy=(left, y), xytext=(right, y),
                    arrowprops={'arrowstyle': '<->', 'color': '#555555', 'lw': 1})
        ax.text((left + right) / 2, y - 0.7, label, ha='center', va='top')
    fig.text(0.5, 0.095, 'Detector at the intermediate image: m = −5.  Eyepiece viewing: Mₑ = 250/25 = 10.',
             ha='center', fontsize=11)
    fig.text(0.5, 0.049, 'Total signed angular magnification: −50.  Toy geometry; vertical heights enlarged.',
             ha='center', fontsize=11)
    fig.subplots_adjust(left=0.035, right=0.97, bottom=0.19, top=0.86)
    fig.savefig(Path(__file__).stem + '.png', facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
