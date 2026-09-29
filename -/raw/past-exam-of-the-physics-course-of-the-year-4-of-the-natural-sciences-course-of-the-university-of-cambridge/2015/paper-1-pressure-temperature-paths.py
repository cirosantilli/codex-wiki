"""Original symbolic pressure-temperature integration path schematic."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

fig,ax=plt.subplots(figsize=(7,4.9),dpi=100,facecolor="white")
paths=[([0,1,1],[0,0,1],"#a84f32","a: heat first",(.52,-.12)),([0,0,1],[0,1,1],"#28638c","b: compress first",(.42,1.09)),([0,1],[0,1],"#398259","c: straight path",(.42,.37))]
for xs,ys,col,label,pos in paths:
    ax.plot(xs,ys,color=col,lw=2.4);ax.text(*pos,label,color=col,fontsize=12)
    for i in range(len(xs)-1):
        x,y=(xs[i]+xs[i+1])/2,(ys[i]+ys[i+1])/2;dx,dy=(xs[i+1]-xs[i])*.12,(ys[i+1]-ys[i])*.12
        ax.annotate("",xy=(x+dx,y+dy),xytext=(x-dx,y-dy),arrowprops={"arrowstyle":"-|>","lw":1.7,"color":col})
ax.scatter([0,1],[0,1],color="black",s=32,zorder=5)
ax.set(xlim=(-.27,1.3),ylim=(-.25,1.3),xticks=[0,1],xticklabels=[r"$T_1$",r"$T_2$"],yticks=[0,1],yticklabels=[r"$P_1$",r"$P_2$"],xlabel="Temperature",ylabel="Pressure",title="Same endpoints, different pressure-volume work")
ax.spines[['top','right']].set_visible(False)
fig.subplots_adjust(left=.13,right=.98,top=.88,bottom=.14)
fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,facecolor="white")
