from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size':11,'axes.titlesize':13,'savefig.facecolor':'white'})
fig,axes=plt.subplots(1,3,figsize=(12.6,4.5),constrained_layout=True)
theta=np.linspace(0,np.pi,601);z=np.exp(1j*theta)*np.sin(theta)
ax=axes[0];ax.plot(z.real,z.imag,color='#126d8a',lw=2);ax.scatter([0,0],[0,.5],color=['#111111','#b64d36'],s=25,zorder=5)
ax.axhline(0,color='.6',lw=.8);ax.axvline(0,color='.6',lw=.8);ax.plot([-.22,.22],[0,0],color='#b64d36',lw=2)
i=105;ax.annotate('',xy=(z[i+18].real,z[i+18].imag),xytext=(z[i].real,z[i].imag),arrowprops={'arrowstyle':'->','color':'#126d8a','lw':2})
ax.annotate(r'$i/2$',xy=(0,.5),xytext=(.08,.52));ax.set(xlim=(-.66,.66),ylim=(-.15,1.15),xlabel=r'$\operatorname{Re}z$',ylabel=r'$\operatorname{Im}z$',title='Circle, traced twice')
ax.text(.5,.96,r'$\theta:0\to2\pi$',ha='center',va='top',transform=ax.transAxes)
u=np.array([2.,1.])/np.sqrt(5);w=np.array([-1.,2.])/np.sqrt(5);r=np.array([1.,0.])
ax=axes[1];ax.axhline(0,color='.6',lw=.8);ax.axvline(0,color='.6',lw=.8)
for direction,label in [(u,r"$\mathbf{e}'_1$"),(w,r"$\mathbf{e}'_2$")]:
 end=direction*1.32;ax.annotate('',xy=end,xytext=(0,0),arrowprops={'arrowstyle':'->','color':'#126d8a','lw':1.8});ax.text(*(end+.03),label,color='#126d8a')
for direction in [u,w]:
 foot=np.dot(r,direction)*direction;ax.plot([r[0],foot[0]],[r[1],foot[1]],'--',color='.5',lw=1)
ax.scatter([1],[0],color='#b64d36',s=35,zorder=5);ax.annotate(r'$\mathbf{r}=(1,0)$',xy=(1,0),xytext=(.55,-.35));ax.set(title='Same point, rotated axes',xlim=(-.8,1.48),ylim=(-.55,1.45),xlabel='$x$',ylabel='$y$')
ax.text(.97,.94,r"$\alpha'=(2,-1)/\sqrt{5}$",va='top',ha='right',transform=ax.transAxes)
ax=axes[2];ax.axhline(0,color='.6',lw=.8);ax.axvline(0,color='.6',lw=.8);xx=np.array([-.35,1.4]);ax.plot(xx,xx/2,color='.35',lw=1.4,label='$y=x/2$')
s=np.array([.6,.8])
for point,color,label in [(r,'#126d8a',r'$\mathbf{r}$'),(s,'#b64d36',r'$A\mathbf{r}$')]:
 ax.annotate('',xy=point,xytext=(0,0),arrowprops={'arrowstyle':'->','color':color,'lw':2});ax.text(*(point+np.array([.04,.03])),label,color=color)
ax.plot([r[0],s[0]],[r[1],s[1]],'--',color='.45');ax.scatter([.8],[.4],color='.3',s=18);ax.legend(loc='lower right',frameon=False);ax.set(title='Reflection, not rotation',xlim=(-.35,1.45),ylim=(-.35,1.15),xlabel='$x$',ylabel='$y$')
for ax in axes:ax.set_aspect('equal',adjustable='box');ax.grid(alpha=.15)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=110)
