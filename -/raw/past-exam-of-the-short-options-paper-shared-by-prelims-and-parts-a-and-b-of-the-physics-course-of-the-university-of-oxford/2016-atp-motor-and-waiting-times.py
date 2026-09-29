from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11})

from matplotlib.patches import Circle,Rectangle
fig,axs=plt.subplots(1,3,figsize=(12,4.6),layout='constrained',facecolor='white')
ax=axs[0];z=np.linspace(0,3.4,400);a=np.cos(2*np.pi*z/3.4);ax.plot(a,z,color='#126782',lw=2);ax.plot(-a,z,color='#b14c2e',lw=2)
for zz in np.arange(0,3.41,.34):aa=np.cos(2*np.pi*zz/3.4);ax.plot([-aa,aa],[zz,zz],color='gray',lw=1)
ax.annotate('',(-1,-.25),(1,-.25),arrowprops={'arrowstyle':'<->'});ax.text(0,-.5,'2 nm diameter',ha='center');ax.text(0,3.7,'~10 base pairs per 3.4 nm turn',ha='center',fontsize=9);ax.set(xlim=(-1.5,1.5),ylim=(-.7,4),title='B-DNA geometry');ax.axis('off')
ax=axs[1];ax.set(xlim=(0,5),ylim=(0,6));ax.axis('off');ax.add_patch(Rectangle((.2,1.3),4.6,.65,color='#dcebf0'));ax.add_patch(Circle((2.5,1.62),.6,color='#126782'));ax.plot([2.5,2.5],[1.7,4],lw=6,color='#b14c2e');ax.add_patch(Circle((2.5,4.1),1.05,fill=False,lw=3,color='#126782'));ax.plot([4.3,4.3],[1.6,4.5],lw=3,color='gray');ax.text(2.5,5.4,'F1: alpha/beta head',ha='center');ax.text(2.5,.6,'Fo: membrane rotor',ha='center');ax.text(2.1,2.7,'Gamma\nshaft',ha='right');ax.text(4.4,3.2,'Stator',rotation=90);ax.set_title('ATP-synthase motor')
t=np.linspace(0,6,500);k1=1.;ka=2.;kb=.8;P1=k1*np.exp(-k1*t);P2=ka*kb/(ka-kb)*(np.exp(-kb*t)-np.exp(-ka*t));ax=axs[2];ax.plot(t,P1,label='One binding wait',color='#126782');ax.plot(t,P2,label='Two sequential waits',color='#b14c2e');ax.set(xlabel='Time (scaled)',ylabel='Probability density',title='Kinetic waiting-time signatures');ax.legend(fontsize=9)

fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white',transparent=False,metadata={'Software':'Matplotlib'})
plt.close(fig)
