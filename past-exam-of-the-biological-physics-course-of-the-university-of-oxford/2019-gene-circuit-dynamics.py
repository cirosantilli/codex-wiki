"""Original dimensionless threshold-model trajectories; Python 3.14."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 11, 'axes.spines.top': False, 'axes.spines.right': False})
fig, axes = plt.subplots(2, 2, figsize=(11, 8), layout='constrained', facecolor='white')
colors = ['#355a9b', '#bd7820', '#269572', '#a05188', '#777777']
def simulate(mode, end, duration=0):
    dt = .0005
    t = np.arange(0, end+dt/2, dt)
    v = np.zeros((len(t), 5 if mode=='a' else 3))
    if mode=='c': v[0, 0] = 1
    if mode=='d': v[0, 1] = 1
    decay = np.exp(-dt)
    for i in range(len(t)-1):
        x,y,z = v[i,:3]
        if mode=='a': p = np.array([float(1 <= t[i] < 7), x>.2, x>.2, x>.4, y>.5])
        elif mode=='b': p = np.array([float(t[i]<duration), (x>.5 or z>.5), (x>.5 or y>.5)])
        elif mode=='c': p = np.array([y<.5, x>.5, (x>.5 or y>.5)])
        else: p = np.array([z<.5, x<.5, y<.5])
        v[i+1] = p+(v[i]-p)*decay
    return t[::20], v[::20]
a=axes[0,0]
t,v=simulate('a',12)
for j,label in enumerate(['X','Y','Z₁','Z₂','Z₃']): a.plot(t,v[:,j],label=label,color=colors[j],lw=1.8)
for h in [.2,.4,.5]: a.axhline(h,color='grey',lw=.6,ls=':'); a.text(11.6,h+.015,f'{h}',ha='right',fontsize=8)
a.axvspan(1,7,color='#dbe4f0',alpha=.4)
a.set(title='A  Ordered on/off responses (input 1–7)')
a.legend(ncol=5,loc='upper right',frameon=False,fontsize=9)
a=axes[0,1]
for T,ls,label in [(.8,'--','short T = 0.8'),(1.5,'-','long T = 1.5')]:
    t,v=simulate('b',8,T)
    a.plot(t,v[:,0],ls,color=colors[0],label='X, '+label)
    a.plot(t,v[:,1],ls,color=colors[2],label='Y = Z, '+label,lw=2)
a.axhline(.5,color='grey',ls=':',lw=1)
a.set(title='B  Mutual activation: memory threshold ln 3')
a.legend(frameon=False,fontsize=9)
a=axes[1,0]
t,v=simulate('c',6)
for j,label in enumerate(['X','Y','Z']): a.plot(t,v[:,j],color=colors[j],label=label,lw=2)
a.axhline(.5,color='grey',ls=':',lw=1)
a.scatter([np.log(6)],[5/6],color=colors[2],zorder=5)
a.annotate(r'first peak: $(\ln 6,5/6)$', (np.log(6),5/6),(2.8,.98), arrowprops={'arrowstyle':'->'},fontsize=10)
a.set(title='C  Feedback acts after the initial steady state')
a.legend(frameon=False,fontsize=10,loc='lower right')
a=axes[1,1]
t,v=simulate('d',10)
for j,label in enumerate(['X','Y','Z']): a.plot(t,v[:,j],color=colors[j],label=label,lw=1.8)
a.axhline(.5,color='grey',ls=':',lw=1)
a.set(title='D  Cyclic repression from (0,1,0)')
a.legend(frameon=False,fontsize=10,ncol=3)
for a in axes.flat:
    a.set(xlabel=r'$\alpha t$',ylabel=r'concentration / $S$',ylim=(-.02,1.12))
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=110,facecolor='white')
