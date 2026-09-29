"""Original beaming and schematic pulse drawing; PNG basename to cwd.
Python 3.14, NumPy, Matplotlib. Pulse is illustrative, not an exact synchrotron waveform.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
fig,(ax,bx)=plt.subplots(1,2,figsize=(8.8,3.8),layout='constrained')
t=np.linspace(0,2*np.pi,501);ax.plot(np.cos(t),np.sin(t),color='0.6',ls='--');ax.plot(1,0,'o',color='#bd512e',ms=8)
beam=np.array([[1,0],[1-.28,2.2],[1+.28,2.2]])
ax.add_patch(Polygon(beam,facecolor='#f8dc7f',alpha=.8,edgecolor='#d49a13'))
ax.annotate('',xy=(1,1.2),xytext=(1,0),arrowprops={'arrowstyle':'-|>','color':'#2c6c97','lw':2})
ax.annotate('',xy=(.18,0),xytext=(1,0),arrowprops={'arrowstyle':'-|>','color':'#9b4c38','lw':1.5})
ax.text(.28,-.22,'acceleration',fontsize=9);ax.text(1.08,1.02,'velocity',fontsize=9);ax.text(.3,2.3,r'cone width $\sim1/\gamma$',fontsize=10)
ax.set(xlim=(-1.35,1.7),ylim=(-1.2,2.65),aspect='equal',title='Tangent beaming');ax.axis('off')
u=np.linspace(-4,4,1001);bx.plot(u,np.exp(-u*u),color='#2c6c97',lw=2)
bx.annotate('',xy=(1,.37),xytext=(-1,.37),arrowprops={'arrowstyle':'<->','color':'0.3'})
bx.text(0,.44,r'$\Delta t\sim\rho/(\gamma^3c)$',ha='center',fontsize=11)
bx.set(xlabel='Arrival-time offset (relative scale)',ylabel='Illustrative pulse amplitude',title='Compressed pulse: schematic',ylim=(-.02,1.1),yticks=[0,1])
fig.savefig('paper-1-oe2013-synchrotron-cone.png',dpi=140,facecolor='white')
