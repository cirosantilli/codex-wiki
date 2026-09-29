"""Original conservative phase portrait; Python 3.14, NumPy 2.3, Matplotlib 3.10.
Opaque PNG to caller CWD; MPLCONFIGDIR is left to caller.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
u=np.linspace(-2.6,2.4,700);v=np.linspace(-2.5,2.5,600)
U,V=np.meshgrid(u,v);H=V*V/2+U-U**3/3
fig,ax=plt.subplots(figsize=(8.0,5.2),dpi=130,facecolor='white')
ax.contour(U,V,H,levels=[-.65,-.4,0,.3,.6,.85,1.2],colors='#7b9da8',linewidths=1)
q=np.linspace(-2,1,900);vp=np.sqrt(2/3)*(1-q)*np.sqrt(np.maximum(q+2,0))
ax.plot(q,vp,color='#9d3235',lw=2.5);ax.plot(q,-vp,color='#9d3235',lw=2.5,label='Saddle loop: H = 2/3')
ax.scatter([-1],[0],s=55,color='black',label='Center (−1, 0)')
ax.scatter([1],[0],marker='x',s=80,color='black',label='Saddle (1, 0)')
for pos in [-.7,.1]:
 vv=np.sqrt(2/3)*(1-pos)*np.sqrt(pos+2)
 ax.annotate('',xy=(pos+.17,np.sqrt(2/3)*(1-pos-.17)*np.sqrt(pos+.17+2)),xytext=(pos,vv),arrowprops={'arrowstyle':'->','color':'#9d3235','lw':1.6})
 ax.annotate('',xy=(pos-.17,-np.sqrt(2/3)*(1-pos+.17)*np.sqrt(pos-.17+2)),xytext=(pos,-vv),arrowprops={'arrowstyle':'->','color':'#9d3235','lw':1.6})
ax.contour(U,V,H,levels=[2/3],colors='#9d3235',linestyles='--',linewidths=.9)
ax.set(xlim=(-2.6,2.4),ylim=(-2.5,2.5),xlabel='u',ylabel='v',title='Conservative quadratic-force oscillator (α = 1)')
ax.axhline(0,color='gray',lw=.5);ax.axvline(0,color='gray',lw=.5)
ax.legend(loc='upper left',fontsize=9);fig.tight_layout()
fig.savefig('paper-51-hamiltonian-contours.png',facecolor='white',transparent=False);plt.close(fig)
