from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon, Rectangle
plt.rcParams.update({'font.size':13,'axes.titlesize':14,'figure.facecolor':'white','axes.facecolor':'white'})
fig,axs=plt.subplots(1,2,figsize=(12,5.5),layout='constrained');ax=axs[0]
ax.plot([-2.6,0,0],[-.13,-.13,-1.5],lw=3,color='.45');ax.plot([-1.45,0,0],[0,0,-.65],color='#0072B2',lw=4)
ax.add_patch(Rectangle((-1.67,-.025),.4,.26,facecolor='#f1cba0',edgecolor='.2'));ax.text(-1.47,.105,r'$m$',ha='center')
ax.add_patch(Rectangle((-.14,-.92),.28,.27,facecolor='#acd7e5',edgecolor='.2'));ax.text(0,-.79,r'$M$',ha='center')
xx=np.linspace(-2.4,-1.67,13);zz=.09+.06*np.where(np.arange(13)%2,1,-1);zz[[0,-1]]=.09;ax.plot(xx,zz,color='#009E73',lw=1.8);ax.plot([-2.4,-2.4],[-.05,.26],c='.2',lw=3)
ax.annotate('',xy=(.3,0),xytext=(.3,-.65),arrowprops={'arrowstyle':'<->'});ax.text(.38,-.35,r'$x$')
ax.annotate('',xy=(-1.0,-.42),xytext=(-1.5,-.42),arrowprops={'arrowstyle':'->'});ax.text(-1.8,-.65,'m moves towards edge',fontsize=11)
ax.text(-2.35,.4,'Optional spring k',color='#009E73');ax.text(.5,-.8,'floor not shown',fontsize=10)
ax.set(xlim=(-2.65,1.05),ylim=(-1.5,.7),aspect='equal');ax.axis('off');ax.set_title('Every part of the chain moves at the same speed')
ax=axs[1];tau=np.linspace(0,12,600)
for ratio,color in [(1.5,'#0072B2'),(3.,'#D55E00')]:ax.plot(tau,np.cos(np.sqrt(ratio-1)*tau),label=rf'$k/(\rho g)={ratio:g}$',color=color)
ax.axhline(0,c='.7',lw=.8);ax.set(xlabel=r'$t\sqrt{\rho g/(M+m+\rho L)}$',ylabel='displacement / initial displacement',ylim=(-1.16,1.16));ax.legend(loc='upper right');ax.grid(alpha=.2);ax.set_title(r'Stable motion: $\omega^2=(k-\rho g)/(M+m+\rho L)$')
fig.suptitle('Chain gravity increases with hanging length, reducing the spring restoring stiffness',fontsize=14)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=115,facecolor='white');plt.close(fig)
