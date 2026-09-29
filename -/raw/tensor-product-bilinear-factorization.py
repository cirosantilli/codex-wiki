"""Draw an explicit tensor universal-property diagram.

Tested with Python 3.14, matplotlib 3.10.7, numpy 2.3.5.
Run from _media; output has this script's basename in the current directory.
"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def main():
    fig, ax = plt.subplots(figsize=(9.6, 5.8), dpi=110, facecolor='white')
    ax.set(xlim=(0, 9.6), ylim=(0, 5.8))
    ax.axis('off')
    ax.text(.28, 5.52, 'Universal property: both routes give the same answer', fontsize=18, weight='bold')
    boxes = [(0.4, 3.6, 3.0, 1.35), (5.75, 3.6, 3.4, 1.35), (3.15, .42, 3.3, 1.2)]
    for x, y, w, h in boxes:
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.12', linewidth=1.4, edgecolor='#306783', facecolor='#f2f7fa'))
    ax.text(1.9, 4.63, r'$V\times W$', ha='center', fontsize=20)
    ax.text(1.9, 4.15, r'$v=(2,1),\ w=(-1,3)$', ha='center', fontsize=15)
    ax.text(7.45, 4.63, r'$V\otimes_{\mathbb{R}}W$', ha='center', fontsize=20)
    ax.text(7.45, 4.1, r'$C(v\otimes w)=(-2,6;-1,3)$', ha='center', fontsize=14)
    ax.text(4.8, 1.24, r'$U=\mathbb{R}^2$', ha='center', fontsize=20)
    ax.text(4.8, .72, r'$(13,-7)$', ha='center', fontsize=19, color='#21745b')
    for start, end, dashed in [((3.6, 4.2), (5.53, 4.2), False), ((1.9, 3.43), (3.45, 1.79), False), ((7.43, 3.43), (6.06, 1.79), True)]:
        ax.annotate('', xy=end, xytext=start, arrowprops={'arrowstyle':'->', 'lw':2.0, 'color':'#306783', 'linestyle':'--' if dashed else '-'})
    ax.text(4.57, 4.62, r'$\tau(v,w)=v\otimes w$', fontsize=14, ha='center')
    ax.text(4.57, 3.87, 'bilinear', fontsize=12, ha='center')
    ax.text(.33, 2.97, r'$B(v,w)$', fontsize=17)
    ax.text(.33, 2.50, r'$=(v_1w_1+2v_1w_2+v_2w_2,$', fontsize=13)
    ax.text(.33, 2.13, r'$\qquad v_2w_1-v_1w_2)$', fontsize=13)
    ax.text(7.65, 2.97, r'$L(C)$', fontsize=17)
    ax.text(6.91, 2.50, r'$=(c_{11}+2c_{12}+c_{22},$' , fontsize=13)
    ax.text(6.91, 2.13, r'$\qquad c_{21}-c_{12})$', fontsize=13)
    ax.text(4.8, 2.50, r'$B=L\circ\tau$', fontsize=21, ha='center', color='#21745b')
    ax.text(7.4, 1.47, 'unique linear map', fontsize=12, ha='center')
    ax.text(1.3, 1.47, 'bilinear map', fontsize=12, ha='center')
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
    fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), facecolor='white', transparent=False)
    plt.close(fig)

if __name__ == '__main__':
    main()
