"""Original field and small excluded-volume pulse calculation; PNG to cwd."""
import numpy as np
import matplotlib.pyplot as plt

def radius(z,a=1.,b=2.):
 return a+(b-a)*(1-np.abs(np.asarray(z)-1))
def passage_radius(t,a=1.,b=2.):
 f=np.minimum(np.clip(t,0,1),1-np.clip(t,0,1))
 return (a**3+2*f*(b**3-a**3))**(1/3)
def pulse(t,a=1.,b=2.,depth=.15,edge=.012):
 r=passage_radius(t,a,b);q=np.minimum(np.maximum(t,0),np.maximum(1-t,0));ramp=np.sin(np.pi/2*np.clip(q/edge,0,1))**2
 return 1-depth*ramp*(a/r)**4
def main():
 plt.rcParams.update({'font.size':10})
 z=np.linspace(0,2,700);a,b=1.,2.;E=a*b/radius(z,a,b)**2
 t=np.linspace(-.08,1.08,1000)
 fig,ax=plt.subplots(1,2,figsize=(8.5,3.7),layout='constrained')
 ax[0].plot(z/2,E,lw=2,c='#2f74a0');ax[0].axhline(1,c='.5',ls=':',lw=1,label='Axial mean')
 ax[0].set(xlabel=r'$z/(2l)$',ylabel=r'$E/[V/(2l)]$',title='Narrow ends, wide centre',ylim=(0,2.3));ax[0].legend(fontsize=9)
 ax[1].plot(t,pulse(t),lw=2,c='#b44442');ax[1].axhline(1,c='.5',ls=':',lw=1);ax[1].axvline(0,c='.7',lw=.8);ax[1].axvline(1,c='.7',lw=.8)
 ax[1].set(xlabel=r'$t/\Delta t$',ylabel=r'$I/I_0$',title='Illustrative weak volume-exclusion pulse',ylim=(.84,1.02));ax[1].text(.5,.86,'Small object; rounded entry and exit',ha='center',fontsize=8)
 for p in ax:p.spines[['top','right']].set_visible(False);p.grid(alpha=.16)
 fig.suptitle(r'Chosen dimensionless example: $b/a=2$; not measured data',fontsize=10)
 fig.savefig('paper-1-pore-signals.png',dpi=170,facecolor='white');plt.close(fig)
if __name__=='__main__':main()
