"""Original allowed charged-current tree diagrams; PNG output is to CWD.

Root dependency pins: Python 3.14, matplotlib 3.10.7, numpy 2.3.5.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def segment(ax,a,b):
    a,b=np.array(a),np.array(b)
    ax.plot([a[0],b[0]],[a[1],b[1]],color="#333333",lw=1.6)
    ax.annotate("",xy=a+.65*(b-a),xytext=a+.4*(b-a),
                arrowprops={"arrowstyle":"-|>","lw":1.3,"color":"#333333"})
def wave(ax,a,b):
    a,b=np.array(a),np.array(b);d=b-a
    normal=np.array([-d[1],d[0]])/np.linalg.norm(d)
    t=np.linspace(0,1,500)
    pts=a[:,None]+d[:,None]*t+normal[:,None]*.017*np.sin(16*np.pi*t)
    ax.plot(*pts,color="#14658c",lw=1.7)
def label(ax,x,y,text):ax.text(x,y,text,fontsize=15,ha="center",va="center")
def vertices(ax,*pts):
    for pt in pts:ax.plot(*pt,"o",color="black",ms=4)
fig,axs=plt.subplots(1,3,figsize=(10,3.6),dpi=100,facecolor="white")
for ax,title in zip(axs,["(i) Annihilation","(ii) Exchange","(iv) Semileptonic decay"]):
    ax.set(xlim=(0,1),ylim=(0,1));ax.axis("off")
    ax.text(.5,.98,title,ha="center",va="top",fontsize=13)
ax=axs[0];a,b=(.34,.5),(.67,.5)
segment(ax,(.08,.78),a);segment(ax,a,(.08,.22))
segment(ax,b,(.91,.78));segment(ax,(.91,.22),b)
wave(ax,a,b);vertices(ax,a,b)
label(ax,.07,.86,"$u$");label(ax,.07,.12,r"$\bar d$")
label(ax,.92,.86,"$c$");label(ax,.92,.12,r"$\bar s$")
label(ax,.5,.62,"$W^+$")
ax=axs[1];a,b=(.5,.73),(.5,.28)
segment(ax,(.08,.73),a);segment(ax,a,(.92,.73))
segment(ax,b,(.08,.28));segment(ax,(.92,.28),b)
wave(ax,a,b);vertices(ax,a,b)
label(ax,.07,.84,"$u$");label(ax,.92,.84,"$d$")
label(ax,.07,.14,r"$\bar c$");label(ax,.92,.14,r"$\bar s$")
label(ax,.67,.5,"$W^+$")
ax=axs[2];a,b=(.34,.58),(.65,.35)
segment(ax,(.05,.58),a);segment(ax,a,(.91,.81))
wave(ax,a,b)
segment(ax,(.94,.45),b);segment(ax,b,(.94,.13))
vertices(ax,a,b)
label(ax,.06,.7,"$c$");label(ax,.94,.87,"$d$")
label(ax,.93,.53,r"$\mu^+$");label(ax,.93,.06,r"$\nu_\mu$")
label(ax,.45,.38,"$W^+$")
fig.text(.5,.015,"Solid arrows follow fermion number; wavy lines are W propagators.",
         ha="center",fontsize=11)
fig.subplots_adjust(left=.02,right=.98,bottom=.1,top=.97,wspace=.16)
fig.savefig(Path.cwd()/(Path(__file__).stem+".png"),dpi=100,facecolor="white",
            transparent=False)
plt.close(fig)
