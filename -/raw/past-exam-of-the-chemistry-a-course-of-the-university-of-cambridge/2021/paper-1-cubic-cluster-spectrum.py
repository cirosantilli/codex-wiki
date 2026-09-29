"""Original spectrum of the equal-site, equal-edge cubic Hückel model."""
from pathlib import Path
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(7, 4.4), dpi=150)
for energy, count, label in [(-3,1,r"$a_1$"),(-1,3,r"$t_2$"),(1,3,r"$t_2$"),(3,1,r"$a_1$")]:
    for i in range(count):
        x = (i-(count-1)/2)*.7
        ax.plot([x-.23,x+.23],[energy,energy],lw=2,color="#236e9c" if energy<0 else "#8d939a")
        if energy<0:ax.text(x,energy+.08,r"$\uparrow\downarrow$",ha="center",fontsize=17)
    ax.text(1.3,energy,label,ha="left",va="center",fontsize=14)
ax.axhline(0,color="#b9bfc5",ls="--",lw=1)
ax.set(xlim=(-1.7,2.2),ylim=(-3.8,3.8),xticks=[],yticks=[-3,-1,0,1,3],
       ylabel=r"$(E-\alpha)/|\beta|$, with $\beta<0$",
       title="Cubic cluster: eight valence electrons")
ax.spines[["top","right","bottom"]].set_visible(False)
fig.text(.5,.025,"One site orbital per vertex; coupling only along equal cube edges.",ha="center",fontsize=10)
fig.tight_layout(rect=(0,.05,1,1))
fig.savefig(Path(__file__).with_suffix(".png").name,facecolor="white")
