import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, FancyArrowPatch
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False,'figure.facecolor':'white','savefig.facecolor':'white'})

fig,ax=plt.subplots(1,3,figsize=(11,3.8),layout='constrained');pts=np.array([(x,y) for x in range(4) for y in range(4)])
for x,y in pts:ax[0].add_patch(Circle((x,y),.13,color='0.55'))
theta=np.linspace(0,2*np.pi,200);ax[0].plot(1+.5*np.cos(theta),1+.5*np.sin(theta),color='#17639b');ax[0].annotate('',xy=(1,1.5),xytext=(1.15,1.47),arrowprops={'arrowstyle':'->','color':'#17639b'});ax[0].annotate('',xy=(2,2.6),xytext=(1,2.6),arrowprops={'arrowstyle':'<->'});ax[0].text(1.5,2.72,'a',ha='center');ax[0].set(title='Periodic antidots: selected orbit')
rng=np.random.default_rng(120245)
for x,y in rng.uniform(-.1,3.1,(16,2)):ax[1].add_patch(Circle((x,y),.13,color='0.55'))
ax[1].set(title='Random control: same mean density')
for a in ax[:2]:a.set(xlim=(-.5,3.5),ylim=(-.5,3.5),aspect='equal');a.axis('off')
x=np.linspace(-3,3,1600);base=1+.04*x*x;res=.38*np.exp(-.5*((x-1)/.13)**2)+.38*np.exp(-.5*((x+1)/.13)**2)
ax[2].plot(x,base+res,label='Periodic (chosen model)');ax[2].plot(x,base,'--',label='Random reference');ax[2].axvline(0,color='.7',ls=':');ax[2].set(xlabel=r'$(B-B_{1/2})/\Delta B_{\rm geom}$',ylabel='Longitudinal response (arbitrary)',title=r'Geometric scale around $B^*=0$');ax[2].legend(fontsize=9);ax[2].text(-2.9,1.02,'No experimental trace reconstructed',fontsize=8)
fig.suptitle(r'Fully polarized counting: $k_F^*=\sqrt{4\pi n_s}$; illustrative geometry, not historical dimensions',fontsize=11)
fig.savefig('paper-1-composite-orbits.png',dpi=155)
