"""Qualitative mass-radius sequence, not an evolutionary fit.
Python 3.14 and root dependencies; write only basename PNG in cwd.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
m=np.array([.02,.03,.054,.3,1,3,10,30,75,90,150,300])
r=np.array([.27,.32,.35,.84,1.,1.1,1.,.87,.8,.94,1.5,3.])
x=np.geomspace(m[0],m[-1],600)
y=np.exp(np.interp(np.log(x),np.log(m),np.log(r)))
fig,ax=plt.subplots(figsize=(8.6,4.6),dpi=100,facecolor='white')
ax.loglog(x,y,color='#245786',lw=2.8,label='Joined schematic; age and composition dependent')
for (a,b,label,color) in [(.02,.08,'Ice giants','#c8dced'),(.08,13,'Gas giants','#d4e8dc'),(13,75,'Brown dwarfs','#eddec6'),(75,300,'Low-mass stars','#ecd0d0')]:
 ax.axvspan(a,b,color=color,alpha=.35);ax.text(np.sqrt(a*b),3.85,label,ha='center',fontsize=9)
for value,label in [(13,'Deuterium threshold'),(75,'Sustained H burning')]:
 ax.axvline(value,color='#999999',ls=':',lw=1);ax.text(value,.22,label,ha='right',va='bottom',rotation=90,fontsize=8)
q=np.geomspace(.025,.17,70);ax.loglog(q,.31*(q/.025)**(1/3),'--',color='#476c43',lw=1.7);ax.text(.045,.64,r'$R\propto M^{1/3}$',fontsize=10)
q=np.geomspace(.6,5,50);ax.loglog(q,np.full_like(q,1.3),'--',color='#476c43',lw=1.7);ax.text(.9,1.45,r'$R\propto M^0$',fontsize=10)
q=np.geomspace(15,55,50);ax.loglog(q,1.18*(q/15)**(-1/3),'--',color='#a36131',lw=1.7);ax.text(9.5,1.55,r'$R\propto M^{-1/3}$',fontsize=10);ax.text(12,1.32,'Cold degeneracy limit',fontsize=8)
q=np.geomspace(90,270,50);ax.loglog(q,.011*q,'--',color='#944444',lw=1.7);ax.text(120,2.5,r'$R\propto M$',fontsize=10)
ax.set(xlabel='Mass / Jupiter mass',ylabel='Radius / Jupiter radius',xlim=(.02,300),ylim=(.2,4.3),title='Compression, degeneracy and the onset of sustained fusion')
ax.grid(alpha=.16,which='both');ax.legend(loc='lower left',fontsize=8);ax.set_facecolor('white');fig.tight_layout()
fig.savefig(Path.cwd()/'paper-59-mass-radius.png',dpi=100,facecolor='white',transparent=False)
plt.close(fig)
