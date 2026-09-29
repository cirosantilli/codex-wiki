"""Original dimensionless plate response and symmetric ridge junction; Python 3.14, NumPy, Matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white','savefig.facecolor':'white'})
x=np.linspace(-20,20,8192,endpoint=False);q=2*np.pi*np.fft.fftfreq(len(x),d=x[1]-x[0]);h=np.exp(-(x/.5)**2/2);w=np.fft.ifft(np.fft.fft(h)/(1+q**4)).real
fig,axs=plt.subplots(1,2,figsize=(9.5,3.9),layout='constrained');ax=axs[0]
ax.plot(x,h,color='#bd7831',lw=2,label='volcanic load h');ax.plot(x,-w,color='#246d9c',lw=2,label='plate displacement −w');ax.axhline(0,color='grey',lw=.7);ax.set(xlim=(-7,7),xlabel='distance / flexural scale',ylabel='illustrative height',title='Regional flexure, not local compensation');ax.legend(fontsize=8);ax.grid(alpha=.17);ax.annotate('depression',xy=(0,-w.max()),xytext=(-3,-.42),arrowprops={'arrowstyle':'->'},fontsize=9);ax.annotate('outer arch',xy=(4,-w[np.argmin(abs(x-4))]),xytext=(3,.35),arrowprops={'arrowstyle':'->'},fontsize=9)
ax=axs[1]
for angle in [90,210,330]:
 r=np.deg2rad(angle);ax.plot([0,1.8*np.cos(r)],[0,1.8*np.sin(r)],color='#333333',lw=2.5)
for name,angle,col in [('A',150,'#246d9c'),('B',270,'#bd7831'),('C',30,'#7a5d9b')]:
 r=np.deg2rad(angle);vec=np.array([np.cos(r),np.sin(r)]);pos=.7*vec
 ax.annotate('',xy=pos+.65*vec,xytext=pos,arrowprops={'arrowstyle':'->','color':col,'lw':2});ax.text(*(1.55*vec),f'plate {name}',ha='center',va='center',color=col)
ax.plot(0,0,'ko',ms=4);ax.text(.13,.05,'junction: u = 0',fontsize=8);ax.set(aspect='equal',xlim=(-2,2),ylim=(-2,2),title='Symmetric ridge–ridge–ridge example');ax.axis('off')
fig.savefig(Path(__file__).stem+'.png',dpi=145,bbox_inches='tight',facecolor='white');plt.close(fig)
