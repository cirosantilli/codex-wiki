"""Original prism geometry and ray calculation; emit matching PNG in CWD.

Tested with Python 3.14, matplotlib 3.10.7, numpy 2.3.5.
All angles and the deviation curve are computed from a chosen constant relative
index at one fixed wavelength. No experimental observations are plotted.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Polygon
import numpy as np


def arc(ax, center, radius, a, b, label, label_radius=None, color='#555555'):
    ax.add_patch(Arc(center, 2*radius, 2*radius, theta1=a, theta2=b, color=color, lw=1.3))
    r = label_radius if label_radius else radius + .14
    theta = np.deg2rad((a+b)/2)
    ax.text(center[0]+r*np.cos(theta), center[1]+r*np.sin(theta), label,
            ha='center', va='center', fontsize=12, color=color)


def main():
    A = np.pi / 3
    index = 1.5
    imin = np.arcsin(index*np.sin(A/2))
    dmin = 2*imin-A
    bend = imin-A/2
    # Symmetric triangular prism and horizontal internal ray.
    h, y = np.sqrt(3), .80
    x = 1-y/h
    entry, exit = np.array([-x, y]), np.array([x, y])
    uin = np.array([np.cos(bend), np.sin(bend)])
    uout = np.array([np.cos(bend), -np.sin(bend)])
    fig, (ax, plot) = plt.subplots(1, 2, figsize=(11, 6.3), dpi=120,
                                    gridspec_kw={'width_ratios': [1.25, 1]}, facecolor='white')
    fig.subplots_adjust(left=.035, right=.97, bottom=.24, top=.80, wspace=.20)
    ax.add_patch(Polygon([(-1, 0), (1, 0), (0, h)], facecolor='#eef5fa', edgecolor='#47748e', lw=2))
    start, end = entry-1.75*uin, exit+1.8*uout
    for p, q in [(start, entry), (entry, exit), (exit, end)]:
        ax.plot([p[0], q[0]], [p[1], q[1]], color='#bb4c28', lw=2.5)
        mid = .5*(p+q)
        ax.annotate('', xy=mid+.09*(q-p), xytext=mid-.09*(q-p),
                    arrowprops={'arrowstyle': '-|>', 'color': '#bb4c28', 'lw': 2})
    for p, angle in [(entry, -30), (exit, 30)]:
        v = np.array([np.cos(np.deg2rad(angle)), np.sin(np.deg2rad(angle))])
        ax.plot([p[0]-.78*v[0], p[0]+.78*v[0]], [p[1]-.78*v[1], p[1]+.78*v[1]],
                ls='--', color='#777777', lw=1.1)
    ax.text(-1.8, 1.30, 'face normal', color='#666666', fontsize=9)
    arc(ax, entry, .44, 150, 180+np.rad2deg(bend), '$i$', .58)
    arc(ax, entry, .30, -30, 0, '$r_1$', .43)
    arc(ax, exit, .30, 180, 210, '$r_2$', .43)
    arc(ax, exit, .44, -np.rad2deg(bend), 30, '$e$', .57)
    arc(ax, (0, h), .39, 240, 300, '$A$', .54)
    # Incident direction translated to the exit: deviation is between directions.
    undeviated = exit+1.75*uin
    ax.plot([exit[0], undeviated[0]], [exit[1], undeviated[1]], ls=':', lw=1.5, color='#176ba0')
    arc(ax, exit, 1.1, -np.rad2deg(bend), np.rad2deg(bend), r'$\delta_{\min}$', 1.40, '#176ba0')
    ax.text(1.40, 1.53, 'incident direction\ntranslated to exit', ha='center', color='#176ba0', fontsize=9)
    ax.text(-1.67, -.12, 'incoming beam', fontsize=10, color='#bb4c28')
    ax.text(.95, -.12, 'to telescope', fontsize=10, color='#bb4c28')
    ax.set_aspect('equal')
    ax.set_xlim(-2.3, 2.6)
    ax.set_ylim(-.3, 2.05)
    ax.axis('off')
    ax.set_title('Symmetry at minimum deviation', fontsize=14, pad=25)
    incidence = np.deg2rad(np.linspace(30, 84, 1200))
    r1 = np.arcsin(np.sin(incidence)/index)
    r2 = A-r1
    permitted = np.abs(index*np.sin(r2)) <= 1
    incidence, r2 = incidence[permitted], r2[permitted]
    emergence = np.arcsin(index*np.sin(r2))
    deviation = incidence+emergence-A
    plot.plot(np.rad2deg(incidence), np.rad2deg(deviation), color='#176ba0', lw=2.4)
    plot.plot(np.rad2deg(imin), np.rad2deg(dmin), 'o', color='#bb4c28', ms=8)
    plot.axvline(np.rad2deg(imin), ls=':', color='#777777')
    plot.annotate('Minimum\n' + r'$i=e=48.5904^\circ$' + '\n' + r'$\delta_{\min}=37.1808^\circ$',
                  xy=(np.rad2deg(imin), np.rad2deg(dmin)), xytext=(54, 47),
                  arrowprops={'arrowstyle': '->', 'color': '#333333'}, fontsize=11)
    plot.set(xlim=(30, 84), ylim=(35.5, 57), xlabel='Incidence angle $i$ (degrees)',
             ylabel=r'Deviation $\delta$ (degrees)')
    plot.set_title('Rotate prism; follow the turning point', fontsize=13, pad=18)
    plot.grid(alpha=.2)
    plot.spines[['top', 'right']].set_visible(False)
    fig.suptitle('Infer relative refractive index from the minimum', fontsize=18, y=.965)
    fig.text(.5, .875, r'Chosen model at one wavelength: $A=60^\circ$, $n_{\rm rel}=3/2$; same external medium at both faces',
             ha='center', fontsize=12)
    fig.text(.5, .115, r'$r_1=r_2=A/2$    $\delta_{\min}=2i-A$    $n_{\rm rel}=\sin[(A+\delta_{\min})/2]/\sin(A/2)$',
             ha='center', fontsize=14)
    fig.text(.5, .038, 'All face angles are measured from normals. The curve is calculated, not measured.\n'
             'The inference formula applies at the minimum; other points use the full two-interface ray calculation.',
             ha='center', fontsize=10)
    fig.savefig(Path(__file__).with_suffix('.png').name, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
