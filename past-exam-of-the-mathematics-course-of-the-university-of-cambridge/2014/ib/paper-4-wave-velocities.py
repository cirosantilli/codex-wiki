"""Python 3.14; NumPy 2.3.5, Matplotlib 3.10.7. Writes only the PNG basename in cwd."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig,ax=plt.subplots(1,2,figsize=(9,4.2),dpi=100,facecolor='white',gridspec_kw={'width_ratios':[1.6,1]})
phase=np.linspace(-.3,1.65*np.pi,300)
ax[0].plot(phase,np.cos(phase),color='#3f78a5',lw=2)
ax[0].axhline(0,color='0.8',lw=.8)
for n in range(4):
 x=n*np.pi/2
 dx=[.55,0,-.55,0][n];dy=[0,.45,0,-.45][n]
 ax[0].annotate('',xy=(x+dx,np.cos(x)+dy),xytext=(x,np.cos(x)),arrowprops={'arrowstyle':'-|>','color':'#bd362f','lw':2.4})
 ax[0].plot(x,np.cos(x),'o',color='#3f78a5',ms=4)
ax[0].set_xticks(np.arange(4)*np.pi/2,['0',r'$\pi/2$',r'$\pi$',r'$3\pi/2$'])
ax[0].set_ylim(-1.65,1.65);ax[0].set_xlabel(r'Wave phase $\theta$ (at a fixed time)')
ax[0].set_ylabel(r'Surface height $\eta/\eta_0$');ax[0].set_title('Velocity: right, up, left, down')
ax[0].text(.03,.02,'Arrows show horizontal (x, y) velocities.\nRed vertical arrows mean the +y or -y direction.',transform=ax[0].transAxes,fontsize=8)
t=np.linspace(0,2*np.pi,300);ratio=.6
ax[1].plot(-np.sin(t),ratio*np.cos(t),color='#3f78a5',lw=2)
for n in range(4):
 t0=n*np.pi/2;x=-np.sin(t0);y=ratio*np.cos(t0)
 ax[1].plot(x,y,'o',color='#3f78a5',ms=4)
 ax[1].annotate(str(n),xy=(x,y),xytext=(8,6),textcoords='offset points',fontsize=9)
 ax[1].annotate('',xy=(x+.25*np.cos(t0),y+.25*ratio*np.sin(t0)),xytext=(x,y),arrowprops={'arrowstyle':'-|>','color':'#bd362f','lw':2})
ax[1].set_aspect('equal');ax[1].set_xlim(-1.3,1.4);ax[1].set_ylim(-1,1)
ax[1].set_xlabel(r'$\xi/(U/\omega)$');ax[1].set_ylabel(r'$\upsilon/(U/\omega)$')
ax[1].set_title('Particle orbit is clockwise\nIllustration: f / ω = 0.6')
for a in ax:
 a.spines[['top','right']].set_visible(False)
fig.tight_layout(pad=1.6)
fig.savefig('paper-4-wave-velocities.png',facecolor='white',transparent=False)
plt.close(fig)
