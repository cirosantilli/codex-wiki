"""Original solution diagram; Python 3.14.4, numpy 2.3.5, matplotlib 3.10.7.
Run from the mirrored _media directory; the output is a basename in cwd.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'figure.facecolor':'white','axes.spines.top':False,'axes.spines.right':False})

p=np.linspace(0,2*np.pi,1000);psi=np.where(p<=np.pi,np.sqrt(8/(3*np.pi))*np.sin(p)**2,0);ms=np.arange(-7,8);P=np.zeros(len(ms))
for i,m in enumerate(ms):
 if m==0:P[i]=1/3
 elif abs(m)==2:P[i]=1/12
 elif m%2:P[i]=64/(3*np.pi**2*m*m*(m*m-4)**2)
fig,axs=plt.subplots(1,2,figsize=(8.5,3.7));axs[0].plot(p/np.pi,psi,lw=2);axs[0].set(xlabel='Angular position φ/π',ylabel='ψ(φ)',title='Real half-ring wavefunction');axs[0].grid(alpha=.2);axs[1].bar(ms,P,color='steelblue');axs[1].set(xlabel='Angular momentum / ℏ',ylabel='Measurement probability',title='Symmetric probabilities, zero mean');axs[1].set_xticks([-6,-4,-2,0,2,4,6]);fig.tight_layout()

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
