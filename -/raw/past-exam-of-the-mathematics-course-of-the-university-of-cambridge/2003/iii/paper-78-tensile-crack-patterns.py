"""Generate the fixed-radius displacement sketch; write the PNG in caller CWD."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

theta=np.linspace(0,2*np.pi,24,endpoint=False)
e=np.column_stack([np.sin(theta),np.cos(theta)])
c=np.cos(theta)
n=np.array([0.,1.])
patterns=[(1+2*c*c)[:,None]*e,2*c[:,None]*(n-c[:,None]*e),(6*c*c-1)[:,None]*e+2*c[:,None]*n]
titles=['Transient P displacement','Transient S displacement','Final static displacement']
subtitles=[r'$\mathbf{u}_P\propto(1+2\cos^2\theta)\,\mathbf{e}$',r'$\mathbf{u}_S\propto2\cos\theta(\mathbf{n}-\cos\theta\,\mathbf{e})$',r'$\mathbf{u}_{\mathrm{stat}}\propto(6\cos^2\theta-1)\mathbf{e}+2\cos\theta\,\mathbf{n}$']
fig,axes=plt.subplots(1,3,figsize=(10.5,3.65),layout='constrained',facecolor='white')
for ax,vec,title,subtitle,color in zip(axes,patterns,titles,subtitles,['#2166ac','#c34a27','#298250']):
 scaled=.42*vec/np.max(np.linalg.norm(vec,axis=1))
 circle=np.linspace(0,2*np.pi,400)
 ax.plot(np.sin(circle),np.cos(circle),color='#bfc4c9',lw=1)
 ax.quiver(e[:,0],e[:,1],scaled[:,0],scaled[:,1],angles='xy',scale_units='xy',scale=1,width=.011,headwidth=3.3,headlength=4.5,color=color)
 ax.plot([-.35,.35],[0,0],color='#292d31',lw=3)
 ax.annotate('',xy=(0,.55),xytext=(0,0),arrowprops={'arrowstyle':'->','color':'#292d31','lw':1.3})
 ax.text(.05,.49,r'$\mathbf{n}$',fontsize=10)
 ax.text(0,-.13,'crack',ha='center',va='top',fontsize=8,color='#555555')
 ax.set(xlim=(-1.57,1.57),ylim=(-1.57,1.57),aspect='equal')
 ax.axis('off');ax.set_title(title+'\n'+subtitle,fontsize=10,pad=7)
fig.suptitle('Tensile opening in a Poisson solid: fixed observation radius',fontsize=13)
fig.text(.5,.015,'Crack normal is vertical. Positive opening rate for P/S; positive final opening for static field. Panels scaled independently.',ha='center',fontsize=8,color='#444444')
fig.savefig(Path('paper-78-tensile-crack-patterns.png'),dpi=150,facecolor='white')
plt.close(fig)
