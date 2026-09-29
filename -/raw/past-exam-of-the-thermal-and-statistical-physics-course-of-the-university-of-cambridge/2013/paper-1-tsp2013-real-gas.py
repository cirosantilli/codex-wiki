"""Original reduced van der Waals model with computed equal-area pressure.
Python 3.14, NumPy, Matplotlib. PNG basename to cwd.
"""
import numpy as np
import matplotlib.pyplot as plt
t=.9
p=lambda v,T:8*T/(3*v-1)-3/v**2
spin=np.sort([z.real for z in np.roots([4*t,-9,6,-1]) if abs(z.imag)<1e-10 and z.real>1/3])
lo,hi=sorted([p(spin[0],t),p(spin[1],t)]);lo+=1e-8;hi-=1e-8
def endpoints(P):
 return np.sort([z.real for z in np.roots([3*P,-P-8*t,9,-3]) if abs(z.imag)<1e-8 and z.real>1/3])
def area(P):
 a,_,b=endpoints(P);return 8*t/3*np.log((3*b-1)/(3*a-1))+3*(1/b-1/a)-P*(b-a)
for _ in range(80):
 mid=(lo+hi)/2
 if area(mid)>0:lo=mid
 else:hi=mid
P=(lo+hi)/2;vl,vm,vg=endpoints(P);v=np.linspace(.4,4.2,2401)
fig,ax=plt.subplots(figsize=(6.7,3.8),layout='constrained')
ax.plot(v,p(v,.9),color='#365d93',ls='--',lw=1.5,label=r'$T/T_c=0.9$: raw homogeneous curve')
ax.plot(v,p(v,1),color='#3d8b70',lw=1.8,label=r'$T/T_c=1$');ax.plot(v,p(v,1.15),color='#b45d32',lw=1.8,label=r'$T/T_c=1.15$')
w=np.linspace(vl,vg,501);ax.plot([vl,vg],[P,P],color='#365d93',lw=2.5,label='Equilibrium coexistence at T/Tc=0.9');ax.fill_between(w,p(w,t),P,where=p(w,t)>P,color='#e9c6a0',alpha=.7);ax.fill_between(w,p(w,t),P,where=p(w,t)<P,color='#a9cbe1',alpha=.7)
ax.plot(1,1,'o',color='black',ms=4);ax.set(xlabel=r'$v/v_c$',ylabel=r'$p/p_c$',title='Real-gas model: critical isotherm and equal-area coexistence',xlim=(.4,4.2),ylim=(0,2.1));ax.legend(fontsize=8,loc='upper right')
fig.savefig('paper-1-tsp2013-real-gas.png',dpi=140,facecolor='white')
