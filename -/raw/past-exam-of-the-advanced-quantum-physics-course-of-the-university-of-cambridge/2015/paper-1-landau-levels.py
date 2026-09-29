"""Original explanatory plot. Python 3.14, numpy, matplotlib.
Run from the destination directory; writes a PNG basename to cwd.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'figure.facecolor':'white','savefig.facecolor':'white','font.size':10,'axes.spines.top':False,'axes.spines.right':False})
fig,axs=plt.subplots(1,2,figsize=(10,4),layout='constrained');a,b=axs;x=np.linspace(-4.6,4.6,1000)
for xc,col in [(-2,'#1766a5'),(0,'#c33c29'),(2,'#398447')]:
 v=(x-xc)**2/2;a.plot(x,v,color=col,lw=1.7,label=fr'$x_c/\ell_B={xc}$')
 for n in range(3):a.plot([xc-.5,xc+.5],[n+.5,n+.5],color=col,lw=1.3)
a.set(xlabel=r'$x/\ell_B$',ylabel=r'$E/(\hbar\omega_c)$',ylim=(0,4),title='Guiding-centre shift leaves spacing unchanged');a.legend(frameon=False,fontsize=9)
ky=np.linspace(-2,2,100)
for n in range(4):b.plot(ky,np.full_like(ky,n+.5),color='#1766a5',lw=2);b.text(2.06,n+.5,fr'$n={n}$',va='center')
b.annotate('',(-1.4,1.5),(-1.4,.5),arrowprops=dict(arrowstyle='<->'));b.text(-1.25,.94,r'$\hbar\omega_c$',fontsize=10)
b.set(xlabel=r'$k_y\ell_B$ (bulk centres)',ylabel=r'$E/(\hbar\omega_c)$',xlim=(-2.2,2.75),ylim=(0,4),title='Each orbital level has many centres')
fig.savefig('paper-1-landau-levels.png',dpi=170);plt.close(fig)
