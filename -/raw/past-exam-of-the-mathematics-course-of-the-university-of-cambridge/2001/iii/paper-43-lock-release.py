"""Original diagram; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7. Output to caller CWD."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
F=np.sqrt(2);cf=2/(F+2);uf=F*cf;tr=1.;ts=((F+2)/2)**1.5;thit=2*ts
fig=plt.figure(figsize=(12,6.2),facecolor='white');gs=GridSpec(2,2,figure=fig,width_ratios=[1.05,1.15]);a=fig.add_subplot(gs[0,0]);b=fig.add_subplot(gs[1,0]);c=fig.add_subplot(gs[:,1])
t=.45;x=np.linspace(0,1+uf*t,400);s=(x-1)/t;h=np.where(s<-1,1,np.where(s<uf-cf,((2-s)/3)**2,cf**2))
a.fill_between(x,0,h,color='#8cb9df');a.plot(x,h,color='#155a92',lw=2);a.plot([1+uf*t]*2,[0,cf**2],color='#155a92',lw=2);a.plot([0,1,1],[1,1,0],color='gray',ls='--');a.axvline(0,color='black',lw=3);a.annotate('rarefaction',xy=(.9,.64),xytext=(.65,1.15),arrowprops={'arrowstyle':'->'});a.annotate('uniform shelf + head',xy=(1.24,cf**2),xytext=(1.04,.76),arrowprops={'arrowstyle':'->'});a.text(.08,.08,'dense current');a.text(1.53,.42,'ambient');a.set(xlim=(-.08,1.9),ylim=(0,1.35),xlabel='x / initial lock length',ylabel='h / initial depth',title='Early release from a rectangular lock')
y=np.linspace(0,1,240);late=.5*(1+y*y);b.fill_between(y,0,late,color='#8cb9df');b.plot(y,late,color='#155a92',lw=2);b.plot([1,1],[0,1],color='#155a92');b.axvline(0,color='black',lw=3);b.quiver([.2,.5,.8],[.18]*3,[.05,.11,.18],[0]*3,angles='xy',scale_units='xy',scale=1,color='#155a92');b.set(xlim=(-.08,1.15),ylim=(0,1.2),xlabel='x / L(t)',ylabel='h / front depth',title='Late similarity: L grows as time to the 2/3 power')
times=np.linspace(0,thit,400);c.plot(1+uf*times,times,color='#155a92',lw=2,label='constant-speed front');c.plot([0,0],[0,6.5],color='black',lw=2,label='closed wall')
for speed in np.linspace(-1,uf-cf,7):
 tt=np.linspace(0,min(tr,-1/speed) if speed<0 else tr,120);c.plot(1+speed*tt,tt,color='#a8b4c5',lw=.9)
tt=np.linspace(tr,ts,200);xx=1+2*tt-3*tt**(1/3);c.plot(xx,tt,color='#c75c18',lw=2,label='first reflected information');tt=np.linspace(ts,thit,140);xx=(1+(uf-cf)*ts)+(uf+cf)*(tt-ts);c.plot(xx,tt,color='#c75c18',lw=2)
Lhit=1+uf*thit;age=2*Lhit/(3*uf);tt=np.linspace(thit,6.4,150);xx=Lhit*((tt-thit+age)/age)**(2/3);c.plot(xx,tt,color='#155a92',ls='--',lw=2,label='later deceleration (schematic)')
c.scatter([0,Lhit],[tr,thit],color='#c75c18');c.annotate('wall reached',xy=(0,tr),xytext=(.65,1.45),arrowprops={'arrowstyle':'->'});c.annotate('head first informed',xy=(Lhit,thit),xytext=(2.3,5.25),arrowprops={'arrowstyle':'->'});c.set(xlim=(-.12,6.8),ylim=(0,6.6),xlabel='x / initial lock length',ylabel='t / wall-arrival time',title='Information and transition in the x–t plane');c.legend(loc='lower right',fontsize=8)
fig.tight_layout();fig.savefig('paper-43-lock-release.png',dpi=120,facecolor='white');plt.close(fig)
