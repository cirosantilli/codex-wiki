"""Original model illustration; Python 3.14, NumPy 2.3, Matplotlib 3.10."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Circle
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False,'figure.facecolor':'white','savefig.facecolor':'white'})

fig,axs=plt.subplots(2,2,figsize=(10.6,8.1),layout='constrained')
ax=axs[0,0];ax.set(xlim=(-.5,10.7),ylim=(-.2,6));ax.axis('off');ax.set_title('Transcription complex: strand polarity and RNA exit')
ax.add_patch(Ellipse((5,2.6),7,4.8,fc='#edf1f5',ec='.45',lw=1.4));ax.text(5,4.6,r'RNA polymerase core + $\sigma$',ha='center',fontsize=11)
x=np.linspace(0,10,401);bubble=np.exp(-((x-5)/2.1)**6)
ax.plot(x,2.9+1.05*bubble,color='tab:blue',lw=2);ax.plot(x,2.45-.75*bubble,color='tab:orange',lw=2)
ax.text(-.1,3.35,"5′",ha='right');ax.text(10.1,3.35,"3′");ax.text(-.1,2.15,"3′",ha='right');ax.text(10.1,2.15,"5′")
ax.text(5,5.4,'non-template DNA',color='tab:blue',ha='center');ax.text(7,.15,'template DNA',color='tab:orange',ha='center')
ax.plot([1.4,2.5,3.4,5.4],[.1,.7,1.95,1.95],color='tab:green',lw=3);ax.text(1.1,.15,"5′ RNA",ha='right',color='tab:green');ax.plot(5.4,1.95,'o',color='tab:green',ms=5);ax.text(5.7,1.45,"3′ growth site",fontsize=9,color='tab:green')
ax.annotate('',xy=(6.5,.85),xytext=(4.6,.85),arrowprops={'arrowstyle':'->'});ax.text(5.55,.4,'enzyme advances',ha='center',fontsize=9)
ax=axs[0,1];ax.set(xlim=(-.5,10.5),ylim=(-.3,5));ax.axis('off');ax.set_title('One possible DNA reporter geometry')
for y,gap,label in [(3.5,2,'closed'),(1.3,4.3,'open')]:
    left=5-gap/2;right=5+gap/2
    ax.plot([0,10],[y,y],color='.5',lw=2)
    ax.plot(left,y,'o',color='tab:green',ms=11);ax.plot(right,y,'o',color='tab:red',ms=11)
    ax.annotate('',xy=(right,y+.5),xytext=(left,y+.5),arrowprops={'arrowstyle':'<->','color':'.3'})
    ax.text(0,y+.4,label,fontsize=10);ax.text(10,y-.5,'donor / acceptor',ha='right',fontsize=9)
ax.text(5,-.15,'Opening increases distance only for this chosen geometry',ha='center',fontsize=9)
A=4.;B=7.;r0=np.linspace(1,12,601);ea=1/(1+(A/r0)**6);eb=1/(1+(B/r0)**6);opt=np.sqrt(A*B)
axs[1,0].plot(r0,ea-eb,lw=2);axs[1,0].axvline(opt,color='.5',ls='--',label=rf'$R_0=\sqrt{{AB}}={opt:.2f}$ nm')
axs[1,0].set(xlabel=r'Förster distance $R_0$ (nm)',ylabel='efficiency contrast',title='Illustrative distances A = 4 nm, B = 7 nm');axs[1,0].legend(fontsize=9)
t=np.array([0,1,1,2.3,2.3,4,4,5,5,6.5,6.5,8]);state=np.array([0,0,1,1,0,0,1,1,0,0,1,1]);eclose=1/(1+(A/opt)**6);eopen=1/(1+(B/opt)**6);e=eclose+(eopen-eclose)*state
axs[1,1].plot(t,e,lw=2,color='purple');axs[1,1].set(xlabel='illustrative time (arbitrary units)',ylabel='FRET efficiency',ylim=(0,1),title='Toy reporter trace; not measured kinetics')
axs[1,1].text(.2,.88,'closed',fontsize=10);axs[1,1].text(1.2,.12,'open',fontsize=10)

fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white',transparent=False)
plt.close(fig)
