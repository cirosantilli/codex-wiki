from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Arc
plt.rcParams.update({"font.size":12,"font.family":"DejaVu Sans","figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})

fig,(ax,bx)=plt.subplots(1,2,figsize=(9.5,4.8))
r=1.5;theta=np.arcsin(1/r);tt=np.linspace(0,theta,150);xx=r*np.sin(tt);zz=r*(1-np.cos(tt));ax.axvspan(0,1,color="#dbeaf3",alpha=.8);ax.axvline(1,color="#777777",ls="--",lw=1)
ax.plot(xx,zz,color="#236a9b",lw=2.4);end=np.array([xx[-1],zz[-1]]);out=end+.6*np.array([np.cos(theta),np.sin(theta)]);ax.plot([end[0],out[0]],[end[1],out[1]],color="#236a9b",lw=2);ax.annotate("",xy=out,xytext=(out+end)/2,arrowprops=dict(arrowstyle="->",color="#236a9b",lw=2))
ax.plot([end[0],end[0]+.3],[end[1],end[1]],color="#777777",ls=":",lw=1);ax.add_patch(Arc(end,.42,.42,theta1=0,theta2=np.degrees(theta),color="#a84a36",lw=1.5));ax.text(end[0]+.24,end[1]+.05,r"$\theta_b$",fontsize=12,color="#a84a36")
ax.scatter([0,1],[0,end[1]],color="#a84a36",s=28,zorder=4);ax.text(.48,.87,"Magnetic region",ha="center",fontsize=11);ax.text(.48,.7,r"$r=1.5b>b$",ha="center",fontsize=12)
ax.set(xlim=(-.12,1.65),ylim=(-.08,1.05),xlabel="x / b",ylabel="z / b",title="Transmission across a finite magnetic strip");ax.grid(alpha=.12)
phi=np.linspace(0,np.pi,200);X=-.5*(1-np.cos(phi));Y=.5*np.sin(phi);bx.axhspan(0,.82,color="#dbeaf3",alpha=.8);bx.axhspan(-1.15,0,color="#f8f0db",alpha=.8);bx.axhline(0,color="#777777",ls="--",lw=1);bx.plot(X,Y,color="#236a9b",lw=2.4)
bx.annotate("",xy=(0,0),xytext=(0,-1),arrowprops=dict(arrowstyle="->",color="#277b62",lw=2.2));idx=95;bx.annotate("",xy=(X[idx+15],Y[idx+15]),xytext=(X[idx-15],Y[idx-15]),arrowprops=dict(arrowstyle="->",color="#236a9b",lw=2))
bx.scatter([0,-1],[0,0],color="#a84a36",s=28,zorder=4);bx.annotate("",xy=(-1,-.18),xytext=(0,-.18),arrowprops=dict(arrowstyle="<->",color="#777777"));bx.text(-.5,-.34,"Return separation d",ha="center",fontsize=10)
bx.annotate("",xy=(.23,0),xytext=(.23,-1),arrowprops=dict(arrowstyle="<->",color="#777777"));bx.text(.32,-.5,"d",va="center",fontsize=12);bx.text(-.66,.67,"B into the page",ha="center",fontsize=10);bx.text(-.72,-.8,"Electric region\nE upwards",ha="center",fontsize=11)
bx.set(xlim=(-1.25,.5),ylim=(-1.12,.82),xlabel="Lateral position / d",ylabel="Normal position / d",title="Semicircle: orbit diameter equals d");fig.tight_layout()

fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=140,facecolor="white",transparent=False)
plt.close(fig)
