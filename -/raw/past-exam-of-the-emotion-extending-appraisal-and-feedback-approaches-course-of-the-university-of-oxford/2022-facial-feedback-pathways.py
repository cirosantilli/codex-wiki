"""Original causal schematic: alternative routes, not estimated effects.
Python 3.14; Matplotlib from the repository pyproject.toml.
Writes the same-basename opaque white PNG into the current directory.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
fig,ax=plt.subplots(figsize=(11,4.6),layout="constrained",facecolor="white");ax.set(xlim=(0,1),ylim=(0,1));ax.axis("off")
blue="#245b83";orange="#a24820"
def box(x,y,text,color=blue,w=.15):
 p=FancyBboxPatch((x-w/2,y-.09),w,.18,boxstyle="round,pad=0.009",facecolor="white",edgecolor=color,lw=1.7);ax.add_patch(p);ax.text(x,y,text,ha="center",va="center",fontsize=11,color=color);return(x,y)
def arrow(a,b,color=blue,rad=0):
 ax.add_patch(FancyArrowPatch(a,b,arrowstyle="-|>",mutation_scale=13,connectionstyle=f"arc3,rad={rad}",lw=1.6,color=color))
xs=[.09,.295,.50,.705,.91];y=.70
texts=["Randomized\nfacial task","Facial\nactivity","Sensory\nfeedback","Felt\nemotion","Emotion\nreport"]
for x,t in zip(xs,texts):box(x,y,t)
for x,z in zip(xs[:-1],xs[1:]):arrow((x+.083,y),(z-.083,y))
box(.30,.27,"Effort /\nattention",orange,w=.18);box(.56,.27,"Task meaning /\nexpectancy",orange,w=.21)
arrow((.09,.60),(.205,.30),orange,rad=.08)
ax.plot([.09,.09,.56],[.60,.10,.10],color=orange,lw=1.6)
arrow((.56,.10),(.56,.17),orange)
arrow((.30,.37),(.67,.60),orange,rad=-.13)
arrow((.56,.37),(.705,.60),orange,rad=-.08)
arrow((.67,.27),(.91,.60),orange,rad=.05)
ax.text(.5,.95,"Randomizing the facial task identifies its total effect, not a unique mediator",ha="center",va="center",fontsize=13,weight="bold")
ax.text(.5,.035,"Arrows show possible routes. Their sizes and existence are not estimated here.",ha="center",fontsize=10,color="#444444")
fig.savefig(Path(__file__).stem+".png",dpi=100,facecolor="white",transparent=False)
