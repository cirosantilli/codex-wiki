"""Python 3.14; Matplotlib in ../pyproject.toml. Output in CWD."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
pos={1:(0,2),2:(-1,1),3:(1,1),4:(-1.5,0),5:(-.5,0),6:(.5,0),7:(1.5,0)}
edges=[(1,2),(1,3),(2,4),(2,5),(3,6),(3,7)]
fig,ax=plt.subplots(figsize=(6,3.7),facecolor="white")
for a,b in edges:ax.plot([pos[a][0],pos[b][0]],[pos[a][1],pos[b][1]],color=".4",lw=2)
for n,(x,y) in pos.items():
 ax.scatter([x],[y],s=550,facecolor="#fff0cf" if n==1 else "white",edgecolor="C0",lw=2,zorder=3)
 ax.text(x,y,str(n),ha="center",va="center",zorder=4)
ax.text(.3,2,"Root",va="center",fontsize=10)
ax.set_title("Prüfer code (2, 2, 1, 3, 3)")
ax.set_aspect("equal");ax.axis("off");ax.margins(.2)
fig.tight_layout();fig.savefig("2008-rooted-binary-tree.png",dpi=150,facecolor="white")
