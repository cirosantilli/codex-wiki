"""Original model illustrations; tested Python 3.14.4, numpy 2.3.5, matplotlib 3.10.7.
Dependencies are in the repository pyproject.toml. Writes all PNGs to the output CWD.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'figure.facecolor':'white','axes.facecolor':'white','font.size':10})
fig,axes=plt.subplots(1,3,figsize=(11,3.6),layout='constrained')
x=np.linspace(0,5,500);axes[0].plot(x,x**(1/3),ls='--',label='No cavities');axes[0].plot(x,x**(1/3)/(1+.5*x),label='A cavity-weakening bed');axes[0].set(xlabel=r'$u/N^n$',ylabel=r'$\tau/N=f(u/N^n)$',title='Qualitative sliding laws');axes[0].legend(fontsize=8)
q=np.linspace(.1,4,300);axes[1].plot(q,.6+.65*np.sqrt(q),label=r'$N_R(Q)$');axes[1].plot(q,2.5/(1+.45*q),label=r'$N_K(Q)$');axes[1].set(xlabel='Water flux Q',ylabel='Effective pressure N',title='Opposite drainage feedbacks');axes[1].legend(fontsize=8)
qr=np.linspace(.4,1.6,200);nr=1+1.2*(qr-1);nk=1+.4*(qr-1);axes[2].plot(qr,nr,label=r'$N_R(Q_R)$');axes[2].plot(qr,nk,label=r'$N_K(Q-Q_R)$');axes[2].scatter([1],[1],color='black',s=20);axes[2].annotate('less channel flux',xy=(.65,.56),xytext=(1.0,.35),arrowprops={'arrowstyle':'->'},fontsize=8);axes[2].fill_between(qr,nr,nk,where=qr<1,alpha=.15,color='#d07b20');axes[2].set(xlabel='Channel flux QR (total Q fixed)',ylabel='Equilibrium effective pressure',title='Channel-loss instability');axes[2].legend(fontsize=8)
for ax in axes:ax.grid(alpha=.2)
fig.suptitle('Schematic basal sliding and subglacial drainage',fontsize=12);fig.savefig('2011-cavitation-drainage.png',dpi=140,facecolor='white');plt.close(fig)
