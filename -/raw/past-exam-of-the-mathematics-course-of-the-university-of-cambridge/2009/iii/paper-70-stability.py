"""Sketch quintic amplitude existence/stability; Python 3.14, numpy 2.3.5, matplotlib 3.10.7.
Writes paper-70-stability.png to the caller's working directory.
"""
import os
import tempfile
if 'MPLCONFIGDIR' not in os.environ:
    os.environ['MPLCONFIGDIR'] = tempfile.mkdtemp(prefix='paper-70-mpl-')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

mu=np.linspace(-.25,2.5,1000)
x_upper=(1+np.sqrt(1+4*mu))/2
x_lower=np.maximum((1-np.sqrt(1+4*mu))/2,0)
x_e=(3+np.sqrt(9+32*mu))/8
q_exist=np.sqrt(np.maximum(mu+.25,0))
q_e=np.sqrt(np.maximum((16*mu+3+np.sqrt(9+32*mu))/32,0))
fig,axes=plt.subplots(1,2,figsize=(10.8,4.4),layout='constrained',facecolor='white')
for ax in axes:
    ax.set_facecolor('white')
    ax.set_xlim(-.37,2.5)
    ax.grid(alpha=.2)
    ax.set_xlabel(r'$\mu/\alpha^2$')
ax=axes[0]
ax.fill_between(mu,np.sqrt(x_lower),np.sqrt(x_upper),color='#dedede',label='Nonzero waves exist')
ax.fill_between(mu,np.sqrt(x_e),np.sqrt(x_upper),color='#8ed7b0',label='Stable upper waves')
ax.plot(mu,np.sqrt(x_upper),color='#333333',lw=1.7,label=r'Existence edge: $Q=0$')
ax.plot(mu,np.sqrt(x_lower),color='#333333',lw=1.2)
ax.plot(mu,np.sqrt(x_e),color='#156948',lw=1.8,linestyle='--',label='Marginal Eckhaus edge')
ax.plot(-.25,1/np.sqrt(2),'ko',ms=4)
ax.set_ylim(0,1.68)
ax.set_ylabel(r'$R/\sqrt{\alpha}$')
ax.set_title('Amplitude and control parameter')
ax.legend(loc='lower right',fontsize=8,framealpha=.95)
ax=axes[1]
ax.fill_between(mu,-q_exist,q_exist,color='#dedede',label='Nonzero waves exist')
ax.fill_between(mu,-q_e,q_e,color='#8ed7b0',label='Stable upper waves')
for sign in [-1,1]:
    ax.plot(mu,sign*q_exist,color='#333333',lw=1.5,label='Existence edge' if sign==1 else None)
    ax.plot(mu,sign*q_e,color='#156948',lw=1.8,linestyle='--',label='Marginal Eckhaus edge' if sign==1 else None)
ax.plot(-.25,0,'ko',ms=4)
ax.set_ylim(-1.73,1.73)
ax.set_ylabel(r'$Q/\alpha$')
ax.set_title('Detuning and control parameter')
ax.legend(loc='lower right',fontsize=8,framealpha=.95)
fig.suptitle('Quintic amplitude equation: existence and phase stability',fontsize=13)
fig.savefig('paper-70-stability.png',dpi=150,facecolor='white',transparent=False)
plt.close(fig)
