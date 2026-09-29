"""Original mathematical plots. Python 3.14 / NumPy 2.3.5 / Matplotlib 3.10.7.
Preserves caller MPLCONFIGDIR; writes its PNG basename to cwd.
"""
import math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig=plt.figure(figsize=(11,7.6),dpi=100,layout='constrained')
grid=fig.add_gridspec(2,2); a=fig.add_subplot(grid[0,0]); b=fig.add_subplot(grid[0,1]); c=fig.add_subplot(grid[1,:])
k=np.linspace(-1.35,1.35,600); a.plot(k,k*k-k**4); a.axhline(0,color='gray',lw=.8); a.scatter([-1/np.sqrt(2),1/np.sqrt(2)],[.25,.25],color='#bb3344')
a.set(xlabel='wavenumber k',ylabel='growth rate s',title='s = k² − k⁴',ylim=(-1.5,.4)); a.grid(alpha=.2)
h=np.linspace(.00001,3.4,800); b.plot(h,h*(np.log(h)-1),color='black')
for en,col in [(-1,'#777777'),(-.8,'#3579a6'),(-.3,'#e59b1d'),(0,'#bb3344')]: b.axhline(en,color=col,ls=':',label=f'E = {en:g}')
b.set(xlabel='positive thickness H',ylabel='V(H)',title='V(H) = H(ln H − 1)',ylim=(-1.15,1)); b.legend(fontsize=8); b.grid(alpha=.2)
def root_upper(en):
    lo,hi=1.,math.e
    for _ in range(70):
        m=(lo+hi)/2
        if m*(math.log(m)-1)<en: lo=m
        else: hi=m
    return (lo+hi)/2
def derivative(y): return np.array([y[1],-math.log(y[0])])
for en,col in [(-.8,'#3579a6'),(-.3,'#e59b1d')]:
    dt=.001; y=np.array([root_upper(en),0.]); xx=np.arange(0,5+dt/2,dt); yy=[]
    for x in xx:
        yy.append(y[0]); k1=derivative(y); k2=derivative(y+dt*k1/2); k3=derivative(y+dt*k2/2); k4=derivative(y+dt*k3); y+=dt*(k1+2*k2+2*k3+k4)/6
    c.plot(np.concatenate((-xx[:0:-1],xx)),np.concatenate((yy[:0:-1],yy)),color=col,label=f'periodic, E = {en:g}')
w=np.linspace(0,7,1500); xd=math.sqrt(math.pi*math.e)*np.array([math.erf(z/math.sqrt(2)) for z in w]); hd=math.e*np.exp(-w*w)
c.plot(np.concatenate((-xd[:0:-1],xd)),np.concatenate((hd[:0:-1],hd)),color='#bb3344',lw=2,label='limiting drop, E = 0')
c.axhline(1,color='gray',ls=':',label='uniform, E = −1'); c.set(xlabel='horizontal coordinate X',ylabel='thickness H',title='Steady profiles (arbitrary translations)',xlim=(-5,5),ylim=(0,3)); c.grid(alpha=.2); c.legend(fontsize=8,ncol=2)
fig.savefig('paper-68-film-profiles.png',facecolor='white',transparent=False)
