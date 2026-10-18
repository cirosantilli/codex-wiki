"""Original oriented curve and enclosed region. Python 3.14, NumPy, Matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig,ax=plt.subplots(figsize=(6.5,4.8),layout='constrained');t=np.linspace(0,np.pi,1501);x=np.sin(2*t);y=np.sin(t)
ax.fill(x,y,color='tab:blue',alpha=.12);ax.plot(x,y,color='tab:blue',lw=2,label=r'$x=\sin 2t,\ y=\sin t$')
for tt in [.3,1.15,1.95,2.7]:
 p=np.array([np.sin(2*tt),np.sin(tt)]);v=np.array([2*np.cos(2*tt),np.cos(tt)]);v*=.11/np.linalg.norm(v);ax.annotate('',xy=p+v,xytext=p-v,arrowprops={'arrowstyle':'->','color':'black','lw':1.2})
yy=.55;xx=2*yy*np.sqrt(1-yy*yy);ax.annotate('',xy=(xx,yy),xytext=(-xx,yy),arrowprops={'arrowstyle':'<->','color':'tab:red'});ax.text(0,yy+.06,r'$4y\sqrt{1-y^2}$',ha='center',color='tab:red')
ax.plot(0,0,'o',color='black',ms=4);ax.text(.05,.04,'start / finish',fontsize=10);ax.set(xlabel='x',ylabel='y',ylim=(-.1,1.16),xlim=(-1.15,1.15),title='Positive circulation equals enclosed area');ax.set_aspect('equal');ax.legend(fontsize=10);ax.grid(alpha=.16)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white',transparent=False);plt.close(fig)
