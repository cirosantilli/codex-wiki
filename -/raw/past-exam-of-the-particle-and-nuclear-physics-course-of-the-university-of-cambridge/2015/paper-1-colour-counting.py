from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})

fig,ax=plt.subplots(1,2,figsize=(10,3.7))
a=ax[0]
for p,q,label,where in [((0,1),(1,.55),r'$e^-$',(.05,1.05)),((1,.55),(2,1),r'$e^-$',(1.8,1.05)),((0,-.5),(1,-.05),r'$q$',(.05,-.7)),((1,-.05),(2,-.5),r'$q$',(1.85,-.7))]:
 a.annotate('',xy=q,xytext=p,arrowprops={'arrowstyle':'->','color':'black','lw':1.7});a.text(*where,label)
y=np.linspace(-.05,.55,180);a.plot(1+.045*np.sin(np.linspace(0,9*np.pi,180)),y,color='tab:blue');a.text(1.1,.24,r'$\gamma^*$')
a.text(0,-1,'A virtual photon resolves a charged parton',fontsize=9)
a.set(xlim=(-.15,2.25),ylim=(-1.1,1.3),title='Deep-inelastic scattering: parton-level vertex');a.axis('off')
x=np.arange(3);r=np.array([2,10/3,11/3]);w=.32
ax[1].bar(x-w/2,r/3,w,label='One colour (hypothetical)',color='gray');ax[1].bar(x+w/2,r,w,label='Three colours',color='tab:orange')
ax[1].set(xticks=x,xticklabels=['u,d,s','u,d,s,c','u,d,s,c,b'],ylabel=r'$R=N_c\sum e_q^2$',title='Leading-order colour-counting predictions',ylim=(0,4.6));ax[1].legend(fontsize=8)
for i,lab in enumerate(['2','10/3','11/3']):ax[1].text(i+w/2,r[i]+.08,lab,ha='center')

fig.tight_layout()
fig.savefig(Path(__file__).stem+'.png',dpi=145,facecolor='white',bbox_inches='tight')
plt.close(fig)
