"""Original calculated figure. Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
The only output is a same-basename PNG in the current working directory.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':12,'axes.titlesize':14,'figure.facecolor':'white','axes.facecolor':'white','savefig.facecolor':'white'})

A=21.774193548387096;B=203.2258064516129;Fc=A*A/(4*B)
F=np.linspace(0,.95,1000);mask=F<=Fc
qplus=(A+np.sqrt(np.maximum(A*A-4*B*F[mask],0)))/2
qminus=(A-np.sqrt(np.maximum(A*A-4*B*F[mask],0)))/2
reverse=(A-np.sqrt(A*A+4*B*F))/2
fig,ax=plt.subplots(figsize=(8.4,4.9),layout='constrained')
ax.plot(F[mask],qplus,color='#126782',lw=2.5,label='Stable positive circulation')
ax.plot(F[mask],qminus,color='#a44418',lw=2.3,ls='--',label='Unstable positive circulation')
ax.plot(F,reverse,color='#62676d',lw=2.5,label='Stable reversed circulation')
ax.plot(.5,15,'o',color='#a44418');ax.annotate('Present state: 15 Sv',xy=(.5,15),xytext=(.10,18),arrowprops={'arrowstyle':'->','color':'#777777'},fontsize=11)
ax.plot(Fc,A/2,'o',color='#68468c');ax.annotate('Fold: 0.583 Sv',xy=(Fc,A/2),xytext=(.66,15.2),arrowprops={'arrowstyle':'->','color':'#777777'},fontsize=11)
ax.annotate('',xy=(Fc+.035,-4.7),xytext=(Fc+.035,9.8),arrowprops={'arrowstyle':'-|>','color':'#68468c','lw':1.7})
ax.text(Fc+.06,3.7,'Loss of positive\nsteady branch',fontsize=10,color='#68468c')
ax.axhline(0,color='#bbbbbb',lw=1);ax.set(xlabel='Freshwater forcing F (Sv)',ylabel='Signed overturning transport q (Sv)',xlim=(0,.95),ylim=(-8,24),title='Two-box steady roots with the stated freshwater convention')
ax.grid(alpha=.2);ax.legend(fontsize=10,loc='lower left')

fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name, dpi=140, facecolor='white', transparent=False)
plt.close(fig)
