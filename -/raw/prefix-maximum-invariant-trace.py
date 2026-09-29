"""Draw exact prefix-maximum states; run from the desired output directory."""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def main():
    values = [3, 1, 4, 4, 2]
    fig, ax = plt.subplots(figsize=(9.6, 5.6), dpi=110, facecolor='white')
    ax.set(xlim=(-1.45, 7.6), ylim=(-0.9, 6.2))
    ax.axis('off')
    ax.text(-1.3, 5.87, 'The maximum of everything read so far', fontsize=17, weight='bold')
    ax.text(-1.3, 5.4, r'At each condition check: best = max(first $k$ entries), remaining = $5-k$', fontsize=11)
    ax.text(-1.12, 4.9, r'$k$', ha='center', fontsize=13)
    for j in range(5):
        ax.text(j + 0.43, 4.9, f'index {j}', ha='center', fontsize=10, color='#555555')
    ax.text(5.67, 4.9, 'best', ha='center', fontsize=12, weight='bold')
    ax.text(6.99, 4.9, 'remaining', ha='center', fontsize=11)
    for row, k in enumerate(range(1, 6)):
        y = 4.05 - row * 0.86
        best = max(values[:k])
        ax.text(-1.12, y + 0.28, str(k), ha='center', va='center', fontsize=14)
        for j, value in enumerate(values):
            processed = j < k
            ax.add_patch(Rectangle((j, y), 0.86, 0.56, facecolor='#d4e6f5' if processed else '#eeeeee', edgecolor='#72899a' if processed else '#cccccc'))
            ax.text(j + 0.43, y + 0.28, str(value), ha='center', va='center', fontsize=15, color='#15334c' if processed else '#888888')
        ax.text(5.67, y + 0.28, str(best), ha='center', va='center', fontsize=16, weight='bold', color='#176e54')
        ax.text(6.99, y + 0.28, str(5-k), ha='center', va='center', fontsize=14)
        ax.plot([k-0.09, k-0.09], [y-0.06, y+0.62], color='#176e54', linewidth=2)
    ax.text(-1.3, -0.66, 'Blue: processed prefix     Grey: unread     Final row: return 4', fontsize=11)
    fig.subplots_adjust(left=0.035, right=0.99, top=0.98, bottom=0.03)
    fig.savefig(Path(__file__).stem + '.png', facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
