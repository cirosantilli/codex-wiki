from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
x=2**(-2/3);q=np.array([2.5,1.5*(x-2),0]);work=np.array([1.,0.,-1.5*(1-x)]);sg=np.array([2.5*np.log(2),-2.5*np.log(2),0]);sr=np.array([-1.,-2*q[1],0]);st=sg+sr
fig,ax=plt.subplots(1,2,figsize=(9.4,3.6),layout='constrained');v=np.arange(3)
ax[0].bar(v-.18,q,.35,label='heat into gas',color='#2469a0');ax[0].bar(v+.18,work,.35,label='work by gas',color='#9e4a10');ax[0].set(ylabel=r'energy / $(p_1V_1)$',title='Net work is the heat balance');ax[0].legend(fontsize=9)
ax[1].bar(v-.24,sg,.23,label='gas',color='#2469a0');ax[1].bar(v,sr,.23,label='reservoir',color='#9e4a10');ax[1].bar(v+.24,st,.23,label='total',color='#367c46');ax[1].set(ylabel=r'entropy change / $(p_1V_1/T_1)$',title='Finite-temperature contacts generate entropy');ax[1].legend(fontsize=9)
for a in ax:a.set_xticks(v,['1 to 2','2 to 3','3 to 1']);a.axhline(0,color='black',lw=.8);a.grid(axis='y',alpha=.2)
fig.savefig(Path(__file__).stem+'.png',dpi=140,facecolor='white')
