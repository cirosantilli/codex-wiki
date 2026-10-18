from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11})
fig,axs=plt.subplots(1,2,figsize=(10,4),layout='constrained',facecolor='white')
p=np.linspace(0,1,801)
for L,color in [(1,'#777777'),(10,'#126782'),(100,'#b14c2e')]:
 post=p*L/(p*L+1-p);axs[0].plot(p,post,color=color,label=f'Bayes factor {L}')
axs[0].plot(.01,10/109,'o',color='#126782');axs[0].annotate('Prior 0.01\nPosterior 0.0917',(.01,10/109),(.15,.2),arrowprops={'arrowstyle':'->'},fontsize=10)
axs[0].set(xlabel='Prior probability',ylabel='Posterior probability',xlim=(0,1),ylim=(0,1),title='Support is not the same as certainty');axs[0].legend(loc='lower right',fontsize=9);axs[0].grid(alpha=.2)
x=np.linspace(-1.4,1.4,701);observed=np.array([-1.,-1/3,1/3,1.]);base=lambda x:1+.5*x;product=lambda x:np.prod(x[...,None]-observed,axis=-1)
for coefficient,color in [(-1.5,'#b14c2e'),(0,'#126782'),(1.5,'#7a5195')]:axs[1].plot(x,base(x)+coefficient*product(x),color=color,label=f'Coefficient {coefficient:g}')
axs[1].scatter(observed,base(observed),color='black',s=32,zorder=5,label='Same four observations');axs[1].set(xlabel='Input x (illustrative units)',ylabel='Response (illustrative units)',title='Finite agreement leaves other predictions');axs[1].grid(alpha=.2);axs[1].legend(loc='upper left',fontsize=9)
fig.suptitle('Chosen mathematical examples; no experimental or historical data',fontsize=11)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white',transparent=False,metadata={'Software':'Matplotlib'})
plt.close(fig)
