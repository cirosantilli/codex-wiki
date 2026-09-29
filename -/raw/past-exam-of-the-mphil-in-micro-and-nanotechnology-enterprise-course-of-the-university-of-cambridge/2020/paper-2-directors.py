"""Original nematic director sketches; NumPy and Matplotlib, Python 3.14."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.collections import LineCollection
fig,axs=plt.subplots(3,4,figsize=(14,11),layout="constrained")
def rods(ax,x,y,u,v,length=.20):
 x,y,u,v=np.broadcast_arrays(x,y,u,v);norm=np.hypot(u,v);ok=norm>1e-8
 x=x[ok];y=y[ok];u=u[ok]/norm[ok];v=v[ok]/norm[ok]
 segments=np.stack([np.column_stack([x-length*u/2,y-length*v/2]),np.column_stack([x+length*u/2,y+length*v/2])],axis=1)
 ax.add_collection(LineCollection(segments,colors="#234f78",linewidths=1.2))
def setup(ax,title):
 ax.set_aspect("equal");ax.set(xlim=(-2.5,2.5),ylim=(-2.2,2.2),title=title);ax.axis("off")
g=np.linspace(-2.2,2.2,15);X,Y=np.meshgrid(g,g)
ax=axs.flat[0];setup(ax,"A  Nematic");rods(ax,X,Y,np.ones_like(X),0*Y)
ax=axs.flat[1];setup(ax,"B  Cholesteric: successive planes")
for j,z in enumerate(np.linspace(-1.8,1.8,7)):
 phi=j*np.pi/4;rods(ax,np.full(5,z),np.linspace(-1.3,1.3,5),np.cos(phi),np.sin(phi),.34)
ax.text(0,-1.9,"helix coordinate increases →",ha="center",fontsize=9)
for index,s in [(2,.5),(3,-.5),(4,1)]:
 ax=axs.flat[index];setup(ax,f"{chr(65+index)}  Planar winding s = {s:+g}")
 phi=s*np.arctan2(Y,X);mask=np.hypot(X,Y)>.25;rods(ax,X[mask],Y[mask],np.cos(phi[mask]),np.sin(phi[mask]));ax.add_patch(Circle((0,0),.13,color="#ac4b42"))
for index,homeo in [(5,True),(6,False)]:
 ax=axs.flat[index];setup(ax,f"{chr(65+index)}  Flat {'homeotropic' if homeo else 'planar'} wall")
 ax.plot([-2.3,2.3],[-1.6,-1.6],"k",lw=2);xx,yy=np.meshgrid(np.linspace(-2,2,11),np.linspace(-1.3,1.7,8))
 rods(ax,xx,yy,0*xx if homeo else 1+0*xx,1+0*yy if homeo else 0*yy,.25)
for index,homeo in [(7,True),(8,False)]:
 ax=axs.flat[index];setup(ax,f"{chr(65+index)}  {'Radial sphere + hedgehog' if homeo else 'Tangential sphere + boojums'}")
 rr=np.hypot(X,Y);mask=rr>0.85;x=X[mask];y=Y[mask];r=rr[mask];co=x/r;si=y/r
 if homeo:
  a=.8;alpha=(a/(r-a))**3;u=1+alpha*co;v=alpha*si
  keep=np.hypot(x+1.6,y)>.18;x=x[keep];y=y[keep];u=u[keep];v=v[keep]
 else:
  a=.8;ur=(1-a**3/r**3)*co;ut=-(1+a**3/(2*r**3))*si
  u=ur*co-ut*si;v=ur*si+ut*co
 rods(ax,x,y,u,v,.19);ax.add_patch(Circle((0,0),.8,fc="white",ec="k",lw=1.7))
 if homeo:ax.add_patch(Circle((-1.6,0),.12,color="#ac4b42"));ax.text(-1.65,-.4,"−1",ha="center")
 else:
  for xx in [-.8,.8]:ax.add_patch(Circle((xx,0),.1,color="#ac4b42"))
for index,homeo in [(9,True),(10,False)]:
 ax=axs.flat[index];setup(ax,f"{chr(65+index)}  {'Escaped radial channel' if homeo else 'Axial planar channel'}")
 xx,zz=np.meshgrid(np.linspace(-.95,.95,9),np.linspace(-1.8,1.8,11))
 beta=np.pi*xx/2;u=np.sin(beta) if homeo else 0*xx;v=np.cos(beta) if homeo else 1+0*xx
 rods(ax,xx,zz,u,v,.22)
 for wall in [-1,1]:ax.plot([wall,wall],[-2,2],"k",lw=2)
 ax.text(1.3,1.6,"axis z",rotation=90,fontsize=9)
ax=axs.flat[11];ax.axis("off");ax.text(.03,.85,"Rods represent n ≡ −n.\nRed marks: defect cores.\n\nSphere fields satisfy the intended\nnear-wall/far-field geometry;\nnot variational energy minimizers.\n\nChannel sketches: axial sections.\nEscaped radial field tilts out of\nthe transverse plane.",va="top",fontsize=11,linespacing=1.6)
fig.savefig("paper-2-directors.png",dpi=155,facecolor="white")

