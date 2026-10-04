"""Linear RG flow in the h=0 slice; Python 3.14 and root NumPy/Matplotlib.
Writes its PNG basename to the caller's CWD; honors supplied MPLCONFIGDIR.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig,ax=plt.subplots(figsize=(8,5),layout='constrained',facecolor='white')
t=np.linspace(-1,1,41);w=np.linspace(-1,1,41);T,W=np.meshgrid(t,w)
ax.streamplot(t,w,2*T,-W,density=1,color='#8c9aa6',arrowsize=1.1,linewidth=.8)
ax.axvline(0,color='#188950',lw=2,label='critical surface in the h = 0 slice')
ax.axhline(0,color='#be5234',lw=2,label='repulsive thermal trajectories')
ax.scatter([0],[0],s=70,c='#17202a',zorder=5)
ax.annotate('critical fixed point',(0,0),(.15,.5),arrowprops={'arrowstyle':'->'})
ax.text(-.92,.84,'ordered side',fontsize=12)
ax.text(.4,.84,'disordered side',fontsize=12)
ax.text(.15,-.65,r'$\dot t= y_t t,\quad y_t=2>0$'+'\n'+r'$\dot w=-\omega w,\quad\omega=1>0$',fontsize=12)
ax.set(xlabel='thermal scaling field t (relevant)',ylabel='irrelevant coordinate w',title='Coarse-graining flows toward longer lengths (h = 0)',xlim=(-1,1),ylim=(-1,1))
ax.legend(loc='lower left',fontsize=9)
fig.savefig('paper-50-rg-flow.png',dpi=120,facecolor='white')
plt.close(fig)
