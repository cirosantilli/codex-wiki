"""Asymptotic pulse sketch, not a solved transition boundary-value problem; cwd PNG."""
from pathlib import Path
import os
if not os.environ.get('MPLCONFIGDIR'):raise RuntimeError('Supply an owned MPLCONFIGDIR')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
c=12.;kappa=.643;s=(3*c)**(1/3);peak=kappa*s*s
fig,(ax,tail)=plt.subplots(1,2,figsize=(10,5),dpi=100,facecolor='white',gridspec_kw={'width_ratios':[1.45,1]})
for a in [ax,tail]:a.set_facecolor('white');a.grid(alpha=.15)
x=np.linspace(-1.8,8.8,1600);H=np.empty_like(x);behind=x<0;core=(x>=0)&(x<=2*np.pi);ahead=x>2*np.pi
H[behind]=1+.15*np.exp(s*x[behind]);H[core]=1.15+peak*(1-np.cos(x[core]));X=s*(x[ahead]-2*np.pi);H[ahead]=1+.15*np.exp(-X/2)*np.cos(np.sqrt(3)*X/2)
ax.plot(x,H,color='#286890',lw=2);ax.axhline(1,color='#777777',ls=':',lw=1)
ax.axvline(0,color='#999999',ls=':',lw=.8);ax.axvline(2*np.pi,color='#999999',ls=':',lw=.8)
ax.annotate('',xy=(5.9,12),xytext=(4.5,12),arrowprops={'arrowstyle':'->','lw':1.6});ax.text(5.2,12.7,'Downward travel',ha='center',fontsize=10)
ax.text(-1.6,3.0,'Trailing\nmonotone tail',fontsize=9);ax.text(6.5,3.0,'Leading\ncapillary tail',fontsize=9)
ax.set_xlabel(r'$x=z-ct$ (positive downward)');ax.set_ylabel('H');ax.set_title('Leading pulse core and schematic edge joins',fontsize=11);ax.set_ylim(.7,H.max()*1.12)
X=np.linspace(0,22,900);ht=.15*np.exp(-X/2)*np.cos(np.sqrt(3)*X/2);tail.plot(X,ht,color='#ad5630',lw=2);tail.axhline(0,color='#777777',lw=1)
tail.set_xlabel(r'Front coordinate $X=(3c)^{1/3}(x-2\pi)$');tail.set_ylabel('H - 1 (tail detail)');tail.set_title('Oscillations decay ahead of the pulse',fontsize=11)
tail.text(3,.10,r'Period in $X$: $4\pi/\sqrt{3}$',fontsize=10);tail.set_ylim(-.045,.16)
fig.subplots_adjust(left=.07,right=.97,top=.84,bottom=.20,wspace=.29)
fig.suptitle('Large solitary wave on a vertical cylindrical film',fontsize=13,y=.95)
fig.text(.5,.055,'Core amplitude follows the leading asymptotics; edge joins and tail amplitude are schematic.',ha='center',fontsize=9)
fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=100,facecolor='white',transparent=False);plt.close(fig)
