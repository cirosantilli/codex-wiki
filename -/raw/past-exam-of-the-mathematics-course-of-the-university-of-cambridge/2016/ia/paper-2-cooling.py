"""Draw the original cooling sketch. Run from the output directory.
Tested with Python 3.14.4, matplotlib 3.10.7 and NumPy 2.3.5.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
alpha,beta=4.,3.
t1=np.log(2*(alpha-1)/(alpha-2))
a=np.linspace(0,t1,240);b=np.linspace(t1,6.2,500)
fig,ax=plt.subplots(figsize=(6.8,3.5),dpi=120,facecolor='white');ax.set_facecolor('white')
ax.plot(a,1+(alpha-1)*np.exp(-a),color='#196b9c',lw=2.5)
ax.plot(b,1+(alpha/2-1+beta)*np.exp(-(b-t1)),color='#196b9c',lw=2.5)
ax.plot([t1,t1],[alpha/2,alpha/2+beta],':',color='#d06928',lw=1.7)
ax.scatter([t1],[alpha/2],facecolors='white',edgecolors='#196b9c',s=35,zorder=4)
ax.scatter([t1],[alpha/2+beta],color='#196b9c',s=35,zorder=4)
ax.annotate('$\\beta/T_0$',xy=(t1,3.5),xytext=(t1+.24,3.5),fontsize=11)
ax.axhline(1,color='#888',ls='--',lw=1)
ax.axhline(alpha,color='#bbb',ls=':',lw=.8)
ax.set(xlim=(0,6.2),ylim=(.7,5.4),xlabel='$kt$',ylabel='$T/T_0$')
ax.set_xticks([0,t1,3,6],['0','$kt_1$','3','6'])
ax.set_yticks([1,2,4,5],['1','$\\alpha/2$','$\\alpha$','$\\alpha/2+\\beta/T_0$'])
ax.spines[['top','right']].set_visible(False)
fig.subplots_adjust(left=.2,right=.97,bottom=.18,top=.94)
fig.savefig('paper-2-cooling.png',facecolor='white',transparent=False)
plt.close(fig)
