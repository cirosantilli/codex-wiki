"""Original binding counterexample, not an experimental stimulus or dataset.
Python 3.14; Matplotlib from the repository pyproject.toml.
Writes same-basename opaque white PNG to CWD.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
fig,ax=plt.subplots(figsize=(9,3.5),layout="constrained",facecolor="white");ax.set(xlim=(0,1),ylim=(0,1));ax.axis("off")
colors={"L":"#245b83","R":"#b65324"}
for center,title,events in [(.25,"Event set 1",[("A","L","1"),("B","R","2")]),(.75,"Event set 2",[("A","R","1"),("B","L","2")])]:
 ax.text(center,.90,title,ha="center",weight="bold",fontsize=14)
 ax.text(center,.77,"Item     Place     Time",ha="center",fontsize=11,color="#555555")
 for y,(item,place,t) in zip([.61,.40],events):
  ax.add_patch(FancyBboxPatch((center-.19,y-.075),.38,.15,boxstyle="round,pad=.01",fc="white",ec=colors[place],lw=1.8))
  ax.text(center,y,f"{item}          {place}          {t}",ha="center",va="center",fontsize=14,color=colors[place])
ax.text(.5,.19,"Same lists: items {A, B}; places {L, R}; times {1, 2}",ha="center",fontsize=12)
ax.text(.5,.055,"Different binding: A occurred at L in set 1, but at R in set 2.",ha="center",fontsize=12,weight="bold")
fig.savefig(Path(__file__).stem+".png",dpi=100,facecolor="white",transparent=False)
