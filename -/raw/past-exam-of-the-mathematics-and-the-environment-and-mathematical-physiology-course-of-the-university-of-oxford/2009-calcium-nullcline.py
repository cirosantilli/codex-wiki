# Original figure. Tested Python3.14, NumPy2.3.5, Matplotlib3.10.7.
# Run from the desired output directory; writes one same-basename PNG to CWD.
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":10,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})
beta=.1;delta=1e-5;gamma=.1
def J(u):return beta*u*u/(1+u*u)
def K(u):return u**4/(1+u**4)
def f(u,v):return J(u)-K(u)*v*v/(1+v*v)-delta*v
def V(u):
 u=np.asarray(u,dtype=float);lo=np.zeros_like(u);hi=J(u)/delta+1
 for _ in range(65):
  m=(lo+hi)/2;positive=f(u,m)>0;lo=np.where(positive,m,lo);hi=np.where(positive,hi,m)
 return (lo+hi)/2
def fu(u,v):return 2*beta*u/(1+u*u)**2-4*u**3/(1+u**4)**2*v*v/(1+v*v)
def fv(u,v):return -2*K(u)*v/(1+v*v)**2-delta
def wp(u):return 1-gamma*fu(u,V(u))/fv(u,V(u))
def bisect(fn,a,b):
 fa=fn(a)
 for _ in range(70):
  m=(a+b)/2
  if fn(m)*fa>0:a=m
  else:b=m
 return (a+b)/2
left=bisect(wp,.15,.25);right=bisect(wp,.33,.5)
wl=left+gamma*V(left);wr=right+gamma*V(right)
ul=bisect(lambda u:u+gamma*V(u)-wr,1e-8,.1)
ur=bisect(lambda u:u+gamma*V(u)-wl,1,30)
def arrow(ax,x,y,i,color):
 j=min(i+max(1,len(x)//18),len(x)-1);ax.annotate("",xy=(x[j],y[j]),xytext=(x[i],y[i]),arrowprops=dict(arrowstyle="->",color=color,lw=1.8))

u=np.unique(np.r_[np.linspace(.00001,.42,1500),np.linspace(.42,3,700)]);v=V(u);uc=np.sqrt((-1+np.sqrt(1+4*beta*(1-beta)))/(2*(1-beta)));kc=K(uc);dc=4*uc**3/(1+uc**4)**2-2*beta*uc/(1+uc*uc)**2
fig,axes=plt.subplots(1,2,figsize=(11,4.6),layout='constrained')
for ax in axes:
 ax.plot(u,v,color='black',lw=2,label='Exact $f=0$')
 a=u[(u<uc)&(u>.015)];ax.plot(a,(J(a)-K(a))/delta,'--',color='tab:green',label='Large-store balance')
 a=u[u>uc+.00001];r=J(a)/K(a);ax.plot(a,np.sqrt(r/(1-r)),'--',color='tab:blue',label='Negligible-leak balance')
 a=np.geomspace(3,180,600);ax.plot(uc+(kc/a**2-delta*a)/dc,a,':',color='tab:orange',lw=2,label='Crossing-region balance');ax.set(xlabel='Cytoplasmic calcium $u$',ylabel='Store calcium $v$');ax.grid(alpha=.2)
axes[0].set(xlim=(0,1.6),ylim=(0,260),title='Rise, high peak and rapid fall');axes[0].legend(fontsize=8)
axes[1].set(xlim=(.285,.35),ylim=(.7,100),yscale='log',title='Transition near $u_c$ (logarithmic store axis)');axes[1].axvline(uc,color='grey',lw=.7);axes[1].text(uc+.001,1.1,'$u_c$')

fig.savefig(Path.cwd()/"2009-calcium-nullcline.png",dpi=150)
