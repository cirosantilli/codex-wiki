"""Original explanatory figure; Python 3.14, NumPy and Matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white','savefig.facecolor':'white'})

Tr=.85
pres=lambda v:8*Tr/(3*v-1)-3/v**2
spin=sorted(v.real for v in np.roots([4*Tr,-9,6,-1]) if abs(v.imag)<1e-9 and v.real>1/3)
def roots(p):return sorted(v.real for v in np.roots([3*p,-p-8*Tr,9,-3]) if abs(v.imag)<1e-8 and v.real>1/3)
def area(p):
 lo,mid,hi=roots(p);return (8*Tr/3)*np.log((3*hi-1)/(3*lo-1))+3*(1/hi-1/lo)-p*(hi-lo)
lo=max(1e-8,pres(spin[0])+1e-8);hi=pres(spin[1])-1e-8
for _ in range(90):
 mid=(lo+hi)/2
 if area(mid)>0:lo=mid
 else:hi=mid
p=(lo+hi)/2;vl,vm,vg=roots(p)
fig,axs=plt.subplots(1,2,figsize=(10.5,4),layout='constrained')
v=np.linspace(.43,5,1400);axs[0].plot(v,pres(v),color='#999999',ls='--',label='homogeneous vdW isotherm')
for vs in [np.linspace(.43,vl,200),np.linspace(vg,5,200)]:axs[0].plot(vs,pres(vs),color='#2871a1')
axs[0].plot([vl,vg],[p,p],color='#2871a1',lw=2,label='equilibrium coexistence')
inside=np.linspace(vl,vg,600);axs[0].fill_between(inside,pres(inside),p,where=pres(inside)>=p,color='#b34f28',alpha=.3);axs[0].fill_between(inside,pres(inside),p,where=pres(inside)<p,color='#438a51',alpha=.3)
axs[0].scatter([vl,vg],[p,p],color='#2871a1');axs[0].annotate('liquid',xy=(vl,p),xytext=(.7,1.1),arrowprops={'arrowstyle':'->'});axs[0].annotate('vapour',xy=(vg,p),xytext=(3.3,.9),arrowprops={'arrowstyle':'->'});axs[0].text(1.65,1.28,'equal signed areas',ha='center')
axs[0].set(xlabel='reduced molar volume v / v_c',ylabel='reduced pressure p / p_c',ylim=(0,1.6),xlim=(.4,5),title='Maxwell construction at T / T_c = 0.85');axs[0].legend(fontsize=8,loc='upper right')
t=np.linspace(.2,1,100);axs[1].plot(t,.5*np.exp(3*(t-1)),c='#6a509a');t=np.linspace(1,2.4,100);axs[1].plot(t,.5+.6*(t-1)+.17*(t-1)**2,c='#2871a1');axs[1].plot([1,1.5],[.5,2.6],c='#438a51');axs[1].scatter([1,2.4],[.5,.5+.6*1.4+.17*1.4**2],c='k',s=25)
axs[1].annotate('triple point',xy=(1,.5),xytext=(.18,.8),arrowprops={'arrowstyle':'->'},fontsize=9);axs[1].annotate('critical point',xy=(2.4,1.6732),xytext=(2.35,2.1),arrowprops={'arrowstyle':'->'},fontsize=9)
axs[1].text(.5,1.7,'solid');axs[1].text(1.65,1.65,'liquid');axs[1].text(1.9,.45,'gas');axs[1].text(2.6,2.45,'supercritical\nregion',ha='center',fontsize=9)
axs[1].set(xlabel='temperature (schematic)',ylabel='pressure (schematic)',xlim=(.15,3),ylim=(0,2.8),xticks=[],yticks=[],title='Generic positive-slope melting diagram')
axs[0].grid(alpha=.18)
fig.suptitle('Equilibrium phase coexistence — illustrative models, not measured material data')

fig.savefig(Path(__file__).stem+'.png',dpi=150,bbox_inches='tight',facecolor='white');plt.close(fig)
