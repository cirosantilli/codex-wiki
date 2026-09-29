"""Original HZZ and HHZZ vertices. Run from the desired PNG output directory.

Root dependency pins: Python 3.14, matplotlib 3.10.7, numpy 2.3.5.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def wave(ax, a, b):
    a, b = np.array(a), np.array(b)
    delta = b-a
    normal = np.array([-delta[1],delta[0]])/np.linalg.norm(delta)
    t=np.linspace(0,1,500)
    pts=a[:,None]+delta[:,None]*t+normal[:,None]*.017*np.sin(16*np.pi*t)
    ax.plot(*pts,color="#14658c",lw=1.7)

fig,axs=plt.subplots(1,2,figsize=(8,3.2),dpi=100,facecolor="white")
for ax,quartic in zip(axs,[False,True]):
    ax.set(xlim=(0,1),ylim=(0,1));ax.axis("off");ax.set_facecolor("white")
    centre=(.45,.53)
    for y in ([.8,.25] if quartic else [.53]):
        ax.plot([.12,centre[0]],[y,centre[1]],"--",color="#333333",lw=1.8)
        ax.text(.065,y,"$H$",ha="center",va="center",fontsize=16)
    for y in [.8,.25]:
        wave(ax,centre,(.85,y))
        ax.text(.92,y,"$Z$",ha="center",va="center",fontsize=16)
    ax.plot(*centre,"o",color="black",ms=5)
    ax.text(.5,.96,"Quartic vertex" if quartic else "Cubic vertex",
            ha="center",va="top",fontsize=14)
    ax.text(.5,.08,r"$2i m_Z^2 g_{\mu\nu}/v^2$" if quartic else
            r"$2i m_Z^2 g_{\mu\nu}/v$",ha="center",fontsize=16)
fig.subplots_adjust(left=.02,right=.98,bottom=.03,top=.97,wspace=.18)
fig.savefig(Path.cwd()/(Path(__file__).stem+".png"),dpi=100,facecolor="white",
            transparent=False)
plt.close(fig)
