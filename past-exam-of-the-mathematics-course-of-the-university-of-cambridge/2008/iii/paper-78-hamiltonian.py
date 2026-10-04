"""Draw Hamiltonian level curves; output basename to caller CWD.
Tested with Python 3.14; uses repository numpy/matplotlib dependencies; preserves caller MPLCONFIGDIR.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
u=np.linspace(-2.65,2.4,850);v=np.linspace(-2.7,2.7,700)
U,V=np.meshgrid(u,v);H=.5*V**2+U-U**3/3
fig,ax=plt.subplots(figsize=(7.8,5.2),facecolor='white')
levels=[-1.05,-.48,0,.38,1.12]
cs=ax.contour(U,V,H,levels=levels,colors=['#999999','#3478a3','#3478a3','#3478a3','#999999'],linewidths=1.2)
ax.clabel(cs,fmt='H = %.2f',fontsize=8)
s=np.linspace(-2,1,650);w=np.sqrt(2/3)*(1-s)*np.sqrt(np.maximum(s+2,0))
ax.plot(s,w,color='#b43030',lw=2,label='Homoclinic level H = 2/3');ax.plot(s,-w,color='#b43030',lw=2)
right=np.linspace(1,2.4,250);wr=np.sqrt(2/3)*(right-1)*np.sqrt(right+2)
ax.plot(right,wr,color='#b43030',lw=1.4);ax.plot(right,-wr,color='#b43030',lw=1.4)
ax.scatter([-1],[0],color='black',s=32,zorder=4);ax.scatter([1],[0],marker='x',color='black',s=65,zorder=4)
ax.annotate('Center',(-1,0),xytext=(-1.62,-.35),fontsize=10);ax.annotate('Saddle',(1,0),xytext=(1.12,-.35),fontsize=10)
for a,b in [(-1.0,1.5),(-1.0,-1.5),(.7,.18),(.7,-.18)]:
 vec=np.array([b,a*a-1]);vec=vec/np.linalg.norm(vec)*.23
 ax.annotate('',xy=(a+vec[0],b+vec[1]),xytext=(a,b),arrowprops={'arrowstyle':'->','color':'#555555'})
ax.axhline(0,color='#bbbbbb',lw=.5);ax.axvline(0,color='#bbbbbb',lw=.5)
ax.set(xlim=(-2.65,2.4),ylim=(-2.7,2.7),xlabel='u',ylabel="v = du / d t̃",title='Hamiltonian phase portrait (κ = 1)')
ax.legend(loc='upper left',fontsize=9,framealpha=1);fig.tight_layout()
fig.savefig('paper-78-hamiltonian.png',dpi=145,facecolor='white',transparent=False)
