"""Compare recoverable and flow-containing spring-dashpot models.

Run from the media directory; writes rheology-creep-recovery.png to cwd.
Parameters and units are illustrative, not material measurements.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

SIGMA=1.0
E0=4.0
E1=2.0
ETA1=3.0
ETA0=8.0
HOLD=4.0
TAU=ETA1/E1

def loaded(t, flow=False):
    t=np.asarray(t)
    return SIGMA/E0+SIGMA/E1*(-np.expm1(-t/TAU))+(SIGMA*t/ETA0 if flow else 0)

def recovered(t, flow=False):
    t=np.asarray(t)
    return SIGMA/E1*(-np.expm1(-HOLD/TAU))*np.exp(-(t-HOLD)/TAU)+(SIGMA*HOLD/ETA0 if flow else 0)

def main():
    plt.rcParams.update({"font.size":11,"figure.facecolor":"white","axes.facecolor":"white"})
    fig,(top,bottom)=plt.subplots(2,1,figsize=(9.8,6.2),height_ratios=(1,3),sharex=True)
    top.step([-.5,0,HOLD,12],[0,SIGMA,0,0],where="post",color="#333333",linewidth=2)
    top.set_ylabel("Applied stress")
    top.set_ylim(-.1,1.2)
    top.set_yticks([0,1])
    top.text(2,.57,"Hold load",ha="center")
    top.text(8,.57,"Remove load; allow recovery",ha="center")
    loading=np.linspace(0,HOLD,300)
    recovery=np.linspace(HOLD,12,500)
    for flow,color,label in [(False,"#17618a","Standard linear solid"),(True,"#b74d20","Burgers material")]:
        bottom.plot([-.5,0],[0,0],color=color)
        bottom.vlines(0,0,SIGMA/E0,color=color,linewidth=2)
        bottom.plot(loading,loaded(loading,flow),color=color,label=label,linewidth=2)
        bottom.vlines(HOLD,float(recovered(HOLD,flow)),float(loaded(HOLD,flow)),color=color,linewidth=2)
        bottom.plot(recovery,recovered(recovery,flow),color=color,linewidth=2)
    residual=SIGMA*HOLD/ETA0
    bottom.hlines(residual,HOLD,12,color="#b74d20",linestyle="--",linewidth=1)
    bottom.annotate("Residual viscous strain",xy=(10.4,residual),xytext=(7.2,.76),
                    arrowprops={"arrowstyle":"->","color":"#b74d20"},color="#8d3512")
    bottom.annotate("Immediate elastic recovery",xy=(HOLD,.60),xytext=(4.5,1.18),
                    arrowprops={"arrowstyle":"->","color":"#333333"})
    bottom.set_ylabel("Strain")
    bottom.set_xlabel("Time (arbitrary consistent units)")
    bottom.set_xlim(-.5,12)
    bottom.set_ylim(-.05,1.4)
    bottom.legend(loc="upper left")
    for ax in [top,bottom]:
        ax.axvline(HOLD,color="#777777",linestyle=":",linewidth=1)
        ax.grid(alpha=.15)
        ax.spines[["top","right"]].set_visible(False)
    fig.suptitle("A finite-duration load distinguishes recovery from viscous flow",fontsize=15)
    fig.text(.5,.015,r"Illustrative: $\sigma_0=1$, $E_0=4$, $E_1=2$, $\eta_1=3$, $\eta_0=8$; load removed at $t_h=4$.",ha="center",fontsize=10)
    fig.tight_layout(rect=(0,.055,1,.95))
    fig.savefig(Path("rheology-creep-recovery.png"),dpi=120,facecolor="white")
    plt.close(fig)

if __name__=="__main__":
    main()
