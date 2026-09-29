"""Original schematic magnetic responses; Python 3.14/numpy/matplotlib.

No fitted anisotropy law. Equal moments and abrupt independent switching.
Output: PNG basename in the current working directory.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig,axes=plt.subplots(1,2,figsize=(9,3.8),layout='constrained')
fig.patch.set_facecolor('white')
t=np.linspace(1,4,300)
theta=np.pi/2*(1-(t-1)/3)
axes[0].plot(t,np.cos(theta),color='#2d718b',lw=2)
axes[0].set(xlabel='Co thickness (nm)',ylabel=r'$M_{r,\parallel}/M_s$',
            title='Chosen continuous canting interpolation',ylim=(-.05,1.08))
axes[0].text(1.15,.8,r'$M_{r,\parallel}=M_s\cos\theta$',fontsize=11)
h_down=np.linspace(2.2,-2.2,1000)
h_up=h_down[::-1]
c1,c2=.55,1.3
m_down=(np.where(h_down>-c1,1.,-1.)+np.where(h_down>-c2,1.,-1.))/2
m_up=(np.where(h_up>c1,1.,-1.)+np.where(h_up>c2,1.,-1.))/2
axes[1].plot(h_down,m_down,color='#2d718b',label='Decreasing field')
axes[1].plot(h_up,m_up,color='#b6623e',label='Increasing field')
axes[1].text(-1.2,.12,'Antiparallel',fontsize=9,color='#2d718b')
axes[1].text(.55,-.21,'Antiparallel',fontsize=9,color='#b6623e')
axes[1].set(xlabel='Perpendicular field (normalized)',ylabel=r'$m_{\rm total}/(2m)$',
            title='Equal moments; distinct coercive fields',ylim=(-1.2,1.25))
axes[1].legend(fontsize=8,loc='upper left')
for ax in axes:ax.grid(alpha=.17)
fig.savefig('paper-2-magnetic-memory.png',dpi=150,facecolor='white')
plt.close(fig)
