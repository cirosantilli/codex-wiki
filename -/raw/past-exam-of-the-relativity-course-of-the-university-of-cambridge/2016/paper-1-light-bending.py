"""Original analytic teaching diagram; Python 3.14, numpy, matplotlib.
Run from the desired output directory; writes its basename PNG to cwd.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from matplotlib.patches import Circle
# Weak-field transverse ray equation, drawn with exaggerated deflection.
x=np.linspace(-6,6,1000);eta=.025;b=1.
y=b-2*eta*(x+np.sqrt(x*x+b*b))
xobs=6.;yobs=y[-1];slope=-2*eta*(1+xobs/np.sqrt(xobs*xobs+b*b))
fig,ax=plt.subplots(figsize=(10,4),layout="constrained")
ax.add_patch(Circle((0,0),.42,facecolor="#ebc459",edgecolor="#675421"))
ax.text(0,0,"M",ha="center",va="center",fontsize=12)
ax.plot(x,y,color="#326a97",lw=2,label="curved null-ray approximation")
ax.plot([-6,6],[1,1],ls=":",color="#777777",label="incoming asymptotic direction")
xx=np.linspace(-6,6,300);ax.plot(xx,yobs+slope*(xx-xobs),ls="--",color="#aa5c31",label="back-projected apparent direction")
ax.plot(xobs,yobs,"o",color="black");ax.text(4.6,yobs-.28,"observer",fontsize=10)
ax.annotate("",xy=(0,1),xytext=(0,0),arrowprops=dict(arrowstyle="<->",color="#555555"));ax.text(.1,.65,"b",fontsize=12)
ax.annotate("incoming light",xy=(-3.3,float(np.interp(-3.3,x,y))),xytext=(-5.5,.45),arrowprops=dict(arrowstyle="->"),fontsize=10)
ax.set(xlim=(-6.4,6.5),ylim=(-.65,1.9),aspect="equal",title="Weak gravitational bending; angular deflection exaggerated for visibility")
ax.legend(loc="lower center",bbox_to_anchor=(.5,-.35),ncol=3,frameon=False,fontsize=8.5);ax.axis("off")
fig.savefig("paper-1-light-bending.png",dpi=155,facecolor="white")
