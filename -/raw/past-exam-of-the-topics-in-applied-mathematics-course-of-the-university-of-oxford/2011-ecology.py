"""Original cobwebs and phase portraits; output CWD. Python3.14.4/numpy2.3.5/matplotlib3.10.7."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig,axes=plt.subplots(2,2,figsize=(10,7),layout='constrained',facecolor='white')
for ax,S in zip(axes[0],[.5,1.3]):
 x=np.linspace(0,2.6,500);f=lambda x:2*x*x/(x*x+S);ax.plot(x,f(x),label='Population map');ax.plot(x,x,color='gray',ls='--',label='N next = N')
 for n in [.15,1,2.4]:
  xx=[n];yy=[0.]
  for _ in range(22):new=f(n);xx.extend([n,new]);yy.extend([new,new]);n=new
  ax.plot(xx,yy,lw=.9)
 ax.set(xlabel='Current population N',ylabel='Next population',xlim=(0,2.6),ylim=(0,2.6),title=f'S={S:g}: '+('below' if S<1 else 'above')+' critical release Sc=1');ax.legend(fontsize=8)
for ax,beta in zip(axes[1],[.7,2]):
 u=np.linspace(.015,1.5,120);v=np.linspace(.015,2.2,120);U,V=np.meshgrid(u,v);du=U*(1-U-V);dv=V*(1-beta*U);scale=np.hypot(du,dv);ax.streamplot(u,v,du/(scale+.01),dv/(scale+.01),density=.8,color='#8d9ba2',linewidth=.7,arrowsize=.8)
 ax.plot([0,1],[1,0],color='#b45630',label='u+v=1');ax.axvline(1/beta,color='#21815a',ls='--',label='u=1/β')
 if beta>1:ax.plot([0,1.5],[0,1.5],color='#6939a0',lw=2,label='Saddle stable manifold v=u');ax.scatter([.5,1],[.5,0],color='black',s=22)
 else:ax.scatter([1],[0],color='black',s=22)
 ax.set(xlabel='u',ylabel='v',xlim=(0,1.5),ylim=(0,2.2),title=f'Two-species model: r=1, β={beta:g}');ax.legend(fontsize=8)
for ax in axes.flat:ax.grid(alpha=.15);ax.set_facecolor('white')
fig.savefig('2011-ecology.png',dpi=135,facecolor='white');plt.close(fig)
