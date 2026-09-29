"""Original exponential capture-window tradeoff; no historical measurements or fitted rates."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(.0001,5,1400);eff=-np.expm1(-x);metric=eff/np.sqrt(x)
lo,hi=.5,2.
for _ in range(60):
 mid=(lo+hi)/2
 if np.exp(mid)-1-2*mid>0:hi=mid
 else:lo=mid
opt=(lo+hi)/2;norm=(-np.expm1(-opt))/np.sqrt(opt)
fig,(a,b)=plt.subplots(1,2,figsize=(11.5,6));fig.patch.set_facecolor('white')
fig.suptitle('A wider capture window accepts signal and background',fontsize=17,y=.97)
a.plot(x,eff,color='#315f9c',lw=2.4,label=r'Genuine capture fraction $1-e^{-x}$')
a.plot(x,x/5,color='#a3364c',lw=2,ls='--',label=r'Accidental pair rate / value at $x=5$')
a.set(xlabel=r'Window / mean capture time, $x=W/\tau$',ylabel='Normalized response',xlim=(0,5),ylim=(0,1.05));a.legend(fontsize=10,loc='lower right')
b.plot(x,metric/norm,color='#657e38',lw=2.4);b.axvline(opt,color='#555',ls='--');b.plot(opt,1,'o',color='#657e38')
b.annotate(f'Chosen criterion peaks at\nx = {opt:.5f}',xy=(opt,.995),xytext=(2.3,.53),fontsize=12,arrowprops={'arrowstyle':'->'},linespacing=1.4)
b.set(xlabel=r'$x=W/\tau$',ylabel=r'Relative $S/\sqrt{B}$',xlim=(0,5),ylim=(0,1.12))
for ax in [a,b]:ax.grid(alpha=.2);ax.tick_params(labelsize=11);ax.xaxis.label.set_size(12);ax.yaxis.label.set_size(12)
fig.text(.5,.045,'Independent constant-rate backgrounds; exponential capture time; no lower timing cut or dead time.\nRight panel uses a background-dominated, large-count criterion. Original model, not an experimental optimization.',ha='center',fontsize=11,linespacing=1.45,color='#444')
fig.subplots_adjust(left=.075,right=.97,top=.86,bottom=.22,wspace=.28)
fig.savefig(Path(__file__).with_suffix('.png').name,dpi=110,facecolor='white');plt.close(fig)
