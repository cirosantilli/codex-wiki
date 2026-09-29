"""Original teaching plot. Python3.14, NumPy and Matplotlib. Writes basename PNG to cwd."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
x=np.linspace(-5,4,3001)
def pulse(s):
 return np.where((s>=-1)&(s<=.5),(s+1)/1.5,np.where((s>.5)&(s<=1),2*(1-s),0))
fig,axs=plt.subplots(2,1,figsize=(8.4,5.4),layout='constrained',sharex=True)
axs[0].plot(x,pulse(x+3)*(x<0),color='#306d9b',lw=2.2)
axs[1].plot(x,-pulse(-x-3)/3*(x<0),color='#a54b29',lw=2.2,label='Reflected: height 1/3, width unchanged')
axs[1].plot(x,2*pulse(2*x-3)/3*(x>=0),color='#267759',lw=2.2,label='Transmitted: height 2/3, half width')
axs[0].set_title('Incident profile: illustrative density ratio 4')
axs[1].set_title('Later snapshot after the junction crossing')
for ax in axs:
 ax.axvline(0,color='black',ls=':');ax.axhline(0,color='gray',lw=.7);ax.set(ylabel='Displacement / incident height',ylim=(-.48,1.18));ax.grid(alpha=.15)
axs[1].set_xlabel('Distance / incident half-width');axs[1].legend(loc='upper left',fontsize=9)
axs[0].annotate('',xy=(-1.7,1),xytext=(-2.4,1),arrowprops={'arrowstyle':'->'})
axs[1].annotate('',xy=(-4.3,-.37),xytext=(-3.7,-.37),arrowprops={'arrowstyle':'->','color':'#a54b29'})
axs[1].annotate('',xy=(2.9,.84),xytext=(2.3,.84),arrowprops={'arrowstyle':'->','color':'#267759'})

fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=140,facecolor='white')
