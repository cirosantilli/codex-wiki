"""Original covariance ellipses and pure-loss quadrature variances. Output cwd."""
import numpy as np
import matplotlib.pyplot as plt
r=.7;theta=np.linspace(0,2*np.pi,400);fig,ax=plt.subplots(1,2,figsize=(9,3.5),layout='constrained')
for name,vx,vy,style in [('Vacuum',.25,.25,'--'),('Pure squeezed',np.exp(-2*r)/4,np.exp(2*r)/4,'-'),('50% transmission',(.5*np.exp(-2*r)+.5)/4,(.5*np.exp(2*r)+.5)/4,'-')]:
 ax[0].plot(np.sqrt(vx)*np.cos(theta),np.sqrt(vy)*np.sin(theta),style,label=name)
ax[0].set(xlabel='X quadrature',ylabel='Y quadrature',title='One-standard-deviation covariance contours',aspect='equal');ax[0].legend(fontsize=8);ax[0].grid(alpha=.2)
eta=np.linspace(0,1,300);ax[1].plot(eta,eta*np.exp(-2*r)+(1-eta),label='Quiet-axis variance / vacuum');ax[1].plot(eta,eta*np.exp(2*r)+(1-eta),label='Noisy-axis variance / vacuum');ax[1].axhline(1,ls='--',color='.5');ax[1].set(xlabel='Intensity transmission',ylabel='Variance / vacuum variance',title='Loss introduces independent vacuum noise');ax[1].legend(fontsize=8);ax[1].grid(alpha=.2)
fig.savefig('paper-1-squeezing-ellipse.png',dpi=150,facecolor='white')
