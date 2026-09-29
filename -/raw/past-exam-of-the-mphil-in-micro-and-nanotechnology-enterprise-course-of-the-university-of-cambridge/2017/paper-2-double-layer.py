"""Original explanatory figure; Python 3.14, matplotlib 3.10, numpy 2.3. Writes a basename PNG to cwd, normally mirrored _media."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,Rectangle,Polygon,Arc
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white'})

fig,axs=plt.subplots(1,2,figsize=(8,3.6));ax=axs[0];ax.set(xlim=(-1.7,1.7),ylim=(-1.7,1.7),aspect='equal');ax.axis('off');ax.add_patch(Circle((0,0),.65,facecolor='#c3dbe4',edgecolor='#456777'));ax.add_patch(Circle((0,0),.95,fill=False,ls='--',edgecolor='#a6804f'))
for th in np.arange(0,2*np.pi,np.pi/4):
 ax.text(.6*np.cos(th),.6*np.sin(th),'−',ha='center',va='center',color='#35698c');ax.text(.83*np.cos(th),.83*np.sin(th),'+',ha='center',va='center',color='#b86628')
for x,y,s in [(-1.2,.5,'+'),(1.15,.3,'+'),(.8,1.2,'+'),(-.8,-1.2,'+'),(1.4,-.8,'−'),(-1.3,1.2,'−')]:ax.text(x,y,s,ha='center',va='center')
ax.text(0,0,'Charged\nparticle',ha='center');ax.text(0,-1.55,'Compact layer → diffuse ions',ha='center',fontsize=9)
x=np.linspace(0,4,401);potential=np.where(x<.4,-1+.5*x,-.8*np.exp(-(x-.4)));axs[1].plot(x,potential,color='#176b9a');axs[1].axhline(0,color='.6',lw=.7);axs[1].axvline(.4,color='#a6804f',ls='--');axs[1].axvline(.65,color='#4e9966',ls=':');axs[1].text(.48,-.3,'Slip plane\n(zeta potential)',fontsize=8);axs[1].set(xlabel='Distance from surface (scaled)',ylabel='Potential (scaled)',ylim=(-1.15,.1));fig.tight_layout()

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
