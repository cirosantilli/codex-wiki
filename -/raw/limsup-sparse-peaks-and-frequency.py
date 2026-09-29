"""Powers-of-two indicator: limsup one, natural density and Cesaro means zero.

Run from the desired output directory. Dependencies/versions: pyproject.toml.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

n=np.arange(1,513)
peaks=(n & (n-1))==0
N=np.arange(1,8193)
# Integer bit lengths give exact counts of nonnegative powers of two through N.
count=np.array([int(k).bit_length() for k in N])
fraction=count/N
assert count[1023]==11
fig,axes=plt.subplots(1,2,figsize=(10.6,4.6),dpi=120,facecolor='white')
for ax in axes:ax.set_facecolor('white');ax.grid(alpha=0.16)
axes[0].plot(n,np.zeros_like(n),color='#176c91',linewidth=2,label='All other indices have value 0')
axes[0].vlines(n[peaks],0,1,color='#ad3c43',linewidth=1.5)
axes[0].scatter(n[peaks],np.ones(peaks.sum()),color='#ad3c43',s=28,zorder=4,label='Powers of two have value 1')
axes[0].set(xlim=(0,520),ylim=(-0.1,1.2),xlabel='Index n',ylabel='aₙ',title='The peaks grow farther apart but never end')
axes[0].legend(loc='center right',fontsize=9,framealpha=0.95)
axes[1].loglog(N,fraction,color='#176c91',linewidth=2.1,label='Number of peaks through N / N')
axes[1].scatter([1024],[11/1024],color='#ad3c43',s=40,zorder=4)
axes[1].annotate('N = 1024: 11 peaks\nMean = 11/1024 ≈ 0.0107',xy=(1024,11/1024),xytext=(14,0.003),fontsize=10,arrowprops=dict(arrowstyle='->',color='#ad3c43'))
axes[1].set(xlim=(1,8192),ylim=(0.001,1.25),xlabel='Prefix length N (log scale)',ylabel='Peak fraction (log scale)',title='Peak density tends to zero while limsup stays 1')
fig.text(0.5,0.025,'Every tail contains zeros and later peaks, so liminf = 0 and limsup = 1.',ha='center',fontsize=10)
fig.subplots_adjust(left=0.065,right=0.98,top=0.89,bottom=0.16,wspace=0.25)
fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),facecolor='white');plt.close(fig)
