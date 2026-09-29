"""Original physiological-model figures; writes PNGs to output CWD.
Tested Python3.14.4, numpy2.3.5, matplotlib3.10.7; repository pyproject.toml.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'figure.facecolor':'white','axes.facecolor':'white','font.size':10})
# Method of steps with RK4; all delayed RK stage times precede the current step.
tau=2;dt=.002;t=np.arange(0,40+dt/2,dt);u=np.empty(len(t));u[0]=.5
for i in range(len(t)-1):
 def old(s):return .5 if s<=0 else np.interp(s,t[:i+1],u[:i+1])
 y=u[i];a=y*(1-old(t[i]-tau));b=(y+dt*a/2)*(1-old(t[i]+dt/2-tau));c=(y+dt*b/2)*(1-old(t[i]+dt/2-tau));d=(y+dt*c)*(1-old(t[i]+dt-tau));u[i+1]=y+dt*(a+2*b+2*c+d)/6
past=np.where(t-tau<=0,.5,np.interp(np.maximum(t-tau,0),t,u));du=u*(1-past)
fig,axes=plt.subplots(1,3,figsize=(11,3.5),layout='constrained')
axes[0].plot(t,u);axes[0].axhline(1,color='gray',ls='--');axes[0].set(xlabel='Time',ylabel='u(t)',title='Delay-induced overshoot (τ=2)')
axes[1].plot(t,du);axes[1].axhline(0,color='gray',ls='--');axes[1].set(xlabel='Time',ylabel='du/dt',title='The response changes sign late')
x=np.linspace(0,2,300);axes[2].plot(x,x,label='λ');axes[2].plot(x,-np.exp(-np.pi*x/2),label='−exp(−λτc)');axes[2].axhline(0,color='gray',lw=.8);axes[2].set(xlabel='Real λ ≥ 0',ylabel='Characteristic sides',title='No nonnegative real root');axes[2].legend(fontsize=8)
for ax in axes:ax.grid(alpha=.2)
fig.suptitle('Delayed logistic feedback and its characteristic equation',fontsize=12);fig.savefig('2011-delay-feedback.png',dpi=140,facecolor='white');plt.close(fig)
