"""Original explanatory figure; run from the mirrored _media directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 10, "figure.facecolor": "white", "axes.facecolor": "white"})

fig,axs=plt.subplots(2,2,figsize=(10,7),layout='constrained');a=axs[0,0]
x=np.linspace(0,1,200);y=.2*x+.25*x*x;a.plot(x,y,lw=3,color='tab:blue')
for xx,direction,label in [(0,-1,r'$-T\hat{t}_L$'),(1,1,r'$T\hat{t}_R$')]:
 yy=.2*xx+.25*xx*xx;slope=.2+.5*xx;dx=direction*.42;dy=slope*dx
 a.annotate('',(xx+dx,yy+dy),(xx,yy),arrowprops=dict(arrowstyle='->',lw=2,color='tab:red'))
 a.text(xx+dx,yy+dy+.05,label,ha='center');a.plot([xx-.1,xx+.45],[yy,yy],':',color='0.6')
 theta=np.arctan(slope);ang=np.linspace(0,theta,40);a.plot(xx+.24*np.cos(ang),yy+.24*np.sin(ang),color='0.3');a.text(xx+.28,yy+.05,r'$\theta_L$' if xx==0 else r'$\theta_R$')
a.text(.5,.04,r'Mass $\rho\,\Delta x$',ha='center');a.annotate('',(1,-.25),(0,-.25),arrowprops=dict(arrowstyle='<->'));a.text(.5,-.3,r'$\Delta x$',ha='center',va='top');a.text(0,-.14,r'$x$',ha='center');a.text(1,-.14,r'$x+\Delta x$',ha='center');a.set(xlim=(-.6,1.7),ylim=(-.55,1.05),title='Forces on a small string segment');a.axis('off')
x=np.linspace(0,2,500);a=axs[0,1];a.plot(x,np.cos(2*np.pi*x),label=r'$t=0$');a.plot(x,np.sin(2*np.pi*x),label=r'$t=P/4$');a.set(xlabel=r'$x/\lambda$',ylabel=r'$y/y_0$',title='A right-moving sinusoid');a.legend(fontsize=8)
x=np.linspace(-5,5,700)
for t in [0,1,2]:
 axs[1,0].plot(x,np.exp(-(x-t)**2/2),label=rf'$ct\sqrt{{a}}={t}$')
 axs[1,1].plot(x,.5*(np.exp(-(x-t)**2/2)+np.exp(-(x+t)**2/2)),label=rf'$ct\sqrt{{a}}={t}$')
for a in axs[1]:a.set(xlabel=r'$x\sqrt{a}$',ylabel=r'$y/A$');a.legend(fontsize=8);a.grid(alpha=.2)
axs[1,0].set_title('Initial velocity selects rightward travel');axs[1,1].set_title('Zero initial velocity produces two pulses')

fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name, dpi=150, facecolor="white", bbox_inches="tight")
plt.close(fig)
