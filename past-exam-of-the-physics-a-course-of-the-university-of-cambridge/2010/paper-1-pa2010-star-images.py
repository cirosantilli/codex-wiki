"""Original teaching plot. Python3.14, NumPy and Matplotlib. Writes basename PNG to cwd."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
D=2.4;separation=.5e-6;theta=np.linspace(-.9e-6,.9e-6,1001)
def airy(u,lam):
 x=np.pi*D*u/lam;t=np.linspace(0,np.pi,1201)
 j1=np.trapezoid(np.cos(t[None,:]-x[:,None]*np.sin(t)[None,:]),t,axis=1)/np.pi
 amplitude=np.ones_like(x);np.divide(2*j1,x,out=amplitude,where=np.abs(x)>1e-9)
 return amplitude**2
fig,axs=plt.subplots(1,2,figsize=(10,4.2),layout='constrained')
for ax,lam in zip(axs,[300e-9,1000e-9]):
 p=airy(theta-separation/2,lam);q=airy(theta+separation/2,lam)
 ax.plot(theta*1e6,p+q,color='#27689c',lw=2,label='Incoherent intensity sum')
 ax.plot(theta*1e6,p,':',color='gray');ax.plot(theta*1e6,q,':',color='gray')
 ax.set(xlabel='Angular coordinate (microradians)',ylabel='Intensity / one-star peak',title=f'Wavelength {lam*1e9:.0f} nm',ylim=(0,1.38));ax.grid(alpha=.2)
axs[0].legend(fontsize=9,loc='upper center')
axs[1].text(.5,.96,'Marginal Rayleigh case; a dip can remain',transform=axs[1].transAxes,ha='center',va='top',fontsize=9)

fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=140,facecolor='white')
