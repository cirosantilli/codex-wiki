"""Original educational figure. Python3.14, NumPy2.3.5, Matplotlib3.10.7.
PNG basename is written in the current working directory.
"""
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":11,"figure.facecolor":"white","savefig.facecolor":"white"})
def L(x):
 x=np.asarray(x);out=np.zeros_like(x,dtype=float);m=abs(x)>.001
 out[m]=1/np.tanh(x[m])-1/x[m];out[~m]=x[~m]/3-x[~m]**3/45
 return out
fig,axs=plt.subplots(1,2,figsize=(9.7,4.3),layout='constrained')
x=np.linspace(0,6,700);axs[0].plot(x,L(x),lw=2,color='black',label=r'$\mathcal{L}(x)=\coth x-1/x$')
for tau in [.22,1/3,.43]:axs[0].plot(x,tau*x,lw=1.5,label=rf'$\tau={tau:.3g}$')
axs[0].set(xlabel=r'$x=4JS/(k_BT)$',ylabel=r'$\mathcal{L}(x)$ and $\tau x$',ylim=(0,1.15),title='Self-consistency intersections');axs[0].legend(fontsize=8);axs[0].grid(alpha=.2)
tr=np.linspace(.025,1.3,450);s=[]
for temp in tr:
 if temp>=1:s.append(0);continue
 # Solve S=L(3S/t) for the nonzero root by bisection.
 lo=1e-7;hi=1.
 for j in range(55):
  mid=(lo+hi)/2
  if float(L(np.array([3*mid/temp]))[0])-mid>0:lo=mid
  else:hi=mid
 s.append((lo+hi)/2)
axs[1].plot(tr,s,lw=2,color='#2563a6',label='Mean-field ordered branch')
axs[1].axvline(1,color='.5',ls=':');axs[1].set(xlabel=r'$T/T_c^{\rm MF}$',ylabel='Mean spin magnitude S',ylim=(-.04,1.04),title='Mean-field prediction only')
axs[1].text(.45,.14,'Not true finite-temperature order\nin the 2D short-range isotropic model',ha='center',fontsize=8,color='#9a3829');axs[1].legend(fontsize=8,loc='upper right');axs[1].grid(alpha=.2)
fig.savefig('paper-1-langevin-mean-field.png',dpi=165)
