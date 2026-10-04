"""Original weak-pressure channel profile; Python 3.14, root deps.

Emits matching PNG basename to caller CWD and honors MPLCONFIGDIR.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
Y=np.linspace(-1,1,400);n=.7;delta=.1
profile=Y+delta/(2*n)*(1-Y*Y)
fig,ax=plt.subplots(figsize=(5.8,4.3),layout='constrained',facecolor='white')
ax.plot(Y,Y,'--',color='#777777',label='Pure Couette flow')
ax.plot(profile,Y,color='#176b9b',lw=2,label='First-order pressure correction')
for yy,speed,label in [(-1,-1,r'Lower wall: $-U$'),(1,1,r'Upper wall: $+U$')]:
    ax.axhline(yy,color='#333333',lw=1.5)
    ax.annotate('',xy=(speed,yy),xytext=(speed-.23*np.sign(speed),yy),arrowprops={'arrowstyle':'->','lw':1.7,'color':'#333333'})
    ax.text(-1.16,yy+.07 if yy<0 else yy+.035,label,fontsize=10)
ax.set(xlim=(-1.2,1.2),ylim=(-1.12,1.12),xlabel=r'Velocity $u/U$',ylabel=r'Height $y/h$',title='Weak-pressure Couette–Poiseuille flow')
ax.text(.08,-.49,r'$n=0.7,\quad Gh/[k(U/h)^n]=0.1$',fontsize=10)
ax.legend(loc='upper left',bbox_to_anchor=(.0,.91),fontsize=8)
ax.axvline(0,color='#aaaaaa',lw=.65);ax.grid(alpha=.13);ax.set_facecolor('white')
fig.savefig('paper-78-channel-profile.png',dpi=130,facecolor='white',transparent=False)
plt.close(fig)
