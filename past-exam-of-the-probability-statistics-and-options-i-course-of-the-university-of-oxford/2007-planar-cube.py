"""Original planar cube graph. Python3.14 and Matplotlib. Output in CWD."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
fig,ax=plt.subplots(figsize=(5,5),facecolor="white")
outer=[(-2,-2),(2,-2),(2,2),(-2,2)];inner=[(-.8,-.8),(.8,-.8),(.8,.8),(-.8,.8)]
for pts in [outer,inner]:
 for i in range(4):
  p,q=pts[i],pts[(i+1)%4];ax.plot([p[0],q[0]],[p[1],q[1]],color="#2166ac",lw=2)
for p,q in zip(outer,inner):ax.plot([p[0],q[0]],[p[1],q[1]],color="#2166ac",lw=2)
pts=outer+inner;ax.scatter([p[0]for p in pts],[p[1]for p in pts],s=45,color="#b2182b",zorder=4)
ax.set(xlim=(-2.5,2.5),ylim=(-2.5,2.5),aspect="equal",title="Cube graph: 8 vertices, 12 edges, 6 faces")
ax.axis("off");fig.tight_layout();fig.savefig("2007-planar-cube.png",dpi=150,facecolor="white")
