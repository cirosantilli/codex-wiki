"""Exact polar trajectories. Python 3.14; NumPy and Matplotlib."""
import numpy as np
import matplotlib.pyplot as plt
fig,ax=plt.subplots(figsize=(6,6),facecolor='white')
t=np.linspace(0,10,900)
for rho in [.18,.52,1.65,2.45]:
 for alpha in [0,np.pi*.7,np.pi*1.4]:
  r=1+(rho-1)*np.exp(-t);x=r*np.cos(alpha+t);y=r*np.sin(alpha+t)
  ax.plot(x,y,color='#1769aa' if rho<1 else '#c45514',lw=1.05)
  k=55;ax.annotate('',xy=(x[k+12],y[k+12]),xytext=(x[k],y[k]),arrowprops={'arrowstyle':'->','color':'#1769aa' if rho<1 else '#c45514'})
a=np.linspace(0,2*np.pi,500);ax.plot(np.cos(a),np.sin(a),color='black',lw=2,label=r'Attracting orbit; period $2\pi$')
ax.plot(0,0,'o',mfc='white',mec='black',ms=5,label='Origin excluded')
ax.set(xlim=(-2.6,2.6),ylim=(-2.6,2.6),xlabel='$x$',ylabel='$y$',title=r'$\dot r=1-r,\quad\dot\theta=1$');ax.set_aspect('equal');ax.grid(alpha=.13);ax.legend(loc='upper right',fontsize=9);fig.tight_layout();fig.savefig('2006-phase-portrait.png',dpi=150,facecolor='white')
