"""Original side-view free-body diagram and exact ideal rail oscillator. Output cwd."""
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({"axes.titlesize":10,"axes.labelsize":10})
fig,ax=plt.subplots(1,2,figsize=(9,3.5),layout='constrained');a=ax[0];theta=np.deg2rad(25);tt=np.array([np.cos(theta),-np.sin(theta)]);nn=np.array([np.sin(theta),np.cos(theta)]);q=np.linspace(-1.3,1.3,2);a.plot(q*tt[0],q*tt[1],color='.3',lw=3);a.scatter([0],[0],color='k',s=70,zorder=4)
for vec,label,col in [(np.array([0,-1]),'mg','#b33b3b'),(np.array([-0.65,0]),'I l B','#3569ac'),((np.cos(theta)+.65*np.sin(theta))*nn,'N','#008261')]:
 a.annotate('',xy=vec,xytext=(0,0),arrowprops=dict(arrowstyle='->',lw=2,color=col));a.text(*(vec*1.08),label,color=col,ha='center',va='center')
a.annotate('',xy=(1.1,.8),xytext=(1.1,.25),arrowprops=dict(arrowstyle='->',lw=2,color='.3'));a.text(1.1,.9,'vertical B',ha='center',fontsize=9);a.text(.8,-.5,'downhill s',fontsize=9);a.set(xlim=(-1.4,1.6),ylim=(-1.3,1.3),aspect='equal',title='Forces on the sliding rod');a.axis('off')
t=np.linspace(0,2*np.pi,400);ax[1].plot(t/np.pi,1-np.cos(t),lw=2);ax[1].axhline(1,color='.5',ls='--',label='Force-free position');ax[1].scatter([1],[2],color='#b33b3b');ax[1].set(xlabel=r'$\omega_Bt/\pi$',ylabel=r'$s/s_e$',title='First turning point at twice equilibrium');ax[1].legend();ax[1].grid(alpha=.2)
fig.savefig('paper-1-inductive-rails.png',dpi=150,facecolor='white')
