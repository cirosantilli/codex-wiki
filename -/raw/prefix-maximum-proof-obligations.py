"""Draw original control flow and its separate correctness obligations."""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Polygon


def main():
    fig, ax = plt.subplots(figsize=(10.0, 7.4), dpi=110, facecolor='white')
    ax.set(xlim=(0, 10), ylim=(0, 10))
    ax.axis('off')
    blue, green, orange = '#e6f0f8', '#e0f2e8', '#fff0d8'

    def box(x, y, w, h, text, color=blue, size=11):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.06', facecolor=color, edgecolor='#627c8e', linewidth=1.3))
        ax.text(x+w/2, y+h/2, text, ha='center', va='center', fontsize=size, linespacing=1.6)

    def arrow(start, end, **kwargs):
        ax.annotate('', xy=end, xytext=start, arrowprops=dict(arrowstyle='->', color='#465869', linewidth=1.7, **kwargs))

    ax.text(0.2, 9.65, 'The answer stays right; unread entries run out', fontsize=17, weight='bold')
    box(2.25, 8.25, 4.5, 0.92, 'Precondition: unchanged nonempty integer array\nExact comparisons and index arithmetic', green)
    box(2.65, 6.85, 3.7, 0.8, r'best = $a_0$;  $k = 1$')
    arrow((4.5, 8.25), (4.5, 7.7))
    box(2.05, 5.43, 4.9, 0.86, r'$I$:  $1\leq k\leq n$;  best = max(first $k$ entries)', green)
    arrow((4.5, 6.85), (4.5, 6.32))
    ax.text(0.2, 6.72, '1. INITIALIZE', fontsize=10, weight='bold', color='#176e54')
    ax.text(0.2, 6.34, 'First prefix has one entry.', fontsize=10)
    diamond = [(4.5, 5.02), (5.38, 4.4), (4.5, 3.78), (3.62, 4.4)]
    ax.add_patch(Polygon(diamond, closed=True, facecolor=orange, edgecolor='#627c8e'))
    ax.text(4.5, 4.4, r'$k<n$?', ha='center', va='center', fontsize=13)
    arrow((4.5, 5.43), (4.5, 5.04))
    box(2.62, 2.03, 3.76, 1.0, 'If $a_k$ > best: best = $a_k$\nAlways: $k = k+1$')
    arrow((4.5, 3.78), (4.5, 3.06))
    ax.text(4.7, 3.38, 'true', fontsize=10)
    # A return route outside the boxes makes the invariant checkpoint visible.
    ax.plot([2.62, 1.75, 1.75], [2.53, 2.53, 5.86], color='#465869', linewidth=1.7)
    arrow((1.75, 5.86), (2.02, 5.86))
    ax.text(0.2, 4.3, '2. PRESERVE', fontsize=10, weight='bold', color='#176e54')
    ax.text(0.2, 3.7, 'Extend the prefix\nby one entry.', fontsize=10, linespacing=1.5)
    box(7.15, 3.85, 2.45, 1.14, '3. EXIT\n$I$ and false guard:\n$k=n$; return best', green, size=10)
    arrow((5.38, 4.4), (7.09, 4.4))
    ax.text(5.92, 4.62, 'false', fontsize=10)
    box(7.15, 1.84, 2.45, 1.19, '4. TERMINATE\n' + r'$V=n-k\geq0$' + '\n' + r'Each body: $V\mapsto V-1$', orange, size=10)
    arrow((6.38, 2.53), (7.09, 2.53))
    ax.text(0.2, 0.89, '1 + 2 + 3: partial correctness     Add 4: total correctness', fontsize=12, weight='bold')
    ax.text(0.2, 0.35, 'The invariant is required at the green checkpoint, not between the two assignments.', fontsize=10)
    fig.subplots_adjust(left=0.015, right=0.995, top=0.99, bottom=0.02)
    fig.savefig(Path(__file__).stem + '.png', facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
