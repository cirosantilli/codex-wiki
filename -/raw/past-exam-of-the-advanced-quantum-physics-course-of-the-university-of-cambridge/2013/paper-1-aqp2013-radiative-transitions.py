"""Original Einstein-transition schematic; Matplotlib 3.10/Python 3.14.
Save PNG basename to cwd, normally the mirrored _media year directory.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams.update({"font.size": 11, "figure.facecolor": "white", "axes.facecolor": "white"})
fig, axes=plt.subplots(1,3,figsize=(9,3.3),layout="constrained")
def photon(ax,x0,x1,y):
    x=np.linspace(x0,x1,150)
    ax.plot(x,y+0.035*np.sin(np.linspace(0,6*np.pi,len(x))),color="#c16c12",lw=1.6)
    ax.annotate("",(x1,y),(x1-0.07,y),arrowprops={"arrowstyle":"->","color":"#c16c12"})
for i,(ax,title,rate) in enumerate(zip(axes,["Absorption","Stimulated emission","Spontaneous emission"],[r"$B_{12}u(\omega_0)$",r"$B_{21}u(\omega_0)$",r"$A_{21}$"])):
    for y,lab in [(0.2,r"$E_1$"),(0.8,r"$E_2$")]:
        ax.plot([0.19,0.82],[y,y],color="0.2",lw=2)
        ax.text(0.06,y,lab,ha="center",va="center")
    ax.annotate("",(0.5,0.8 if i==0 else 0.2),(0.5,0.2 if i==0 else 0.8),arrowprops={"arrowstyle":"->","lw":2,"color":"#155a91"})
    if i<2:photon(ax,0.04,0.44,0.5)
    if i>0:photon(ax,0.6,0.98,0.5)
    if i==1:photon(ax,0.6,0.98,0.62)
    ax.set_title(title)
    ax.text(0.5,0.02,rate,ha="center",va="center")
    ax.set(xlim=(0,1.03),ylim=(-0.04,0.97))
    ax.axis("off")
fig.suptitle(r"Rates per atom; spectral energy density $u(\omega_0)$")
fig.savefig("paper-1-aqp2013-radiative-transitions.png",dpi=140,facecolor="white",bbox_inches="tight")
