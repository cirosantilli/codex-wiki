"""Self-gravitating slab dispersion curves.
Python 3.14; NumPy 2.3.5 and Matplotlib 3.10.7.
Run with mirrored _media directory as cwd; outputs only the basename PNG.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
q=np.linspace(.0001,2.8,800)
even=q*np.tanh(q)-.5*(1-np.exp(-2*q))
odd=q/np.tanh(q)-.5*(1+np.exp(-2*q))
lo,hi=.5,1.
for _ in range(60):
 mid=(lo+hi)/2
 if mid-(1+np.exp(-2*mid))/2>0:hi=mid
 else:lo=mid
qc=(lo+hi)/2
fig,ax=plt.subplots(figsize=(6.5,3.5),dpi=120,facecolor='white')
ax.set_facecolor('white')
ax.axhline(0,color='#777777',lw=1)
ax.plot(q,even,color='#b64a35',lw=2,label='Even: thickness mode')
ax.plot(q,odd,color='#265b91',lw=2,label='Odd: bending mode')
ax.fill_between(q,even,0,where=even<0,color='#b64a35',alpha=.18)
ax.axvline(qc,color='#777777',lw=1,ls=':')
ax.text(qc+.035,.7,fr'$q_c={qc:.6f}$',rotation=90,va='center',fontsize=10)
ax.text(.13,-.26,'Even-mode instability',fontsize=9,color='#993523')
ax.set(xlim=(0,2.8),ylim=(-.32,2.55),xlabel=r'$q=kH$',ylabel=r'$\omega^2/(2\pi G\Sigma/H)$',title='Surface modes of a self-gravitating slab')
ax.legend(loc='upper left',frameon=False,fontsize=10)
ax.grid(alpha=.15)
fig.subplots_adjust(left=.115,right=.975,bottom=.16,top=.88)
fig.savefig('paper-314-slab-dispersion.png',dpi=120,facecolor='white',transparent=False)
plt.close(fig)
