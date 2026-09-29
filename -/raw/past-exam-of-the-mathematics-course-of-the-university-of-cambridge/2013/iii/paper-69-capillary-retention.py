"""Plot capillary trapping; emit the PNG basename to the working directory.

Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7. Caller controls MPLCONFIGDIR.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

s=0.4
v_a=1.0
v_r=v_a/(1-s)
t_end=2/(v_r-v_a)
x_end=2/s
fig,axes=plt.subplots(1,2,figsize=(9,6),dpi=140,facecolor='white')
ax=axes[0]
time=np.linspace(0,t_end,301)
ax.fill_betweenx(time,v_r*time,2+v_a*time,color='#d8eaf4',alpha=0.6)
for height in np.linspace(0,1,7):
 stop=2*(1-height)/(v_r-v_a)
 tt=np.linspace(0,stop,100)
 ax.plot(height+v_r*tt,tt,color='#1b6a9c',lw=1)
 ax.plot(2-height+v_a*tt,tt,color='#c66b19',lw=1)
ax.plot(1+(v_r+v_a)*time/2,time,'k-',lw=2,label='moving crest')
ax.plot(v_r*time,time,color='#1b6a9c',lw=2,label='receding tail')
ax.plot(2+v_a*time,time,color='#c66b19',lw=2,label='advancing front')
ax.scatter([x_end],[t_end],color='black',zorder=5)
ax.text(x_end-.12,t_end-.28,r'$x_*,t_*$',ha='right',fontsize=10)
ax.set(xlabel=r'Upslope position $x/L$',ylabel=r'Time $t v_A/L$',title='Height characteristics',xlim=(0,5.3),ylim=(0,3.3))
ax.legend(loc='upper left',fontsize=8,framealpha=1)
ax.grid(alpha=.18)
ax=axes[1]
x=np.linspace(0,x_end,1501)
envelope=np.where(x<=1,x,(2-s*x)/(2-s))
ax.fill_between(x,0,envelope,color='#eac78f',alpha=.7,label=r'final invaded region (saturation $s$)')
ax.plot(x,envelope,'k--',lw=1.5,label='maximum thickness')
colors=['#174d77','#36849f','#a15569','#812c48']
for frac,color in zip([0,.25,.5,.75],colors):
 t=frac*t_end
 h=np.maximum(0,np.minimum(x-v_r*t,2+v_a*t-x))
 ax.plot(x,h,color=color,lw=2,label=rf'$t/t_*={frac:g}$')
ax.set(xlabel=r'Upslope position $x/L$',ylabel=r'Thickness $h/(aL)$',title='Mobile profiles and trapped envelope',xlim=(0,5.3),ylim=(0,1.16))
ax.legend(loc='upper right',fontsize=7.5,framealpha=1)
ax.grid(alpha=.18)
fig.suptitle(r'Capillary retention: a faster tail consumes the advancing current',fontsize=12)
fig.text(.5,.035,r'Illustrative residual saturation $s=0.4$; every characteristic carries a constant height.',ha='center',fontsize=9)
fig.subplots_adjust(left=.075,right=.98,bottom=.15,top=.87,wspace=.3)
fig.savefig('paper-69-capillary-retention.png',dpi=140,facecolor='white',transparent=False)
plt.close(fig)
