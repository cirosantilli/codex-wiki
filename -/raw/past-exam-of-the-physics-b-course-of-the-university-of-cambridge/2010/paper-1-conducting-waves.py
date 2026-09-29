import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False,'figure.facecolor':'white','savefig.facecolor':'white'})

fig,ax=plt.subplots(2,2,figsize=(10,7),layout='constrained')
x=np.linspace(.02,3,1200);above=x>=1;below=~above
ax[0,0].plot(x[above],np.sqrt(x[above]**2-1),label=r'Re$(k)c/\omega_p$');ax[0,0].plot(x[below],np.sqrt(1-x[below]**2),label=r'Im$(k)c/\omega_p$');ax[0,0].axvline(1,color='.6',ls=':');ax[0,0].set(xlabel=r'$\omega/\omega_p$',ylabel='Scaled wave number',title='Collisionless plasma: cutoff and penetration');ax[0,0].legend(fontsize=9)
x=np.linspace(1.015,3,700);s=np.sqrt(1-1/x**2);ax[0,1].plot(x,1/s,label=r'$v_p/c$');ax[0,1].plot(x,s,label=r'$v_g/c$');ax[0,1].axhline(1,color='.6',ls=':');ax[0,1].set(xlabel=r'$\omega/\omega_p$',ylabel='Velocity / c',title='Transparent collisionless regime',ylim=(0,6));ax[0,1].legend(fontsize=9)
z=np.linspace(0,4,700);ax[1,0].plot(z,np.exp(-z)*np.cos(z),label='Instantaneous field');ax[1,0].plot(z,np.exp(-z),'--',label='Amplitude envelope');ax[1,0].plot(z,np.exp(-2*z),':',lw=2,label='Intensity ratio');ax[1,0].set(xlabel=r'Depth / $\delta$',ylabel='Normalized response',title='Good conductor: amplitude versus intensity');ax[1,0].legend(fontsize=8)
x=np.linspace(.2,10,700);metal=.01*np.sqrt(x);dielectric=.01*x;ax[1,1].plot(x,metal,label='Chosen conductor loss');ax[1,1].plot(x,dielectric,label='Chosen dielectric loss');ax[1,1].plot(x,metal+dielectric,'k--',label='Sum');ax[1,1].set(xlabel='Frequency / chosen reference',ylabel='Amplitude attenuation / chosen unit',title='Low-loss line: separate loss mechanisms');ax[1,1].legend(fontsize=8)
fig.suptitle('Original response models; distinct physical limits, no measured material data',fontsize=12)
fig.savefig('paper-1-conducting-waves.png',dpi=155)
