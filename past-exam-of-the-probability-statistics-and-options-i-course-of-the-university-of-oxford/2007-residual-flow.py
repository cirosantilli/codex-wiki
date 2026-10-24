"""Original residual rerouting diagram. Python3.14 and Matplotlib. Output CWD."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
pos={1:(0,1),2:(1,2),3:(1,0),4:(2,2),5:(2,0),6:(3,1)}
arcs=[(1,2,3,1,2),(1,3,3,3,3),(2,4,2,1,2),(3,4,2,2,1),(3,5,3,1,2),(4,6,3,3,3),(5,6,2,1,2)]
fig,axes=plt.subplots(1,2,figsize=(10,4),facecolor="white")
for ax,idx,title in zip(axes,[3,4],["Initial flow: value 4","After rerouting: value 5"]):
 for arc in arcs:
  u,v,cap=arc[:3];flow=arc[idx];p,q=pos[u],pos[v]
  ax.annotate("",q,p,arrowprops=dict(arrowstyle="->",lw=1.8,color="#2166ac",shrinkA=15,shrinkB=15))
  mx,my=(p[0]+q[0])/2,(p[1]+q[1])/2
  dx,dy=(.15,0)if(u,v)==(3,4)else(0,.12)
  ax.text(mx+dx,my+dy,f"{flow}/{cap}",fontsize=11,ha="center",bbox=dict(fc="white",ec="none",pad=1))
 for n,(x,y)in pos.items():
  ax.scatter([x],[y],s=360,facecolor="white",edgecolor=".2",zorder=4)
  ax.text(x,y,str(n),ha="center",va="center",fontsize=12,zorder=5)
 ax.set(xlim=(-.3,3.3),ylim=(-.4,2.5),aspect="equal",title=title);ax.axis("off")
axes[0].text(1.5,-.35,"arc labels: flow / capacity",ha="center",fontsize=10)
axes[1].text(1.5,-.35,"augment 1 → 2 → 4 → 3 → 5 → 6",ha="center",fontsize=10,color="#b2182b")
fig.tight_layout();fig.savefig("2007-residual-flow.png",dpi=150,facecolor="white")
