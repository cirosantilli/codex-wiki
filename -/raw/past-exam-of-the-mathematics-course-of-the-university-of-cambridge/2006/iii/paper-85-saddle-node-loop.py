"""Original local return graphs and schematic global saddle-node-loop portraits."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch,Rectangle
from matplotlib.path import Path
fig,axs=plt.subplots(2,4,figsize=(14.6,7.6),layout='constrained')
plt.rcParams.update({'font.size':9})
h=1.;lam=1.;coef=.1
ax=axs[0,0];k=.05;x=np.linspace(k+.0001,.23,700)
Y=h*((h+k)/(h-k)*(x-k)/(x+k))**(lam/(2*k))
ax.plot(x,x,'k--',lw=1,label='diagonal')
for nu,color in [(.065,'#d95f02'),(.035,'#2166ac')]:
 P=nu+coef*Y
 ax.plot(x,P,color=color,lw=1.8,label=fr'$\nu={nu}$')
ax.axvline(k,color='#999999',ls=':',lw=1)
ax.set(xlim=(.04,.23),ylim=(.025,.16),xlabel='entry x',ylabel='next entry',title=r'Return map: $\mu=0.0025$')
ax.legend(fontsize=7)
ax=axs[1,0]
v,m=np.meshgrid(np.linspace(-.5,.5,450),np.linspace(-.045,.14,450))
cyc=(m<0)|((m>0)&(v>0)&(v*v>m))
ax.contourf(v,m,cyc.astype(int),levels=[.5,1.5],colors=['#ffe1be'])
p=np.linspace(0,np.sqrt(.14),400);ax.plot(p,p*p,color='#b2182b',lw=2);ax.plot(-p,p*p,color='#999999',ls='--',lw=1)
ax.plot([-.5,0],[0,0],color='#b2182b',lw=2);ax.plot([0,.5],[0,0],color='black',lw=1)
ax.plot(0,0,'k*',ms=9)
ax.text(.32,.02,'cycle',fontsize=8);ax.text(-.31,.09,'node capture',fontsize=8);ax.text(-.4,-.028,'cycle; no local equilibria',fontsize=8)
ax.set(xlim=(-.5,.5),ylim=(-.045,.14),xlabel=r'$\nu$',ylabel=r'$\mu$',title='Local unfolding')

def return_arc(ax,start,end,color):
 path=Path([start,(1.52,1.44),(end[0],1.63),end],[Path.MOVETO,Path.CURVE4,Path.CURVE4,Path.CURVE4])
 ax.add_patch(FancyArrowPatch(path=path,arrowstyle='->',mutation_scale=9,lw=1.7,color=color))

def portrait(ax,mu,nu,label):
 xs=np.linspace(-.87,1,100);ys=np.linspace(-.12,1,70);X,Y=np.meshgrid(xs,ys)
 U=X*X-mu;V=-lam*Y;speed=np.hypot(U,V)
 ax.add_patch(Rectangle((-.88,-.13),1.89,1.14,facecolor='#f7f7f7',edgecolor='#bbbbbb',lw=.6,zorder=0))
 ax.streamplot(xs,ys,U/(speed+.04),V/(speed+.04),color='#bcbcbc',density=.6,linewidth=.45,arrowsize=.6)
 ax.plot([-.87,1],[h,h],'--',color='#aaaaaa',lw=.6)
 ax.text(-.82,1.06,r'$y=h$',fontsize=7,color='#777777')
 if mu>0:
  k=np.sqrt(mu);ax.plot(-k,0,'ko',ms=4);ax.plot(k,0,'D',mfc='white',mec='black',ms=4)
  cycle=nu>k
 else:k=np.sqrt(-mu);cycle=True
 if cycle:
  entry=nu
  for _ in range(80):
   if mu>0:t=np.log((h-k)/(h+k)*(entry+k)/(entry-k))/(2*k)
   else:t=(np.arctan(h/k)-np.arctan(entry/k))/k
   out=h*np.exp(-lam*t);entry=nu+coef*out
  xx=np.linspace(entry,h,500)
  if mu>0:tt=np.log((xx-k)/(xx+k)*(entry+k)/(entry-k))/(2*k)
  else:tt=(np.arctan(xx/k)-np.arctan(entry/k))/k
  yy=h*np.exp(-lam*tt)
  ax.plot(xx,yy,color='#d95f02',lw=1.8)
  j=190;ax.annotate('',xy=(xx[j+24],yy[j+24]),xytext=(xx[j],yy[j]),arrowprops=dict(arrowstyle='->',color='#d95f02',lw=1.5))
  return_arc(ax,(h,yy[-1]),(entry,h),'#d95f02')
  ax.text(-.83,1.42,'attracting cycle',fontsize=8,color='#d95f02')
 else:
  ax.plot([k+.003,h],[0,0],color='#444444',lw=1.5)
  return_arc(ax,(h,0),(nu,h),'#444444')
  t=np.linspace(0,18,700);q=(nu-k)/(nu+k)*np.exp(2*k*t)
  xx=k*(1+q)/(1-q);yy=h*np.exp(-lam*t)
  ax.plot(xx,yy,color='#444444',lw=1.5)
  j=60;ax.annotate('',xy=(xx[j+25],yy[j+25]),xytext=(xx[j],yy[j]),arrowprops=dict(arrowstyle='->',color='#444444',lw=1.4))
  ax.text(-.83,1.42,'return captured by node',fontsize=8)
 ax.set(xlim=(-.94,1.57),ylim=(-.2,1.72),xlabel='x',ylabel='y',title=label)
 ax.tick_params(labelsize=7)
for row,sign in [(0,-1),(1,1)]:
 portrait(axs[row,1],.12,sign*.2,fr'$\mu>\nu^2$, $\nu{">" if sign>0 else "<"}0$')
 portrait(axs[row,2],.025,sign*.35,fr'$0<\mu<\nu^2$, $\nu{">" if sign>0 else "<"}0$')
 portrait(axs[row,3],-.02,sign*.35,fr'$\mu<0$, $\nu{">" if sign>0 else "<"}0$')
fig.savefig('paper-85-saddle-node-loop.png',dpi=150,facecolor='white',transparent=False)
