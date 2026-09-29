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

mu=.3
def timing(u):
 q=wp(u)/(mu-u);dt=(q[1:]+q[:-1])*np.diff(u)/2;return np.r_[0,np.cumsum(dt)]
a=np.linspace(ul,left,3500);ta=timing(a);b=np.geomspace(ur,right,4500);tb=timing(b)+ta[-1];period=tb[-1]
fig,axes=plt.subplots(2,1,figsize=(10,5.5),sharex=True,layout='constrained')
for ax in axes:
 for n in range(2):
  ax.plot(ta+n*period,a,color='tab:blue',lw=2);ax.plot(tb+n*period,b,color='tab:green',lw=2);ax.plot([ta[-1]+n*period]*2,[left,ur],color='tab:red',lw=1.4);ax.plot([(n+1)*period]*2,[right,ul],color='tab:red',lw=1.4)
 ax.set(ylabel='Cytoplasmic calcium $u$');ax.grid(alpha=.2)
axes[0].set(title='Leading relaxation waveform: slow accumulation, fast release, slow clearance, fast uptake',ylim=(0,25));axes[0].text(.12*period,10,'Slow left branch',color='tab:blue');axes[0].annotate('Fast discharge',xy=(ta[-1],18),xytext=(ta[-1]-35,21),arrowprops=dict(arrowstyle='->',color='tab:red'),color='tab:red');axes[0].text(ta[-1]+2,8,'Slow right branch',color='tab:green',rotation=75)
axes[1].set(ylim=(0,.55),xlabel='Physical time $t$ (units $1/k$; numerical coordinate is $kt$)',title='Low-concentration detail of the same waveform');fig.suptitle('Singular cycle from exact nullcline quadrature; rapid transitions have zero duration at this order',fontsize=10)

fig.savefig(Path.cwd()/"2009-calcium-oscillation.png",dpi=150)
