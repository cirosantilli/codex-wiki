"""Original analyser diagram and Bell signal; Python 3.14, NumPy/Matplotlib."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,Ellipse
import numpy as np

plt.rcParams.update({'font.size':12,'axes.spines.top':False,'axes.spines.right':False})
fig,(setup,bell)=plt.subplots(1,2,figsize=(11,4.5),layout='constrained',facecolor='white')
setup.set(xlim=(-.2,5.8),ylim=(-1.3,2.2),aspect='equal',title='One analyser (repeat independently for Bob)')
setup.axis('off')
setup.annotate('',xy=(2.9,0),xytext=(0,0),arrowprops={'arrowstyle':'->','lw':1.8})
setup.text(.1,.2,'Photon',fontsize=11)
setup.add_patch(Ellipse((1.4,0),.12,.9,facecolor='#dce9ee',edgecolor='#315b71'))
setup.text(1.4,-.65,'Half-wave plate\naxis at '+r'$\alpha/4$',ha='center',va='top',fontsize=11)
setup.add_patch(Rectangle((2.9,-.25),.5,.5,facecolor='#e9e9e9',edgecolor='#444444'))
setup.plot([2.9,3.4],[-.25,.25],color='#444444')
setup.text(3.15,-.5,'Fixed H/V PBS',ha='center',fontsize=11)
setup.annotate('',xy=(4.8,0),xytext=(3.4,0),arrowprops={'arrowstyle':'->','lw':1.8,'color':'#26704b'})
setup.annotate('',xy=(3.15,1.4),xytext=(3.15,.25),arrowprops={'arrowstyle':'->','lw':1.8,'color':'#3566a3'})
for x,y,label in [(4.8,0,'H detector\n'+r'outcome $+1$'),(3.15,1.65,'V detector\n'+r'outcome $-1$')]:
    setup.text(x,y,label,ha='center',va='center',fontsize=11,bbox={'boxstyle':'round,pad=.3','fc':'white','ec':'#666666'})
setup.text(2.8,-1.2,r'Effective measurement: $\cos\alpha\,Z+\sin\alpha\,X$',ha='center',fontsize=11)
x=np.linspace(0,3.7,1001)
y=np.sqrt(2)*(1+np.sinc(x/np.pi))
threshold=2.092751479055039
bell.plot(x,y,color='#2b6d99',lw=2)
bell.axhline(2,color='#9a4938',ls='--',label='Local upper bound')
bell.axvline(threshold,color='#666666',ls=':')
bell.fill_between(x,2,y,where=x<threshold,color='#d9e9df')
bell.text(.95,2.13,'Violation',ha='center',fontsize=11)
bell.text(threshold+.08,2.6,r'$\varphi_0\simeq2.093$',rotation=90,va='center',fontsize=11)
bell.set(xlabel=r'Phase half-width $\varphi_0$ (radians)',ylabel=r'Bell signal $\mathcal{B}_{\varphi_0}$',title='Uniform phase averaging at fixed settings',xlim=(0,3.7),ylim=(1.15,3.02))
bell.legend(loc='upper right',fontsize=10)
bell.grid(alpha=.18)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white',transparent=False)
