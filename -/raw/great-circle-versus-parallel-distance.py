"""Compare spherical great-circle and constant-latitude paths; PNG to CWD.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Run from _media to regenerate the published image. This is idealized geometry.
"""

from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    latitude = np.pi / 6
    longitude = np.linspace(-np.pi / 3, np.pi / 3, 501)
    parallel = np.column_stack((np.cos(latitude) * np.cos(longitude),
                                np.cos(latitude) * np.sin(longitude),
                                np.full_like(longitude, np.sin(latitude))))
    p, q = parallel[0], parallel[-1]
    delta = np.arccos(np.clip(p @ q, -1, 1))
    t = np.linspace(0, 1, 501)
    great = (np.sin((1 - t) * delta)[:, None] * p
             + np.sin(t * delta)[:, None] * q) / np.sin(delta)
    great_lon = np.arctan2(great[:, 1], great[:, 0])
    great_lat = np.arctan2(great[:, 2], np.hypot(great[:, 0], great[:, 1]))
    apex = great[len(great) // 2]
    parallel_length = np.cos(latitude) * (2 * np.pi / 3)
    assert np.isclose(p @ q, -1 / 8)
    assert np.allclose(np.linalg.norm(great, axis=1), 1)
    assert np.allclose(great @ np.cross(p, q), 0)
    assert np.isclose(great_lat.max(), np.arctan(2 / np.sqrt(3)))
    assert delta < parallel_length

    plt.rcParams.update({'font.size': 12})
    fig = plt.figure(figsize=(9.6, 6.5), facecolor='white')
    ax = fig.add_axes([-.03, .17, .58, .69], projection='3d', computed_zorder=False)
    ax.set_facecolor('white')
    ax.set_proj_type('ortho')
    ax.view_init(elev=22, azim=0)
    ax.set_box_aspect((1, 1, 1), zoom=1.18)
    ax.set(xlim=(-1.1, 1.1), ylim=(-1.1, 1.1), zlim=(-1.1, 1.1))
    ax.set_axis_off()
    phi, theta = np.meshgrid(np.linspace(0, 2 * np.pi, 85), np.linspace(0, np.pi, 43))
    ax.plot_wireframe(np.sin(theta) * np.cos(phi), np.sin(theta) * np.sin(phi),
                      np.cos(theta), rstride=4, cstride=7, color='#acbdca',
                      alpha=.35, lw=.65, zorder=1)
    equator = np.column_stack((np.cos(phi[0]), np.sin(phi[0]), np.zeros_like(phi[0])))
    ax.plot(*equator.T, color='#8a9aa7', lw=1, alpha=.6, zorder=2)
    ax.plot(*parallel.T, color='#c05d1d', lw=3, ls='--', zorder=3)
    ax.plot(*great.T, color='#147789', lw=3.2, zorder=4)
    for vertex, label, align in [(p, r'$P:\ -60^\circ$', 'right'),
                                  (q, r'$Q:\ +60^\circ$', 'left')]:
        ax.scatter(*vertex, color='#253c48', s=25, depthshade=False, zorder=5)
        ax.text(*(1.13 * vertex), label, ha=align, va='center', fontsize=12, zorder=6)
    ax.scatter(*apex, color='#147789', s=22, depthshade=False, zorder=5)
    ax.text(*(apex + [0, 0, .13]), r'$49.1066^\circ$', ha='center', fontsize=12,
            color='#147789', zorder=6)
    fig.text(.25, .23, 'Ideal sphere of radius R', ha='center', color='#465865', fontsize=12)

    chart = fig.add_axes([.60, .35, .36, .43])
    chart.set_facecolor('white')
    chart.plot(np.degrees(great_lon), np.degrees(great_lat), color='#147789', lw=3,
               label='Great circle')
    chart.plot(np.degrees(longitude), np.full_like(longitude, 30), color='#c05d1d',
               lw=2.5, ls='--', label='Constant latitude')
    chart.scatter([-60, 60], [30, 30], color='#253c48', s=23, zorder=5)
    chart.set(xlim=(-65, 65), ylim=(25, 56), xticks=[-60, -30, 0, 30, 60],
               yticks=[30, 40, 50], xlabel='Longitude (degrees)', ylabel='Latitude (degrees)')
    chart.spines[['top', 'right']].set_visible(False)
    chart.grid(alpha=.2)
    chart.legend(loc='upper center', fontsize=10, frameon=False)
    chart.annotate('49.1066°', xy=(0, np.degrees(great_lat.max())), xytext=(20, 46),
                   fontsize=10, color='#147789',
                   arrowprops={'arrowstyle': '-', 'color': '#147789'})
    fig.suptitle('Same latitude, different surface paths', fontsize=18, y=.96)
    fig.text(.5, .87, 'Endpoints: latitude 30°, longitudes −60° and +60°', ha='center', fontsize=13)
    fig.text(.60, .20, r'$d_{\mathrm{great}}=R\arccos(-1/8)\approx1.696124R$',
             color='#147789', fontsize=13)
    fig.text(.60, .12, r'$\ell_{\mathrm{parallel}}=R\cos30^\circ(2\pi/3)\approx1.813799R$',
             color='#c05d1d', fontsize=12)
    fig.text(.5, .035, 'The latitude-longitude chart shows positions; its plotted line lengths are not surface distances.',
             ha='center', fontsize=11)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name,
                dpi=130, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
