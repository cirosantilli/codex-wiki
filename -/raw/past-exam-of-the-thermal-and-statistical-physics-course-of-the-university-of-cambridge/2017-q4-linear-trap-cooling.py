"""Classical linear-trap entropy curves and reversible cooling; Python 3.14, numpy, matplotlib.

Write the PNG basename to the current working directory.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

T=np.linspace(.5,1.6,500)
base=np.log(1e4)+5.5
entropy=lambda temperature,strength:base+4.5*np.log(temperature)-3*np.log(strength)
fig,ax=plt.subplots(figsize=(6.8,4.5),layout='constrained',facecolor='white')
ax.set_facecolor('white')
for strength,color in [(1,'#165b99'),(2,'#cc7a1d')]:
    ax.plot(T,entropy(T,strength),lw=2,color=color,label=fr'$a/a_*= {strength}$')
Ti=1.;Tf=2**(-2/3);S=entropy(Ti,2)
ax.scatter([Tf,Ti],[S,S],color='#333333',s=25,zorder=4)
ax.annotate('',xy=(Tf,S),xytext=(Ti,S),arrowprops={'arrowstyle':'->','lw':1.7,'color':'#333333'})
ax.text(.82,S+.25,'Reversible decompression',ha='center',fontsize=9)
ax.text(.82,S-.55,r'$T_f/T_i=2^{-2/3}$',ha='center',fontsize=11)
ax.set(xlim=(.5,1.6),xlabel=r'$T/T_*$',ylabel=r'$S/(Nk_B)$',title='Weaker confinement gives lower temperature at fixed entropy')
ax.legend(loc='lower right',fontsize=9)
ax.text(.02,.97,r'Chosen normalization: $Z_1(T_*,a_*)/N=10^4$',transform=ax.transAxes,va='top',fontsize=9,bbox={'facecolor':'white','edgecolor':'none','alpha':.9})
fig.savefig(Path(__file__).stem+'.png',dpi=145,facecolor='white')
