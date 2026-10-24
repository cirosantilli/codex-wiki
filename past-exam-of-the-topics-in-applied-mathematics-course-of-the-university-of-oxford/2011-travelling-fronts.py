"""Original exact-front comparison; output CWD. Python3.14.4/numpy2.3.5/matplotlib3.10.7."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig,axes=plt.subplots(1,2,figsize=(10,3.7),layout='constrained',facecolor='white');z=np.linspace(-20,20,1200)
for q in [.5,1,2,4,8]:
 a=2**(q/2)-1;b=q/np.sqrt(2*(q+2));u=(1+a*np.exp(b*z))**(-2/q);axes[0].plot(z,u,label=f'q={q:g}')
axes[0].set(xlabel='Moving coordinate z (half heights aligned)',ylabel='Population U',title='Unequal changes in the two tails');axes[0].legend(fontsize=8)
q=np.linspace(.01,12,500);axes[1].plot(q,(q+4)/np.sqrt(2*(q+2)),lw=2,label='Explicit-front speed');axes[1].axhline(2,color='gray',ls='--',label='Minimum admissible speed');axes[1].set(xlabel='q',ylabel='Wave speed c',title='Speed increases with q');axes[1].legend(fontsize=8)
for ax in axes:ax.grid(alpha=.2);ax.set_facecolor('white')
fig.savefig('2011-travelling-fronts.png',dpi=140,facecolor='white');plt.close(fig)
