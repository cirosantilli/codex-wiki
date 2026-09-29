"""Original scientific figure; Python 3.14 with numpy/matplotlib. Writes one PNG in the current directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":11,"font.family":"DejaVu Sans","savefig.facecolor":"white"})
def save(fig):
    fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=120,facecolor="white",transparent=False,metadata={"Software":"Matplotlib"})
    plt.close(fig)

a=(1+np.sqrt(3))/2;b=(1-np.sqrt(3))/2;logI0=-b*np.log(a-1)+a*np.log(1-b)
fig,axs=plt.subplots(1,2,figsize=(11.5,5.1),layout="constrained")
for ax,lims in zip(axs,[(-3,4,-2.6,2.6),(-.65,1.65,-1.25,1.25)]):
    xmin,xmax,ymin,ymax=lims;x=np.linspace(xmin,xmax,400);y=np.linspace(ymin,ymax,400);X,Y=np.meshgrid(x,y);U=Y**3-Y;V=X-Y*Y;speed=np.sqrt(U*U+V*V);scale=np.where(speed>1e-12,speed,1)
    ax.streamplot(x,y,U/scale,V/scale,color="#aeb4b9",density=1.1,linewidth=.65,arrowsize=.75,zorder=1)
    ys=np.linspace(ymin,ymax,800)
    ax.plot(1+a*(ys*ys-1),ys,color="#bf5a13",lw=1.9,label="F plus = 0")
    ax.plot(1+b*(ys*ys-1),ys,color="#488523",lw=1.9,label="F minus = 0")
    ax.plot(ys*ys,ys,color="#777777",ls=":",lw=1,label="x = y squared")
    for yn in (-1,0,1):ax.axhline(yn,color="#777777",ls=":",lw=.7)
    Fp=X-1-a*(Y*Y-1);Fm=X-1-b*(Y*Y-1);mask=(Fp<=0)|(Fm>=0)|(abs(Y)>=1)
    logI=-b*np.log(np.maximum(Fp,1e-30))+a*np.log(np.maximum(-Fm,1e-30));logI=np.ma.array(logI,mask=mask)
    ax.contour(X,Y,logI,levels=logI0-np.array([3,1.5,.8,.3,.08]),colors="#165b91",linewidths=1.1,zorder=3)
    ax.plot(0,0,"o",color="black",ms=4,zorder=5);ax.plot([1,1],[-1,1],"x",color="black",ms=7,mew=1.5,zorder=5)
    ax.set(xlim=(xmin,xmax),ylim=(ymin,ymax),xlabel="x",ylabel="y");ax.grid(alpha=.12)
axs[0].set_title("Global separatrices and exterior flow");axs[0].legend(fontsize=8,loc="upper left")
axs[1].set_title("Closed orbits inside the heteroclinic lens")
fig.supxlabel("Dot: nonlinear center. Crosses: saddles. Colored parabolas are exact invariant manifolds.",fontsize=10)
save(fig)
