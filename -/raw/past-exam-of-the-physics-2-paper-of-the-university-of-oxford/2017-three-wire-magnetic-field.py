"""Original field-line plot from the summed Biot-Savart fields of three wires."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':12,'figure.facecolor':'white','axes.facecolor':'white'})
x=np.linspace(-2.8,2.8,401);y=np.linspace(-2.1,2.1,301);X,Y=np.meshgrid(x,y)
bx=np.zeros_like(X);by=np.zeros_like(X);mask=np.zeros_like(X,dtype=bool)
for a in [-1.,0.,1.]:
    r2=(X-a)**2+Y**2;mask|=r2<.105**2
    bx-=Y/np.maximum(r2,1e-8);by+=(X-a)/np.maximum(r2,1e-8)
bx=np.ma.array(bx,mask=mask);by=np.ma.array(by,mask=mask)
fig,ax=plt.subplots(figsize=(9,6),layout='constrained')
ax.streamplot(x,y,bx,by,color='#3c6b87',density=1.65,linewidth=.85,arrowsize=1.05)
for a in [-1,0,1]:
    ax.add_patch(plt.Circle((a,0),.105,color='white',ec='black',lw=1.5,zorder=4))
    ax.plot(a,0,'ko',ms=4,zorder=5);ax.text(a,-.27,r'$I\odot$',ha='center',bbox={'facecolor':'white','edgecolor':'none','pad':1},zorder=6)
for a in [-1/np.sqrt(3),1/np.sqrt(3)]:
    ax.plot(a,0,'o',mfc='white',mec='#bb3f34',ms=7,mew=1.7,zorder=6)
    ax.annotate(r'$B=0$',(a,0),(a,.49),ha='center',color='#a63831',arrowprops={'arrowstyle':'->','color':'#a63831'},bbox={'facecolor':'white','edgecolor':'none','pad':1},zorder=7)
ax.set(xlim=(-2.8,2.8),ylim=(-2.1,2.1),aspect='equal',xlabel=r'$x/d$',ylabel=r'$y/d$')
ax.set_title(r'Three currents out of the page; nulls at $x/d=\pm1/\sqrt{3}$')
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=115,facecolor='white',transparent=False)
