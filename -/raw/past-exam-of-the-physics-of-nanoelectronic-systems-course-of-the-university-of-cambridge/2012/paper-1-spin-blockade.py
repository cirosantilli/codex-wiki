import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, FancyArrowPatch
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False,'figure.facecolor':'white','savefig.facecolor':'white'})

fig,ax=plt.subplots(2,2,figsize=(10,7),layout='constrained');a=ax[0,0]
for x,label in [(0,'Source'),(2,'Left dot'),(4,'Right dot'),(6,'Drain')]:
 a.add_patch(Circle((x,0),.43,facecolor='#edf5fa',edgecolor='k'));a.text(x,-.75,label,ha='center',fontsize=10)
for x in [.6,2.6,4.6]:a.annotate('',xy=(x+.8,0),xytext=(x,0),arrowprops={'arrowstyle':'->'})
a.text(2,0,r'$\uparrow$',ha='center',va='center');a.text(4,0,r'$\uparrow$',ha='center',va='center');a.text(3,.55,'Triplet blocked',ha='center',color='crimson');a.text(3,1.2,'Gates set (1,1) and (0,2); transverse RF drive',ha='center',fontsize=9);a.set(xlim=(-.6,6.6),ylim=(-1.2,1.8),title='Functional double-dot device');a.axis('off')
a=ax[0,1]
for x,y,label in [(0,0,r'$S(1,1)$'),(0,1,r'$T(1,1)$'),(2,0,r'$S(0,2)$'),(2,2,r'$T(0,2)$')]:
 a.plot([x-.35,x+.35],[y,y],color='k');a.text(x,y+.1,label,ha='center',fontsize=10)
a.annotate('',xy=(1.6,0),xytext=(.4,0),arrowprops={'arrowstyle':'->','color':'#17639b','lw':2});a.plot([.5,1.5],[1,0],'r:');a.text(1,.65,'Spin forbidden',ha='center',fontsize=9,color='crimson');a.axhspan(1.45,2.4,color='.93');a.text(1,1.6,'Outside bias window',ha='center',fontsize=9);a.set(xlim=(-.6,2.6),ylim=(-.4,2.4),title='Accessible singlet; excited triplet excluded');a.axis('off')
bb=np.linspace(-.15,.15,1400);g=.35;muBoverh=13.99624555e9;f=400e6;b0=f/(g*muBoverh);base=.07+.22*np.exp(-.5*(bb/.008)**2);res=.7*(np.exp(-.5*((bb-b0)/.006)**2)+np.exp(-.5*((bb+b0)/.006)**2))
a=ax[1,0];a.plot(bb*1000,base,label='RF off');a.plot(bb*1000,base+res,label='RF on');a.set(xlabel='Static field (mT)',ylabel='Leakage current (arbitrary)',title=r'Illustrative $f=400$ MHz, $|g|=0.35$');a.legend(fontsize=9)
t=np.linspace(0,6,800);p=.5*(1-np.cos(2*np.pi*t)*np.exp(-t/3));a=ax[1,1];a.plot(t,p);a.set(xlabel='Burst duration / chosen Rabi period',ylabel='Spin-flip readout (arbitrary)',ylim=(-.05,1.05),title='Illustrative damped coherent rotations')
fig.suptitle('Original diagrams and model curves; no measured data reconstructed',fontsize=12)
fig.savefig('paper-1-spin-blockade.png',dpi=155)
