"""Original anomer comparison with a shared open-chain connection.

Python 3.14, matplotlib 3.10.7. Output is basename.png in CWD.
Haworth diagrams are symbolic configurations, not flat molecular geometries.
"""
from pathlib import Path

import matplotlib.pyplot as plt


INK = "#223344"
OXYGEN = "#166280"
ANOMERIC = "#aa3b20"


def label(ax, x, y, s, size=13, color=INK, **kwargs):
    ax.text(x, y, s, fontsize=size, color=color, ha="center", va="center", **kwargs)


def line(ax, a, b, color=INK, lw=1.8):
    ax.plot([a[0], b[0]], [a[1], b[1]], color=color, lw=lw, solid_capstyle="round")


def ring(ax, cx, cy, beta):
    points = {1:(cx+1.75,cy), 2:(cx+.88,cy-.62), 3:(cx-.88,cy-.62),
              4:(cx-1.75,cy), 5:(cx-.88,cy+.62), "O":(cx+.88,cy+.62)}
    order = [1, 2, 3, 4, 5, "O", 1]
    for a,b in zip(order, order[1:]):
        line(ax, points[a], points[b], lw=3.5 if a in [1,2,3] else 1.6)
    for n,(x,y) in points.items():
        label(ax, x, y, "O" if n == "O" else f"C{n}", 12,
              OXYGEN if n == "O" else ANOMERIC if n == 1 else INK,
              bbox={"facecolor":"white", "edgecolor":"none", "pad":1.2}, zorder=4)
    # Up/down refers to the reference ring plane, not axial/equatorial.
    for n, up in [(1,beta), (2,False), (3,True), (4,False), (5,True)]:
        x,y=points[n]
        sign=1 if up else -1
        col=ANOMERIC if n == 1 else OXYGEN if n == 5 else INK
        length, offset = (.55,.78) if n == 3 else (.89,1.12)
        line(ax,(x,y+sign*.12),(x,y+sign*length),col)
        label(ax,x,y+sign*offset,r"C6: CH$_2$OH" if n == 5 else "OH",12,col,
              bbox={"facecolor":"white", "edgecolor":"none", "pad":.7})
    label(ax,cx,cy+2.28,"β-D-glucopyranose" if beta else "α-D-glucopyranose",18,weight="bold")
    label(ax,cx,cy-2.10,"C1 OH up: same face as C6" if beta else "C1 OH down: opposite face to C6",12,ANOMERIC)


def open_chain(ax, x, y):
    # Compact Fischer formula with explicit aldehyde and all retained stereocenters.
    for i in range(5):
        line(ax,(x,y-i*.57-.10),(x,y-(i+1)*.57+.10))
    for i in range(6):
        yy=y-i*.57
        label(ax,x-1.16,yy,f"C{i+1}",10,ANOMERIC if i == 0 else INK)
        if i == 0:
            label(ax,x,yy,"CHO",12,ANOMERIC,bbox={"facecolor":"white","edgecolor":"none","pad":1})
        elif i == 5:
            label(ax,x,yy,r"CH$_2$OH",12,bbox={"facecolor":"white","edgecolor":"none","pad":1})
        else:
            right=i != 2
            line(ax,(x-.54,yy),(x+.54,yy))
            label(ax,x-.77,yy,"H" if right else "HO",11)
            label(ax,x+.77,yy,"OH" if right else "H",11,OXYGEN if i == 4 else INK)


def main():
    plt.rcParams.update({"font.family":"DejaVu Sans"})
    fig,ax=plt.subplots(figsize=(11,8),dpi=140,facecolor="white")
    fig.subplots_adjust(left=.02,right=.98,bottom=.03,top=.98)
    ax.set(xlim=(0,16),ylim=(0,12))
    ax.axis("off")
    label(ax,8,11.57,"Anomers share the same six carbon atoms",21,weight="bold")
    ring(ax,4,8.2,False)
    ring(ax,12,8.2,True)
    open_chain(ax,8,4.83)
    for a,b in [((5.9,6.45),(7.05,4.78)),((10.1,6.45),(8.95,4.78))]:
        ax.annotate("",xy=b,xytext=a,arrowprops={"arrowstyle":"<->","lw":1.7,"color":OXYGEN,
                                                            "shrinkA":0,"shrinkB":0})
    label(ax,4.3,4.6,"Open C1–O5 bond;\nrestore C1 aldehyde",12,OXYGEN)
    label(ax,11.9,4.6,"C5 OH can close\nonto either C1 face",12,OXYGEN)
    label(ax,4.2,2.95,"Same C2/C3/C4 OH:\ndown / up / down",12)
    label(ax,12,2.95,"O5 becomes ring oxygen;\nC6 stays outside the ring",12,OXYGEN)
    label(ax,8,1.30,"Open-chain D-glucose (minor form in water)",12)
    label(ax,8,.76,"Haworth rings encode above/below; real rings are puckered. Ring C–H bonds omitted.",11)
    label(ax,8,.30,"Fischer crosses: horizontal toward you, vertical away. Arrows show connectivity, not rates.",11)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"),facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
