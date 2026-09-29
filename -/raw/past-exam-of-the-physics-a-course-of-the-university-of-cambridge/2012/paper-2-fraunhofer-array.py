"""Original calculated illustration; Python3.14,NumPy,Matplotlib; PNG output to cwd."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import math
fig,axs=plt.subplots(1,3,figsize=(13,3.8),facecolor='white',layout='constrained')
a=axs[0];a.plot([0,0],[-1.3,1.3],lw=3,color='#296c9e');a.plot([4,4],[-1.3,1.3],lw=2,color='.5');a.plot([0,4],[0,0],ls=':',color='.5');a.plot([0,4],[.6,1],color='#ad5932');a.plot([0,4],[0,1],ls='--',color='#296c9e');a.scatter([0,4],[.6,1],s=25,color='#ad5932')
a.text(-.1,.72,'P: x',ha='right');a.text(4,1.1,'Q: x₀',ha='right');a.annotate('',xy=(4,-.8),xytext=(0,-.8),arrowprops=dict(arrowstyle='<->'));a.text(2,-1,'Axial separation R',ha='center');a.text(0,-1.5,'Aperture field ψΣ(x,y)',ha='center',fontsize=8);a.text(4,-1.5,'Detector',ha='center',fontsize=8)
for yy in [-.5,0,.5]:a.annotate('',xy=(-.1,yy),xytext=(-.75,yy),arrowprops=dict(arrowstyle='->',color='.3'))
a.set(xlim=(-1,4.4),ylim=(-1.7,1.6),title='Original paraxial geometry');a.axis('off')
def array(s):return (10*np.sinc(10*s)/np.sinc(s))**2
s=np.linspace(-.3,.3,2400);axs[1].plot(s,array(s)/100,color='#296c9e');axs[1].axvline(.1,color='#ad5932',ls=':');axs[1].axvline(-.1,color='#ad5932',ls=':');axs[1].set(xlabel=r'$D\theta/\lambda$',ylabel='Central peak normalized to 1',title='Ten coherent dishes: first zeros ±0.1')
s=np.linspace(-40,40,40001);x=np.pi*25/800*s;j=np.zeros_like(x)
for order in range(25):j+=(-1)**order*(x/2)**(2*order+1)/(float(math.factorial(order)*math.factorial(order+1)))
env=np.ones_like(x);nz=x!=0;env[nz]=(2*j[nz]/x[nz])**2
# sinc ratio at integer orders is evaluated with the exact removable limit.
arr=array(s);sing=abs(np.sin(np.pi*s))<1e-10;arr[sing]=100
axs[2].plot(s,env*arr/100,lw=.5,color='#296c9e');axs[2].plot(s,env,color='#ad5932',ls='--',lw=1,label='25 m dish envelope');axs[2].set(xlabel=r'$D\theta/\lambda$',ylabel='Normalized intensity',title='Sparse-array grating orders');axs[2].legend(fontsize=8)
for a in axs[1:]:a.grid(alpha=.2)
fig.savefig('paper-2-fraunhofer-array.png',dpi=150,facecolor='white');plt.close(fig)
