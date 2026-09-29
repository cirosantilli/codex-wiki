"""Original solution diagram. Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7. Output to current working directory."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path
plt.rcParams.update({"figure.facecolor":"white","axes.facecolor":"white","font.size":10,"axes.spines.top":False,"axes.spines.right":False})

a=.15;gamma=2;I=.74;f=lambda v:v*(a-v)*(v-1);d=np.sqrt(1-a+a*a);vl=(1+a-d)/3;vr=(1+a+d)/3;wl=f(vl);wr=f(vr)
def roots(w):return sorted(np.roots([1,-(1+a),a,w]).real)
left=roots(wr)[0];right=roots(wl)[-1]
fig,ax=plt.subplots(figsize=(6.8,4.3),layout='constrained');x=np.linspace(-.4,1.2,700);ax.plot(x,f(x),color='.5',label='W=f(v)');ax.plot(x,gamma*x-I,'--',color='#be6a2b',label='W=γv−I');xx=np.linspace(right,vr,200);ax.plot(xx,f(xx),lw=3,color='#227caa');xx=np.linspace(left,vl,200);ax.plot(xx,f(xx),lw=3,color='#227caa');ax.plot([vr,left],[wr,wr],color='#227caa');ax.plot([vl,right],[wl,wl],color='#227caa');ax.annotate('',(.83,f(.83)),(.9,f(.9)),arrowprops={'arrowstyle':'->','color':'#227caa','lw':2});ax.annotate('',(left+.04,wr),(vr-.04,wr),arrowprops={'arrowstyle':'->','color':'#227caa'});ax.annotate('',(right-.04,wl),(vl+.04,wl),arrowprops={'arrowstyle':'->','color':'#227caa'});ax.scatter([vl,vr],[wl,wr],color='black');ax.text(vl,wl-.025,r'$W_*$',ha='center');ax.text(vr,wr+.012,r'$W^*$',ha='center');ax.set(xlabel='v',ylabel='W = w − I',ylim=(-.08,.18),title='Shifted slow drift retains −I');ax.legend(fontsize=9)
fig.savefig(Path.cwd()/'2010-fhn-oscillation.png',dpi=150,facecolor='white');plt.close(fig)
