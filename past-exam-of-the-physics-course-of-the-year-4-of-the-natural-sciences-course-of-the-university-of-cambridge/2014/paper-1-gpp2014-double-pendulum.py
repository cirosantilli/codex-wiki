"""Original educational plot; Python 3.14, NumPy and Matplotlib. Writes a basename PNG in the current working directory."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white'})
from matplotlib.patches import Circle
fig=plt.figure(figsize=(8.8,5.3),layout='constrained');gs=fig.add_gridspec(2,2,height_ratios=[1,1.15])
for j,(ratio,title) in enumerate([(2,r'Low mode: $\theta_2=2\theta_1$'),(-2,r'High mode: $\theta_2=-2\theta_1$')]):
 ax=fig.add_subplot(gs[0,j]);theta=.18
 for sgn,col,style in [(1,'#225c91','-'),(-1,'#9aa3aa','--')]:
  p1=np.array([np.sin(sgn*theta),-np.cos(theta)]);p2=p1+np.array([np.sin(sgn*ratio*theta),-np.cos(ratio*theta)])
  ax.plot([0,p1[0],p2[0]],[0,p1[1],p2[1]],style,color=col,lw=1.7)
  if sgn==1:
   ax.add_patch(Circle(p1,.085,facecolor=col));ax.add_patch(Circle(p2,.05,facecolor=col));ax.text(*(p1+np.array([.13,0])),'3m',va='center');ax.text(*(p2+np.array([.1,0])),'m',va='center')
 ax.plot([-.3,.3],[0,0],color='black',lw=4);ax.set(xlim=(-.8,.9),ylim=(-2.2,.2),aspect='equal',title=title);ax.axis('off')
ax=fig.add_subplot(gs[1,:]);t=np.linspace(0,35,5000);xx=(9*np.cos(t)-np.cos(np.sqrt(3)*t))/4;ax.plot(t,xx,color='#225c91',lw=1.2);ax.axhline(2.5,color='#b25424',ls='--');ax.axhline(-2.5,color='#b25424',ls='--');ax.text(1,2.6,'Supremum bound = 2.5',fontsize=9,color='#b25424');ax.scatter([0],[2],color='#225c91',s=20);ax.set(xlabel=r'$\omega_-t$',ylabel=r'$x_m/(\alpha\ell)$',xlim=(0,35),ylim=(-2.8,2.95),title='Equal-angle release excites both incommensurate modes');ax.grid(alpha=.2)
fig.savefig('paper-1-gpp2014-double-pendulum.png',dpi=150,facecolor='white');plt.close(fig)
