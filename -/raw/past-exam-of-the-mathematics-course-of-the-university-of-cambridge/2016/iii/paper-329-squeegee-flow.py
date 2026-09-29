"""Generate paper-329-squeegee-flow.png in the caller's working directory."""
from pathlib import Path
import os
os.environ.setdefault('MPLCONFIGDIR',str(Path.cwd()/'.matplotlib-cache'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
fig,ax=plt.subplots(1,2,figsize=(11.6,4.4),dpi=100,facecolor='white')
w=np.linspace(-90,3,16000);h=1+np.exp(w)
X=h**3/9+h**2/6+h/3+w/3;x=40-X;ok=(x>=0)&(x<=65)
ax[0].plot(x[ok],h[ok],lw=2,label='Exact implicit profile')
xx=np.linspace(0,40,600);ax[0].plot(xx,(9*(40-xx))**(1/3),'--',color='#b8691c',label='Deep-pile approximation')
ax[0].axhline(1,color='gray',lw=1);ax[0].axvline(0,color='black',lw=4)
ax[0].set(xlim=(-1,65),ylim=(0,8),xlabel='Distance ahead of infinite blade, x',ylabel='Film thickness, h',title='Infinite blade: smooth tail to h = 1')
ax[0].legend(fontsize=8,loc='upper right');ax[0].grid(alpha=.15)
y=np.linspace(-1,1,400);z=np.linspace(0,1.3,300)
yy,zz=np.meshgrid(y,z);nose=np.maximum(0,1-yy**2)**(3/7)
height=np.maximum(0,nose-zz)**(1/3)
ax[1].contourf(yy,zz,np.ma.masked_where(zz>nose,height),levels=np.linspace(0,1,13),cmap='Blues')
ax[1].plot(y,(1-y**2)**(3/7),color='#176eab',lw=2)
ax[1].plot([-1,1],[0,0],color='black',lw=4)
for v in [-.7,0,.7]:ax[1].annotate('',(v,1.07),(v,1.35),arrowprops={'arrowstyle':'->','color':'#333'})
for sign in [-1,1]:
 ax[1].annotate('',(sign*.9,.17),(sign*.35,.4),arrowprops={'arrowstyle':'->','color':'#333','connectionstyle':'arc3,rad='+str(sign*.1)})
 ax[1].annotate('',(sign*1.15,-.19),(sign*.96,.14),arrowprops={'arrowstyle':'->','color':'#333','connectionstyle':'arc3,rad='+str(sign*.3)})
ax[1].text(0,.38,'deep pile, h ≫ 1',ha='center',color='#123b5a')
ax[1].text(0,-.21,'depleted near wake',ha='center',fontsize=9)
ax[1].text(0,1.3,'incoming film',ha='center',fontsize=9)
ax[1].set(xlim=(-1.3,1.3),ylim=(-.36,1.43),xlabel=r'Lateral position $y/\alpha$',ylabel=r'Distance ahead $x/x_N(0)$',title='Finite blade: schematic sideways drainage')
for a in ax:a.spines[['top','right']].set_visible(False)
fig.tight_layout();fig.savefig('paper-329-squeegee-flow.png',facecolor='white',transparent=False)
