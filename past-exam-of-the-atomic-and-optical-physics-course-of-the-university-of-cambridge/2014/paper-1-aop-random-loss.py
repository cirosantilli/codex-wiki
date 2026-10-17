from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

eta=1.684045883;nend=eta**(-2.5);n=np.linspace(nend,1,400);t=n**.4;f=1-1/(eta*t)
fig,ax=plt.subplots(1,2,figsize=(8.5,3.5),layout='constrained');ax[0].plot(n,t,lw=2);ax[1].plot(n,f,lw=2,color='#367c46')
for a in ax:a.axvline(nend,color='gray',ls=':');a.set(xlabel=r'$N/N_i$',xlim=(.23,1.03));a.grid(alpha=.2)
ax[0].set(ylabel=r'$T/T_i$',title=r'Unbiased loss: $T\propto N^{2/5}$');ax[0].annotate('loss',(.45,.45**.4),(.7,.92),arrowprops=dict(arrowstyle='->'),fontsize=10);ax[0].plot([nend],[1/eta],'o',color='#9e4a10');ax[0].text(.29,.61,'29.7 nK',fontsize=10)
ax[1].set(ylabel=r'$N_0/N$',title='Condensate depleted at the endpoint');ax[1].plot([nend],[0],'o',color='#9e4a10')

fig.savefig(Path(__file__).stem+'.png',dpi=140,facecolor='white')
