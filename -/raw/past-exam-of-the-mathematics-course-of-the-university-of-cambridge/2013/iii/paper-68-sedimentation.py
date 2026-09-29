"""Original sketch; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Run with an externally supplied MPLCONFIGDIR. Writes only its PNG basename to cwd.
"""
import math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig,axes=plt.subplots(1,2,figsize=(11,6.4),dpi=100,layout='constrained')
for ax,lam,endpoint in zip(axes,[.5,2.],[math.pi/4,-3*math.pi/4]):
    th=np.linspace(0,endpoint*.93,1000)
    psi=th-math.pi/4
    x=2/3*(1+np.sin(th)-np.cos(th))
    z=2*math.sqrt(2)*(1+2*lam)/(3*(1-lam))*np.log(np.abs(np.tan(psi/2))/math.tan(math.pi/8))-2*math.sqrt(2)/3*(np.cos(psi)-1/math.sqrt(2))
    ax.plot(x,z,color='black',lw=2,label='trajectory of O')
    targets=np.linspace(0,min(12,-z[-1]),5)
    for d in targets:
        i=np.argmin(np.abs(z+d)); t=th[i]; origin=np.array([x[i],z[i]])
        # Full rods are 2L long. Axes are in units of L, with equal aspect.
        ends=[origin+2*np.array([np.cos(t),np.sin(t)]),origin+2*np.array([-np.sin(t),np.cos(t)])]
        for end in ends:
            ax.plot([origin[0],end[0]],[origin[1],end[1]],color='#3579a6',lw=2)
            ax.scatter(*end,s=40*lam,color='#e6a029',zorder=3)
        ax.scatter(*origin,s=40,color='#942b37',zorder=3)
    ax.axvline(2/3,ls=':',color='#888888',label='final x = 2L/3')
    ax.set(xlim=(-2.6,3),ylim=(-14,3),xlabel='horizontal displacement / L',ylabel='height of O / L',title=f'end/joint mass ratio λ = {lam:g}')
    ax.set_aspect('equal'); ax.grid(alpha=.15); ax.legend(loc='lower left',fontsize=8)
    inset=ax.inset_axes([1.05,.53,.85,.31])
    for angle in [endpoint,endpoint+math.pi/2]:
        end=2*np.array([math.cos(angle),math.sin(angle)])
        inset.plot([0,end[0]],[0,end[1]],color='#3579a6',lw=2)
        inset.scatter(*end,s=40*lam,color='#e6a029')
    inset.scatter(0,0,s=40,color='#942b37')
    inset.set(xlim=(-2.6,2.6),ylim=(-2.6,2.6)); inset.set_aspect('equal'); inset.axis('off')
    inset.set_title('limiting orientation\n'+('θ = π/4' if lam<1 else 'θ = −3π/4'),fontsize=8)
fig.savefig('paper-68-sedimentation.png',facecolor='white',transparent=False)
