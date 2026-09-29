"""Original computed scattered intensities, not source-image copies; PNG to cwd."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10})
fig,axs=plt.subplots(2,2,figsize=(12,9),layout='constrained')
lam=500e-9;f=.2;a=.2e-3;b=.5e-3;D=1e-3
X=np.linspace(-1,1,1001)*1e-3;Y=np.linspace(-.6,.6,601)*1e-3
single=np.sinc(a*X/(lam*f))[None,:]**2*np.sinc(b*Y/(lam*f))[:,None]**2
factor=(1+2*np.cos(2*np.pi*D*X/(lam*f)))**2/9
triple=single*factor[None,:]
for ax,z,title in zip(axs[0],[single,triple],['A  One rectangle; scattered component','B  Three elements; scattered component']):
 im=ax.imshow(np.log10(np.maximum(z,1e-6)),extent=(-1,1,-.6,.6),origin='lower',vmin=-6,vmax=0,cmap='magma',aspect='auto')
 ax.set(xlabel='X (mm)',ylabel='Y (mm)',title=title)
 fig.colorbar(im,ax=ax,label='log₁₀ normalized scattered intensity')
x=np.linspace(-.65,.65,5000)*1e-3
env=np.sinc(a*x/(lam*f))**2
mult=(1+2*np.cos(2*np.pi*D*x/(lam*f)))**2/9
axs[1,0].plot(x*1e3,env,color='gray',label='single-rectangle envelope')
axs[1,0].plot(x*1e3,env*mult,label='three elements')
for sign in [-1,1]:axs[1,0].axvline(sign*.5,color='tab:red',ls=':',lw=.8)
axs[1,0].set(xlabel='X (mm),Y=0',ylabel='normalized scattered intensity',title='C  0.1mm principal spacing; fifth order absent');axs[1,0].legend(fontsize=8)
sel=abs(x)<.15e-3;axs[1,1].plot(x[sel]*1e3,(env*mult)[sel])
for v in [-.0666667,-.0333333,.0333333,.0666667]:axs[1,1].axvline(v,color='gray',lw=.6,ls=':')
axs[1,1].set(xlabel='X (mm),Y=0',ylabel='normalized scattered intensity',title='D  Central detail; undiffracted beam excluded')
fig.savefig('paper-2-diffraction.png',dpi=155,facecolor='white')

