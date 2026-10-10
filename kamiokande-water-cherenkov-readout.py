"""Original functional Kamiokande readout; Python 3.14, matplotlib 3.10, NumPy 2.3.

Run from _media; writes kamiokande-water-cherenkov-readout.png to CWD.
All geometry and timing examples are illustrative, not detector measurements.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Arc


def main():
    plt.rcParams.update({'font.size': 11, 'font.family': 'DejaVu Sans'})
    fig = plt.figure(figsize=(10, 6.3), facecolor='white')
    fig.suptitle('Kamiokande: light gives timing and track direction', fontsize=17, y=.97)
    ax = fig.add_axes([.035, .28, .59, .60]); ax.set_aspect('equal')
    ax.set(xlim=(-.5, 6.8), ylim=(0, 5.7)); ax.axis('off')
    ax.add_patch(Rectangle((.3, .7), 5.9, 4.5, facecolor='#edf8fc', edgecolor='#22577a', lw=2))
    ax.text(3.25, 4.7, 'Water', ha='center', color='#22577a', fontsize=13)
    for x in np.linspace(.65, 5.85, 9):
        for y in (.7, 5.2):
            ax.add_patch(Circle((x, y), .11, color='#c05a19'))
    for y in np.linspace(1.25, 4.65, 5):
        for x in (.3, 6.2): ax.add_patch(Circle((x, y), .11, color='#c05a19'))
    origin = np.array([1.5, 2.95]); end = np.array([3.3, 2.95])
    ax.annotate('', xy=origin, xytext=(-.4, 2.95), arrowprops={'arrowstyle':'->', 'lw':1.5, 'ls':'--', 'color':'#666'})
    ax.text(-.35, 3.23, r'Incident $\nu$', fontsize=11)
    ax.plot(*origin, marker='o', color='#173e59', ms=7)
    ax.annotate('', xy=end, xytext=origin, arrowprops={'arrowstyle':'->', 'lw':3, 'color':'#173e59'})
    ax.text(2.4, 2.55, 'Charged track', ha='center', fontsize=11)
    angle = np.arccos(1/1.33)
    for x0 in [1.5, 2.05, 2.6]:
        for yend in [.7, 5.2]:
            xend = x0+abs(yend-origin[1])/np.tan(angle)
            ax.annotate('', xy=(xend, yend), xytext=(x0, origin[1]),
                        arrowprops={'arrowstyle':'->', 'lw':1.5, 'color':'#2696ad', 'alpha':.85})
    ax.add_patch(Arc(origin, 1.5, 1.5, theta1=0, theta2=np.degrees(angle), color='#173e59', lw=1.2))
    ax.text(2.28, 3.24, r'$\theta_C$', color='#173e59', fontsize=12)
    ax.text(4.2, 3.5, 'Light paths', color='#16788c', fontsize=11)
    ax.text(3.25, .13, 'Wall sensors: photomultipliers', ha='center', fontsize=11, color='#8b4313')
    ax.text(3.25, 5.52, 'Schematic cross-section; illustrative geometry', ha='center', fontsize=10)
    p = fig.add_axes([.67, .34, .29, .48]); p.axis('off')
    p.text(0, .95, 'Ideal point-flash timing', weight='bold', fontsize=12)
    p.text(0, .78, r'$t_i=t_0+nL_i/c$', fontsize=16)
    p.text(0, .60, 'Chosen inputs:\n' + r'$n=1.33$; $L_1=3$ m; $L_2=6$ m', fontsize=11, linespacing=1.8)
    p.text(0, .32, r'$t_2-t_1=13.31$ ns', fontsize=16, color='#22577a')
    p.text(0, .12, 'Time difference removes\nthe unknown flash time.', fontsize=11, linespacing=1.5)
    fig.text(.5, .21, 'Pulse times + sensor positions  →  vertex and time', ha='center', fontsize=13, color='#22577a')
    fig.text(.5, .145, 'Light pattern  →  charged-track direction  →  statistical source information', ha='center', fontsize=12)
    fig.text(.5, .055, 'Point-flash timing is an ideal model; a moving track emits along its path.', ha='center', fontsize=10, color='#4a4a4a')
    fig.savefig(Path.cwd() / (Path(__file__).stem+'.png'), dpi=110, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
