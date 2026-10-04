"""Original diagram sketches. Python 3.14, NumPy and Matplotlib from root pyproject."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

BLUE="#184e79"
PURPLE="#71498c"
RED="#b13333"

def line(ax,p,q,arrow=True):
    ax.plot([p[0],q[0]],[p[1],q[1]],color=BLUE,lw=1.8)
    if arrow:
        p,q=np.asarray(p),np.asarray(q)
        a=p+.44*(q-p);b=p+.59*(q-p)
        ax.add_patch(FancyArrowPatch(a,b,arrowstyle="-|>",mutation_scale=11,
                                    color=BLUE,linewidth=1.3))

def wave(ax,p,q,cycles=6):
    p,q=np.array(p,float),np.array(q,float)
    d=q-p;n=np.array([-d[1],d[0]])/np.linalg.norm(d)
    t=np.linspace(0,1,260)
    pts=p[:,None]+d[:,None]*t+n[:,None]*(.052*np.sin(cycles*2*np.pi*t))
    ax.plot(pts[0],pts[1],color=PURPLE,lw=1.3)

def arch(ax,a,b,h=.86):
    t=np.linspace(0,1,300)
    dx=b-a
    x=a+dx*t;y=h*np.sin(np.pi*t)
    tangent=np.array([np.full_like(t,dx),h*np.pi*np.cos(np.pi*t)])
    norm=np.array([-tangent[1],tangent[0]])/np.sqrt(np.sum(tangent*tangent,axis=0))
    x,y=np.array([x,y])+norm*(.042*np.sin(14*np.pi*t))
    ax.plot(x,y,color=PURPLE,lw=1.25)
    ax.plot([a,b],[0,0],"o",color=BLUE,ms=3)

def electron(ax,y=0):
    line(ax,(0,y),(5,y))
    ax.text(-.08,y+.16,r"$p$",fontsize=10)
    ax.text(5.0,y+.16,r"$p'$",fontsize=10)

def photons(ax,a,b,crossed=False,bubble=False):
    labels=[r"$k'$ (out)",r"$k$ (in)"] if crossed else [r"$k$ (in)",r"$k'$ (out)"]
    lower=[(a-.35,-1.34),(b+.35,-1.34)]
    for i,(x,lo) in enumerate(zip([a,b],lower)):
        if bubble and i==0:
            cx=x-.35;cy=-.82;rx=.33;ry=.28
            wave(ax,(cx,-1.34),(cx,cy-ry),3)
            ts=np.linspace(0,2*np.pi,160)
            ax.plot(cx+rx*np.cos(ts),cy+ry*np.sin(ts),color=BLUE,lw=1.5)
            t0=2.4;t1=2.8
            p=(cx+rx*np.cos(t0),cy+ry*np.sin(t0))
            q=(cx+rx*np.cos(t1),cy+ry*np.sin(t1))
            ax.add_patch(FancyArrowPatch(p,q,arrowstyle="-|>",mutation_scale=10,color=BLUE))
            for yy in [cy-ry,cy+ry]:ax.plot([cx],[yy],"o",color=BLUE,ms=3)
            wave(ax,(cx,cy+ry),(x,0),3)
        else:wave(ax,lo,(x,0))
        ax.plot([x],[0],"o",color=BLUE,ms=3)
        ax.text(lo[0],-1.58,labels[i],ha="center",fontsize=10)

def cross(ax,x,y=0):
    ax.plot([x-.11,x+.11],[y-.11,y+.11],color=RED,lw=1.8)
    ax.plot([x-.11,x+.11],[y+.11,y-.11],color=RED,lw=1.8)

def panel(ax,title):
    ax.set_xlim(-.4,5.4);ax.set_ylim(-1.95,1.4);ax.axis("off")
    ax.set_title(title,fontsize=12,pad=8)

def main():
    fig,axs=plt.subplots(2,3,figsize=(13.2,8.4),dpi=100,facecolor="white")
    ax=axs[0,0];panel(ax,"External electron leg insertion")
    electron(ax);photons(ax,2.3,3.7);arch(ax,.45,1.45,.72)
    ax.text(2.5,1.04,"LSZ / residue; also outgoing leg",ha="center",fontsize=10)
    ax=axs[0,1];panel(ax,"External photon vacuum polarization")
    electron(ax);photons(ax,1.6,3.4,bubble=True)
    ax.text(2.5,.9,"LSZ / residue; also outgoing photon",ha="center",fontsize=10)
    ax=axs[0,2];panel(ax,"Internal mass / field counterterm")
    electron(ax);photons(ax,1.3,3.7);cross(ax,2.5)
    ax.text(2.5,.4,r"$\delta m,\ \delta Z_2$",ha="center",fontsize=12,color=RED)
    ax=axs[1,0];panel(ax,"One vertex counterterm")
    electron(ax);photons(ax,1.3,3.7);cross(ax,1.3)
    ax.text(1.3,.4,r"$\delta Z_1$",ha="center",fontsize=12,color=RED)
    ax.text(2.5,1.02,"Also at the other photon vertex",ha="center",fontsize=10)
    ax=axs[1,1];panel(ax,"Three-photon fermion loop: zero")
    electron(ax,.65);wave(ax,(2.5,.65),(2.5,-.3),4);ax.plot([2.5],[.65],"o",color=BLUE,ms=3)
    vertices=[(2.5,-.3),(1.4,-1.13),(3.6,-1.13)]
    for i in range(3):line(ax,vertices[i],vertices[(i+1)%3])
    for p in vertices:ax.plot([p[0]],[p[1]],"o",color=BLUE,ms=3)
    wave(ax,(.5,-1.65),vertices[1],4);wave(ax,vertices[2],(4.5,-1.65),4)
    ax.text(.5,-1.86,r"$k$ (in)",ha="center",fontsize=9)
    ax.text(4.5,-1.86,r"$k'$ (out)",ha="center",fontsize=9)
    ax.text(2.5,1.04,"Opposite orientations cancel",ha="center",fontsize=10,color=RED)
    ax=axs[1,2];panel(ax,"One-photon tadpole: zero")
    electron(ax);photons(ax,1.3,3.7)
    wave(ax,(2.5,0),(2.5,.55),3);ax.plot([2.5],[0],"o",color=BLUE,ms=3)
    ts=np.linspace(0,2*np.pi,150);cx,cy,r=2.5,.88,.33
    ax.plot(cx+r*np.cos(ts),cy+r*np.sin(ts),color=BLUE,lw=1.5)
    ax.plot([2.5],[.55],"o",color=BLUE,ms=3)
    a=(cx+r*np.cos(.2),cy+r*np.sin(.2));b=(cx+r*np.cos(.65),cy+r*np.sin(.65))
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle="-|>",mutation_scale=10,color=BLUE))
    fig.suptitle("Fourth-order bookkeeping: residues, single counterterms and Furry cancellations",fontsize=15)
    fig.text(.5,.02,"Exchange the external photons for crossed partners. Red crosses denote one counterterm insertion.",ha="center",fontsize=11)
    fig.subplots_adjust(left=.03,right=.98,top=.91,bottom=.08,wspace=.18,hspace=.44)
    fig.savefig(Path.cwd()/"paper-44-compton-bookkeeping.png",facecolor="white",transparent=False)
    plt.close(fig)

if __name__=="__main__":
    main()
