"""Original explanatory diagram; run in the desired output directory. Tested with Python 3.14, numpy and matplotlib."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon, Circle, FancyArrowPatch
plt.rcParams.update({"font.size":10,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})
fig,axs=plt.subplots(1,2,figsize=(10,3.8),layout='constrained')
a=axs[0];a.set_title('Aperture-cone approximation')
a.plot([-1.2,-.23],[2.6,2.6],color='black',lw=5);a.plot([.23,1.2],[2.6,2.6],color='black',lw=5)
a.plot([-.23,0,.23],[2.6,.35,2.6],color='#165a96',lw=1.8)
a.plot([-1.2,1.2],[.3,.3],color='black',lw=2)
a.annotate('',(-.23,2.9),(.23,2.9),arrowprops={'arrowstyle':'<->'});a.text(0,3.0,r'$2r_a=50\,\mu$m',ha='center')
a.annotate('',(.65,.35),(.65,2.6),arrowprops={'arrowstyle':'<->'});a.text(.73,1.5,r'$L\simeq2.4$ mm',rotation=90,va='center')
a.plot([0,0],[.35,2.6],ls=':',color='#999');a.text(.08,1,r'$\alpha$',color='#165a96');a.text(0,.06,r'probe diameter $d_o$',ha='center');a.set(xlim=(-1.5,1.5),ylim=(-.2,3.5));a.axis('off')
a=axs[1];a.set_title('One possible section through porous relief')
x=np.array([0,.5,.65,.85,1.05,1.2,1.5,1.8,1.9,2.15,2.45,2.7,3.1,3.25,3.45,3.6,4])
y=np.array([.8,.8,2.3,2.35,.85,.7,.65,2.1,2.2,.8,.7,.85,2.45,2.55,.85,.7,.8])
a.fill_between(x,.15,y,color='#c7dbe8');a.plot(x,y,color='#245774',lw=2)
for z in [.75,1.85,3.2]:a.annotate('SE escape',(z,2.3),(z+.18,3.1),ha='center',fontsize=9,arrowprops={'arrowstyle':'<-','color':'#c56116'})
a.text(2.25,.3,'solid',ha='center');a.text(2.55,1.5,'recess',ha='center');a.annotate('incident beam',(2.6,1),(2.6,2.6),ha='center',arrowprops={'arrowstyle':'->','color':'#165a96'})
a.set(xlim=(-.1,4.1),ylim=(0,3.6));a.axis('off')
fig.savefig('paper-1-sem-relief.png',dpi=160);plt.close(fig)
