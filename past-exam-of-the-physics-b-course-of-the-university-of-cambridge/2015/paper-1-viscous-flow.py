from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})

fig,ax=plt.subplots(1,3,figsize=(11,3.6))
a=ax[0];a.plot([0,1],[0,0],color='black',lw=3)
for z in [.18,.37,.56,.75,.94]:a.arrow(.12,z,.68*z,0,color='tab:blue',width=.007,head_width=.04,length_includes_head=True)
a.plot([.08,.88],[.35,.35],ls='--',color='gray');a.arrow(.4,.35,.28,0,color='tab:orange',width=.012,head_width=.05,length_includes_head=True)
a.text(.05,.05,r'$x\ \rightarrow$');a.text(.12,.43,r'Positive traction on a $+z$ face',fontsize=8);a.set(title='Shear and momentum transport',xlim=(0,1.15),ylim=(0,1.1),ylabel=r'$z$');a.set_xticks([])
z=np.linspace(0,1,200)
for P in [-2,0,2]:ax[1].plot(z+.5*P*z*(z-1),z,label=fr'$p^\prime a^2/(\eta u_0)={P}$')
ax[1].set(xlabel=r'$u/u_0$',ylabel=r'$z/a$',title='Steady flow');ax[1].legend(fontsize=7)
z=np.linspace(0,5,250)
for phase in [0,np.pi/2,np.pi]:ax[2].plot(np.exp(-z)*np.cos(z-phase),z,label=fr'$\omega t={phase/np.pi:.1f}\pi$')
ax[2].plot(np.exp(-z),z,'k--',lw=1,label='Amplitude envelope');ax[2].plot(-np.exp(-z),z,'k--',lw=1)
ax[2].set(xlabel=r'$u/U_0$',ylabel=r'$z/\delta$',title='Oscillatory viscous penetration');ax[2].legend(fontsize=7)

fig.tight_layout()
fig.savefig(Path(__file__).stem+'.png',dpi=140,facecolor='white',bbox_inches='tight')
plt.close(fig)
