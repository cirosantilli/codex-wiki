"""Original schematic; writes only to the current working directory.
Tested: Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({'font.size': 10, 'axes.spines.top': False, 'axes.spines.right': False})

fig,ax=plt.subplots(figsize=(10,4.5),dpi=100)
m=np.geomspace(.03,300,500)
r=np.exp(np.interp(np.log(m),np.log([.03,.1,.3,1,4,13,80,150,300]),np.log([.35,.55,.83,1.05,1.1,1,.8,1.4,2.8])))
ax.loglog(m,r,color='#263e69',lw=2.7,label='Schematic cooled sequence (composition varies)')
for mass,label in [(13,'Deuterium ignition\n~13 $M_J$'),(80,'Hydrogen fusion\n~80 $M_J$')]:
 ax.axvline(mass,color='.55',ls=':',lw=1);ax.text(mass*1.10 if mass==13 else 310,.32,label,fontsize=9,va='bottom',ha='left' if mass==13 else 'right')
for mm,rr,txt,x,y in [(np.geomspace(.04,.2,40),.65*(np.geomspace(.04,.2,40)/.1)**(1/3),r'$R\propto M^{1/3}$',.037,.9),(np.geomspace(.7,6,40),np.full(40,1.4),r'$R\propto M^0$',.8,1.52),(np.geomspace(15,65,40),1.8*(np.geomspace(15,65,40)/15)**(-1/3),r'$R\propto M^{-1/3}$',14,2.02),(np.geomspace(110,230,40),.011*np.geomspace(110,230,40),r'$R\sim M$',120,2.85)]:
 ax.plot(mm,rr,'--',color='#a65333',lw=1.5);ax.text(x,y,txt,color='#a65333',fontsize=11)
for x,y,txt in [(.07,.37,'Ice giants'),(1,.72,'Gas giants'),(24,.68,'Brown dwarfs'),(150,.68,'Low-mass stars')]: ax.text(x,y,txt,ha='center',fontsize=10)
ax.set_ylim(.28,4);ax.set_xlim(.027,340);ax.set_xlabel(r'Mass / Jupiter mass');ax.set_ylabel(r'Radius / Jupiter radius')
ax.set_title('Mass-radius sequence and limiting slope guides',pad=10);ax.grid(which='major',alpha=.17)
ax.legend(loc='upper left',frameon=False,fontsize=9)
fig.text(.52,.015,'Illustrative low-entropy sequence, not an equation-of-state fit; young objects can be larger.',ha='center',fontsize=9)
fig.subplots_adjust(left=.085,right=.98,bottom=.16,top=.86)

fig.savefig(Path.cwd() / 'paper-315-mass-radius.png', dpi=100, facecolor='white', transparent=False)
plt.close(fig)
