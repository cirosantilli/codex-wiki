from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size':11,'axes.titlesize':13,'axes.labelsize':12})
fig,(ax,bx)=plt.subplots(1,2,figsize=(10.6,4.2),dpi=125,facecolor='white',gridspec_kw={'width_ratios':[1.2,1]})
delta=np.linspace(-2*np.pi,2*np.pi,10001)
def transmission(phase,R):return 1/(1+4*R/(1-R)**2*np.sin(phase/2)**2)
for R,c in [(.1,'#2268a3'),(.9,'#b13939')]:
 ax.plot(delta/np.pi,transmission(delta,R),lw=2,color=c,label=fr'$\mathcal{{R}}={R}$')
ax.axhline(.5,color='0.5',lw=1,ls='--')
ax.text(.15,.54,'Half maximum',fontsize=10,color='0.35')
ax.set(xlim=(-2,2),ylim=(0,1.06),xlabel=r'$\delta/\pi$',ylabel=r'$I_t/I_0$',title='Periodic transmission')
ax.legend(loc='lower right',frameon=True,facecolor='white')
phase=np.linspace(-.42,.42,2001);R=.9
bx.plot(phase,transmission(phase,R),lw=2.5,color='#b13939')
width=4*np.arcsin((1-R)/(2*np.sqrt(R)))
bx.axhline(.5,color='0.5',lw=1,ls='--')
bx.plot([-width/2,width/2],[.5,.5],color='#2268a3',lw=3)
bx.annotate(fr'FWHM = {width:.4f} rad',xy=(width/2,.5),xytext=(.02,.84),fontsize=10,arrowprops={'arrowstyle':'->','color':'0.3'})
bx.set(xlim=(-.42,.42),ylim=(0,1.06),xlabel=r'$\delta$ (radians from resonance)',ylabel=r'$I_t/I_0$',title=r'Central peak, $\mathcal{R}=0.9$')
for a in (ax,bx):
 a.set_facecolor('white');a.spines[['top','right']].set_visible(False);a.grid(alpha=.15)
fig.tight_layout()
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,facecolor='white',transparent=False)
