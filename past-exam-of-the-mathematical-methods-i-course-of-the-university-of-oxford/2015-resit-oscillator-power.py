from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':12,'axes.titlesize':13,'figure.facecolor':'white','axes.facecolor':'white'})
fig,ax=plt.subplots(figsize=(8,5.2),layout='constrained');w=np.linspace(0,2.2,1500)
for gamma,color in [(.2,'#0072B2'),(.7,'#D55E00')]:
 response=gamma**2*w*w/((1-w*w)**2+gamma**2*w*w);ax.plot(w,response,label=rf'$\gamma/\omega_0={gamma:g}$',color=color,lw=2)
gamma=.2;low=(np.sqrt(4+gamma**2)-gamma)/2;high=low+gamma;ax.axhline(.5,c='.5',ls='--',lw=1);ax.scatter([low,high],[.5,.5],c='#0072B2',s=50,zorder=5)
for x,label in [(low,r'$\omega_1$'),(high,r'$\omega_2$')]:ax.plot([x,x],[.13,.5],c='#0072B2',ls=':',lw=1);ax.text(x,.07,label,ha='center',color='#0072B2')
ax.annotate('',xy=(low,.2),xytext=(high,.2),arrowprops={'arrowstyle':'<->','color':'#0072B2'});ax.text((low+high)/2,.25,r'$\Delta\omega=\gamma$',ha='center',color='#0072B2');ax.axvline(1,c='.75',ls=':',lw=1)
ax.set(xlim=(0,2.2),ylim=(0,1.08),xlabel=r'driving angular frequency $\omega/\omega_0$',ylabel=r'average power / peak power');ax.grid(alpha=.15);ax.legend(loc='upper right');ax.set_title('Power peak at the natural frequency; exact half-power bandwidth')
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white');plt.close(fig)
