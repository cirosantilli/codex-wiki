"""Original Jones-eigenvector solution figure; Python 3.14, root dependencies.
Write the opaque PNG basename in cwd, including its mirrored _media directory.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

a, b = .75, .25  # Illustrative amplitude coefficients, not additional exam data.
lp, lm = a+b, a-b
phi = np.pi/4
vp = lp/2*np.array([np.cos(phi),-np.sin(phi)])
vm = lm/2*np.array([np.cos(phi),np.sin(phi)])
total = vp+vm
fig, (vectors, trajectory) = plt.subplots(1,2,figsize=(8.8,4.1),dpi=130,facecolor='white')
for ax in (vectors,trajectory):
    ax.axhline(0,color='.75',lw=.8)
    ax.axvline(0,color='.75',lw=.8)
    ax.set_aspect('equal')
    ax.spines[['top','right']].set_visible(False)
    ax.set(xlabel=r'$E_x/E_0$',ylabel=r'$E_y/E_0$')
for start,end,color in [(np.zeros(2),vp,'#31688e'),(vp,total,'#d55e00'),
                         (np.zeros(2),total,'#009e73')]:
    vectors.annotate('',end,start,arrowprops=dict(arrowstyle='->',color=color,lw=2.5))
vectors.plot([0,vm[0]],[0,vm[1]],'--',color='#d55e00',lw=1.4)
vectors.text(.04,-.39,r'$\lambda_+\mathbf{u}_+$ component',fontsize=9,color='#31688e')
vectors.text(.25,.13,r'$\lambda_-\mathbf{u}_-$ component',fontsize=9,color='#d55e00')
vectors.text(.40,-.13,'sum',fontsize=10,color='#009e73')
vectors.set(xlim=(-.1,.9),ylim=(-.48,.43),title=r'Real vectors at $\omega t=\pi/4$')
t=np.linspace(0,2*np.pi,600)
trajectory.plot(a*np.cos(t),-b*np.sin(t),color='#009e73',lw=2)
trajectory.annotate('',total,(0,0),arrowprops=dict(arrowstyle='->',color='#009e73',lw=2))
for q in [.3,2.1,3.5,5.2]:
    trajectory.annotate('',(a*np.cos(q+.25),-b*np.sin(q+.25)),(a*np.cos(q),-b*np.sin(q)),
                        arrowprops=dict(arrowstyle='->',color='#009e73',lw=1.5))
trajectory.set(xlim=(-.95,.95),ylim=(-.6,.6),title=r'$E_x=aE_0\cos\omega t,\ E_y=-bE_0\sin\omega t$')
fig.suptitle(r'Illustration: $a=0.75,\ b=0.25,\ \lambda_+=1,\ \lambda_-=0.5$',fontsize=12)
fig.tight_layout()
fig.savefig(Path(__file__).with_suffix('.png').name,facecolor='white',transparent=False)
plt.close(fig)
