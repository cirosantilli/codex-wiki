"""Original explanatory model; output is a basename in the working directory."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, FancyArrowPatch
plt.rcParams.update({'font.size':9,'axes.titlesize':10,'axes.labelsize':10})

fig,axs=plt.subplots(1,3,figsize=(11,3.8),layout='constrained')
for ax,title,mu,ys in [(axs[0],'Energy selection',1,[.6,1.4]),(axs[1],'Rate selection',.4,[1.2,1.5])]:
 ax.plot([.1,.1,.9,.9],[1.9,.1,.1,1.9],color='black');ax.axhline(mu,color='grey',ls=':',lw=1);ax.text(1.05,mu+.05,r'$\mu_R$',fontsize=9)
 for y,col in zip(ys,['#2166ac','#b2182b']):ax.hlines(y,.25,.75,color=col,lw=2)
 ax.annotate('',xy=(1.3,ys[1]),xytext=(.8,ys[1]),arrowprops={'arrowstyle':'->','color':'#b2182b','lw':2});ax.text(.3,ys[1]+.12,'Fast / allowed',fontsize=8)
 if mu<ys[0]:ax.annotate('',xy=(1.3,ys[0]),xytext=(.8,ys[0]),arrowprops={'arrowstyle':'->','color':'#2166ac','lw':.7});ax.text(.27,.75,'Slow but allowed',fontsize=8)
 else:ax.text(.27,.3,'Ground state retained',fontsize=8)
 ax.set(xlim=(0,1.6),ylim=(0,2.2),title=title);ax.set_xticks([]);ax.set_ylabel('Removal energy (chosen units)');ax.set_yticks([])
t=np.linspace(0,1,600);r=20;err=.5*(np.exp(-r*t)+1-np.exp(-t));opt=np.log(r)/(r-1);axs[2].plot(t,err,lw=2);axs[2].axvline(opt,ls=':',color='grey');axs[2].plot(opt,.5*(np.exp(-r*opt)+1-np.exp(-opt)),'o');axs[2].set(xlabel=r'$\Gamma_s\tau$',ylabel='Ideal mean error',ylim=(0,.52),title=r'Chosen rate ratio $\Gamma_f/\Gamma_s=20$');axs[2].grid(alpha=.2)
fig.savefig('paper-1-spin-readout.png',dpi=170,facecolor='white');plt.close(fig)
