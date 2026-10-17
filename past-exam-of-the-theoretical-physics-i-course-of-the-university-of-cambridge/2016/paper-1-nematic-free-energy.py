"""Original explanatory plot. Tested with Python 3.14, NumPy and Matplotlib.
Write the PNG basename into the current working directory (Make mirrors it).
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":11,"figure.facecolor":"white","axes.facecolor":"white"})
a=c=1.;bt=-np.sqrt(12);qt=1/np.sqrt(3)
fig,axs=plt.subplots(1,2,figsize=(9.3,3.9),layout='constrained');Q=np.linspace(-.17,1.,1200)
for b,color,label in [(0,'#337ab7','b = 0'),(-3.2,'#dd9c28','b = -3.2'),(bt,'#6e4591',r'$b=-\sqrt{12}$'),(-4,'#ba3939','b = -4')]:axs[0].plot(Q,a*Q**2+b*Q**3+3*c*Q**4,color=color,label=label)
axs[0].axhline(0,color='.5',lw=.6);axs[0].set(xlabel='Scalar order Q',ylabel='f / 6',title='Illustrative a = c = 1',ylim=(-.24,.3));axs[0].legend(fontsize=9);axs[0].grid(alpha=.15)
q=np.linspace(-.04,.66,1000);axs[1].plot(q,3*c*q**2*(q-qt)**2,color='#6e4591',lw=2);axs[1].scatter([0,qt],[0,0],color='#6e4591',zorder=3);axs[1].axhline(0,color='.6',lw=.6);axs[1].set(xlabel='Scalar order Q',ylabel='f / 6',title='Equal minima at coexistence');axs[1].annotate(r'$Q_t=1/\sqrt{3}$',xy=(qt,0),xytext=(.36,.013),arrowprops={'arrowstyle':'->'});axs[1].grid(alpha=.15)
fig.savefig('paper-1-nematic-free-energy.png',dpi=150,facecolor='white');plt.close(fig)
