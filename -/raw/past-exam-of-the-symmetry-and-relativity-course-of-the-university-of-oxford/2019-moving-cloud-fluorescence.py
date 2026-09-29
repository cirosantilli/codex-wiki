"""Illustrative fluorescence model; Python 3.14, NumPy and Matplotlib."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

Q=.8
TAU=.4
WIDTH=.02
TURN_ON=-1000.


def history(beta,step=.004):
    z=np.concatenate((np.linspace(-2500,-100,2000,endpoint=False),
                      np.arange(-100,100,step),np.linspace(100,2500,2001)))
    gamma=1/np.sqrt(1-beta**2)
    radius=np.sqrt(1+beta**2*z**2)
    direction=beta*z/radius
    incoming=gamma*(1-beta*direction)
    outgoing=1/(gamma*(1+beta*direction))
    profile=1/(1+4*((Q*incoming-1)/WIDTH)**2)
    pump=(1-beta*direction)*profile/radius**2*(z-radius>=TURN_ON)
    population=np.zeros_like(z)
    decaytime=gamma*TAU
    for i in range(1,len(z)):
        attenuation=np.exp(-(z[i]-z[i-1])/decaytime)
        population[i]=population[i-1]*attenuation+.5*(pump[i]+pump[i-1])*decaytime*(1-attenuation)
    intensity=outgoing**4*population/(TAU*radius**2)
    prompt=outgoing**4*gamma*pump/radius**2
    return {"time":z,"arrival":z+radius,"incoming":incoming,"outgoing":outgoing,
            "pump":pump,"population":population,"intensity":intensity,"prompt":prompt}


def main():
    bmin=(1-Q**2)/(1+Q**2);bperp=np.sqrt(1-Q**2)
    betas=[.05,bmin,bperp,.98]
    labels=["Slow: no line-centre resonance","First threshold: resonance at infinite approach",
            "Second threshold: resonance at closest approach","Ultra-relativistic: resonance after closest approach"]
    data=[history(b) for b in betas]
    norm=max(np.max(d["intensity"]) for d in data)
    fig,axes=plt.subplots(4,2,figsize=(10.8,11.2),dpi=100,facecolor="white",sharex=True)
    for row,(beta,label,d) in enumerate(zip(betas,labels,data)):
        x=d["arrival"];nu=d["outgoing"];I=d["intensity"]/norm
        left,right=axes[row]
        left.plot(x,nu,color="#777777",lw=1)
        visible=I>max(I)*.001
        left.plot(x,np.where(visible,nu,np.nan),color="#1263a0",lw=2)
        left.fill_between(x,nu*(1-WIDTH/2),nu*(1+WIDTH/2),color="#1263a0",alpha=.27)
        left.axhline(Q,color="#b44728",ls="--",lw=1,label=r"Source $f_0/f=0.8$")
        left.set_yscale("log");left.set_ylim(.08,12)
        left.set_yticks([.1,.3,1,3,10],labels=["0.1","0.3","1","3","10"])
        left.set_ylabel(r"Returned $f_R/f$")
        left.set_title(fr"$v/c={beta:.4g}$: "+label,fontsize=9,loc="left")
        right.semilogy(x,I,color="#1263a0",lw=2,label="Finite lifetime")
        right.semilogy(x,d["prompt"]/norm,color="#777777",ls="--",lw=1,label="Prompt comparison")
        right.set_ylim(1e-9,2);right.set_ylabel("Intensity / common maximum")
        if beta>bmin+1e-8:
            gamma=1/np.sqrt(1-beta**2);s=(1-1/(gamma*Q))/beta
            tstar=s/(beta*np.sqrt(1-s*s));arstar=tstar+np.sqrt(1+beta**2*tstar**2)
            for ax in (left,right):ax.axvline(arstar,color="#b44728",ls=":",lw=1)
        for ax in (left,right):
            ax.axvline(1,color="#888888",ls="-.",lw=.7)
            ax.set_xlim(-25,25);ax.grid(alpha=.18)
    axes[0,0].legend(loc="lower left",fontsize=8)
    axes[0,1].legend(loc="upper left",fontsize=8)
    for ax in axes[-1]:ax.set_xlabel(r"Return reception time $ct_R/L$")
    fig.suptitle("Returning fluorescence: lifetime, line width, beaming and light-travel time",fontsize=13,y=.995)
    fig.text(.5,.013,"Grey dash-dot: closest-approach emission arrives. Red dots: prompt line-centre resonance arrives.\n"
             "Line-width band is narrow; intensity shares one normalization across all speeds. Source turns on at ct/L = -1000.",
             ha="center",va="bottom",fontsize=9)
    fig.tight_layout(rect=(0,.065,1,.98),h_pad=1.7,w_pad=2)
    fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,
                facecolor="white",transparent=False,metadata={"Software":"Codex Wiki"})
    plt.close(fig)

if __name__=="__main__":main()
