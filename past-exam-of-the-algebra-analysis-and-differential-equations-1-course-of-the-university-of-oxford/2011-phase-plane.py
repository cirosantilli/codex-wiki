"""Oxford AC1 2011: phase portrait, written to the process CWD.

Output: 2011-phase-plane.png, white background.
Tested: Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Dependencies are recorded in the repository root pyproject.toml.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def field(v):
    x, y = v
    return np.array([x*(y-x+1), y*(2*y-x-2)])


def trajectory(start, direction):
    v = np.asarray(start, dtype=float)
    points = [v.copy()]
    def rhs(z):
        f = field(z)
        return direction*f/(1+np.linalg.norm(f))
    for _ in range(7000):
        h = .025
        k1 = rhs(v)
        k2 = rhs(v+h*k1/2)
        k3 = rhs(v+h*k2/2)
        k4 = rhs(v+h*k3)
        v = v+h*(k1+2*k2+2*k3+k4)/6
        points.append(v.copy())
        if not (-1.6 < v[0] < 6.6 and -1.6 < v[1] < 6.1):
            break
        if len(points)>100 and np.linalg.norm(field(v))<1e-7:
            break
    return np.asarray(points)


def main():
    fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.8), facecolor="white", gridspec_kw={"width_ratios":[1.35, 1]})
    stable, unstable = "#1767a0", "#b64e17"
    for ax, limits in zip(axes, [(-1.2, 6.2, -1.2, 5.7), (-.25, 1.75, -.25, 1.75)]):
        a, b, c, d = limits
        x, y = np.linspace(a,b,260), np.linspace(c,d,260)
        X,Y = np.meshgrid(x,y)
        U,V = X*(Y-X+1), Y*(2*Y-X-2)
        speed = np.hypot(U,V)
        U,V = U/(1+speed),V/(1+speed)
        ax.streamplot(x,y,U,V,density=1.25,color="#a1aab1",linewidth=.65,arrowsize=.8)
        ax.plot(x,x-1,"--",color="#768238",lw=1.25,label=r"$\dot x=0$: $y=x-1$")
        ax.plot(x,x/2+1,":",color="#98629f",lw=1.5,label=r"$\dot y=0$: $y=x/2+1$")
        ax.axhline(0,color="#596168",lw=.8)
        ax.axvline(0,color="#596168",lw=.8)
        ax.set(xlim=(a,b),ylim=(c,d),xlabel="$x$",ylabel="$y$")
        ax.set_aspect("equal",adjustable="box")
        ax.spines[["top","right"]].set_visible(False)
        ax.set_facecolor("white")
        for point, marker, color in [((0,0),"x","black"),((1,0),"o",stable),((0,1),"s",unstable),((4,3),"x","black")]:
            ax.plot(*point,marker,color=color,ms=6,zorder=6)
    saddle=np.array([4.,3.])
    for direction, vector, color, name in [(-1,np.array([4.,5-np.sqrt(13)]),stable,"Stable separatrix"),(1,np.array([4.,5+np.sqrt(13)]),unstable,"Unstable separatrix")]:
        vector /= np.linalg.norm(vector)
        for sign in [-1,1]:
            line=trajectory(saddle+sign*.002*vector,direction)
            axes[0].plot(line[:,0],line[:,1],color=color,lw=1.8,label=name if sign==-1 else None)
            n=min(110,len(line)-10)
            start,end=(line[n+8],line[n]) if direction<0 else (line[n],line[n+8])
            axes[0].annotate("",xy=end,xytext=start,arrowprops={"arrowstyle":"->","color":color,"lw":1.5})
    for point,text,offset in [((0,0),"Saddle",(-35,-19)),((1,0),"Stable node",(7,-18)),((0,1),"Improper source",(8,8)),((4,3),"Saddle",(9,-15))]:
        axes[0].annotate(text,point,xytext=offset,textcoords="offset points",fontsize=9)
    axes[0].set_title("Full portrait and saddle separatrices")
    axes[1].set_title("Near the three axial equilibria")
    axes[0].legend(loc="upper left",fontsize=8,framealpha=.95)
    fig.suptitle(r"$\dot x=x(y-x+1),\qquad\dot y=y(2y-x-2)$",fontsize=15)
    fig.tight_layout(rect=(0,0,1,.92))
    fig.savefig("2011-phase-plane.png",dpi=150,facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
