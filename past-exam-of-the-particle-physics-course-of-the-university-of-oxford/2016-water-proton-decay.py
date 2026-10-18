from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, FancyArrowPatch
plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans", "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white"})

fig,(ax,bx)=plt.subplots(1,2,figsize=(10,5.1),gridspec_kw={"width_ratios":[1.25,1]})
ax.set(xlim=(-3.1,3.1),ylim=(-2.9,2.9),aspect="equal");ax.axis("off")
ax.add_patch(Circle((0,0),2.55,facecolor="#e9f6fc",edgecolor="#234e70",lw=2))
for th in np.linspace(0,2*np.pi,30,endpoint=False):ax.add_patch(Circle((2.4*np.cos(th),2.4*np.sin(th)),.07,facecolor="#2b5672"))
vertex=np.array([-.6,0]);ax.scatter(*vertex,s=38,color="black");ax.text(-1.15,-.32,r"$p$",fontsize=15)
for endpoint,lab,col,ty in [(np.array([-2.1,0]),r"$\mu^+$","#cb623d",.2),(np.array([1.95,.76]),r"$\gamma_1$","#267e9c",.2),(np.array([1.95,-.76]),r"$\gamma_2$","#267e9c",-.35)]:
 ax.annotate("",xy=endpoint,xytext=vertex,arrowprops=dict(arrowstyle="->",lw=2,color=col));ax.text(*[endpoint[0],endpoint[1]+ty],lab,fontsize=14,color=col,ha="center")
ax.text(.8,-1.7,r"$\pi^0\to\gamma\gamma$"+"\nat the decay vertex",ha="center",fontsize=11);ax.text(0,-2.85,"Water volume surrounded by inward-facing photomultipliers",ha="center",fontsize=10);ax.set_title("Prompt two-body decay and photon conversion")
bx.set(xlim=(0,1),ylim=(0,1));bx.axis("off");bx.set_title("Reconstructed event checks")
for y,txt in [(.88,"One sharp muon-like ring"),(.74,"Two diffuse shower-like rings"),(.60,r"$m_{\gamma\gamma}\simeq m_{\pi^0}$"),(.47,r"$m_{\mu\gamma\gamma}\simeq m_p$"),(.34,r"$\sum\mathbf{p}\simeq0$ (free proton)"),(.19,r"Delayed $\mu^+\to e^+\nu\bar\nu$"),(.08,r"Mean delay $2.2\ \mu\mathrm{s}$")]:bx.text(.03,y,txt,fontsize=12,va="center")
fig.subplots_adjust(left=.03,right=.99,bottom=.08,top=.89,wspace=.08)

fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, dpi=140, facecolor="white", transparent=False)
plt.close(fig)
