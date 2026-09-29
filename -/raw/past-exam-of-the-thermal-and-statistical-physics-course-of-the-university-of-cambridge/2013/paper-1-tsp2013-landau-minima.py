"""Original illustrative quartic Landau minima, not a reproduction of the exam graph.
Python 3.14, NumPy, Matplotlib. Chosen dimensionless coefficients; PNG basename to cwd.
"""
import numpy as np
import matplotlib.pyplot as plt
m=np.linspace(-1.8,1.8,1001);fig,axes=plt.subplots(1,3,figsize=(10.1,3.4),layout='constrained')
params=[(1,0,'(i) H = 0, T > Tc',np.array([0.])),(-1,0,'(ii) H = 0, T < Tc',np.array([-1.,1.])),(1,.6,'(iii) H > 0, T > Tc',None)]
for ax,(a,h,title,mins) in zip(axes,params):
 f=lambda m:a*m*m/2+m**4/4-h*m
 if mins is None:mins=np.array([z.real for z in np.roots([1,0,a,-h]) if abs(z.imag)<1e-12])
 ax.plot(m,f(m),color='#2e709b',lw=2);ax.axhline(0,color='0.7',lw=.8);ax.axvline(0,color='0.7',lw=.8);ax.plot(mins,f(mins),'o',color='#a74b31',ms=6)
 for mm in mins:ax.annotate('minimum',xy=(mm,f(mm)),xytext=(mm,.55 if a<0 else 1.0),ha='center',arrowprops={'arrowstyle':'->'},fontsize=8)
 ax.set(title=title,xlabel='Magnetisation (relative units)',ylabel='Free-energy density (relative units)',xlim=(-1.8,1.8),ylim=(-.5,2.7))
fig.suptitle('Illustrative dimensionless Landau potentials and their stable equilibria',fontsize=12)
fig.savefig('paper-1-tsp2013-landau-minima.png',dpi=140,facecolor='white')
