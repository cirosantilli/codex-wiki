"""Original educational diagram; Python 3.14, NumPy and Matplotlib. Saves a basename PNG to the current working directory."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white'})
k=np.linspace(-1.6,1.6,600);fig,axs=plt.subplots(1,2,figsize=(8.8,3.7),layout='constrained')
for gap,col,label in [(3.,'#225c91',r'$H=0$'),(1.,'#b25424',r'$H=H_g$'),(0.,'#388773',r'$H=H_c=H_g+\nu n/\eta$')]:axs[0].plot(k,k*k+gap,color=col,label=label)
axs[0].set(xlabel=r'$k\hbar/\sqrt{2m\nu n}$',ylabel=r'$\epsilon/(\nu n)$',ylim=(-.1,5.8),title=r'Fixed reference n; illustrative $\eta H_g/(\nu n)=2$');axs[0].legend(fontsize=9);axs[0].grid(alpha=.2)
t=np.linspace(0,1.5,600);boundary=t**1.5;axs[1].fill_between(t,boundary,2.4,color='#dbebe5');axs[1].fill_between(t,0,boundary,color='#e9eff7');axs[1].plot(t,boundary,color='#388773',lw=2);axs[1].text(.45,1.8,'Condensed',ha='center');axs[1].text(1.1,.35,'Normal',ha='center');axs[1].text(.58,.82,r'$H_c-H_g\propto T^{3/2}$',rotation=36,fontsize=10)
axs[1].set(xlabel='Temperature / reference scale',ylabel=r'$(H-H_g)$ / reference field scale',xlim=(0,1.5),ylim=(0,2.4),title='Dilute low-temperature phase boundary');axs[1].grid(alpha=.2)
fig.savefig('paper-1-tsp2014-triplons.png',dpi=150,facecolor='white');plt.close(fig)
