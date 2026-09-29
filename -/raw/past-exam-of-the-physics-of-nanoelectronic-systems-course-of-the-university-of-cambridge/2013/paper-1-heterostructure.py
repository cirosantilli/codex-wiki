"""Original explanatory model; output is a basename in the working directory."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, FancyArrowPatch
plt.rcParams.update({'font.size':9,'axes.titlesize':10,'axes.labelsize':10})

fig,axs=plt.subplots(1,3,figsize=(11,4.1),layout='constrained');ax=axs[0]
x1=np.linspace(-3,0,300);x2=np.linspace(0,2.5,250);ax.plot(x1,.65*(-x1),color='black',lw=2);ax.plot([0,0],[0,.95],color='black',lw=2);ax.plot(x2,.95-.13*x2,color='black',lw=2);ax.axhline(.32,ls='--',color='#b2182b',label=r'$E_F$');ax.hlines(.15,-.65,-.02,color='#2166ac',lw=2);ax.hlines(.46,-1.1,-.02,color='#2166ac',lw=1,ls=':');ax.text(-2.5,1.2,'GaAs');ax.text(.3,1.25,'AlGaAs');ax.text(-.75,.01,'2DEG',fontsize=8);ax.set(xlabel='Depth coordinate (chosen units)',ylabel='Energy (arbitrary scale)',ylim=(-.1,1.8),title='Interface conduction band');ax.legend(fontsize=8)
ax=axs[1];layers=[('GaAs cap','#d9d9d9'),('Doped AlGaAs supply','#ef8a62'),('Undoped AlGaAs spacer','#fddbc7'),('Undoped GaAs channel','#d1e5f0'),('GaAs buffer/substrate','#92c5de')]
for i,(name,col) in enumerate(layers):ax.add_patch(Rectangle((0,4-i),3,.8,fc=col,ec='white'));ax.text(1.5,4.4-i,name,ha='center',va='center',fontsize=8)
ax.set(xlim=(-.1,3.1),ylim=(-.3,5.3),title='Qualitative growth stack');ax.axis('off')
ax=axs[2];ax.add_patch(Rectangle((-1.8,-1.5),3.6,3,fc='#eef4f6'))
for y in [-1.2,.5]:ax.add_patch(Rectangle((-1,y),2,.7,fc='#777777'));ax.text(0,y+.35,'Negative gate',ha='center',va='center',color='white',fontsize=8)
ax.plot([-1.8,1.8],[0,0],lw=5,color='#2166ac');ax.annotate('',xy=(.55,0),xytext=(-.55,0),arrowprops={'arrowstyle':'->','color':'white','lw':1.5});ax.text(0,-.35,'Ballistic channel',ha='center',fontsize=8);ax.set(xlim=(-2,2),ylim=(-1.6,1.6),title='Split-gate plan view');ax.axis('off')
fig.savefig('paper-1-heterostructure.png',dpi=170,facecolor='white');plt.close(fig)
