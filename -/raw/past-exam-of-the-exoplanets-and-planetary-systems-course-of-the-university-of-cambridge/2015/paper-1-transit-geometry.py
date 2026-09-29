"""Original solution diagram; Python3.14.4, numpy2.3.5, matplotlib3.10.7.
Run from mirrored _media directory; saves a basename in cwd.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,FancyBboxPatch
plt.rcParams.update({'font.size':11,'figure.facecolor':'white','axes.spines.top':False,'axes.spines.right':False})
GM=.5*1.3271244e20;R=.5*6.957e8;P=1.3*86400;T=2400;k=np.sqrt(.0015);A=(GM*P*P/(4*np.pi*np.pi))**(1/3)/R;st=np.sin(np.pi*T/P)**2;b=np.sqrt(((1+k)**2-A*A*st)/(1-st));cosi=b/A
minutes=np.linspace(-35,35,900);phase=2*np.pi*minutes*60/P;z=A*np.sqrt(np.sin(phase)**2+cosi*cosi*np.cos(phase)**2)
def area(z):
 if z>=1+k:return 0.
 if z<=1-k:return np.pi*k*k
 v=(z*z+k*k-1)/(2*z*k);w=(z*z+1-k*k)/(2*z);return k*k*np.arccos(np.clip(v,-1,1))+np.arccos(np.clip(w,-1,1))-.5*np.sqrt(max(0,(-z+k+1)*(z+k-1)*(z-k+1)*(z+k+1)))
flux=1-np.array([area(x) for x in z])/np.pi
fig,axs=plt.subplots(1,2,figsize=(10.8,4.5));ax=axs[0];ax.add_patch(Circle((0,0),1,fc='#fff0ce',ec='#a86500'));ax.add_patch(Circle((0,b),k,fc='#205ca0'));x=np.sqrt((1+k)**2-b*b);ax.plot([-1.15,1.15],[b,b],'--',color='#205ca0',label='Planet-centre track');ax.plot([-x,x],[b,b],lw=3,color='#205ca0');ax.annotate('',(0,b),(0,0),arrowprops={'arrowstyle':'<->','color':'black'});ax.text(.04,b/2,'b = %.3f'%b);ax.text(-.78,-.5,'Uniform stellar disc');ax.set(aspect='equal',xlim=(-1.22,1.22),ylim=(-1.12,1.25),xlabel='Projected x / stellar radius',ylabel='Projected y / stellar radius',title='Finite planet radius k = 0.03873');ax.legend(fontsize=8,loc='upper right')
ax=axs[1];ax.plot(minutes,(1-flux)*100,lw=2);ax.axvline(-20,color='.5',ls=':');ax.axvline(20,color='.5',ls=':');ax.annotate('40 min total duration',xy=(0,.008),ha='center');ax.set(xlabel='Time from mid-transit / min',ylabel='Blocked stellar flux / %',title='Original uniform-disc contact model',ylim=(-.01,.17));ax.grid(alpha=.15);fig.tight_layout()

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
