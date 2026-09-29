"""Qualitative solar abundances; not a fitted or computed solar model.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Writes only paper-53-solar-abundances.png in the caller's cwd.
MPLCONFIGDIR is supplied by the caller and is never overridden here.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

r=np.linspace(0,1,800)
x1=.48+.52*(1-np.exp(-(r/.23)**2))
s=r/.30
peak=s**4*np.exp(2-2*s**2)
u=np.clip((r-.65)/.06,0,1)
peak*=1-3*u*u+2*u**3
x3=.025+.975*peak
x3/=x3.max()
fig,axes=plt.subplots(1,2,figsize=(10,6),dpi=100,facecolor='white')
fig.subplots_adjust(left=.08,right=.96,bottom=.13,top=.78,wspace=.28)
for ax in axes:
 ax.set_facecolor('white');ax.set_xlim(0,1);ax.set_ylim(0,1.12)
 ax.axvspan(.71,1,color='#edf1f4',zorder=0)
 ax.set_xlabel(r'Fractional radius $r/R_\odot$',fontsize=12)
 ax.grid(alpha=.18);ax.tick_params(labelsize=10)
 ax.text(.86,.1,'mixed outer\nenvelope',ha='center',fontsize=10,color='#5a6873')
axes[0].plot(r,x1,color='#1d659c',lw=2.8)
axes[0].set_ylabel(r'$X_1/X_{1,\mathrm{envelope}}$',fontsize=13)
axes[0].set_title('Hydrogen',fontsize=15)
axes[0].annotate('central hydrogen\ndepletion',xy=(.05,.5),xytext=(.30,.30),arrowprops={'arrowstyle':'->','color':'#1d659c'},fontsize=11,ha='center')
axes[1].plot(r,x3,color='#b35a20',lw=2.8)
axes[1].set_ylabel(r'$X_3/\max X_3$',fontsize=13)
axes[1].set_title('Helium-3',fontsize=15)
axes[1].annotate('off-centre\nabundance peak',xy=(.30,1),xytext=(.55,.75),arrowprops={'arrowstyle':'->','color':'#b35a20'},fontsize=11,ha='center')
fig.suptitle('Present solar abundance profiles: qualitative sketch',fontsize=17,y=.97)
fig.text(.5,.88,'Separate vertical normalizations; curves illustrate shape only',ha='center',fontsize=12,color='#46535d')
fig.savefig('paper-53-solar-abundances.png',dpi=100,facecolor='white',transparent=False)
plt.close(fig)
