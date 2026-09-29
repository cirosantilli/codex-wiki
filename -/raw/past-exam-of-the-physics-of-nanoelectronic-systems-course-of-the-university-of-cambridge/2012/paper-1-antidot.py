import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, FancyArrowPatch
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False,'figure.facecolor':'white','savefig.facecolor':'white'})

fig,ax=plt.subplots(1,2,figsize=(10,3.8),layout='constrained');a,g=ax
for yy,sign in [(1.2,1),(-1.2,-1)]:
 a.plot([-2.5,2.5],[yy,yy],color='#17639b',lw=2);a.annotate('',xy=(1.8*sign,yy),xytext=(.8*sign,yy),arrowprops={'arrowstyle':'->','lw':2,'color':'#17639b'})
a.add_patch(Circle((0,0),.48,facecolor='.8',edgecolor='k'));a.text(0,0,'Depleted\nhill',ha='center',va='center',fontsize=10)
th=np.linspace(0,2*np.pi,200);a.plot(.8*np.cos(th),.8*np.sin(th),color='crimson');a.annotate('',xy=(0,.8),xytext=(.22,.77),arrowprops={'arrowstyle':'->','color':'crimson','lw':2})
for yy in [-1,1]:a.plot([0,0],[yy*1.2,yy*.8],'k:');a.text(.12,yy*.99,r'$\Gamma_{L,R}$',fontsize=10)
a.text(-2.4,.5,r'$B_z>0$',fontsize=11);a.set(xlim=(-2.6,2.6),ylim=(-1.65,1.65),title='Resonant transfer into the returning edge');a.axis('off')
x=np.linspace(-2.5,2.5,1300);reflection=np.zeros_like(x)
for j in range(-2,3):reflection+=.8*.045**2/((x-j)**2+.045**2)
g.plot(x,2-reflection);g.axhline(2,color='.6',ls='--');g.set(xlabel=r'Flux offset / $(h/e)$',ylabel=r'$G/(e^2/h)$',ylim=(.9,2.1),title='Chosen weak, isolated resonance dips');g.text(-2.35,1.02,'Illustrative; no charging or spin splitting',fontsize=9)
fig.savefig('paper-1-antidot.png',dpi=155)
