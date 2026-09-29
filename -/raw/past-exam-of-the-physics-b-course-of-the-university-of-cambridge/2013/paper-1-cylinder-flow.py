"""Original evaluated zero-circulation potential-flow streamlines and pressure. Output cwd."""
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({"axes.titlesize":10,"axes.labelsize":10})
from matplotlib.patches import Circle
fig,ax=plt.subplots(1,2,figsize=(9,3.6),layout='constrained');x=np.linspace(-3,3,601);y=np.linspace(-2.3,2.3,461);xx,yy=np.meshgrid(x,y);r2=xx*xx+yy*yy;psi=yy*(1-1/np.maximum(r2,1e-12));psi=np.ma.masked_where(r2<=1,psi);ax[0].contour(xx,yy,psi,levels=np.linspace(-2,2,21),colors='#3569ac',linewidths=.85);ax[0].add_patch(Circle((0,0),1,fc='#edf0f3',ec='k',zorder=3));ax[0].annotate('uniform flow',xy=(-1.8,1.9),xytext=(-2.8,1.9),arrowprops=dict(arrowstyle='->'),va='center');ax[0].set(aspect='equal',xlabel='x/a',ylabel='y/a',title='No penetration, zero circulation');th=np.linspace(0,2*np.pi,400);ax[1].plot(th/np.pi,1-4*np.sin(th)**2,lw=2);ax[1].axhline(0,color='.5',lw=.8);ax[1].set(xlabel=r'$\theta/\pi$',ylabel=r'$C_p=(p-p_\infty)/(\rho U^2/2)$',title='Fore–aft and top–bottom pressure symmetry');ax[1].grid(alpha=.2)
fig.savefig('paper-1-cylinder-flow.png',dpi=150,facecolor='white')
