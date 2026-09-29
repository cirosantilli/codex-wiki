"""Original Hohmann and wrong-burn geometry; Python 3.14, NumPy, Matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white','savefig.facecolor':'white'})
t=np.linspace(0,2*np.pi,1200);arc=np.linspace(0,np.pi,600);alpha=3;lead=np.pi-np.pi*((1+alpha)/(2*alpha))**1.5
q=3-2*np.sqrt(2);e=1-q;rp=3*q/(1+e);bad_a=(3+rp)/2;bad_c=(rp-3)/2;bad_b=np.sqrt(3*rp)
fig,axs=plt.subplots(1,2,figsize=(10,4.5),layout='constrained');ax=axs[0]
ax.plot(np.cos(t),np.sin(t),color='#246d9c',ls=':',label='initial circle R');ax.plot(3*np.cos(t),3*np.sin(t),color='#7a5d9b',ls=':',label='station circle 3R');ax.plot(-1+2*np.cos(arc),np.sqrt(3)*np.sin(arc),color='#bd7831',lw=2,label='half-ellipse transfer');ax.add_patch(Circle((0,0),1/3,color='#bbbbbb'));ax.plot([1,-3],[0,0],'ko',ms=4)
ax.annotate('first burn: prograde',xy=(1,0),xytext=(1.1,-1.0),arrowprops={'arrowstyle':'->'},fontsize=8);ax.annotate('second burn: prograde',xy=(-3,0),xytext=(-3,-1.2),arrowprops={'arrowstyle':'->'},fontsize=8)
start=3*np.array([np.cos(lead),np.sin(lead)]);ax.plot(*start,'o',color='#7a5d9b',ms=5);ax.text(start[0]+.1,start[1]-.25,'station at launch',fontsize=8);ax.set(title='Rendezvous requires correct station phase',xlim=(-3.4,3.4),ylim=(-3.4,3.4),xlabel='x/R',ylabel='y/R',aspect='equal');ax.legend(fontsize=7,loc='lower right')
ax=axs[1];xx=bad_c+bad_a*np.cos(t);yy=bad_b*np.sin(t);outside=xx*xx+yy*yy>1/9;ax.plot(xx,np.where(outside,yy,np.nan),color='#b34040',lw=2,label='wrong-burn orbit outside Moon');ax.plot(xx,np.where(~outside,yy,np.nan),color='#b34040',lw=1.3,ls='--',label='formal continuation only');ax.add_patch(Circle((0,0),1/3,color='#cccccc',zorder=0));ax.plot(rp,0,'x',color='#b34040',ms=7);ax.annotate(f'formal pericentre\n{rp:.4f} R < R/3',xy=(rp,0),xytext=(-.52,-.5),arrowprops={'arrowstyle':'->'},fontsize=9);ax.text(-.12,.04,'Moon',fontsize=9);ax.set(xlim=(-.62,.62),ylim=(-.62,.62),aspect='equal',xlabel='x/R',ylabel='y/R',title='Reversed burn intersects the lunar surface');ax.legend(fontsize=7,loc='upper left')
for ax in axs:ax.grid(alpha=.15)
fig.savefig(Path(__file__).stem+'.png',dpi=150,bbox_inches='tight',facecolor='white');plt.close(fig)
