"""Original Hamiltonian amplitude contours. Python 3.14/numpy/matplotlib.
Writes a PNG basename to the caller's current working directory.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
v=np.linspace(-1.45,1.45,400);u=np.linspace(0,2.1,400)
V,U=np.meshgrid(v,u)
F=U*(1-U*U/3-V*V)
fig,ax=plt.subplots(figsize=(7.2,4.8),constrained_layout=True)
cs=ax.contour(V,U,F,levels=[.12,.28,.45,.60],colors=['#749ebb','#4989b5','#1d6b9d','#004c7a'],linewidths=1.5)
ax.clabel(cs,fmt='F = %.2f',fontsize=8)
z=np.linspace(-1,1,600)
ax.plot(z,np.sqrt(3*(1-z*z)),color='#c05a22',lw=2,label='F = 0: interior connection')
ax.plot([-1,1],[0,0],color='#c05a22',lw=2)
ax.annotate('',xy=(.58,1.40),xytext=(.25,1.68),arrowprops={'arrowstyle':'->','color':'#c05a22','lw':1.5})
ax.annotate('',xy=(-.2,.018),xytext=(.25,.018),arrowprops={'arrowstyle':'->','color':'#c05a22','lw':1.5})
ax.plot([-1,1],[0,0],'kx',ms=8,clip_on=False)
ax.plot(0,1,'o',mfc='white',mec='#004c7a',ms=7)
ax.annotate(r'centre: $F=2/3$',(0,1),(.25,.91),fontsize=9)
ax.annotate('saddle',(-1,0),(-1.3,.13),fontsize=9)
ax.annotate('saddle',(1,0),(1.05,.13),fontsize=9)
ax.set(xlabel='v (axial amplitude)',ylabel='u (nonnegative radial amplitude)',title=r'Fold–Hopf contours, $\lambda_2=-1$',xlim=(-1.45,1.45),ylim=(0,2.1))
ax.legend(fontsize=8,loc='upper right')
ax.spines[['top','right']].set_visible(False)
fig.savefig('paper-59-fold-hopf-contours.png',dpi=120,facecolor='white')
plt.close(fig)
