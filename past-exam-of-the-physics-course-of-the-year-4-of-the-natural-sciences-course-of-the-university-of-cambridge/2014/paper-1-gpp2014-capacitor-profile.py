"""Original educational plot; Python 3.14, NumPy and Matplotlib. Writes a basename PNG in the current working directory."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white'})
r=np.linspace(0,1,800);x=np.pi*r;term=np.ones_like(x);J=term.copy()
for k in range(1,55):term*=(-x*x/4)/(k*k);J+=term
fig,ax=plt.subplots(figsize=(7,4),layout='constrained');ax.plot(r,np.ones_like(r),ls='--',color='#b25424',label=r'Quasistatic $\omega a/c\ll1$');ax.plot(r,J,color='#225c91',lw=2,label=r'Ideal interior: $J_0(\pi r/a)$');ax.axhline(0,color='#777',lw=.8);zero=2.404825557695773/np.pi;ax.scatter([zero,1],[0,J[-1]],color='#225c91',s=23)
ax.annotate('First zero at r/a = 0.765',xy=(zero,0),xytext=(.23,.23),arrowprops={'arrowstyle':'->','color':'#777'},fontsize=10);ax.annotate('Edge has opposite phase: -0.304',xy=(1,J[-1]),xytext=(.27,-.34),arrowprops={'arrowstyle':'->','color':'#777'},fontsize=10)
ax.set(xlabel='Radius r/a',ylabel=r'$E_z(r,t)/E_z(0,t)$',xlim=(0,1.03),ylim=(-.5,1.15),title='Axisymmetric thin-capacitor model at fixed nonzero sine phase');ax.legend(fontsize=9,loc='upper right');ax.grid(alpha=.2)
fig.savefig('paper-1-gpp2014-capacitor-profile.png',dpi=150,facecolor='white');plt.close(fig)
