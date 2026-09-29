"""Original interference and zone-plate calculations; Python3.14, numpy, matplotlib.
Write only the matching PNG basename in the current working directory.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
plt.rcParams.update({'font.size':10})
fig,axs=plt.subplots(2,2,figsize=(12,9),layout='constrained')
ax=axs[0,0]
wavelength=6.62607015e-34*299792458/(30000*1.602176634e-19);f=.01
r=np.sqrt(np.arange(1,13)*wavelength*f)*1e6
for j in range(11,-1,-1):
 ax.add_patch(Circle((0,0),r[j],facecolor='#363a43' if j%2==0 else 'white',edgecolor='#666',lw=.6))
ax.set(xlim=(-2.5,2.5),ylim=(-2.5,2.5),aspect='equal',xlabel='x (µm)',ylabel='y (µm)',title='A  First twelve half-period zones;30keV')
ax.annotate('r₁ =0.643µm',xy=(r[0],0),xytext=(.9,-2),arrowprops={'arrowstyle':'->'})
ax=axs[0,1]
x=np.linspace(0,14,6000);l1=.5;l2=.51
en=np.abs(np.cos(2*np.pi*x*(1/l1-1/l2)))
I=1+np.cos(2*np.pi*x*(1/l1-1/l2))*np.cos(2*np.pi*x*(1/l1+1/l2))
ax.plot(x,I,lw=.65);ax.plot(x,1+en,'--',color='tab:red');ax.plot(x,1-en,'--',color='tab:red')
ax.set(xlabel='mirror displacement (µm)',ylabel='intensity / (2 I₀)',title='B  Illustrative Michelson pair:500,510nm',ylim=(-.05,2.05))
ax.axvline(l1*l2/(4*(l2-l1)),color='gray',ls=':',label='first contrast zero');ax.legend(fontsize=8)
R=.8;T=.2
ax=axs[1,0];delta=np.linspace(-np.pi,3*np.pi,4000)
trans=T*T/(1+R*R-2*R*np.cos(delta))
ax.plot(delta/np.pi,trans);ax.axhline(.5,color='gray',ls=':');ax.set(xlabel='round-trip phase / π',ylabel='transmission',title='C  Fabry–Pérot:R=0.8,T=0.2',ylim=(0,1.05))
ax=axs[1,1];d=np.linspace(.4998e-3,.5003e-3,10000)
def airy(lam):return T*T/(1+R*R-2*R*np.cos(4*np.pi*d/lam))
values=[airy(l*1e-9) for l in [1000,1000.2,1001.1]]
for l,y,col in zip([1000,1000.2,1001.1],values,['tab:blue','tab:green','tab:red']):
 ax.plot((d-.5e-3)*1e6,y,color=col,lw=1,ls='--',label=f'{l:g}nm individual')
ax.plot((d-.5e-3)*1e6,values[0]+values[1],color='black',lw=1.6,label='first two summed')
ax.plot((d-.5e-3)*1e6,sum(values),color='tab:orange',lw=1.8,label='all three; equal input chosen')
ax.set(xlabel='gap −0.500mm (µm)',ylabel='output / one-line input',title='D  Scanning resonances and order ambiguity',ylim=(0,1.6))
ax.legend(fontsize=7)
fig.savefig('paper-2-interference.png',dpi=155,facecolor='white')

