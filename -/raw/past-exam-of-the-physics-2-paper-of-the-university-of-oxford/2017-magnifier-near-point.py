"""Original paraxial ray construction; focal and image positions are calculated."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'figure.facecolor':'white','axes.facecolor':'white'})
f,D,h=4.,25.,.20
u=f*D/(f+D);hi=D/u*h
fig,axs=plt.subplots(1,2,figsize=(11.6,4.8),width_ratios=[1.4,1],layout='constrained')
for ax in axs:
    ax.axhline(0,color='0.5',lw=1)
    ax.plot([0,0],[-.25,1.7],color='#377da0',lw=2)
    ax.annotate('',(0,1.7),(0,-.25),arrowprops={'arrowstyle':'<->','color':'#377da0','lw':3})
    for x,label in [(-f,'F'),(f,"F′")]:ax.plot(x,0,'ko',ms=3);ax.text(x,-.18,label,ha='center')
    ax.annotate('',(-u,h),(-u,0),arrowprops={'arrowstyle':'->','color':'#bd5142','lw':2.2})
    ax.annotate('',(-D,hi),(-D,0),arrowprops={'arrowstyle':'->','color':'#bd5142','lw':2.2,'linestyle':'--'})
    ax.plot([-u,0],[h,h],color='#bc8240',lw=1.8)
    ax.plot([-u,0],[h,0],color='#735da8',lw=1.8)
    x=np.linspace(0,7,100)
    for col,y in [('#bc8240',h*(1-x/f)),('#735da8',-h*x/u)]:
        ax.plot(x,y,color=col,lw=1.8)
        ax.annotate('',(5,float(np.interp(5,x,y))),(3,float(np.interp(3,x,y))),arrowprops={'arrowstyle':'->','color':col,'lw':1.8})
    xb=np.linspace(-D,0,100)
    ax.plot(xb,h*(1-xb/f),'--',color='#bc8240',lw=1.2)
    ax.plot(xb,-h*xb/u,'--',color='#735da8',lw=1.2)
    ax.set(xlabel='Distance along optical axis (cm)',ylim=(-.4,1.8))
axs[0].set(xlim=(-27,7),ylabel='Height (cm; vertical scale enlarged)')
axs[0].text(-24.6,1.52,'Upright virtual image\nat the near point',va='bottom',color='#a34435')
axs[0].set_title(r'$v=-25\,\mathrm{cm}$; angular magnification $7.25$')
axs[1].set(xlim=(-5.5,6.5),ylim=(-.45,.65))
axs[1].annotate('Object inside focus\n$u=3.45$ cm',(-u,h),(-5.3,.49),arrowprops={'arrowstyle':'->'},fontsize=10)
axs[1].text(.25,.5,'Lens; eye close\nto its right side',fontsize=10)
axs[1].set_title('Detail of the physical rays near the lens')
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=115,facecolor='white',transparent=False)
