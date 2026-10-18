from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size':12,'axes.titlesize':14,'axes.labelsize':13})
t=np.geomspace(.03,1e4,900);J=np.arange(800)[:,None];levels=J*(J+1)
weights=(2*J+1)*np.exp(-levels/t)
z=weights.sum(axis=0);u=(weights*levels).sum(axis=0)/z
cvrot=((weights*levels**2).sum(axis=0)/z-u*u)/t**2
q=100/t;em=np.exp(-q);cvvib=q*q*em/(1-em)**2
cv=1.5+cvrot+cvvib;gamma=1+1/cv
fig,ax=plt.subplots(figsize=(8.2,4.5),dpi=130,facecolor='white')
ax.semilogx(t,gamma,lw=2.5,color='#2268a3')
for value,label in [(5/3,r'$5/3$'),(7/5,r'$7/5$'),(9/7,r'$9/7$')]:
 ax.axhline(value,lw=.8,ls='--',color='0.65');ax.text(1.25e4,value,label,va='center')
ax.axvline(1,color='#26764e',ls=':',lw=1.4);ax.axvline(100,color='#b13939',ls=':',lw=1.4)
ax.text(.07,1.59,'Translation',fontsize=10)
ax.text(3,1.47,'Rotations active',fontsize=10)
ax.text(450,1.36,'Vibration active',fontsize=10)
ax.set(xlim=(.03,1e4),ylim=(1.25,1.72),xlabel=r'$T/\Theta_{\rm rot}$',ylabel=r'$\gamma=C_p/C_V$',title=r'Intact heteronuclear molecule, $\Theta_{\rm vib}=100\Theta_{\rm rot}$')
ax.spines[['top','right']].set_visible(False);ax.grid(alpha=.15)
fig.tight_layout()
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,facecolor='white',transparent=False)
