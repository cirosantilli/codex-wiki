"""Generate decoder Karnaugh maps in the current directory."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def main():
    gray = [0, 1, 3, 2]
    cases = [('c: invalid codes are zero', {0,1,3,4,5,6,7,8,9}, False),
             ('d: invalid codes are zero', {0,2,3,5,6,8,9}, False),
             ('f: invalid codes are X', {0,4,5,6,8,9}, True)]
    fig, axes = plt.subplots(1, 3, figsize=(10.5, 3.5), dpi=100, facecolor='white')
    for ax, (title, ones, dc) in zip(axes, cases):
        cells = [[('X' if dc and 4*r+c >= 10 else str(int(4*r+c in ones))) for c in gray] for r in gray]
        ax.axis('off'); ax.set_title(title, fontsize=12, pad=18)
        t = ax.table(cellText=cells, rowLabels=['00','01','11','10'], colLabels=['00','01','11','10'],
                     loc='center', cellLoc='center', rowLoc='center', bbox=[.13,.04,.82,.82])
        t.auto_set_font_size(False); t.set_fontsize(13)
        for (row, col), cell in t.get_celld().items():
            cell.set_edgecolor('#7a8794')
            if row == 0 or col == -1: cell.set_facecolor('#edf1f5')
            elif cells[row-1][col] == '1': cell.set_facecolor('#cce8f3')
            elif cells[row-1][col] == 'X': cell.set_facecolor('#f2e7ce')
        ax.text(.54,.91,'yz', transform=ax.transAxes, ha='center', fontsize=12)
        ax.text(.07,.91,'wx', transform=ax.transAxes, ha='center', fontsize=12)
    fig.suptitle('Seven-segment decoder: Gray-ordered Karnaugh maps', fontsize=14, y=.98)
    fig.subplots_adjust(left=.025,right=.985,bottom=.10,top=.76,wspace=.23)
    fig.savefig(Path.cwd()/'digital-resit-decoder-karnaugh.png', facecolor='white', transparent=False)
    plt.close(fig)
if __name__ == '__main__': main()
