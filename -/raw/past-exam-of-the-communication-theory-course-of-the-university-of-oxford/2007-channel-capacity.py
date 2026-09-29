"""Python 3.14.4; NumPy 2.3.5; Matplotlib 3.10.7. PNG output in CWD."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
p=np.linspace(0,.9999,1500);b=1-p;h=np.zeros_like(p);q=p>0;h[q]=-p[q]*np.log2(p[q])-b[q]*np.log2(b[q]);a=1/(b*(2+np.exp2(h/b)));cap=np.log2(1+np.exp2(1-h/b))
fig,axes=plt.subplots(1,2,figsize=(9.6,4.3),layout='constrained',facecolor='white')
for ax in axes:ax.set_facecolor('white');ax.grid(alpha=.2);ax.set_xlabel('Channel parameter $p$');ax.set_xlim(0,1)
axes[0].plot(p,a,label='Each outer input',lw=2);axes[0].plot(p,1-2*a,label='Middle input',lw=2);axes[0].set(ylabel='Input probability',title='A symmetric maximizing distribution',ylim=(.23,.40));axes[0].legend()
axes[1].plot(p,cap,lw=2,color='#2166ac');axes[1].scatter([.5],[np.log2(1.5)],c='#d6604d',zorder=4);axes[1].annotate(r'$C(1/2)=\log_2(3/2)$',(.5,np.log2(1.5)),xytext=(.39,1.1),arrowprops={'arrowstyle':'->'});axes[1].set(ylabel='Capacity (bits per use)',title='Capacity falls to zero at complete collapse',ylim=(0,1.7))
fig.savefig(Path.cwd()/'2007-channel-capacity.png',dpi=170,facecolor='white')
