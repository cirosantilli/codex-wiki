"""Exact transient of a stipulated Hookean conformation model; not experimental data."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def comp(rate,u):
 if abs(rate)<1e-12:return 1+u
 return np.exp(rate*u)+np.expm1(rate*u)/rate
u=np.linspace(0,8,500);ws=[.1,.4,.5,.6];colors=['#3579a4','#d08a25','#657d3d','#a63348']
fig,(a,b)=plt.subplots(1,2,figsize=(11.6,6))
fig.patch.set_facecolor('white');fig.suptitle('A linear spring cannot balance sufficiently strong extension',fontsize=16,y=.97)
for w,c in zip(ws,colors):
 a.plot(u,comp(2*w-1,u),label=f'Wi = {w:.1f}',color=c,lw=2.2)
 assert np.all(comp(2*w-1,u)>0)
a.set(xlabel=r'Dimensionless time $u=t/\lambda$',ylabel=r'Longitudinal mean-square separation $C_{xx}$',ylim=(0,26))
a.legend(fontsize=11)
w=np.linspace(0,.475,500)
b.plot(w,1/(1-2*w),color='#3579a4',lw=2.3,label=r'$C_{xx}=1/(1-2\mathrm{Wi})$')
b.plot(w,1/(1+2*w),color='#a63348',lw=2.3,label=r'$C_{yy}=1/(1+2\mathrm{Wi})$')
b.axvline(.5,color='#555',ls='--');b.text(.515,15,'No finite\npositive steady\nstate for\nWi ≥ 1/2',fontsize=10,ha='left',va='center')
b.set(xlabel=r'Weissenberg number $\mathrm{Wi}=\lambda\dot\epsilon$',ylabel='Steady conformation component',xlim=(0,.7),ylim=(0,21));b.legend(fontsize=10,loc='upper left')
for ax in [a,b]:ax.grid(alpha=.2);ax.tick_params(labelsize=11);ax.xaxis.label.set_size(12);ax.yaxis.label.set_size(11)
fig.text(.5,.045,'Initially C = I; prescribed planar extension; no finite extensibility, intermolecular coupling or flow feedback.\nOriginal model calculation. Unbounded growth marks the failure of the ideal spring, not an infinite physical chain.',ha='center',fontsize=11,linespacing=1.5,color='#444')
fig.subplots_adjust(left=.075,right=.98,top=.87,bottom=.22,wspace=.28)
fig.savefig(Path(__file__).with_suffix('.png').name,dpi=110,facecolor='white');plt.close(fig)
