"""Equilibrium calculation plus explicitly schematic kinetic sketch.
Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7; opaque cwd-only PNG.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
B=13.6;coefficient=3e-16
lo,hi=30.,60.
for _ in range(80):
 y=(lo+hi)/2
 if y-1.5*np.log(y)<np.log(2/coefficient):lo=y
 else:hi=y
Trec=B/((lo+hi)/2)
def saha(T):
 y=B/T;R=np.exp(np.log(coefficient)+y-1.5*np.log(y));return 2/(1+np.sqrt(1+4*R))
x=np.linspace(1.55,.32,900);equilibrium=saha(x*Trec)
effective=np.where(x>=1,x,1-.7*(1-x));kinetic=np.maximum(saha(effective*Trec),2e-4)
fig,ax=plt.subplots(figsize=(8.5,4),dpi=100,facecolor='white')
ax.semilogy(x,equilibrium,'--',lw=2,color='#236c99',label='Saha equilibrium (calculated)');ax.semilogy(x,kinetic,lw=2,color='#a65a25',label='Delayed kinetics (schematic)')
ax.axvline(1,color='#444444',lw=1);ax.axvline(.8,color='#777777',lw=1,ls=':');ax.text(1.01,.011,'Trec',rotation=90,ha='right');ax.text(.8,.012,'Tdec',rotation=90,ha='right');ax.text(.59,4e-4,'Residual electrons',fontsize=10,ha='center')
ax.set(xlim=(1.55,.32),ylim=(1e-6,1.2),xlabel='Temperature / Saha half-ionization temperature  (cooling to the right)',ylabel='Free-electron fraction Xe');ax.grid(alpha=.2);ax.legend(fontsize=10,loc='upper right');ax.set_title('Equilibrium versus departure from equilibrium; Tdec position is illustrative',fontsize=11)
fig.subplots_adjust(left=.10,right=.98,bottom=.16,top=.87)
fig.savefig(Path.cwd()/'paper-48-recombination-sketch.png',dpi=100,facecolor='white',transparent=False);plt.close(fig)
