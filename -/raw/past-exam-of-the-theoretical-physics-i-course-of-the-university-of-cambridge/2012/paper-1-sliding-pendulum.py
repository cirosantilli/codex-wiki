"""Original explanatory figure; Python 3.14, NumPy and Matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white','savefig.facecolor':'white'})

fig,ax=plt.subplots(figsize=(6.8,5.3),layout='constrained');m1=1.;m2=1.5;M=m1+m2;phi=np.linspace(-np.pi,np.pi,1000)
ax.plot(m1/M*np.sin(phi),-np.cos(phi),color='#b3b3b3',ls='--',label='containing ellipse')
phi=np.linspace(-.9,.9,500);ax.plot(m1/M*np.sin(phi),-np.cos(phi),color='#2b6d91',lw=3,label='allowed oscillation arc')
ax.axhline(0,color='k',lw=.8);ax.axvline(0,color='#777777',ls=':',label='fixed horizontal centre of mass')
for ph,col in [(-.8,'#b56744'),(0,'#777777'),(.8,'#488872')]:
 cart=-m2/M*np.sin(ph);bob=m1/M*np.sin(ph);by=-np.cos(ph);ax.plot([cart,bob],[0,by],color=col,alpha=.8);ax.plot(cart,0,'s',color=col,ms=6);ax.plot(bob,by,'o',color=col,ms=7)
ax.annotate('support counter-moves',xy=(-m2/M*np.sin(.8),0),xytext=(-1,.45),arrowprops={'arrowstyle':'->'},fontsize=9)
ax.annotate('bob',xy=(m1/M*np.sin(.8),-np.cos(.8)),xytext=(.57,-.65),arrowprops={'arrowstyle':'->'},fontsize=9)
ax.set(xlim=(-1.1,1.1),ylim=(-1.2,1.2),aspect='equal',xlabel=r'$(X-X_c)/l$',ylabel=r'$Y/l$',title=r'Zero horizontal momentum; illustrative $m_2/m_1=1.5$');ax.legend(fontsize=8,loc='upper right');ax.grid(alpha=.15)

fig.savefig(Path(__file__).stem+'.png',dpi=150,bbox_inches='tight',facecolor='white');plt.close(fig)
