"""Original diagrams; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Run in the desired output directory. A caller-supplied MPLCONFIGDIR is retained.
"""
import os
from pathlib import Path
os.environ.setdefault("MPLCONFIGDIR", str(Path.cwd() / ".mplconfig"))
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch

def line(ax,a,b,kind="fermion",flow=1):
 a=np.asarray(a,dtype=float);b=np.asarray(b,dtype=float)
 if kind=="photon":
  v=b-a;length=np.linalg.norm(v);normal=np.array([-v[1],v[0]])/length
  t=np.linspace(0,1,250);xy=a[None,:]+t[:,None]*v[None,:]+.016*np.sin(2*np.pi*7*t)[:,None]*normal[None,:]
  ax.plot(xy[:,0],xy[:,1],color="#1e5d9e",lw=1.9)
 else:
  ax.plot([a[0],b[0]],[a[1],b[1]],color="#192533",lw=1.9,ls="--" if kind=="scalar" else "-")
  if flow:
   c=a+.42*(b-a);d=a+.62*(b-a)
   if flow<0:c,d=d,c
   ax.add_patch(FancyArrowPatch(c,d,arrowstyle="-|>",mutation_scale=11,color="#192533",lw=1.3))

def setup(ax,title):
 ax.set_xlim(0,1);ax.set_ylim(0,1);ax.set_aspect("auto");ax.axis("off");ax.set_title(title,fontsize=13,pad=8)
def dot(ax,p):ax.plot(*p,"o",color="#192533",ms=4)
def label(ax,p,text,ha="center"):ax.text(*p,text,ha=ha,va="center",fontsize=11)
def exchange(ax,title,out3=3,out4=4,anti=False,boson="scalar",scalar=False):
 setup(ax,title);v=(.47,.67);z=(.47,.3);ends=[(.08,.9),(.88,.9),(.08,.08),(.88,.08)]
 line(ax,ends[0],v,"scalar" if scalar else "fermion",1)
 line(ax,v,ends[1],"scalar" if scalar else "fermion",1)
 line(ax,ends[2],z,"scalar" if scalar else "fermion",-1 if anti else 1)
 line(ax,z,ends[3],"scalar" if scalar else "fermion",-1 if anti else 1)
 line(ax,v,z,boson,0);dot(ax,v);dot(ax,z)
 particle=r"\phi" if scalar else r"\psi";ap=r"\bar\phi" if scalar else r"\bar\psi"
 for p,text in zip([(.16,.94),(.79,.94),(.16,.025),(.79,.025)],[f"${particle}_1$ in",f"${particle}_{out3}$ out",f"${ap if anti else particle}_2$ in",f"${ap if anti else particle}_{out4}$ out"]):label(ax,p,text)
def annihilation(ax,title,scalar=False,boson="scalar"):
 setup(ax,title);v=(.32,.5);z=(.68,.5);ends=[(.08,.85),(.08,.15),(.92,.85),(.92,.15)];kind="scalar" if scalar else "fermion"
 for a,b,flow in [(ends[0],v,1),(ends[1],v,-1),(z,ends[2],1),(z,ends[3],-1)]:line(ax,a,b,kind,flow)
 line(ax,v,z,boson,0);dot(ax,v);dot(ax,z)
 particle=r"\phi" if scalar else r"\psi";ap=r"\bar\phi" if scalar else r"\bar\psi"
 for p,text in zip([(.16,.94),(.16,.04),(.84,.94),(.84,.04)],[f"${particle}_1$ in",f"${ap}_2$ in",f"${particle}_3$ out",f"${ap}_4$ out"]):label(ax,p,text)

fig,axes=plt.subplots(1,2,figsize=(11,3.6),dpi=100,facecolor="white")
exchange(axes[0],r"$t$ photon exchange: $q=p_1-p_3$",anti=True,boson="photon",scalar=True)
annihilation(axes[1],r"$s$ photon annihilation: $q=p_1+p_2$",scalar=True,boson="photon")
fig.suptitle("Scalar particle-antiparticle scattering at order $e^2$",fontsize=16,y=.99)
fig.subplots_adjust(left=.025,right=.975,bottom=.05,top=.82,wspace=.15)
fig.savefig(Path.cwd()/"paper-41-scalar-qed-scattering.png",dpi=100,facecolor="white",transparent=False)
plt.close(fig)
