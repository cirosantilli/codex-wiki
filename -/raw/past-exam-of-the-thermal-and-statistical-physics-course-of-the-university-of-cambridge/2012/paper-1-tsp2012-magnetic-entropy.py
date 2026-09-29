import numpy as np
import matplotlib.pyplot as plt
t=np.geomspace(.07,5,600);xgap=1/t;exp=np.exp(-xgap);C=xgap*xgap*exp/(1+exp)**2
fig,axes=plt.subplots(1,2,figsize=(9.3,4.1),layout='constrained')
axes[0].semilogx(t,C,color='#2475aa',lw=2.4);axes[0].set(xlabel=r'$k_BT/\delta$',ylabel=r'$c/k_B$',title='Nondegenerate two-level Schottky peak');axes[0].grid(alpha=.2)
x=np.linspace(0,3.5,600)
for J,col in [(.5,'#2475aa'),(1,'#c94a39'),(2,'#8f59a4')]:
 m=np.arange(-J,J+1);weights=np.exp(x[:,None]*m);Z=weights.sum(axis=1);s=np.log(Z)-x*(weights@m)/Z
 axes[1].plot(x,s/np.log(2*J+1),color=col,label=rf'$J={J:g}$')
 small=x<=min(1,1/J);axes[1].plot(x[small],1-J*(J+1)*x[small]**2/(6*np.log(2*J+1)),color=col,ls='--',alpha=.6)
axes[1].set(xlabel=r'$x=g\mu_BB/(k_BT)$',ylabel=r'$s/[k_B\ln(2J+1)]$',title='Solid: exact entropy; dashed: small-field limit',ylim=(0,1.04));axes[1].legend(frameon=False);axes[1].grid(alpha=.2)
fig.savefig('paper-1-tsp2012-magnetic-entropy.png',dpi=150,facecolor='white')
