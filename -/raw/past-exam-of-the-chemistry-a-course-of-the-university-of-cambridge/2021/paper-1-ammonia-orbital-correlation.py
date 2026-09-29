"""Original qualitative minimal-basis ammonia orbital schemes; no measured energies."""
from pathlib import Path
import matplotlib.pyplot as plt

fig, axs = plt.subplots(1, 2, figsize=(10, 5), dpi=150)
def level(ax, x, y, label, degeneracy, occupied, color="#226c9c"):
    offsets = [-.18, .18] if degeneracy==2 else [0]
    for offset in offsets:
        ax.plot([x+offset-.13, x+offset+.13], [y, y], color=color, lw=2)
        if occupied:
            ax.text(x+offset, y+.03, r"$\uparrow\downarrow$", ha="center", fontsize=14)
    ax.text(x, y-.24, label, ha="center", fontsize=12, color=color)

for ax, title, levels in [
    (axs[0], r"Pyramidal ammonia: $C_{3v}$", [(1,-3.7,r"$2a_1$",1,1),(2.4,-2.1,r"$1e$",2,1),
       (1,-.5,r"$3a_1$: mainly lone pair",1,1),(1,2.3,r"$4a_1$",1,0),(2.4,2.3,r"$2e$",2,0)]),
    (axs[1], r"Planar ammonia: $D_{3h}$", [(1,-3.7,r"$2a_1'$",1,1),(2.4,-2.1,r"$1e'$",2,1),
       (1,.2,r"$1a_2''$: pure $2p_z$",1,1),(1,2.3,r"$3a_1'$",1,0),(2.4,2.3,r"$2e'$",2,0)])]:
    for spec in levels:level(ax,*spec)
    ax.annotate("", (.1, 3), (.1, -4.2), arrowprops={"arrowstyle":"->","color":"#424b55"})
    ax.text(-.03, -.5, "qualitative energy", rotation=90, ha="center", va="center", fontsize=11)
    ax.text(1.65, 3, "empty antibonding orbitals", ha="center", fontsize=11)
    ax.set(title=title, xlim=(-.2, 3.2), ylim=(-4.4, 3.5))
    ax.axis("off")
fig.text(.5,.08, "The planar lone pair correlates with the pyramidal $3a_1$ orbital; pyramidalization allows $s$–$p$ mixing.",
         ha="center", fontsize=11)
fig.text(.5,.025, "Core 1s omitted. Gaps and relative antibonding ordering are schematic, not quantitative.",ha="center", fontsize=10)
fig.tight_layout(rect=(0,.13,1,1))
fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white")
