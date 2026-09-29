"""Mass-action boundaries and the stable lower envelope for Question 8."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

x=np.linspace(-8,0,1201)
g=(52.65-3*x)/5
k=(61.14-x)/5
xt=-8.49/2
yt=(52.65-3*xt)/5
fig,ax=plt.subplots(figsize=(7.6,5.2),layout="constrained")
ax.fill_between(x,np.maximum(g,k),17,color="#e7d9bc",alpha=.7)
ax.fill_between(x,8,np.maximum(g,k),where=x<xt,color="#b8d7ed",alpha=.65)
ax.fill_between(x,8,np.maximum(g,k),where=x>=xt,color="#d0e5bc",alpha=.7)
for yy,col,mask in [(g,"#24719c",x<=xt),(k,"#4b842e",x>=xt)]:
 ax.plot(x,yy,color=col,ls="--",lw=1)
 ax.plot(x[mask],yy[mask],color=col,lw=2.5)
ax.plot([xt,xt],[8,yt],color="#72458d",lw=2.5)
ax.plot([xt,xt],[yt,17],color="#72458d",ls="--",lw=1)
ax.scatter([xt],[yt],color="k",s=25,zorder=5)
ax.text(-7.7,9.4,"Gibbsite")
ax.text(-2.6,9.4,"Kaolinite")
ax.text(-4.0,16.3,"Chlorite")
ax.text(-7.8,11.4,r"$y=12.228-0.2x$",rotation=-9,color="#4b842e")
ax.text(-2.8,11.5,r"$y=10.53-0.6x$",rotation=-24,color="#24719c")
ax.annotate("(−4.245, 13.077)", (xt,yt),(-7.1,13.9),arrowprops={"arrowstyle":"->"},fontsize=9)
ax.text(-7.7,8.25,"solid: stable coexistence; dashed: metastable continuation",fontsize=9)
ax.set(xlim=(-8,0),ylim=(8,17),xlabel=r"$x=\log_{10}a_{\mathrm{H_4SiO_4}}$",ylabel=r"$y=\log_{10}(a_{\mathrm{Mg}^{2+}}/a_{\mathrm{H}^+}^2)$",title="8: chlorite weathering and three-mineral stability")
fig.savefig(Path(__file__).with_suffix(".png").name,dpi=100,facecolor="white",transparent=False)
