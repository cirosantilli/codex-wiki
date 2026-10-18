"""Original Oxford CP2 2013 figure; Python 3.14, NumPy and Matplotlib root dependencies."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":12,"axes.titlesize":14,"axes.labelsize":12,"legend.fontsize":10,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white","font.family":"DejaVu Sans"})

from matplotlib.patches import Circle
n=1.33;d=np.sqrt(2);phi=np.linspace(0,np.pi/4,60001);ell=np.sqrt(3-2*d*np.cos(phi));inc=np.arcsin(d*np.sin(phi)/(n*ell));beta=phi-inc;y=np.sin(phi)-np.cos(phi)*np.tan(beta);j=np.argmax(y);f=y[j];p=phi[j]
fig,(geo,graph)=plt.subplots(1,2,figsize=(10.4,4.8),gridspec_kw={"width_ratios":[1.15,1]},layout="constrained")
geo.add_patch(Circle((0,0),1,fill=False,color=".35",lw=1.8))
geo.plot([0,0],[-1,1],color=".7",lw=5)
geo.plot([0,0],[-f,f],color="#27835b",lw=5,label="Visible swim interval")
eye=np.array([d,0]);geo.plot(*eye,"ko",ms=7);geo.text(d+.05,0,"Eye",va="center")
for sign in [-1,1]:
    P=np.array([np.cos(p),sign*np.sin(p)]);T=np.array([0,sign*f])
    geo.plot([T[0],P[0],eye[0]],[T[1],P[1],eye[1]],color="#146b9c",lw=1.8)
    geo.plot(*T,"o",color="#27835b",ms=6);geo.plot(*P,"o",color="#146b9c",ms=4)
geo.axhline(0,color=".75",lw=.7);geo.text(-.06,1.08,"Swim diameter",ha="center",fontsize=11)
geo.text(-1.02,-1.15,r"Eye at $(\sqrt{2}R,0)$",fontsize=11)
geo.set(xlim=(-1.15,1.9),ylim=(-1.3,1.3),aspect="equal",title="Limiting single-pass refracted rays",xlabel=r"$x/R$",ylabel=r"$y/R$")
graph.plot(phi*180/np.pi,y,color="#146b9c",lw=2.3)
graph.plot(p*180/np.pi,f,"o",color="#d76c20",ms=6);graph.plot(45,y[-1],"o",mfc="white",mec="#146b9c",ms=6)
graph.annotate(f"Maximum {f:.5f}\nat {p*180/np.pi:.2f}°",xy=(p*180/np.pi,f),xytext=(16,.44),arrowprops={"arrowstyle":"-","color":".4"},fontsize=11)
graph.set(xlim=(0,46),ylim=(0,.82),xlabel=r"Wall angle $\phi$ (degrees)",ylabel=r"Swim-line intercept $y/R$",title="Visible fraction ≈ 0.75744")
graph.text(7,.1,"Grazing outgoing ray:\nintercept 0.75350",fontsize=10)
graph.grid(alpha=.18)

fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=160,facecolor="white",metadata={"Software":"Original CP2 solution figure"})
plt.close(fig)
