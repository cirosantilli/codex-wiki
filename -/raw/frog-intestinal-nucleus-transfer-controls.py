"""Original nuclear-transfer apparatus and control schematic.

Tested with Python 3.14 and matplotlib 3.10.7; run from _media.
No reconstructed measurements, copied artwork, or inferred success counts.
"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Ellipse, Polygon, FancyArrowPatch, FancyBboxPatch


def main():
    fig, ax = plt.subplots(figsize=(10, 6.4), dpi=140, facecolor='white')
    ax.set(xlim=(0, 10), ylim=(0, 6.4))
    ax.axis('off')

    def arrow(a, b, color='#425369', dashed=False):
        ax.add_patch(FancyArrowPatch(a, b, arrowstyle='-|>', mutation_scale=15, linewidth=1.6, color=color, linestyle='--' if dashed else '-'))

    def box(x, y, w, h, title, body, color='#edf2f9'):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.08', facecolor=color, edgecolor='#708098'))
        ax.text(x+w/2, y+h-0.25, title, ha='center', va='center', fontsize=12, weight='bold')
        ax.text(x+w/2, y+0.37, body, ha='center', va='center', fontsize=10, linespacing=1.35)

    ax.text(5, 6.11, 'Frog intestinal nucleus transfer', ha='center', fontsize=20, weight='bold')
    ax.text(5, 5.74, 'An intervention tests retained developmental capacity', ha='center', fontsize=12)
    # A columnar donor cell with an absorptive border and basal nucleus.
    ax.add_patch(FancyBboxPatch((0.68, 3.99), 0.66, 1.15, boxstyle='round,pad=0.03', facecolor='#e9effc', edgecolor='#526177'))
    for k in range(7):
        ax.plot([0.72+0.09*k]*2, [5.14,5.3], color='#526177', linewidth=1.3)
    ax.add_patch(Ellipse((1.01,4.28), 0.42, 0.3, color='#5969b0'))
    ax.text(1.06, 3.62, 'Recognized intestinal cell\nfrom a feeding tadpole', ha='center', fontsize=10)
    arrow((1.4,4.45), (2.13,4.45))
    # Pipette denotes transfer into cytoplasm, without falsely showing surgery.
    ax.add_patch(Polygon([(2.17,4.32),(3.17,4.45),(2.17,4.58)], facecolor='#e0e5ed', edgecolor='#526177'))
    ax.add_patch(Circle((2.48,4.45), 0.08, color='#5969b0'))
    ax.text(2.48, 3.94, 'Glass pipette\nDonor nucleus', ha='center', fontsize=10)
    egg=(4.15,4.45)
    ax.add_patch(Circle(egg, 0.84, facecolor='#fff2cd', edgecolor='#8b7954', linewidth=1.7))
    ax.add_patch(Circle((4.15,5.05), 0.1, facecolor='white', edgecolor='#ae473c'))
    ax.plot([4.06,4.24],[4.96,5.14], color='#ae473c', linewidth=2)
    ax.plot([4.06,4.24],[5.14,4.96], color='#ae473c', linewidth=2)
    arrow((4.15,5.63),(4.15,5.2), color='#9b4c9c')
    ax.text(5.0,5.43,'UV illumination', color='#8a438b', fontsize=10)
    ax.text(4.15,3.28,'Recipient unfertilized egg\nNuclear contribution inactivated', ha='center', fontsize=10)
    arrow((5.13,4.45),(5.94,4.45))
    box(6.05,3.92,3.3,1.23,'Follow development','Division alone is insufficient.\nNormal feeding tadpole: one readout.')
    ax.text(7.7,3.56,'Success is possible; no rate is shown.', ha='center', fontsize=10, color='#6d5260')
    box(0.65,1.82,4.12,1.12,'Origin check: donor nuclear marker','Developed embryo carries donor marker.\nTests origin of nuclear contribution.', '#f0eef9')
    box(5.16,1.82,4.12,1.12,'Preparation check: embryonic donor','Interspersed transfers test egg quality.\nA different control answers a different question.', '#eaf5f0')
    arrow((4.2,3.25),(2.75,3.02),dashed=True)
    arrow((5.05,3.25),(7.2,3.02),dashed=True)
    ax.text(5,1.21,'Inference: specialized nuclei can retain capacity for other cell types.', ha='center', fontsize=12, weight='bold')
    ax.text(5,0.67,'Limits: transfer damage, recipient condition and incomplete resetting can cause failure.\nExperimental reprogramming does not trace the donor’s normal developmental fate.', ha='center', fontsize=11, linespacing=1.4)
    ax.text(5,0.18,'Original qualitative schematic • not to scale • no traced figures or measured counts', ha='center', fontsize=9, color='#626974')
    fig.subplots_adjust(left=0.01, right=0.99, bottom=0.02, top=0.98)
    fig.savefig(Path(__file__).stem+'.png', facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
