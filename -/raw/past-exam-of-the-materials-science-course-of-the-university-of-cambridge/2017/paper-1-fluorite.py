"""Original geometric fluorite diagram; Python 3.14, numpy, matplotlib.
Run from the desired output directory; writes a basename PNG to cwd.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle
fig=plt.figure(figsize=(10,4.8),layout="constrained")
a=fig.add_subplot(121)
a.add_patch(Rectangle((0,0),1,1,fill=False,lw=1.8))
for x,y,z in [(0,0,"0, 1"),(1,0,"0, 1"),(0,1,"0, 1"),(1,1,"0, 1"),(.5,.5,"0, 1"),(.5,0,"1/2"),(.5,1,"1/2"),(0,.5,"1/2"),(1,.5,"1/2")]:
 a.scatter(x,y,s=350,color="#336fa5",edgecolor="black",zorder=3)
 a.annotate(z,(x,y),xytext=(7,8),textcoords="offset points",fontsize=9)
for x in [.25,.75]:
 for y in [.25,.75]:
  a.scatter(x,y,s=160,color="#e89540",edgecolor="black",zorder=4)
  a.annotate("1/4, 3/4",(x,y),xytext=(-25,-20),textcoords="offset points",fontsize=9)
a.scatter([],[],s=160,color="#336fa5",label="Ca site")
a.scatter([],[],s=90,color="#e89540",label="F site (two depths)")
a.legend(loc="lower center",bbox_to_anchor=(.5,-.23),ncol=2,frameon=False,fontsize=9)
a.set(xlim=(-.13,1.18),ylim=(-.12,1.15),aspect="equal",xlabel="x/a",ylabel="y/a",title="[001] projection; labels are z/a")
a.set_xticks([0,.25,.5,.75,1]);a.set_yticks([0,.25,.5,.75,1])
b=fig.add_subplot(122,projection="3d")
from itertools import product
corners=np.array(list(product([0,1],repeat=3)))
for i,u in enumerate(corners):
 for v in corners[i+1:]:
  if np.sum(np.abs(u-v))==1:b.plot(*np.array([u,v]).T,color="#808080",lw=1)
b.scatter(*corners.T,s=180,c="#e89540",edgecolor="black",depthshade=False)
b.scatter([.5],[.5],[.5],s=300,c="#336fa5",edgecolor="black",depthshade=False)
b.plot([0,.5],[0,.5],[0,.5],c="#336fa5",lw=2)
b.text(.51,.51,.48,"Ca",fontsize=10);b.text(1,0,1.1,"F",fontsize=10)
b.text(.4,-.22,0,"edge = a/2 = 2 r(F)",fontsize=9)
b.text(-.15,.1,1.35,"centre–corner = sqrt(3) a/4",fontsize=9)
b.set_title("Eight-anion contact cube",pad=18)
b.set_axis_off();b.set_box_aspect((1,1,1));b.view_init(elev=19,azim=-63)
fig.savefig("paper-1-fluorite.png",dpi=155,facecolor="white")
