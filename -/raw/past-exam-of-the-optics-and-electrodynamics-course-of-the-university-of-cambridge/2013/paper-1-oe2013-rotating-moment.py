"""Original induction-driven rotating magnetic moment; PNG basename to cwd.
Python 3.14, NumPy, Matplotlib.
"""
import numpy as np
import matplotlib.pyplot as plt
u=np.linspace(0,2*np.pi,1001);mx=.5*np.sin(2*u);my=.5*(1-np.cos(2*u))
fig,(ax,bx)=plt.subplots(1,2,figsize=(9.1,3.7),layout='constrained')
ax.plot(u/(2*np.pi),np.sin(u),color='0.5',ls='--',label=r'$I/I_0$')
ax.plot(u/(2*np.pi),mx,color='#a74735',label=r'$m_x/m_0$');ax.plot(u/(2*np.pi),my,color='#2a6f9c',label=r'$m_y/m_0$')
ax.set(xlabel='Mechanical revolutions',ylabel='Normalized current / moment',title='One spin cycle, two moment cycles',xlim=(0,1),ylim=(-1.05,1.08));ax.legend(fontsize=9)
bx.plot(mx,my,color='#2a6f9c',lw=2);bx.plot(0,.5,'o',color='black',ms=4)
bx.annotate('',xy=(0,.5),xytext=(0,0),arrowprops={'arrowstyle':'-|>','color':'0.4','lw':1.5})
bx.text(.02,.53,'Static offset',fontsize=9)
for t in [np.pi/8,5*np.pi/8]:
 a=np.array([.5*np.sin(2*t),.5*(1-np.cos(2*t))]);tt=t+.12;b=np.array([.5*np.sin(2*tt),.5*(1-np.cos(2*tt))])
 bx.annotate('',xy=b,xytext=a,arrowprops={'arrowstyle':'-|>','color':'#a74735','lw':1.5})
bx.set(aspect='equal',xlabel=r'$m_x/m_0$',ylabel=r'$m_y/m_0$',title='Moment tip: offset rotating circle',xlim=(-.65,.65),ylim=(-.12,1.12))
fig.savefig('paper-1-oe2013-rotating-moment.png',dpi=140,facecolor='white')
