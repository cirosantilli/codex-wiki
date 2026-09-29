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

eps=.0005;u=np.unique(np.r_[np.geomspace(1e-5,.6,2000),np.linspace(.6,26,2000)]);v=V(u)
fig,axes=plt.subplots(1,2,figsize=(11,4.5),layout='constrained')
for ax,mu,ylim in zip(axes,[.03,1.],[(0,12),(0,1.6)]):
 ax.plot(u,v,color='black',lw=1,label='$v$ nullcline $f=0$');rhs=eps/gamma*(mu-u);lo=np.zeros_like(u);hi=(J(u)-rhs)/delta+2;valid=J(u)>=rhs;hi=np.maximum(hi,1)
 for _ in range(65):
  m=(lo+hi)/2;pos=f(u,m)>rhs;lo=np.where(pos,m,lo);hi=np.where(pos,hi,m)
 un=(lo+hi)/2;ax.plot(u,np.where(valid,un,np.nan),'--',color='tab:orange',lw=1,label='$u$ nullcline')
 initial=bisect(lambda z:z+gamma*V(z)-25,right,25);ax.plot([25,initial],[0,V(initial)],color='tab:red',lw=2);ax.annotate('Fast store loading',xy=(initial,.18),xytext=(2,.8 if mu==1 else 2.6),arrowprops=dict(arrowstyle='->',color='tab:red'),color='tab:red',fontsize=8)
 end=right if mu<right else mu;a=np.geomspace(initial,end,1400);vv=V(a);ax.plot(a,vv,color='tab:green',lw=2.5,label='Slow critical-manifold path');arrow(ax,a,vv,700,'tab:green')
 if mu<right:
  ax.plot([right,ul],[V(right),V(ul)],color='tab:red',ls='--',lw=2,label='Fast jump at fixed $u+\\gamma v$');ax.annotate('',xy=(ul,V(ul)),xytext=(right,V(right)),arrowprops=dict(arrowstyle='->',color='tab:red',lw=1.6))
  a=np.linspace(ul,mu,700);vv=V(a);ax.plot(a,vv,color='tab:green',lw=2.5);arrow(ax,a,vv,350,'tab:green')
 ax.plot(mu,V(mu),'o',color='tab:purple',label='Stable equilibrium');ax.set_xscale('symlog',linthresh=.5);ax.set(xlim=(0,26),ylim=ylim,xlabel='Cytoplasmic calcium $u$ (compressed beyond 0.5)',ylabel='Store calcium $v$',title=f'Input $\\mu={mu:g}$: leading fast/slow geometry');ax.grid(alpha=.2)
axes[0].legend(fontsize=7,loc='upper right');axes[1].legend(fontsize=7,loc='upper right');fig.suptitle('Schematic separated paths; finite-$\\epsilon$ trajectories round the folds',fontsize=11)

fig.savefig(Path.cwd()/"2009-calcium-phase-plane.png",dpi=150)
