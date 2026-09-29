"""Original explanatory diagram; run in the desired output directory. Tested with Python 3.14, numpy and matplotlib."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon, Circle, FancyArrowPatch
plt.rcParams.update({"font.size":10,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})
fig,axs=plt.subplots(1,2,figsize=(10,3.8),layout='constrained')
a=axs[0];x=np.linspace(0,2.4,500);y=np.where(x>=1,1,np.sin(np.pi*np.clip(x,0,1)/2)**1.6)
a.plot(x,y,color='#1d6093',lw=2.3);a.axhline(.75,color='#b94b2f',ls='--',label='amplitude setpoint');a.annotate('approach',(1.05,.2),(2,.2),arrowprops={'arrowstyle':'->'})
a.text(1.65,1.035,'free oscillation',ha='center');a.text(.48,.32,'tapping / damping',rotation=50,ha='center');a.set(xlabel='Mean separation / free one-sided amplitude',ylabel=r'$A/A_{\rm free}$',ylim=(-.02,1.17),xlim=(0,2.4),title='Illustrative damping-only approach curve');a.legend(loc='lower right',fontsize=8)
a=axs[1];a.set_title('Height from feedback motion');a.set(xlim=(0,10),ylim=(0,7));a.axis('off')
for (x,y,w,h,t) in [(0,4.4,2.4,1.2,'Amplitude\ndetector'),(3.4,4.4,2.6,1.2,'Setpoint minus\nmeasured amplitude'),(7,4.4,2.8,1.2,'Controller'),(6.9,1.2,2.9,1.2,'z scanner /\nprobe interaction')]:
 a.add_patch(Rectangle((x,y),w,h,fc='#e6eff6',ec='#2b5a75'));a.text(x+w/2,y+h/2,t,ha='center',va='center',fontsize=9)
for start,end in [((2.4,5),(3.4,5)),((6,5),(7,5)),((8.4,4.4),(8.4,2.4)),((6.9,1.8),(1.2,1.8)),((1.2,1.8),(1.2,4.4))]:a.annotate('',end,start,arrowprops={'arrowstyle':'->'})
a.text(5.0,2.1,'cantilever motion',ha='center',fontsize=9);a.annotate('record z(x,y)',(8.4,3.2),(5.9,3.5),ha='center',arrowprops={'arrowstyle':'->'},color='#a04b22');a.text(4.8,.3,'Large height range uses scanner travel; amplitude stays near setpoint.',ha='center',fontsize=8.5)
fig.savefig('paper-1-tapping-control.png',dpi=160);plt.close(fig)
