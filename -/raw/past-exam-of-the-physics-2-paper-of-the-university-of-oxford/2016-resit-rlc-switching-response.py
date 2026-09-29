"""Original illustration for the 2016 Oxford Physics 2 resit solutions.
Writes only the matching PNG to the current working directory.
Tested with Python 3.14, numpy 2.3.5 and matplotlib 3.10.7 (root pyproject.toml).
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({"font.size": 11, "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white"})

R=3.;L=.008;C=.4e-6;V=6.;t1=.005;I1=V/R*(1-np.exp(-R*t1/L));alpha=R/(2*L);omega=np.sqrt(1/(L*C)-alpha*alpha);deriv=(V-R*I1)/L;B=(deriv+alpha*I1)/omega;env0=np.hypot(I1,B);decay=np.log(20)/alpha
fig,axs=plt.subplots(2,2,figsize=(10.2,7.2),layout='constrained')
ax=axs[0,0];ax.plot([0,0],[0,.8],color='black');ax.plot([0,0],[1.15,2],color='black');ax.plot([-.3,.3],[.8,.8],color='black',lw=2);ax.plot([-.5,.5],[1.15,1.15],color='black',lw=2);ax.text(-.65,1,'$V_0$',ha='right')
ax.plot([0,1.5],[2,2],color='black');ax.plot([1.5,1.5],[1.7,2.3],color='black',lw=2);ax.plot([1.7,1.7],[1.7,2.3],color='black',lw=2);ax.plot([1.7,2.9],[2,2],color='black');ax.text(1.6,1.25,'$C$',ha='center')
x=np.linspace(2.9,4.3,45);ax.plot(x,2+.12*np.sin(np.linspace(0,10*np.pi,len(x))),color='black');ax.plot([4.3,5],[2,2],color='black');ax.text(3.6,2.4,'$R$',ha='center')
x=np.linspace(5,6.9,150);ax.plot(x,2+.22*abs(np.sin(np.linspace(0,4*np.pi,len(x)))),color='black');ax.text(6,2.5,'$L$',ha='center');ax.plot([6.9,8,8,0],[2,2,0,0],color='black')
ax.plot([.9,.9,1.3],[2,3,3],color='black');ax.plot([1.3,1.8],[3,3.3],color='black');ax.plot([1.9,2.4,2.4],[3,3,2],color='black');ax.scatter([1.3,1.9],[3,3],s=12,color='black');ax.text(1.6,3.55,'$S$ bypasses $C$',ha='center');ax.set(xlim=(-1.1,8.3),ylim=(-.3,4),title='Topology during the switching sequence');ax.axis('off')
t=np.linspace(0,t1,450);axs[0,1].plot(1000*t,V/R*(1-np.exp(-R*t/L)),color='#266da6',lw=2);axs[0,1].scatter([5],[I1],color='black',s=22);axs[0,1].axhline(2,color='.6',ls=':',lw=1);axs[0,1].set(xlabel='time since closure (ms)',ylabel='coil current (A)',title=f'Closed switch: I(5 ms) = {I1:.3f} A',xlim=(0,5),ylim=(0,2.15))
for ax,end,long in [(axs[1,0],.001,False),(axs[1,1],.02,True)]:
 tau=np.linspace(0,end,10000);cur=np.exp(-alpha*tau)*(I1*np.cos(omega*tau)+B*np.sin(omega*tau));ax.plot(1000*tau,cur,color=('#777777'if long else'#266da6'),lw=(.8 if long else 1.5));ax.set(xlabel='time since reopening (ms)',ylabel='coil current (A)',xlim=(0,end*1000),ylim=(-1.9,1.9));ax.grid(alpha=.18)
 if long:
  envelope=env0*np.exp(-alpha*tau);ax.plot(tau*1000,envelope,color='#bd7627',lw=1.8);ax.plot(tau*1000,-envelope,color='#bd7627',lw=1.8);ax.axvline(decay*1000,color='#2b834c',ls='--',lw=1);ax.annotate(f'5% at {1000*decay:.2f} ms',(decay*1000,.05*env0),(7.5,1.15),arrowprops={'arrowstyle':'->','color':'#2b834c'},fontsize=10);ax.set_title('Current and exponential amplitude envelope')
 else:ax.set_title('First millisecond after reopening')
axs[0,1].grid(alpha=.18);fig.suptitle('Capacitor bypass: RL growth followed by underdamped series RLC oscillations',fontsize=12)
fig.savefig(Path.cwd()/'2016-resit-rlc-switching-response.png',dpi=140,transparent=False);plt.close(fig)
