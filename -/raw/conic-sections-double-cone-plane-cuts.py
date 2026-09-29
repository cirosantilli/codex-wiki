"""Four exact cone/plane intersections. Write the original PNG to cwd."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def intersection(m):
    if m == 0:
        t = np.linspace(0, 2*np.pi, 501)
        return [(np.cos(t), np.sin(t), np.ones_like(t))]
    if m < 1:
        t = np.linspace(0, 2*np.pi, 501)
        h = 1-m*m
        x = m/h + np.cos(t)/h
        y = np.sin(t)/np.sqrt(h)
        return [(x, y, 1+m*x)]
    if m == 1:
        y = np.linspace(-2.15, 2.15, 501)
        x = (y*y-1)/2
        return [(x, y, 1+x)]
    t = np.linspace(-1, 1, 501)
    h = m*m-1
    lines = []
    for sign in [-1, 1]:
        x = -m/h + sign*np.cosh(t)/h
        y = np.sinh(t)/np.sqrt(h)
        lines.append((x, y, 1+m*x))
    return lines


def main():
    fig = plt.figure(figsize=(11.2, 9.1), facecolor='white')
    titles = [('Circle', 0, r'$m=0$'), ('Ellipse', .6, r'$m=3/5$'),
              ('Parabola', 1., r'$m=1$'), ('Hyperbola', 1.4, r'$m=7/5$')]
    angle, z = np.meshgrid(np.linspace(0, 2*np.pi, 29), np.linspace(-3.25, 3.25, 25))
    cx, cy = np.abs(z)*np.cos(angle), np.abs(z)*np.sin(angle)
    for index, (title, m, label) in enumerate(titles, 1):
        ax = fig.add_subplot(2, 2, index, projection='3d')
        ax.plot_wireframe(cx, cy, z, color='#9eafb9', alpha=.44, lw=.48,
                          rstride=3, cstride=3)
        px, py = np.meshgrid(np.linspace(-2.65, 2.65, 10), np.linspace(-2.65, 2.65, 10))
        pz = 1+m*px
        pz = np.where(np.abs(pz)<=3.25, pz, np.nan)
        ax.plot_surface(px, py, pz, color='#79b7d4', alpha=.17, linewidth=0)
        for x, y, zc in intersection(m):
            # Every displayed point satisfies both equations independently.
            assert np.max(np.abs(zc*zc-x*x-y*y)) < 3e-14
            assert np.max(np.abs(zc-1-m*x)) < 3e-15
            ax.plot(x, y, zc, color='#b84d25', lw=3, zorder=8)
        ax.scatter(0, 0, 0, color='#485561', s=14)
        ax.set_xlim(-3.35, 3.35)
        ax.set_ylim(-3.35, 3.35)
        ax.set_zlim(-3.35, 3.35)
        ax.set_box_aspect((1, 1, 1))
        ax.set_xticks([-2, 0, 2])
        ax.set_yticks([-2, 0, 2])
        ax.set_zticks([-2, 0, 2])
        ax.set_xlabel('x', labelpad=1)
        ax.set_ylabel('y', labelpad=1)
        ax.set_zlabel('z', labelpad=1)
        ax.view_init(elev=25, azim=-110)
        ax.set_title(title+'  '+label, fontsize=15, weight='bold', pad=0)
        ax.set_facecolor('white')
        for axis in (ax.xaxis, ax.yaxis, ax.zaxis):
            axis.pane.set_facecolor((1, 1, 1, 1))
    fig.suptitle('Four plane cuts of the same double cone', fontsize=19, weight='bold', y=.98)
    fig.text(.5, .935, r'Cone: $z^2=x^2+y^2$     Cutting plane: $z=1+mx$',
             ha='center', fontsize=14)
    fig.subplots_adjust(top=.89, bottom=.08, left=.02, right=.98, hspace=.10, wspace=.01)
    fig.text(.5, .025, 'Orange: exact intersection. Blue: plane patch. Gray: cone mesh. Each panel has equal spatial scales.',
             ha='center', fontsize=10.5, color='#405063')
    fig.savefig(Path.cwd() / (Path(__file__).stem+'.png'), dpi=120, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
