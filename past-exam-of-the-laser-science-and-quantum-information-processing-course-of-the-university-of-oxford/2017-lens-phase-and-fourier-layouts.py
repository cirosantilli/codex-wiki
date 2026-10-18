"""Original optical-path and Fourier-layout diagrams; Python 3.14/numpy/matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':12})
fig,axs=plt.subplots(3,1,figsize=(10.5,9),layout='constrained',facecolor='white')
ax=axs[0];x=np.linspace(-.82,.82,501);R=1.5;t0=.65;thick=t0-(R-np.sqrt(R*R-x*x))
ax.fill_betweenx(x,0,thick,color='#dcebf0');ax.plot(np.zeros_like(x),x,color='#126782',lw=2);ax.plot(thick,x,color='#126782',lw=2)
ax.plot([-.3,1.25],[0,0],color='gray',ls=':',lw=1)
for y,lab in [(0,r'$t_0$'),(.65,r'$t(x)$')]:
 tt=t0-(R-np.sqrt(R*R-y*y));ax.annotate('',xy=(0,y),xytext=(tt,y),arrowprops={'arrowstyle':'<->','color':'#a34a32'});ax.text(tt/2,y+.09,lab,ha='center',fontsize=11)
ax.annotate('',xy=(-.15,0),xytext=(-.15,.65),arrowprops={'arrowstyle':'<->'});ax.text(-.22,.33,'x',ha='center')
ax.text(.95,.45,r'$t(x)\simeq t_0-x^2/(2R)$'+'\n'+r'$\phi(x)-\phi(0)=-kx^2/(2f)$'+'\n'+r'$f=R/(n-1)$',va='center')
ax.text(-.30,-1.15,'Propagation direction',fontsize=10);ax.annotate('',xy=(.8,-.99),xytext=(-.3,-.99),arrowprops={'arrowstyle':'->'})
ax.set(xlim=(-.45,2.6),ylim=(-1.2,1.1));ax.set_aspect('equal');ax.axis('off');ax.set_title('Lens thickness produces a quadratic relative phase')
def lens(ax,z):
 ax.plot([z,z],[-.85,.85],color='#126782',lw=2.5)
 ax.annotate('',xy=(z,.9),xytext=(z,.56),arrowprops={'arrowstyle':'->','color':'#126782','lw':2})
 ax.annotate('',xy=(z,-.9),xytext=(z,-.56),arrowprops={'arrowstyle':'->','color':'#126782','lw':2})
def dimension(ax,a,b,y,lab):
 ax.annotate('',xy=(a,y),xytext=(b,y),arrowprops={'arrowstyle':'<->'});ax.text((a+b)/2,y-.12,lab,ha='center',va='top')
ax=axs[1];lens(ax,2);lens(ax,7);ax.plot([0,9],[0,0],color='gray',ls=':',lw=1);dimension(ax,2,7,-1.05,'L = f')
ax.text(2,1.05,'Input plane + lens',ha='center');ax.text(7,1.05,'Lens + output plane',ha='center')
ax.text(4.5,.45,r'$e^{-ikx^2/(2f)}\;P(f)\;e^{-ikx^{\prime2}/(2f)}$',ha='center');ax.text(4.5,-.45,r'$E_{\rm out}(x)\propto\widetilde E_{\rm in}(kx/f)$',ha='center')
ax.set(xlim=(0,9),ylim=(-1.6,1.5));ax.axis('off');ax.set_title('Two lenses: the input and output curvatures cancel')
ax=axs[2];lens(ax,5)
for z,lab in [(1,'Input: front focal plane'),(9,'Output: back focal plane')]:ax.plot([z,z],[-1,1],color='gray',ls='--',lw=1);ax.text(z,1.2,lab,ha='center',fontsize=11)
ax.plot([.3,9.7],[0,0],color='gray',ls=':',lw=1)
for y,col in [(-.5,'#a34a32'),(.5,'#75458d')]:
 yl=y+.4;ax.plot([1,5,9],[y,yl,.4],color=col,lw=1.8)
dimension(ax,1,5,-1.1,'f');dimension(ax,5,9,-1.1,'f')
ax.set(xlim=(0,10),ylim=(-1.6,1.7));ax.axis('off');ax.set_title('One lens: equal spatial frequencies meet at one back-focal-plane point')
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white',transparent=False,metadata={'Software':'Matplotlib'})
plt.close(fig)
