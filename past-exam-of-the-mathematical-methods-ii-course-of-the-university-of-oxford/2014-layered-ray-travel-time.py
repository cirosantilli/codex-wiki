from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":12,"axes.titlesize":14,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white","savefig.transparent":False})

u,v,w=1.,.6,1.4;X=3.;speeds=np.array([u,v,w]);lo=0.;hi=.999999/speeds.max()
for _ in range(80):
 p=(lo+hi)/2;dx=p*speeds/np.sqrt(1-(p*speeds)**2)
 if dx.sum()<X:lo=p
 else:hi=p
p=(lo+hi)/2;dx=p*speeds/np.sqrt(1-(p*speeds)**2);xc=np.r_[0,np.cumsum(dx)]
fig,(ax,bx)=plt.subplots(1,2,figsize=(10,4.8),layout="constrained")
for i,(speed,col) in enumerate(zip(speeds,["#e4eff7","#f6ecd9","#e7f1e5"])):
 ax.axhspan(i,i+1,color=col);ax.text(3.45,i+.5,f"speed {speed:g}",ha="right",fontsize=11)
ax.plot(xc,[0,1,2,3],"o-",color="#374f68",lw=2.5)
for x,y in zip(xc[1:3],[1,2]):ax.plot([x,x],[y-.35,y+.35],ls=":",color="#775394")
ax.set(xlabel="Horizontal position",ylabel="Layer coordinate y",xlim=(-.1,3.55),ylim=(-.05,3.1),title="Illustrative minimum-time ray (X = 3)");ax.set_aspect("equal")
z1,z2=np.meshgrid(np.linspace(-.4,2.5,240),np.linspace(.2,3.4,240));time=np.sqrt(1+z1*z1)/u+np.sqrt(1+(z2-z1)**2)/v+np.sqrt(1+(X-z2)**2)/w
levels=np.min(time)+np.array([.01,.04,.1,.2,.4,.7,1.1,1.6,2.3]);cs=bx.contour(z1,z2,time,levels=levels,cmap="viridis");bx.clabel(cs,fontsize=9,fmt="%.2f");bx.plot(xc[1],xc[2],"*",ms=14,color="#b45636")
bx.set(xlabel="First crossing x₁",ylabel="Second crossing x₂",title="Travel-time contours: one strict minimum");bx.grid(alpha=.12)
fig.suptitle("Positive speeds give a positive-definite crossing-position Hessian",fontsize=14)
fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=120)
plt.close(fig)
