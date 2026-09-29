"""Python3.14; NumPy2.3.5/Matplotlib3.10.7. PNG basename only in cwd.
Caller MPLCONFIGDIR is honored; no hardcoded cache paths.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
phi=np.linspace(0,2*np.pi,1001)
x=np.cos(phi)**3;y=np.sin(phi)**3
fig,ax=plt.subplots(figsize=(5,5),dpi=120,facecolor='white')
ax.set_facecolor('white')
ax.plot(x,y,color='#0072b2',lw=2)
ax.axhline(0,color='#999999',lw=.7);ax.axvline(0,color='#999999',lw=.7)
ax.scatter([1],[0],color='black',s=34,zorder=5)
ax.annotate('t = 0\nrelative speed = 0',xy=(1,0),xytext=(.35,-.39),
            fontsize=10,arrowprops={'arrowstyle':'->','color':'black'})
m=np.sqrt(2)/4
ax.scatter([m],[m],color='#d55e00',s=45,zorder=6)
ax.annotate('First maximum speed\nωt = π/4,  v = 3ω/2',xy=(m,m),xytext=(-.99,.83),
            fontsize=10,arrowprops={'arrowstyle':'->','color':'#d55e00'})
q0=.50;q1=.69
ax.annotate('',xy=(np.cos(q1)**3,np.sin(q1)**3),
            xytext=(np.cos(q0)**3,np.sin(q0)**3),
            arrowprops={'arrowstyle':'->','color':'#0072b2','lw':1.6})
ax.set(xlim=(-1.15,1.15),ylim=(-1.15,1.15),xlabel="Rotating coordinate x′",
       ylabel="Rotating coordinate y′",title='Astroid motion in a rotating frame')
ax.set_aspect('equal');ax.set_xticks([-1,-.5,0,.5,1]);ax.set_yticks([-1,-.5,0,.5,1])
ax.grid(alpha=.16)
fig.subplots_adjust(left=.14,right=.96,bottom=.12,top=.9)
fig.savefig('paper-4-rotating-astroid.png',dpi=120,facecolor='white',transparent=False)
plt.close(fig)
