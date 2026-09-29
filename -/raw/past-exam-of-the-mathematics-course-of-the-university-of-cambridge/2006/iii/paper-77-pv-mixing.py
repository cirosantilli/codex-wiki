"""Original PV mixing profiles: Python 3.14 / NumPy 2.3.5 / matplotlib 3.10.7.
Writes paper-77-pv-mixing.png to caller CWD, honoring supplied MPLCONFIGDIR.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
a,L,S=1.,.08,1.
y=np.linspace(-2*a,2*a,1601);A=a/L;inside=np.abs(y)<=a
C=-S*L**2*(a+L)*np.exp(-A)
D=S*L**2/2*(a-L+(a+L)*np.exp(-2*A))
psi=np.empty_like(y);u=np.empty_like(y)
psi[inside]=S*L**2*y[inside]+C*np.sinh(y[inside]/L)
u[inside]=-S*L**2-C/L*np.cosh(y[inside]/L)
psi[~inside]=np.sign(y[~inside])*D*np.exp(-(np.abs(y[~inside])-a)/L)
u[~inside]=D/L*np.exp(-(np.abs(y[~inside])-a)/L)
fig,axes=plt.subplots(3,1,figsize=(7.2,7.1),dpi=150,sharex=True,facecolor='white')
axes[0].plot([-2,-1], [0,0],color='#75418f',lw=2);axes[0].plot([-1,1],[1,-1],color='#75418f',lw=2);axes[0].plot([1,2],[0,0],color='#75418f',lw=2)
axes[0].plot([-1,-1],[0,1],'--',color='#75418f',lw=1);axes[0].plot([1,1],[-1,0],'--',color='#75418f',lw=1)
axes[1].plot(y/a,u/(S*L*a),color='#286a9b',lw=2)
# zeta/(epsilon*a) = psi/(S*L^2*a), since L^2=gH/f^2.
axes[2].plot(y/a,psi/(S*L**2*a),color='#a95128',lw=2)
for ax in axes:
 ax.axvspan(-1,1,color='#e8e8e8',alpha=.5);ax.axhline(0,color='#999',lw=.8);ax.axvline(-1,color='#aaa',lw=.7);ax.axvline(1,color='#aaa',lw=.7);ax.grid(alpha=.12);ax.set_xlim(-2,2)
axes[0].set_ylabel('PV change / (S a)');axes[0].set_title('PV mixing over the finite slope')
axes[1].set_ylabel('u / (S L a)');axes[1].set_title('Central return flow and narrow positive edge jets')
axes[2].set_ylabel('Surface elevation / (epsilon a)');axes[2].set_xlabel('y / a');axes[2].set_title('Surface follows the bottom centrally and decays outside')
fig.suptitle('Small deformation radius: L / a = 0.08, f > 0',fontsize=12)
fig.tight_layout(rect=(0,0,1,.96));fig.savefig(Path('paper-77-pv-mixing.png'),facecolor='white',transparent=False);plt.close(fig)
