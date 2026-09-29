"""Original explanatory model; output is a basename in the working directory."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, FancyArrowPatch
plt.rcParams.update({'font.size':9,'axes.titlesize':10,'axes.labelsize':10})

fig,axs=plt.subplots(1,3,figsize=(11,3.6),layout='constrained')
ax=axs[0];ax.plot([-1.6,-.65],[0,0],color='black');ax.plot([.65,1.6],[0,0],color='black');ax.add_patch(Circle((0,0),.6,fc='#d1e5f0',ec='#2166ac'));ax.add_patch(Rectangle((-.9,-.45),.12,.9,color='#b2182b'));ax.add_patch(Rectangle((.78,-.45),.12,.9,color='#b2182b'));ax.text(-1.4,.35,'S');ax.text(1.3,.35,'D');ax.annotate('',xy=(.45,.1),xytext=(0,.46),arrowprops={'arrowstyle':'->','connectionstyle':'arc3,rad=-.25'});ax.text(0,-.9,'Potential well; two series barriers',ha='center',fontsize=8);ax.set(xlim=(-1.8,1.8),ylim=(-1.2,1.2),title='Dot orbit and series path');ax.set_aspect('equal');ax.axis('off')
ax=axs[1]
for y,sgn in [(1,1),(-1,-1)]:ax.plot([-1.7,1.7],[y,y],color='black');ax.annotate('',xy=(sgn*.4,y),xytext=(-sgn*.4,y),arrowprops={'arrowstyle':'->'})
ax.add_patch(Circle((0,0),.35,fc='white',ec='black'));ax.add_patch(Circle((0,0),.65,fill=False,ec='#2166ac'));ax.annotate('',xy=(-.2,.62),xytext=(.3,.57),arrowprops={'arrowstyle':'->','color':'#2166ac','connectionstyle':'arc3,rad=.2'});ax.plot([0,0],[.65,1],ls=':',color='#b2182b');ax.plot([0,0],[-1,-.65],ls=':',color='#b2182b');ax.text(0,-1.4,'Potential hill; coupling to open edges',ha='center',fontsize=8);ax.set(xlim=(-1.9,1.9),ylim=(-1.6,1.35),title='Antidot orbit');ax.set_aspect('equal');ax.axis('off')
x=np.linspace(0,5,1200);L=sum(.07**2/((x-t)**2+.07**2) for t in [1,2.5,4]);L=np.clip(L,0,1);axs[2].plot(x,L,lw=1.8,label='Series dot');axs[2].plot(x,2-L,lw=1.8,label='Antidot reflection example');axs[2].set(xlabel='Gate tuning (chosen units)',ylabel=r'$G/(e^2/h)$',title='Different backgrounds and signs',ylim=(-.1,2.15));axs[2].legend(fontsize=8)
fig.savefig('paper-1-dot-comparison.png',dpi=170,facecolor='white');plt.close(fig)
