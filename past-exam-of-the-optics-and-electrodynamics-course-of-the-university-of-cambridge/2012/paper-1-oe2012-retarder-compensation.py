import numpy as np
import matplotlib.pyplot as plt
def R(t):return np.array([[np.cos(t),np.sin(t)],[-np.sin(t),np.cos(t)]])
def plate(angle,phase):return R(-angle)@np.diag([1,np.exp(1j*phase)])@R(angle)
def composite(eps):return plate(5*np.pi/12,np.pi/2+eps)@plate(np.pi/12,np.pi+2*eps)@np.array([1.,0.])
def single(eps):return plate(np.pi/4,np.pi/2+eps)@np.array([1.,0.])
es=np.geomspace(.001,.6,600)
fig,axes=plt.subplots(1,2,figsize=(10.0,4.4),layout='constrained')
for f,label,color in [(single,'Single quarter-wave plate','#c94a39'),(composite,'Half-wave + quarter-wave','#2475aa')]:
 error=[abs(f(e)[1]/f(e)[0]+1j) for e in es]
 axes[0].loglog(es,error,label=label,color=color,lw=2)
axes[0].loglog(es,es,color='#aaa',ls=':',lw=1,label=r'Reference slope 1')
axes[0].loglog(es,.5*es**2,color='#777',ls='--',lw=1,label=r'Reference slope 2')
axes[0].set(xlabel=r'Shared quarter-wave error $\epsilon$ (rad)',ylabel=r'Polarization-ratio error $|J_y/J_x+i|$',title='First-order error is cancelled for x input');axes[0].legend(frameon=False,fontsize=9);axes[0].grid(alpha=.2,which='both')
t=np.linspace(0,2*np.pi,1000)
for J,label,color,ls in [(composite(0),'Ideal circular output','#555','--'),(composite(.5),'Composite, error 0.5 rad','#2475aa','-'),(single(.5),'Single plate, error 0.5 rad','#c94a39','-')]:
 J=J*np.exp(-1j*np.angle(J[0]));E=np.sqrt(2)*np.real(J[:,None]*np.exp(-1j*t))
 axes[1].plot(E[0],E[1],color=color,ls=ls,lw=2,label=label)
axes[1].set(xlabel=r'$\sqrt{2} E_x$',ylabel=r'$\sqrt{2} E_y$',aspect='equal',xlim=(-1.25,1.25),ylim=(-1.25,1.25),title='Electric-vector trajectories (normalized)');axes[1].grid(alpha=.2);axes[1].legend(frameon=False,fontsize=8,loc='lower left')
fig.savefig('paper-1-oe2012-retarder-compensation.png',dpi=160,facecolor='white')
