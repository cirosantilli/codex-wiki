"""Original explanatory calculation. Python 3.14, numpy and matplotlib.
Writes one literal PNG basename to cwd; no source-image pixels or media paths.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','savefig.facecolor':'white','axes.spines.top':False,'axes.spines.right':False})
fig,(a,b)=plt.subplots(1,2,figsize=(9.5,3.7),layout='constrained');th=np.linspace(.0001,np.pi-.0001,4000);Z1,Z2=4.,1.;feed=np.sqrt(Z1*Z2)
trace=1-(Z1+Z2)**2/(2*Z1*Z2)*np.sin(th)**2;disc=4*Z1*Z2-(Z1-Z2)**2*np.tan(th)**2;Z=(1j*(Z1-Z2)*np.tan(th)+np.sqrt(disc.astype(complex)))/2
ref=abs((Z-feed)/(Z+feed))**2;tc=np.arcsin(2*np.sqrt(Z1*Z2)/(Z1+Z2))
a.plot(th/np.pi,trace);a.axhline(-1,color='black',ls=':');a.axhline(1,color='black',ls=':');a.set(xlabel=r'$kl/\pi$',ylabel='Half cell trace',title='Chosen impedance ratio Z₁/Z₂ = 4')
b.plot(th/np.pi,ref);b.set(xlabel=r'$kl/\pi$',ylabel='Reflected power fraction',ylim=(-.04,1.06),title='Semi-infinite line; Zfeed = √(Z₁Z₂)')
for ax in [a,b]:ax.axvspan(tc/np.pi,1-tc/np.pi,color='#e39e30',alpha=.16);ax.text(.5,.05,'stop band',transform=ax.transAxes,ha='center',fontsize=9)
fig.savefig('paper-1-periodic-line.png',dpi=150);plt.close(fig)
