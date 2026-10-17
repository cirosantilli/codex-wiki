"""Original explanatory figure; Python 3.14, numpy and matplotlib.
Writes a literal PNG basename to cwd. No source-image pixels or media paths.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, FancyArrowPatch
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','savefig.facecolor':'white','axes.spines.top':False,'axes.spines.right':False})
fig,axs=plt.subplots(1,4,figsize=(13,3.7),layout='constrained');a=axs[0];alpha=1.15;theta=2*np.pi/3
for z,col,lab in [(alpha,'#1766a5',r'$\alpha$'),(alpha*np.exp(1j*theta),'#c33c29',r'$e^{i\Theta}\alpha$')]:
 a.add_patch(Circle((z.real,z.imag),.5,facecolor=col,edgecolor=col,alpha=.15));a.plot([0,z.real],[0,z.imag],color=col);a.scatter([z.real],[z.imag],color=col);a.text(z.real,z.imag+.6,lab,ha='center')
a.axhline(0,color='lightgray');a.axvline(0,color='lightgray');a.set(xlim=(-2,2),ylim=(-1.5,2),xlabel=r'$X_1$',ylabel=r'$X_2$',title='Coherent-state rotation');a.set_aspect('equal')
u=np.linspace(-2.7,2.7,350);x,y=np.meshgrid(u,u)
for ax,phi,title in zip(axs[1:],[0,np.pi/2,np.pi],['Even cat: φ = 0','Phase cat: φ = π/2','Odd cat: φ = π']):
 s=np.exp(-2*alpha*alpha);N2=1/(2*(1+s*np.cos(phi)));W=2/np.pi*N2*(np.exp(-2*((x-alpha)**2+y*y))+np.exp(-2*((x+alpha)**2+y*y))+2*np.exp(-2*(x*x+y*y))*np.cos(4*alpha*y+phi))
 im=ax.imshow(W,origin='lower',extent=(-2.7,2.7,-2.7,2.7),cmap='RdBu_r',vmin=-.65,vmax=.65);ax.set(xlabel=r'$X_1$',ylabel=r'$X_2$',title=title)
fig.colorbar(im,ax=axs[1:],shrink=.7,label='Wigner function');fig.savefig('paper-1-cat-states.png',dpi=150);plt.close(fig)
