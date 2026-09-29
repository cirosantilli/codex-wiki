"""Original solution diagram. Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7. Output to current working directory."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path
plt.rcParams.update({"figure.facecolor":"white","axes.facecolor":"white","font.size":10,"axes.spines.top":False,"axes.spines.right":False})

a=.15;f=lambda v:v*(a-v)*(v-1);mid=(2-a)/3;w0=f(mid);rr=sorted(np.roots([1,-(1+a),a,w0]).real);r1,r2,r3=rr;c=(1-2*a)/np.sqrt(2)
fig,axs=plt.subplots(1,2,figsize=(10.5,4),layout='constrained');xx=np.linspace(-.4,1.1,500);ax=axs[0];ax.plot(xx,f(xx),color='.6');ax.plot([0,1],[0,0],color='#227caa',lw=2);vv=np.linspace(1,r3,100);ax.plot(vv,f(vv),color='#227caa',lw=2);ax.plot([r3,r1],[w0,w0],color='#227caa',lw=2);vv=np.linspace(r1,0,100);ax.plot(vv,f(vv),color='#227caa',lw=2)
for label,v,w,dx,dy in [('A',0,0,-.06,-.024),('B',1,0,.02,-.024),('C',r3,w0,.02,.008),('D',r1,w0,-.04,.008)]:ax.scatter([v],[w],color='black',s=20);ax.text(v+dx,w+dy,label)
ax.annotate('',(.8,0),(.3,0),arrowprops={'arrowstyle':'->','color':'#227caa'});ax.annotate('',(r1+.08,w0),(r3-.08,w0),arrowprops={'arrowstyle':'->','color':'#227caa'});ax.set(xlabel='v',ylabel='w',ylim=(-.05,.16),title='A→B fast; B→C slow; C→D fast; D→A slow')
ax=axs[1];vv=np.linspace(0,1,400);pp=vv*(1-vv)/np.sqrt(2);ax.plot(vv,pp,lw=2);ax.scatter([0,1],[0,0],color='black');ax.text(.015,.008,'A');ax.text(.96,.008,'B');ax.annotate('',(.65,.65*.35/np.sqrt(2)),(.5,.25/np.sqrt(2)),arrowprops={'arrowstyle':'->'});ax.set(xlabel='v',ylabel='p = dv/dX',title='Increasing-front heteroclinic (w=0)',ylim=(-.015,.21))
fig.savefig(Path.cwd()/'2010-fhn-pulse.png',dpi=150,facecolor='white');plt.close(fig)
