"""Original queue burst diagram. Python 3.14, NumPy and Matplotlib; PNG to CWD."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
s=np.linspace(0,5,501)
t0=2.0;x=2.0;capacity=2.7
z=np.where(s<=t0,s,x-0.9*(s-t0))
fig,ax=plt.subplots(figsize=(7.6,4.5),layout='constrained',facecolor='white')
ax.set_facecolor('white')
ax.plot(s,z,lw=2.8,color='#1769aa')
ax.axhline(0,color='#333333',lw=0.9)
ax.axhline(capacity,color='#a45615',ls='--',lw=1.4)
ax.text(4.9,capacity+0.09,r'Buffer $B\geq x$',ha='right',color='#a45615')
ax.vlines(t0,0,x,color='#777777',lw=1,ls=':')
ax.scatter([t0],[x],color='#1769aa',zorder=4)
ax.annotate(r'$q(a)=\bar q_B(a)=x$',xy=(t0,x),xytext=(2.7,2.22),arrowprops={'arrowstyle':'->','color':'#333333'},fontsize=12)
ax.text(0.70,1.03,r'Slope $v-C>0$',rotation=28,color='#1769aa')
ax.text(3.40,1.04,r'Slope $\mu-C<0$',rotation=-26,color='#1769aa')
ax.set_xticks([0,t0],['0',r'$t_0=x/(v-C)$'])
ax.set_yticks([0,x],['0',r'$x$'])
ax.set_xlim(0,5.05);ax.set_ylim(-0.85,3.18)
ax.set_xlabel('Time into the past, s');ax.set_ylabel('Lookback net work z(s)')
ax.set_title('A constant-rate burst attains x without overflowing B')
ax.spines[['top','right']].set_visible(False)
fig.savefig(Path.cwd()/'paper-31-burst-path.png',dpi=140,facecolor='white',transparent=False)
plt.close(fig)
