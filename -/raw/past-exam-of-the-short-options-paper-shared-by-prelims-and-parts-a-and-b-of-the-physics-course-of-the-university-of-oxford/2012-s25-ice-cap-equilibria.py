"""Original plots of the supplied idealized ice model; Celsius reciprocal law.
Python 3.14, numpy 2.3.5, matplotlib 3.10.7. Writes only CWD basename PNG.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
alpha=4.43;beta=.2;Gamma=6;s=275-273.15
crit=Gamma/beta-2*np.sqrt(alpha*Gamma/beta)
fig,axs=plt.subplots(1,2,figsize=(10.2,3.9),layout='constrained',facecolor='white')
z=np.linspace(s/Gamma+.025,5,700);gain=1-beta*z;loss=alpha/(Gamma*z-s)
a=axs[0];a.plot(z,gain,label='Snow gain',lw=2,color='#27678e');a.plot(z,loss,label='Melt loss at 275 K',lw=2,color='#b96129')
roots=np.roots([-beta*Gamma,Gamma+beta*s,-s-alpha]);a.plot(roots,1-beta*roots,'o',color='#333333');a.annotate('Unstable',xy=(roots.min(),1-beta*roots.min()),xytext=(.65,.91),arrowprops=dict(arrowstyle='->'));a.annotate('Stable',xy=(4,.2),xytext=(3.4,.47),arrowprops=dict(arrowstyle='->'))
a.set(xlabel='Ice-top altitude z (km)',ylabel='Normalized gain or loss rate',xlim=(0,5),ylim=(0,1));a.legend(loc='upper right',fontsize=9);a.grid(alpha=.2)
b=axs[1];sea=np.linspace(s,crit,600);disc=(Gamma-beta*sea)**2-4*alpha*beta*Gamma;disc=np.maximum(disc,0);high=(Gamma+beta*sea+np.sqrt(disc))/(2*beta*Gamma);low=(Gamma+beta*sea-np.sqrt(disc))/(2*beta*Gamma)
b.plot(sea+273.15,high,label='Stable equilibrium',lw=2);b.plot(sea+273.15,low,'--',label='Unstable equilibrium',lw=2);fold=(Gamma+beta*crit)/(2*beta*Gamma);b.plot([crit+273.15],[fold],'o',color='#b96129');b.axvline(crit+273.15,color='#888888',lw=1,ls=':');b.annotate('Fold; equilibria disappear',xy=(crit+273.15,fold),xytext=(275.5,3.05),arrowprops=dict(arrowstyle='->'),fontsize=9)
b.set(xlabel='Sea-level temperature (K)',ylabel='Equilibrium height (km)',xlim=(275,281),ylim=(1,4.4));b.legend(fontsize=9);b.grid(alpha=.2)
fig.savefig('2012-s25-ice-cap-equilibria.png',dpi=150,facecolor='white',metadata={'Software':'Matplotlib'})
