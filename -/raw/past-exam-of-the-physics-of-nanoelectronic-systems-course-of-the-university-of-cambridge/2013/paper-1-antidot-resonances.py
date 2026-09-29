"""Original explanatory model; output is a basename in the working directory."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, FancyArrowPatch
plt.rcParams.update({'font.size':9,'axes.titlesize':10,'axes.labelsize':10})

fig,axs=plt.subplots(2,2,figsize=(9,7),layout='constrained');yy=np.linspace(-1.5,1.5,500);U=.95+.8*abs(yy)
ax=axs[0,0];ax.plot(yy,U,ls=':',color='black',label=r'$U$');ax.plot(yy,U+1/3,label=r'$n=0,-$');ax.plot(yy,U+2/3,label=r'$n=0,+$');ax.plot(yy,U+4/3,ls='--',color='grey',label=r'$n=1,-$');ax.axhline(2,color='black',ls='--',lw=1);ax.set(xlabel='Across neck (chosen units)',ylabel=r'$E/(\hbar\omega_c)$',ylim=(.7,3.3),title='Neck with two occupied branches');ax.legend(fontsize=8,ncol=2)
ax=axs[0,1]
for x,y,t in [(0,1,'Incident'),(1.3,1,'Closed orbit'),(2.8,1.55,'Forward exit'),(2.8,.4,'Return exit')]:ax.text(x,y,t,ha='center',va='center',bbox={'boxstyle':'round','fc':'white','ec':'#777777'})
for a,b in [((.4,1),(.85,1)),((1.7,1.12),(2.35,1.45)),((1.7,.9),(2.35,.5))]:ax.annotate('',xy=b,xytext=a,arrowprops={'arrowstyle':'->','lw':1.6})
ax.text(2.3,1.9,'Transmission',color='#2166ac');ax.text(2.3,.05,'Reflection',color='#b2182b');ax.text(1.4,-.45,'Connectivity schematic; spectator channels omitted',ha='center',fontsize=8);ax.set(xlim=(-.6,3.5),ylim=(-.8,2.2),title='Different outgoing connections');ax.axis('off')
x=np.linspace(0,5,1600);res=sum(.045**2/((x-x0)**2+.045**2) for x0 in [1,2.5,4]);res=np.clip(res,0,1)
for ax,gg,title in [(axs[1,0],2-res,'Reflection-dominated example'),(axs[1,1],1+res,'Transmission-dominated example')]:
 ax.plot(x,gg,lw=1.8);ax.axhline(1,color='grey',ls=':');ax.axhline(2,color='grey',ls=':');ax.set(xlabel=r'$B$ (relative chosen scale)',ylabel=r'$G/(e^2/h)$',ylim=(.8,2.2),yticks=[1,2],title=title);ax.grid(alpha=.15)
fig.savefig('paper-1-antidot-resonances.png',dpi=170,facecolor='white');plt.close(fig)
