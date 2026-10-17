"""Original educational diagram. Python 3.14, NumPy and Matplotlib; output is saved in the current working directory."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white'})
N=30;fig=plt.figure(figsize=(8,5.5),layout='constrained');gs=fig.add_gridspec(2,3,height_ratios=[1,1.1])
for j,(delta,title) in enumerate([(0,'Aligned phasors'),(2*np.pi/N,'One full wrap'),(3*np.pi/N,'1.5 wraps (approximate)')]):
 ax=fig.add_subplot(gs[0,j]);z=np.r_[0,np.cumsum(np.exp(1j*np.arange(N)*delta))]/N
 ax.plot(z.real,z.imag,'o-',color='#225c91',ms=2,lw=1)
 ax.annotate('',xy=(z[-1].real,z[-1].imag),xytext=(0,0),arrowprops={'arrowstyle':'->','color':'#b25424','lw':2})
 label=['Resultant = N','Resultant = 0',r'Resultant $\simeq 2N/(3\pi)$'][j]
 ax.text(.5,-.12,label,ha='center',transform=ax.transAxes,fontsize=9)
 ax.set(title=title,aspect='equal',xlim=(-.38,1.08),ylim=(-.1,.58));ax.axis('off')
ax=fig.add_subplot(gs[1,:]);u=np.linspace(0,8,1500);intensity=np.sinc(u/np.pi)**2
ax.plot(u,intensity,color='#225c91',lw=1.8)
ax.scatter([np.pi,1.5*np.pi],[0,4/(9*np.pi**2)],color='#b25424',s=25,zorder=5)
ax.annotate('First zero',xy=(np.pi,0),xytext=(2.1,.27),arrowprops={'arrowstyle':'->','color':'#666'},fontsize=9)
ax.annotate(r'Approximate subsidiary maximum: $I/I_{\rm main}=4/(9\pi^2)$',xy=(1.5*np.pi,4/(9*np.pi**2)),xytext=(3.1,.5),arrowprops={'arrowstyle':'->','color':'#666'},fontsize=9)
ax.set(xlabel=r'$u=N\Delta\delta/2$ from a principal maximum',ylabel=r'$I/I_{\rm main}$',xlim=(0,8),ylim=(-.03,1.05),title='Large-array limit: squared sinc intensity')
ax.grid(alpha=.2)
fig.savefig('paper-1-ia2014-grating.png',dpi=150,facecolor='white');plt.close(fig)
