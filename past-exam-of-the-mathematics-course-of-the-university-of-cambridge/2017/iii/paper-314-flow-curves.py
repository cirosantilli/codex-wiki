"""Original exam sketch. Python 3.14; matplotlib==3.10.7; numpy==2.3.5.
Matches root dependency pins. Generates an opaque same-basename PNG in CWD.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def F(t):
    return t**4+4/t

def branches(x,lam):
    value=F(x)/lam
    valid=value>=5-2e-13
    safe=np.maximum(value,5)
    ll,lh=np.full_like(x,1e-14),np.ones_like(x)
    ul,uh=np.ones_like(x),np.maximum(2.,safe**.25+1)
    for _ in range(70):
        mid=(ll+lh)/2
        below=F(mid)>safe
        ll=np.where(below,mid,ll);lh=np.where(below,lh,mid)
        mid=(ul+uh)/2
        below=F(mid)<safe
        ul=np.where(below,mid,ul);uh=np.where(below,uh,mid)
    return np.where(valid,(ll+lh)/2,np.nan),np.where(valid,(ul+uh)/2,np.nan)

def shock_parameters(xs=1.4):
    m=xs**5;ys=((m+4)/(6*m-1))**.2
    return xs,ys,F(xs)/F(ys)

def main():
    xs,ys,lam=shock_parameters()
    x=np.sort(np.unique(np.r_[np.linspace(.12,2.55,1800),1.,xs]))
    fig,ax=plt.subplots(figsize=(8,4.8),dpi=100,facecolor="white")
    for value,color,style,label in [
        (.7,"#8a8a8a","--",r"$\lambda=0.7$"),
        (1.,"#2468ae","-",r"$\lambda=1$"),
        (lam,"#d47c12","--",rf"$\lambda={lam:.3f}$ (after shock)")]:
        low,high=branches(x,value)
        ax.plot(x,low,color=color,ls=style,lw=1.65,label=label)
        ax.plot(x,high,color=color,ls=style,lw=1.65)
    low,_=branches(x,lam);valid=np.isfinite(low)
    ax.axvspan(x[(x<1)&valid].max(),x[(x>1)&valid].min(),color="#d47c12",alpha=.09)
    ax.axhline(1,color="#333333",lw=.65,ls=":")
    ax.axvline(1,color="#333333",lw=.65,ls=":")
    ax.plot([1],[1],"o",color="#2468ae",ms=5)
    ax.plot([xs,xs],[xs,ys],"o",color="#17242f",ms=5)
    ax.annotate("",xy=(xs,ys),xytext=(xs,xs),arrowprops=dict(arrowstyle="-|>",color="#17242f",lw=2))
    ax.annotate("stationary shock",xy=(xs,(xs+ys)/2),xytext=(1.7,1.42),fontsize=10,
                arrowprops=dict(arrowstyle="-",color="#17242f",lw=.8))
    mask=(x>=.2)&(x<=xs)
    ax.plot(x[mask],x[mask],color="#17242f",lw=2.8)
    ax.plot(x[x>=xs],low[x>=xs],color="#17242f",lw=2.8)
    ax.annotate("",xy=(.72,.72),xytext=(.60,.60),arrowprops=dict(arrowstyle="-|>",color="#17242f",lw=2))
    xp=np.array([1.85,2.04]);yp=branches(xp,lam)[0]
    ax.annotate("",xy=(xp[1],yp[1]),xytext=(xp[0],yp[0]),arrowprops=dict(arrowstyle="-|>",color="#17242f",lw=2))
    ax.text(.20,1.05,"supersonic",fontsize=9,color="#555555")
    ax.text(.20,.90,"subsonic",fontsize=9,color="#555555")
    ax.text(.80,2.18,rf"No solutions for $\lambda={lam:.3f}$"+"\nin the shaded interval",
            fontsize=9,color="#875209",ha="center")
    ax.set(xlim=(.12,2.55),ylim=(0,2.65),xlabel=r"$x=(r/r_s)^{1/5}$",ylabel=r"$y=\mathcal{M}^{2/5}$")
    ax.legend(loc="upper right",fontsize=9,framealpha=1)
    ax.grid(alpha=.15);fig.tight_layout()
    output=Path.cwd()/(Path(__file__).stem+".png")
    fig.savefig(output,dpi=100,facecolor="white",transparent=False);plt.close(fig)
    print(f"shock x={xs}, y={ys:.12g}, lambda={lam:.12g}; PNG {output}")

if __name__=="__main__":
    main()
