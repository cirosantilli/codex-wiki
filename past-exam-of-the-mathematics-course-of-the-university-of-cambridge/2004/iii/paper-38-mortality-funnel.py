"""Original hospital funnel plot; Python 3.14, root NumPy/Matplotlib dependencies.

Outputs paper-38-mortality-funnel.png to the caller CWD. Honors MPLCONFIGDIR.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

labels=list('ABCDEFGH')
volumes=np.array([10,100,25,100,10,200,20,100])
deaths=np.array([1,12,3,15,2,40,5,30])
rates=deaths/volumes
p0=.2
n=np.linspace(10,215,900)
width=1.959963984540054*np.sqrt(p0*(1-p0)/n)
lower=np.maximum(0,p0-width);upper=np.minimum(1,p0+width)
fig,ax=plt.subplots(figsize=(10.8,5),facecolor='white')
ax.set_facecolor('white')
ax.fill_between(n,lower,upper,color='#dcecf8',alpha=1,label='95% pointwise limits (normal approximation)')
ax.plot(n,lower,color='#2474a6',lw=1.4)
ax.plot(n,upper,color='#2474a6',lw=1.4)
ax.axhline(p0,color='#334155',ls='--',lw=1.5,label='20% target')
out=np.abs(rates-p0)>1.959963984540054*np.sqrt(p0*(1-p0)/volumes)
ax.scatter(volumes[~out],rates[~out],s=52,color='#174f78',edgecolor='white',linewidth=.7,zorder=4,label='Observed rate within limits')
ax.scatter(volumes[out],rates[out],s=58,color='#b91c1c',edgecolor='white',linewidth=.7,zorder=4,label='Observed rate outside limits')
offsets=[(8,-14),(-16,-15),(8,4),(8,-3),(8,6),(8,9),(8,5),(8,0)]
for label,x,y,offset,flag in zip(labels,volumes,rates,offsets,out):
    ax.annotate(label,(x,y),xytext=offset,textcoords='offset points',fontsize=11,
                color='#b91c1c' if flag else '#174f78',fontweight='bold')
ax.set_xlim(0,230);ax.set_ylim(0,.53)
ax.set_xlabel('Number of operations');ax.set_ylabel('Observed mortality proportion')
ax.set_title('Hospital mortality and case volume')
ax.set_yticks(np.arange(0,.51,.1),[f'{int(100*y)}%' for y in np.arange(0,.51,.1)])
ax.grid(alpha=.16)
ax.legend(loc='upper right',framealpha=1,fontsize=9)
fig.tight_layout()
fig.savefig('paper-38-mortality-funnel.png',dpi=130,facecolor='white',transparent=False)
plt.close(fig)
