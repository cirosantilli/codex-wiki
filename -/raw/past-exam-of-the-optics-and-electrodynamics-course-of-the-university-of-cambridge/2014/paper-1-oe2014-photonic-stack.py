"""Original educational diagram. Python 3.14, NumPy and Matplotlib; writes a PNG basename in the current working directory."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white'})
from matplotlib.patches import Rectangle
nH,nL=2.5,1.5
regular=['H','L']*12;defect=['H','L']*6+['L','H']*6
u=np.unique(np.r_[np.linspace(.7,1.3,5001),np.linspace(.99,1.01,1001)])
def transmission(seq):
 M=np.tile(np.eye(2,dtype=complex),(len(u),1,1));delta=np.pi*u/2
 for name in seq:
  n=nH if name=='H' else nL
  L=np.empty_like(M);L[:,0,0]=L[:,1,1]=np.cos(delta);L[:,0,1]=1j*np.sin(delta)/n;L[:,1,0]=1j*n*np.sin(delta)
  M=M@L
 return 4/abs(M[:,0,0]+M[:,0,1]+M[:,1,0]+M[:,1,1])**2
tr=transmission(regular);td=transmission(defect)
fig,axs=plt.subplots(2,1,figsize=(8,5),gridspec_kw={'height_ratios':[1,2]},layout='constrained')
x=0
for j,name in enumerate(defect):
 n=nH if name=='H' else nL;width=1/(4*n);axs[0].add_patch(Rectangle((x,0),width,1,facecolor='#235d92' if name=='H' else '#dce9f2',edgecolor='white',lw=.5));x+=width
axs[0].set(xlim=(0,x),ylim=(-.1,1.7),title='Quarter-wave mirror pair with a central half-wave low-index defect')
axs[0].text(x/2,1.4,r'$n_H=2.5,\ n_L=1.5;\quad n_jd_j=\lambda_0/4$',ha='center');axs[0].annotate('Defect',xy=(x/2,.5),xytext=(x/2,1.12),ha='center',arrowprops={'arrowstyle':'->','color':'#aa412b'},color='#aa412b');axs[0].axis('off')
axs[1].plot(u,tr,color='#235d92',lw=1.3,label='Periodic stack, 12 pairs');axs[1].plot(u,td,color='#b25424',lw=1.3,label='Mirror pair with defect')
axs[1].set(xlabel=r'Frequency / design frequency $\nu/\nu_0$',ylabel='Power transmission',ylim=(-.03,1.05),xlim=(.7,1.3));axs[1].legend(fontsize=9,loc='upper left');axs[1].grid(alpha=.2)
axs[1].annotate('Localized defect resonance',xy=(1,1),xytext=(1.035,.78),arrowprops={'arrowstyle':'->','color':'#555'},fontsize=9)
axs[1].text(.9,.13,'Stop band',ha='center',color='#555')
fig.savefig('paper-1-oe2014-photonic-stack.png',dpi=150,facecolor='white');plt.close(fig)
