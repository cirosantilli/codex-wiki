import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,Rectangle
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False,'figure.facecolor':'white','savefig.facecolor':'white'})

h=np.linspace(-4,4,800);fig,ax=plt.subplots(1,2,figsize=(10,3.8),layout='constrained')
ax[0].plot(h,.17*h,label='Paramagnetic');ax[0].plot(h,-.06*h,label='Diamagnetic');ax[0].axhline(0,color='.7',lw=.7);ax[0].axvline(0,color='.7',lw=.7);ax[0].set(xlabel='Internal H (chosen units)',ylabel='Magnetization (chosen units)',title='Weak-field, reversible response');ax[0].legend()
hup=np.linspace(-4,4,500);hdown=hup[::-1];mup=np.tanh((hup-.65)/.6);mdown=np.tanh((hdown+.65)/.6)
ax[1].plot(hup,mup,color='#17639b');ax[1].plot(hdown,mdown,color='#17639b');ax[1].axhline(0,color='.7',lw=.7);ax[1].axvline(0,color='.7',lw=.7)
for xx in [-1.3,1.3]:
 for direction,offset in [(1,-.65),(-1,.65)]:
  x1=xx;x2=xx+.35*direction;ax[1].annotate('',xy=(x2,np.tanh((x2+offset)/.6)),xytext=(x1,np.tanh((x1+offset)/.6)),arrowprops={'arrowstyle':'->','color':'#17639b'})
ax[1].plot([-.65,.65],[0,0],'ro');ax[1].annotate('Coercive fields',xy=(.65,0),xytext=(1.5,-.5),arrowprops={'arrowstyle':'->'},fontsize=9);ax[1].plot(0,np.tanh(.65/.6),'ro');ax[1].annotate('Remanence',xy=(0,np.tanh(.65/.6)),xytext=(-3.7,.6),arrowprops={'arrowstyle':'->'},fontsize=9);ax[1].set(xlabel='Internal H (chosen units)',ylabel=r'$M/M_s$',title='Chosen ferromagnetic hysteresis model')
fig.suptitle('Illustrative response laws; not a fit to a material or a microscopic domain simulation',fontsize=11)
fig.savefig('paper-1-magnetic-response.png',dpi=155)
