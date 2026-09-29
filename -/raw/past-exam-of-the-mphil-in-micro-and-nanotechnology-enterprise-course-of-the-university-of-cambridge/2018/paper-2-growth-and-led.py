"""Original process, facet-normal and qualitative band diagrams; output basename to cwd."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,Circle
fig,axs=plt.subplots(2,2,figsize=(12,8),layout="constrained")
ax=axs[0,0];ax.set(xlim=(0,10),ylim=(0,6),title="A  Supported CVD carpet")
ax.add_patch(Rectangle((.5,.8),8.8,.5,color="#d6d7d9"));ax.text(5,.3,"quartz support",ha="center")
for j,x in enumerate(np.linspace(1.2,8.5,22)):
 ax.add_patch(Circle((x,1.4),.10,color="#a66d3e"))
 y=np.linspace(1.5,4.5+.18*np.sin(j),80);ax.plot(x+.04*np.sin(5*y+j),y,color="#344d59",lw=1)
ax.annotate("carbon-containing gas",xy=(7,5.3),xytext=(1,5.3),arrowprops={"arrowstyle":"->"})
ax.text(5,1.05,"supported catalyst particles",ha="center",fontsize=9);ax.axis("off")
ax=axs[0,1];ax.set(xlim=(0,10),ylim=(0,6),title="B  Floating catalyst and direct spinning")
ax.add_patch(Rectangle((1,1.8),5.5,2.4,fc="#f2dfcf",ec="#8b5f3e"));ax.text(3.7,4.5,"heated gas-flow reactor",ha="center")
rng=np.random.default_rng(7)
for _ in range(28):
 x=rng.uniform(1.3,5.8);y=rng.uniform(2.1,3.9);ax.plot([x,x+.4],[y,y+.07],color="#4b5a63",lw=.8)
for y in np.linspace(2.1,3.9,14):ax.plot([5.5,7.7],[y,3],color="#4b5a63",lw=.7)
ax.plot([7.7,8.6],[3,3],color="k",lw=2);ax.add_patch(Circle((9,3),.5,fill=False,lw=2))
ax.annotate("feed + catalyst + promoter",xy=(1.1,3),xytext=(.2,1.0),arrowprops={"arrowstyle":"->"},fontsize=9)
ax.text(7.6,1.55,"aerogel → drawn fiber",ha="center");ax.text(9,.8,"take-up spindle",ha="center",fontsize=9);ax.axis("off")
ax=axs[1,0];ax.set_aspect("equal");ax.set(xlim=(-.4,1.8),ylim=(-.3,1.6),title="C  Cubic facet normals in the viewing plane")
for end,label in [((1.5,0),"(001)"),((0,1.35),"(010)"),((1,1),"(011)")]:
 ax.annotate("",xy=end,xytext=(0,0),arrowprops={"arrowstyle":"->","lw":2});ax.text(end[0]+.04,end[1]+.04,label)
ang=np.linspace(0,np.pi/4,50);ax.plot(.55*np.cos(ang),.55*np.sin(ang),"k:");ax.text(.61,.21,"45°")
ax.text(.45,-.25,"[001]");ax.text(-.3,.7,"[010]",rotation=90);ax.axis("off")
ax=axs[1,1];x=np.linspace(0,1,600);inside=(x>.43)&(x<.60)
# Isolate band offsets: electrostatic band bending/quasi-Fermi splitting not solved.
ec=np.where(inside,2.6,3.4);ev=np.where(inside,.5,0)
ax.plot(x,ec,label="conduction-band edge");ax.plot(x,ev,label="valence-band edge")
ax.axvspan(.43,.60,color="#dfe9d3",alpha=.7);ax.text(.1,1.8,"n-GaN");ax.text(.67,1.8,"p-GaN");ax.text(.515,1.2,"InGaN\n5 nm",ha="center")
ax.set(xlabel="radial core → exterior coordinate (schematic)",ylabel="relative band-edge energy",title="D  Type-I active-layer offsets",ylim=(-.3,4))
ax.legend(fontsize=9);ax.text(.03,3.75,"band bending omitted; not to scale",fontsize=9)
fig.savefig("paper-2-growth-and-led.png",dpi=150,facecolor="white")

