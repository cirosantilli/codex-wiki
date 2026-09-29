"""Draw Q10's six-state ring and source-matching dice faces.

Writes to cwd. Tested with Python 3.14.4 and matplotlib 3.10.7.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Polygon


def main():
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11})
    fig, ax = plt.subplots(figsize=(12, 6.6), dpi=120, facecolor='white')
    ax.set(xlim=(-.3, 13.4), ylim=(-.1, 7.0), aspect='equal')
    ax.axis('off')
    color = '#243746'

    def line(xs, ys):
        ax.plot(xs, ys, c=color, lw=1.5)

    for i in range(6):
        x = .65 + 2*i
        ax.add_patch(Rectangle((x, 4.9), 1.25, 1.05, fc='#edf4f8', ec=color, lw=1.5))
        ax.text(x+.15, 5.58, 'D', va='center')
        ax.text(x+1.08, 5.58, f'$Q_{i+1}$', ha='center', va='center')
        ax.add_patch(Polygon([(x+.28, 4.9), (x+.43, 5.07), (x+.58, 4.9)], closed=False, fill=False, ec=color))
        line([x+.43, x+.43], [4.4, 4.9])
        ax.add_patch(Circle((x+.43, 4.4), .035, color=color))
        if i < 5:
            ax.annotate('', xy=(x+2, 5.58), xytext=(x+1.25, 5.58), arrowprops={'arrowstyle': '->', 'color': color, 'lw': 1.5})
    line([11.9, 12.55, 12.55, .1, .1], [5.58, 5.58, 6.32, 6.32, 5.58])
    ax.annotate('', xy=(.65, 5.58), xytext=(.1, 5.58), arrowprops={'arrowstyle': '->', 'color': color, 'lw': 1.5})
    line([.25, 11.4], [4.4, 4.4])
    ax.text(.25, 4.18, 'Common clock', ha='left', va='top')
    ax.text(6.4, 3.75, r'Initialize $Q_1=1$ and $Q_2=\cdots=Q_6=0$; each pulse rotates the 1.', ha='center')
    ax.text(.1, 6.72, 'Six-state one-hot dice register', fontsize=17, weight='bold')
    positions = {'TL': (-.35, .35), 'TR': (.35, .35), 'ML': (-.35, 0), 'C': (0, 0), 'MR': (.35, 0), 'BL': (-.35, -.35), 'BR': (.35, -.35)}
    faces = [('C',), ('TL','BR'), ('TR','C','BL'), ('TL','TR','BL','BR'), ('TL','TR','C','BL','BR'), ('TL','ML','BL','TR','MR','BR')]
    for i, active in enumerate(faces):
        x = 1.275 + 2*i
        y = 2.25
        ax.add_patch(Rectangle((x-.65, y-.65), 1.3, 1.3, fc='white', ec=color, lw=1.5))
        for name, (dx, dy) in positions.items():
            ax.add_patch(Circle((x+dx, y+dy), .082, fc=color if name in active else '#f4f4f4', ec=color if name in active else '#d4d9dc', lw=.7))
        ax.text(x, 1.28, f'$Q_{i+1}=1$: face {i+1}', ha='center')
    ax.text(6.4, .65, 'Faces 2 and 3 use opposite diagonals, exactly as in the examination scan.', ha='center', fontsize=11)
    ax.text(6.4, .25, 'Lamp groups are driven by the OR equations in the solution; an enable can hold every state bit.', ha='center', fontsize=11)
    fig.subplots_adjust(left=.025, right=.99, top=.98, bottom=.035)
    fig.savefig(Path.cwd() / 'computing-prelims-2005-dice-ring.png', facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
