from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

x=np.linspace(0,6,500);up=-.25+.5*np.sqrt(1+x*x);dn=-.25-.5*np.sqrt(1+x*x)
fig,ax=plt.subplots(figsize=(7.2,4.2),layout='constrained');ax.plot(x,up,lw=2,label='mixed upper branch');ax.plot(x,dn,lw=2,label='mixed lower branch');ax.plot(x,np.full_like(x,.25),lw=2,color='#367c46',label=r'$m_F=+1,-1$ (two states)');ax.plot(x,-.25+x/2,':',color='gray');ax.plot(x,-.25-x/2,':',color='gray');ax.axvline(1,color='gray',ls='--',lw=1)
ax.annotate('triplet: three states',(0,.25),(.3,1.2),arrowprops=dict(arrowstyle='->'),fontsize=10);ax.annotate('singlet',(0,-.75),(.6,-1.7),arrowprops=dict(arrowstyle='->'),fontsize=10);ax.text(1.07,-2.9,'mixing crossover',rotation=90,fontsize=9);ax.set(xlabel=r'$x=4\mu_BB/A$',ylabel=r'energy / $A$',title='Positronium spin Hamiltonian, positive A');ax.legend(loc='upper left',fontsize=9);ax.grid(alpha=.2)

fig.savefig(Path(__file__).stem+'.png',dpi=140,facecolor='white')
