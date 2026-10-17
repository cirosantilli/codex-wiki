"""Original interaction and rheology sketches/calculations; outputs to cwd."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,Rectangle
fig,axs=plt.subplots(2,3,figsize=(15,9),layout="constrained")
ax=axs[0,0];ax.set(xlim=(0,6),ylim=(0,6),title="A  Five interaction origins")
labels=["double-layer overlap","correlated fluctuations","grafted-layer overlap","excluded small-solute volume","structured solvent"]
for j,label in enumerate(labels):
 y=5.3-j
 for x in [.7,1.7]:ax.add_patch(Circle((x,y),.29,fc="#d7e3ed",ec="k"))
 ax.text(2.2,y,label,va="center",fontsize=9)
 if j==0:
  for x in [.7,1.7]:ax.add_patch(Circle((x,y),.46,fill=False,ls=":",ec="#4978a2"))
 elif j==1:ax.text(.7,y,"+−",ha="center",va="center");ax.text(1.7,y,"−+",ha="center",va="center")
 elif j==2:
  for x in [.7,1.7]:
   for a in np.linspace(0,2*np.pi,10):ax.plot([x+.3*np.cos(a),x+.48*np.cos(a)],[y+.3*np.sin(a),y+.48*np.sin(a)],color="#617b43",lw=.7)
 elif j==3:
  ax.scatter([.15,2.05,.3,1.4],[y+.5,y+.4,y-.5,y-.5],s=8,color="#b67448")
 elif j==4:
  for x in [.3,.9,1.5,2.1]:ax.text(x,y-.48,"~",ha="center")
ax.axis("off")
ax=axs[0,1];ax.set_aspect("equal");ax.set(xlim=(-1.3,3.2),ylim=(-1.3,1.5),title="B  Point charge and induced dipole")
ax.add_patch(Circle((0,0),.18,fc="#d59a83",ec="k"));ax.text(0,0,"Q",ha="center",va="center")
ax.add_patch(Circle((2,0),.75,fc="#d8e5ef",ec="k"))
ax.text(1.65,0,"−",ha="center",fontsize=19);ax.text(2.35,0,"+",ha="center",fontsize=18)
ax.annotate("",xy=(2,.95),xytext=(0,.95),arrowprops={"arrowstyle":"<->"});ax.text(1,1.1,"center distance R",ha="center",fontsize=9)
ax.annotate("",xy=(1.25,-.8),xytext=(.18,-.8),arrowprops={"arrowstyle":"<->"});ax.text(.7,-1.05,"gap r",ha="center",fontsize=9)
ax.plot([2,2.75],[0,0],"k:");ax.text(2.4,.18,"a");ax.text(1.2,-1.28,"R = a + r (point-ion limit)",ha="center",fontsize=9);ax.axis("off")
ax=axs[0,2];r=np.linspace(.35,3,1200)
ax.plot(r,-1/r**4,label=r"literal $-C_4/r^4$")
ax.plot(r,.03/r**12-1/r**4,label="toy repulsive regularization")
ax.axhline(0,color="gray",lw=.7);ax.set(xlabel="formal separation (chosen units)",ylabel="potential (chosen units)",ylim=(-4,3),title="C  Attraction and short-range failure");ax.legend(fontsize=8)
ax=axs[1,0];t=np.linspace(0,5,400)
ax.plot(t,np.ones_like(t),"k:",label="normalized applied step")
ax.plot(t,1-np.exp(-t),label="KV creep strain / final strain")
ax.plot(t,np.exp(-t),label="Maxwell relaxation stress / initial")
ax.set(xlabel="time / relaxation or retardation time",ylabel="normalized input / response",title="D  Different controlled-step experiments");ax.legend(fontsize=8)
ax=axs[1,1];ax.set(xlim=(-2,2),ylim=(0,5),title="E  Maxwell branch parallel to dashpot")
for yy in [.5,4.4]:ax.plot([-1,1],[yy,yy],"k")
# Left branch: zigzag spring then viscous element.
ax.plot([-1,-1],[4.4,4],"k");ys=np.linspace(4,2.6,13);xs=-1+.16*np.sin(np.arange(13)*np.pi/2);ax.plot(xs,ys,"k")
ax.plot([-1,-1],[2.6,2.2],"k")
for xx,label in [(-1,r"$\eta_M$"),(1,r"$\eta_s$")]:
 ax.add_patch(Rectangle((xx-.25,1.15),.5,1,fill=False));ax.plot([xx,xx],[.5,1.15],"k")
 if xx==1:ax.plot([xx,xx],[2.15,4.4],"k")
 ax.text(xx+.35,1.6,label)
ax.text(-.55,3.2,"G");ax.text(0,4.65,"same strain; stresses add",ha="center",fontsize=9);ax.axis("off")
ax=axs[1,2];w=np.logspace(-3,2,500);G=2;etaM=3;etas=.4;tau=etaM/G
gp=G*(w*tau)**2/(1+(w*tau)**2);gpp=w*etas+G*w*tau/(1+(w*tau)**2)
ax.loglog(w,gp,label="storage G′");ax.loglog(w,gpp,label="loss G″")
ax.set(xlabel="angular frequency (chosen units)",ylabel="modulus (chosen units)",title="F  Anti-Zener: terminal viscous response");ax.legend(fontsize=9)
fig.savefig("paper-2-colloid-rheology.png",dpi=150,facecolor="white")

