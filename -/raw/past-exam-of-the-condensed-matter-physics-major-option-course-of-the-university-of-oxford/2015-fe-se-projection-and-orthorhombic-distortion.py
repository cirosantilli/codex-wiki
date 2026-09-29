from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Polygon
plt.rcParams.update({"font.size":11,"font.family":"DejaVu Sans","figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})

fig,axs=plt.subplots(1,2,figsize=(10.8,5.3),layout="constrained")
ax=axs[0]
for x,y in [(0,0),(1,0),(0,1),(1,1),(.5,.5)]:ax.scatter(x,y,s=170,color="#174c75",zorder=5)
for x,y in [(.5,0),(.5,1)]:ax.scatter(x,y,s=180,marker="^",color="#b35b15",zorder=5)
for x,y in [(0,.5),(1,.5)]:ax.scatter(x,y,s=180,marker="v",color="#7b4280",zorder=5)
ax.add_patch(Rectangle((0,0),1,1,fill=False,lw=1.5));ax.text(.5,.63,"Fe: z = 0",ha="center",color="#174c75")
ax.text(.5,-.14,r"Se: $z=+\eta$",ha="center",color="#9f4d12");ax.text(-.02,.67,r"Se: $z=-\eta$",ha="left",color="#7b4280")
ax.set(xlim=(-.2,1.2),ylim=(-.22,1.2),xlabel="Fractional x",ylabel="Fractional y",title="Tetragonal projection")
ax.set_aspect('equal');ax.set_xticks([0,.5,1]);ax.set_yticks([0,.5,1])
ax=axs[1];A=np.array([1.18,1.18]);B=np.array([.9,-.9]);origin=np.array([0,0]);points=np.array([origin,A,A+B,B,origin]);ax.plot(points[:,0],points[:,1],color="#174c75",lw=2)
for end,label,col in [(A,'A parallel to [110]',"#174c75"),(B,'B parallel to [1 -1 0]',"#b35b15")]:
 ax.annotate('',xy=end,xytext=origin,arrowprops=dict(arrowstyle='->',lw=2,color=col));ax.text(*(end*.55+np.array([.06,.12])),label,color=col,rotation=45 if end[1]>0 else -45,ha='left',fontsize=10)
ax.text(1.0,-1.45,'A and B have unequal lengths.\nThe 90-degree twin swaps them.',ha='center',fontsize=11)
ax.scatter(points[:-1,0],points[:-1,1],s=85,color="#174c75");ax.set(xlim=(-.2,2.4),ylim=(-1.9,1.55),title="Orthorhombic diagonal axes")
ax.set_aspect('equal');ax.axis('off')
fig.suptitle('Coordinate-derived FeSe projection and an exaggerated shear',fontsize=15)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=140,transparent=False)
