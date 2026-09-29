"""Local bifurcations; Python 3.14, numpy 2.3.5, matplotlib 3.10.7.
Writes paper-4-bifurcations.png to CWD and preserves caller MPLCONFIGDIR.
"""
import os
import tempfile
if 'MPLCONFIGDIR' not in os.environ:
    os.environ['MPLCONFIGDIR']=tempfile.mkdtemp(prefix='paper-4-bifurcations-mpl-')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
fig,axs=plt.subplots(1,2,figsize=(9.3,3.8),layout='constrained',facecolor='white')
m=np.linspace(-.4,0,300);p=np.linspace(0,.4,300)
ax=axs[0]
ax.plot(m,np.zeros_like(m),'--',color='#a43e32',label='Unstable')
ax.plot(p,np.zeros_like(p),color='#18643e',label='Stable')
for sign in [-1,1]:ax.plot(m,sign*np.sqrt(-m/2),color='#18643e')
ax.set_xlabel(r'$\nu=\mu-1$');ax.set_ylabel(r'$Y=y$')
ax.set_title('Supercritical pitchfork towards smaller mu')
ax=axs[1]
ax.plot(m,np.zeros_like(m),color='#18643e',label='Stable')
ax.plot(p,np.zeros_like(p),'--',color='#a43e32',label='Unstable')
ax.plot(m,m/2,'--',color='#a43e32');ax.plot(p,p/2,color='#18643e')
ax.set_xlabel(r'$\nu=\mu+1$');ax.set_ylabel(r'$X=x$')
ax.set_title('Transcritical exchange of stability')
for ax in axs:
    ax.set_facecolor('white');ax.axvline(0,color='gray',lw=.6);ax.grid(alpha=.2);ax.legend(fontsize=9)
fig.savefig('paper-4-bifurcations.png',dpi=150,facecolor='white',transparent=False)
plt.close(fig)
