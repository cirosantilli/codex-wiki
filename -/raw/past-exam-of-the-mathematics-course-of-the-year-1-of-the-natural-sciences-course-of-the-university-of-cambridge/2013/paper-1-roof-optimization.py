"""Original exam-solution illustration; write the PNG basename to the cwd.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    A,h=3.0,1.0;left,right=0,A/h
    for _ in range(70):
        mid=(left+right)/2
        if mid**4+16*A*h*mid-16*A*A>0:right=mid
        else:left=mid
    w=(left+right)/2;rise=2*(A-w*h)/w;theta=np.arctan(2*rise/w)
    fig,(ax,curve)=plt.subplots(1,2,figsize=(10.2,4.5),layout="constrained",facecolor="white",gridspec_kw={"width_ratios":[1.1,1]})
    ax.fill([0,w,w,0],[0,0,h,h],color="#dceaf2")
    ax.fill([0,w/2,w],[h,h+rise,h],color="#d7e9da")
    ax.plot([0,0,w/2,w,w,0],[0,h,h+rise,h,0,0],color=".3",lw=1.8)
    ax.plot([0,w],[h,h],color=".5",ls="--",lw=1)
    ax.annotate("",(0,-.14),(w,-.14),arrowprops={"arrowstyle":"<->","color":".35"});ax.text(w/2,-.32,"$w$",ha="center")
    ax.annotate("",(-.18,0),(-.18,h),arrowprops={"arrowstyle":"<->","color":".35"});ax.text(-.35,h/2,"$h$",va="center")
    ax.annotate("",(w+.18,h),(w+.18,h+rise),arrowprops={"arrowstyle":"<->","color":".35"});ax.text(w+.25,h+rise/2,r"$\frac{w}{2}\tan\theta$",va="center",fontsize=11)
    ph=np.linspace(0,theta,50);ax.plot(.4*np.cos(ph),h+.4*np.sin(ph),color="#b84732",lw=1.2);ax.text(.47,h+.06,r"$\theta$",color="#b84732")
    ax.text(w/2,.45,"Area $wh$",ha="center",fontsize=10)
    ax.text(w/2,h+rise/3,r"$w^2\tan\theta/4$",ha="center",fontsize=9)
    ax.set(xlim=(-.5,w+1.05),ylim=(-.4,h+rise+.4),title="Cross-section geometry")
    ax.set_aspect("equal");ax.axis("off")
    ww=np.linspace(.75,2.99,600);Q=ww**2+16*(A-h*ww)**2/ww**2;minimum=w*w+16*(A-h*w)**2/w**2
    curve.plot(ww,Q,color="#17648e",lw=2.2)
    curve.scatter([w],[minimum],s=35,color="#b84732",zorder=6)
    curve.annotate("Unique minimum",(w,minimum),xytext=(1.45,24),arrowprops={"arrowstyle":"->","color":"#b84732"},fontsize=10)
    curve.set(xlim=(.75,3),ylim=(0,65),xlabel="$w$",ylabel=r"$Q(w)=(\mathrm{roof\ length})^2$",title="Illustrative $A=3$, $h=1$")
    curve.grid(alpha=.14)
    fig.savefig(Path("paper-1-roof-optimization.png"),dpi=160,facecolor="white");plt.close(fig)


if __name__ == "__main__":
    main()
