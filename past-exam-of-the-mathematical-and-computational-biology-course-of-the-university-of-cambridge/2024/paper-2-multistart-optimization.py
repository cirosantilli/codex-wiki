"""Original objective plot, with independently computed optimization landmarks."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq
f=lambda x:1+np.exp(-np.asarray(x)**2/5)*np.sin(5*np.asarray(x))
df=lambda x:5*np.cos(5*x)-.4*x*np.sin(5*x)
global_x=brentq(df,-.5,-.1);local_min=brentq(df,-1.8,-1.3);local_max=brentq(df,-1.1,-.7);constrained=brentq(df,2,2.4)
x=np.linspace(-4,4,1800)
fig,ax=plt.subplots(figsize=(8,4.7),layout='constrained',facecolor='white')
ax.plot(x,f(x),color='#245c9f',lw=2)
ax.axvspan(1.5,4,color='#e3f3e8',zorder=0);ax.axvline(1.5,color='.5',ls=':',lw=1)
for xx,label,pos in [(global_x,'Global minimum',(-2.1,.07)),(local_min,'Local minimum',(-3.4,.55)),(local_max,'Local maximum',(-3.4,1.8)),(constrained,'Minimum for x ≥ 1.5',(2.05,.25))]:
 ax.scatter([xx],[f(xx)],s=27,color='black',zorder=4)
 ax.annotate(label,(xx,float(f(xx))),pos,arrowprops={'arrowstyle':'->','color':'.4'},fontsize=10)
ax.set(xlim=(-4,4),ylim=(-.04,2.1),xlabel='x',ylabel='f(x)',title=r'$f(x)=1+e^{-x^2/5}\sin(5x)$')
ax.spines[['top','right']].set_visible(False)
fig.savefig(Path('paper-2-multistart-optimization.png'),dpi=125,facecolor='white');plt.close(fig)
