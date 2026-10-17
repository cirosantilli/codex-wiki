"""Original educational diagram. Python 3.14, NumPy and Matplotlib; writes a PNG basename in the current working directory."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white'})
def j1(x):
 term=x/2;out=term.copy()
 for k in range(1,65):term=term*(-x*x/4)/(k*(k+1));out+=term
 return out
t=np.linspace(0,2.4,8001);x=np.pi*t;jinc=np.ones_like(x);jinc[1:]=2*j1(x[1:])/x[1:];ratio=8.;binary=np.abs(jinc*np.cos(np.pi*ratio*t));envelope=np.abs(jinc)
fig,ax=plt.subplots(figsize=(8.5,4),layout='constrained');ax.plot(t,binary,color='#225c91',lw=1.4,label=r'$|[2J_1(x)/x]\cos(\pi\beta Y/\lambda)|$');ax.plot(t,envelope,color='#b25424',ls='--',lw=1.5,label='Uniform-disc envelope')
null=3.8317059702075125/np.pi;ax.axvline(null,color='#777',ls=':',lw=1.1);ax.text(null+.025,.64,r'$Y_0=1.21967\lambda/\alpha$',fontsize=10)
ax.scatter([1/16,3/16],[0,0],s=26,color='#b25424',zorder=5);ax.annotate(r'First binary zero: $Y=\lambda/(2\beta)$',xy=(1/16,0),xytext=(.18,.47),arrowprops={'arrowstyle':'->','color':'#555'},fontsize=10)
ax.annotate('',xy=(3/16,-.055),xytext=(1/16,-.055),arrowprops={'arrowstyle':'<->','color':'#555'});ax.text(.28,-.06,r'Zero spacing $\lambda/\beta$',ha='left',va='center',fontsize=9)
ax.set(xlabel=r'Baseline $\alpha Y/\lambda$',ylabel='Visibility',xlim=(0,2.4),ylim=(-.1,1.05),title=r'Equal uniform discs; $\alpha$ = angular diameter, $\beta=8\alpha$ along baseline')
ax.legend(fontsize=9,loc='upper right');ax.grid(alpha=.2)
fig.savefig('paper-1-oe2014-binary-visibility.png',dpi=150,facecolor='white');plt.close(fig)
