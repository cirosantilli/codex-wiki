# Tested with Python3.14.4,numpy2.3.5,matplotlib3.10.7. Writes PNG to CWD.
import numpy as np
import matplotlib.pyplot as plt
fig,axs=plt.subplots(1,2,figsize=(10,4.5),facecolor='white');ax=axs[0];end=1+np.sqrt(6)
x=np.linspace(0,1,200);ax.plot(x,0*x,color='#235e9b',lw=2);x=np.linspace(1,end,500);ax.plot(x,0*x,'--',color='#888888');x=np.linspace(1,3,450);ax.plot(x,1-1/x,color='#235e9b',lw=2);x=np.linspace(3,end,450);ax.plot(x,1-1/x,'--',color='#888888');d=np.sqrt((x-3)*(x+1));ax.plot(x,(x+1+d)/(2*x),color='#b33866',lw=2);ax.plot(x,(x+1-d)/(2*x),color='#b33866',lw=2)
for v in [1,3,end]:ax.axvline(v,color='gray',ls=':',lw=.8)
ax.set(xlim=(0,3.52),ylim=(-.03,1),xlabel=r'$\mu$',ylabel='Fixed points / two-cycle',title='First two logistic doublings');ax.text(1.05,.88,'Solid: attracting\nDashed: unstable',fontsize=9);ax.text(3.1,.96,r'$1+\sqrt{6}$',fontsize=10)
ax=axs[1];x=np.linspace(0,1,500);ax.plot(x,4*x*(1-x),color='#235e9b',label='$4x(1-x)$');ax.plot(x,x,'--',color='gray');u=.173;y=0
for i in range(30):
 v=4*u*(1-u);ax.plot([u,u,v],[y,v,v],color='#b94427',alpha=.55,lw=.7);u=v;y=v
ax.set(xlim=(0,1),ylim=(0,1),xlabel='$x_n$',ylabel='$x_{n+1}$',title=r'Chaotic cobweb at $\mu=4$');ax.grid(alpha=.15);fig.tight_layout()
fig.savefig('2007-logistic-bifurcations.png',dpi=160,facecolor='white')
