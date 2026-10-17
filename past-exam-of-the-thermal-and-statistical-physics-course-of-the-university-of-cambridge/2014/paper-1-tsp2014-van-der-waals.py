"""Original educational diagram; Python 3.14, NumPy and Matplotlib. Saves a basename PNG to the current working directory."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white'})
def pressure(v,t):return 8*t/(3*v-1)-3/v**2
def coexist(t):
 spin=np.sort(np.roots([4*t,-9,6,-1]));spin=np.array([z.real for z in spin if abs(z.imag)<1e-9 and z.real>1/3]);lo=max(1e-10,pressure(spin[0],t));hi=pressure(spin[-1],t)
 def area(p):
  roots=np.roots([3*p,-(p+8*t),9,-3]);roots=np.sort([z.real for z in roots if abs(z.imag)<1e-7 and z.real>1/3]);vl,vg=roots[0],roots[-1]
  return (8*t/3)*np.log((3*vg-1)/(3*vl-1))+3*(1/vg-1/vl)-p*(vg-vl),vl,vg
 for _ in range(90):
  pp=(lo+hi)/2;ar,vl,vg=area(pp)
  if ar>0:lo=pp
  else:hi=pp
 pp=(lo+hi)/2;ar,vl,vg=area(pp);return pp,vl,vg
v=np.linspace(.39,6,2400);fig,axs=plt.subplots(1,2,figsize=(9,4),layout='constrained')
for t,col in [(.85,'#225c91'),(.95,'#388773'),(1.,'#b25424'),(1.12,'#865aa1')]:
 pp=pressure(v,t)
 if t<1:
  pc,vl,vg=coexist(t);axs[0].plot(v,pp,color=col,ls=':',lw=1);axs[0].plot(v,np.where((v>vl)&(v<vg),pc,pp),color=col,label=f'T/Tc = {t:g}');axs[0].scatter([vl,vg],[pc,pc],color=col,s=15)
 else:axs[0].plot(v,pp,color=col,label=f'T/Tc = {t:g}')
axs[0].scatter([1],[1],color='black',s=20);axs[0].text(.5,1.8,'Liquid',ha='center');axs[0].text(3,.28,'Vapour',ha='center');axs[0].text(2.3,1.4,'Gas (T > Tc)',ha='center');axs[0].text(2.15,.63,'Liquid–vapour mixture',fontsize=9)
axs[0].set(xlabel=r'Molar volume $v/v_c$',ylabel=r'Pressure $p/p_c$',xlim=(.39,6),ylim=(0,2),title='Isotherms: stable plateaus, dotted raw loops');axs[0].legend(fontsize=8,loc='upper right');axs[0].grid(alpha=.2)
t=np.linspace(.6,.9999,160);pc=np.array([coexist(tt)[0] for tt in t]);axs[1].plot(np.r_[t,1],np.r_[pc,1],color='#225c91',lw=2);axs[1].scatter([1],[1],color='black',s=24);axs[1].annotate('Critical endpoint',xy=(1,1),xytext=(1.04,1.22),arrowprops={'arrowstyle':'->','color':'#555'},fontsize=9)
axs[1].text(.78,.17,'Vapour',ha='center');axs[1].text(.75,1.12,'Liquid',ha='center');axs[1].text(1.19,.6,'Gas /\nsupercritical fluid',ha='center');axs[1].set(xlabel=r'Temperature $T/T_c$',ylabel=r'Pressure $p/p_c$',xlim=(.6,1.35),ylim=(0,1.5),title='Liquid–vapour coexistence curve');axs[1].grid(alpha=.2)
fig.savefig('paper-1-tsp2014-van-der-waals.png',dpi=150,facecolor='white');plt.close(fig)
