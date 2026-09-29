"""Original figure; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7. Output to caller CWD."""
import os
import tempfile
if 'MPLCONFIGDIR' not in os.environ:
    os.environ['MPLCONFIGDIR'] = tempfile.mkdtemp(prefix='ia2-logistic-mpl-')
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
lam=3.2
f=lambda u: lam*u*(1-u)
v=[.65]
for _ in range(45): v.append(f(v[-1]))
u=np.linspace(0,1,500)
minus=(lam+1-np.sqrt((lam-3)*(lam+1)))/(2*lam)
plus=(lam+1+np.sqrt((lam-3)*(lam+1)))/(2*lam)
fig,(a,b)=plt.subplots(1,2,figsize=(10,4.4),layout='constrained')
a.plot(u,f(u),lw=2,label=r'$F(u)=3.2u(1-u)$');a.plot(u,u,color='#777777',ls='--',label=r'$F(u)=u$')
x0,y0=v[0],0
for i in range(35):
    y1=v[i+1]
    a.plot([x0,x0,y1],[y0,y1,y1],color='#c06616',lw=1,alpha=.6)
    x0,y0=y1,y1
a.plot([minus,minus,plus,plus,minus],[minus,plus,plus,minus,minus],color='#882255',lw=1.5,label='Attracting two-cycle')
a.set(xlim=(0,1),ylim=(0,1),xlabel=r'$u_n$',ylabel=r'$u_{n+1}$',title='Cobweb from u₀ = 0.65');a.set_aspect('equal');a.legend(fontsize=8,loc='lower left')
b.plot(range(len(v)),v,'o-',ms=3,color='#1664ba',lw=1)
b.axhline(minus,color='#882255',ls='--',lw=1);b.axhline(plus,color='#882255',ls='--',lw=1)
b.axhline(1-1/lam,color='#777777',ls=':',lw=1,label='Unstable fixed point')
b.set(xlim=(0,45),ylim=(.48,.83),xlabel='Step n',ylabel=r'$u_n$',title='Alternation settles to a finite amplitude');b.legend(fontsize=9)
fig.savefig('paper-2-logistic.png',dpi=125,facecolor='white',transparent=False)
