import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False,'figure.facecolor':'white','savefig.facecolor':'white'})

fig,ax=plt.subplots(1,2,figsize=(10,3.8),layout='constrained');a=ax[0]
a.add_patch(Rectangle((0,0),1,1,facecolor='none',edgecolor='.5',ls='--'));a.add_patch(Rectangle((0,.08),1.35,.84,facecolor='#e6f1f7',edgecolor='#17639b'));a.annotate('',xy=(1.9,.5),xytext=(1.4,.5),arrowprops={'arrowstyle':'->','lw':2});a.annotate('',xy=(-.55,.5),xytext=(-.05,.5),arrowprops={'arrowstyle':'->','lw':2});a.text(1.8,.65,'F',ha='center');a.text(-.45,.65,'F',ha='center');a.text(.65,1.3,r'$\epsilon_{xx}=\Delta L/L_0$',ha='center');a.text(.65,-.45,r'$\epsilon_{yy}=-\nu\epsilon_{xx}$',ha='center');a.set(xlim=(-.65,2),ylim=(-.65,1.7),title='Tension and transverse contraction');a.axis('off')
eps=np.linspace(0,.04,600);stress=np.where(eps<=.01,100*eps,1+10*(eps-.01));emax=.04;smax=1.3;ep=emax-smax/100;unload=np.linspace(emax,ep,150)
a=ax[1];a.plot(eps,stress,label='Loading');a.plot(unload,100*(unload-ep),label='Elastic unloading');a.annotate('',xy=(.032,1.22),xytext=(.025,1.15),arrowprops={'arrowstyle':'->'});a.annotate('',xy=(.031,.4),xytext=(.035,.8),arrowprops={'arrowstyle':'->','color':'#e18320'});a.plot(ep,0,'ko');a.annotate('Residual plastic strain',xy=(ep,0),xytext=(.012,.23),arrowprops={'arrowstyle':'->'},fontsize=9);a.set(xlabel='Engineering axial strain',ylabel='Stress (chosen units)',title='Chosen elastic-plastic material sketch',ylim=(-.05,1.5));a.legend(fontsize=9,loc='upper left')
fig.savefig('paper-1-stress-strain.png',dpi=155)
