"""Original reactive-fragment diagrams with electron-pair arrows.

Python 3.14, matplotlib. Writes paper-2-mechanisms.png into cwd.
Complete steroid skeletons are deliberately suppressed to expose the reasoning.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

fig, axes = plt.subplots(4, 1, figsize=(12, 11.5), facecolor="white")
blue, red = "#286c9c", "#ad4f29"
def txt(ax,x,y,s,size=13,color="black"):
    ax.text(x,y,s,ha="center",va="center",fontsize=size,color=color,
            bbox=dict(fc="white",ec="none",pad=.5))
def arrow(ax,a,b,rad=0,color=blue):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle="->",mutation_scale=12,
                  lw=1.6,color=color,connectionstyle=f"arc3,rad={rad}"))
def fragment(ax, labels, y=0):
    for x,t in zip([1.,2.4,3.8,5.2],labels):txt(ax,x,y,t)
    for a,b,sign in [(1.45,1.95,"="),(2.85,3.35,"—"),(4.25,4.75,"=")]:txt(ax,(a+b)/2,y,sign)
for ax in axes:
    ax.set(xlim=(-.2,11.8),ylim=(-1.2,1.4));ax.axis("off")
ax=axes[0]
ax.set_title("Conjugate hydration: bond formation and charge redistribution",loc="left",fontsize=13)
fragment(ax,["O","C1","C2H","C3H–R′"])
txt(ax,5.2,.9,r"$\mathrm{:OH_2}$")
arrow(ax,(5.15,.72),(5.15,.17),.2)
arrow(ax,(4.5,-.12),(3.05,-.12),-.6)
arrow(ax,(1.7,-.12),(1.05,-.15),-.6)
arrow(ax,(6.2,0),(7.1,0))
txt(ax,9.2,.2,r"$\mathrm{^{-}O{-}C1{=}C2H{-}C3H(OH_2^+){-}R'}$",15)
txt(ax,9.2,-.6,"Water relay → beta-hydroxy ketone",12)
txt(ax,2.1,-.85,"R group on C1 omitted; sigma skeleton retained",11)
ax=axes[1]
ax.set_title("At pH 7: water activation and oxyanion stabilization",loc="left",fontsize=13)
txt(ax,1.3,.55,r"$\mathrm{Glu{-}CO_2^-}$")
txt(ax,4.1,.55,r"$\mathrm{H{-}OH}$")
txt(ax,6.9,.55,"C3 of enone")
arrow(ax,(2.3,.58),(3.5,.58),-.45)
arrow(ax,(4.,.38),(4.6,.38),.6)
arrow(ax,(4.8,.58),(6.0,.58),-.45)
txt(ax,3.5,-.5,"Gln–N–H ··· Oδ−",14)
txt(ax,8.1,-.5,"Arg–guanidinium⁺ ··· Oδ−",14)
txt(ax,6.,-1.,"Hydrogen bonds target the oxygen bearing developing negative charge",11)
ax=axes[2]
ax.set_title("Steroid reduction: use steroid numbering independently of cofactor numbering",loc="left",fontsize=13)
fragment(ax,["O","C3","C4","C5"])
txt(ax,5.2,.95,"NADPH C4–H",12)
arrow(ax,(5.2,.72),(5.2,.2),.25)
arrow(ax,(4.5,-.12),(3.05,-.12),-.6)
arrow(ax,(1.7,-.12),(1.05,-.15),-.6)
arrow(ax,(6.1,0),(7.,0))
txt(ax,9.2,.3,"C4 enolate + NADP⁺",14)
txt(ax,9.2,-.4,"C4 protonation restores C3=O",12)
txt(ax,3.0,-.85,"Hydride reaches C5 from the 5α face",12)
ax=axes[3]
ax.set_title("Finasteride: hydride addition creates a nucleophile that traps oxidized cofactor",loc="left",fontsize=13)
fragment(ax,["O","C3","C2","C1"])
txt(ax,5.2,.95,"NADPH C4–H",12)
arrow(ax,(5.2,.72),(5.2,.2),.25)
arrow(ax,(4.5,-.12),(3.05,-.12),-.6)
arrow(ax,(1.7,-.12),(1.05,-.15),-.6)
arrow(ax,(6.1,0),(7.,0))
txt(ax,8.2,.5,"C2 enolate",13)
txt(ax,10.6,.5,"NADP⁺ C4",13)
arrow(ax,(8.8,.25),(10.1,.25),-.5)
txt(ax,9.4,-.5,"New bond: inhibitor C2–cofactor C4",12,color=red)
txt(ax,3.,-.85,"N4 remains in the inhibitor lactam",12)
fig.tight_layout(h_pad=2)
fig.savefig("paper-2-mechanisms.png",dpi=170,facecolor="white")
