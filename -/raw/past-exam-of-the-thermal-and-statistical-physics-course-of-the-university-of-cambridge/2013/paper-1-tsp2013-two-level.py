"""Original two-level equilibrium curves; Python 3.14, NumPy, Matplotlib. PNG to cwd."""
import numpy as np
import matplotlib.pyplot as plt
t=np.linspace(0,3,2001);x=np.divide(1,t,out=np.full_like(t,1000.),where=t>0);q=np.exp(-x);u=q/(1+q);cv=x*x*q/(1+q)**2
fig,(a,b)=plt.subplots(1,2,figsize=(8.4,3.3),layout='constrained')
a.plot(t,u,color='#1f709d',lw=2);a.axhline(.5,color='0.5',ls='--');a.set(xlabel=r'$k_BT/\Delta$',ylabel=r'$U/(N\Delta)$',title='Energy rises to equal-population plateau',ylim=(-.015,.54))
b.plot(t,cv,color='#ac4d34',lw=2);b.plot(.416778,.439229,'o',color='black');b.annotate('Schottky peak\n(0.417, 0.439)',xy=(.416778,.439229),xytext=(1,.35),arrowprops={'arrowstyle':'->'},fontsize=9);b.set(xlabel=r'$k_BT/\Delta$',ylabel=r'$C/(Nk_B)$',title='Heat capacity vanishes at both limits',ylim=(-.015,.49))
fig.savefig('paper-1-tsp2013-two-level.png',dpi=140,facecolor='white')
