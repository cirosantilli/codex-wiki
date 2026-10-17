"""Original Fresnel calculations using numpy quadrature; PNG output to cwd.
Python3.14, numpy2.3.5 and matplotlib3.10.7. No scipy dependency.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10})
u=np.linspace(0,14,280001);du=u[1]-u[0];phase=np.exp(.5j*np.pi*u*u)
integ=np.r_[0,np.cumsum((phase[:-1]+phase[1:])*.5*du)]
def F(t):
 t=np.asarray(t);z=np.interp(abs(t),u,integ.real)+1j*np.interp(abs(t),u,integ.imag)
 return np.sign(t)*z
fig,axs=plt.subplots(2,2,figsize=(12,9),layout='constrained')
v=np.linspace(-4,5,2500);z=F(v)
edge=.5*((.5+z.real)**2+(.5+z.imag)**2)
axs[0,0].plot(v,edge);axs[0,0].plot(0,.25,'ro');axs[0,0].axvline(0,color='gray',ls=':');axs[0,0].axhline(1,color='gray',ls=':')
axs[0,0].set(xlabel='v =X√(2/λz)',ylabel='intensity / incident intensity',title='A  Straight edge; I(0)/I₀=1/4')
x=np.linspace(-5,5,2200)
for rho in [.6,1.8,3.5]:
 z=F(np.sqrt(2)*(rho-x))-F(np.sqrt(2)*(-rho-x));I=.5*abs(z)**2
 axs[0,1].plot(x,I,label=f'half-width / √(λz)={rho:g}')
axs[0,1].set(xlabel='X / √(λz)',ylabel='slit intensity / incident intensity',title='B  Slits; overlap of opposite-edge fields');axs[0,1].legend(fontsize=8)
X=np.linspace(-3,3,501);Y=np.linspace(-2.5,2.5,401)
Fx=F(np.sqrt(2)*(1.3-X))-F(np.sqrt(2)*(-1.3-X));Fy=F(np.sqrt(2)*(.85-Y))-F(np.sqrt(2)*(-.85-Y))
I=.25*abs(Fy[:,None])**2*abs(Fx[None,:])**2
im=axs[1,0].imshow(I,extent=(-3,3,-2.5,2.5),origin='lower',cmap='magma',aspect='auto')
axs[1,0].set(xlabel='X / √(λz)',ylabel='Y / √(λz)',title='C  Rectangular aperture; chosen half-widths1.3,0.85')
fig.colorbar(im,ax=axs[1,0],label='intensity / incident intensity')
t=np.linspace(-4,4,5000);z=F(t);axs[1,1].plot(z.real,z.imag,lw=1)
end=F(np.array([-1.5,1.5]));axs[1,1].plot(end.real,end.imag,'o-',color='tab:red',label='field interval: chord, not arc length')
axs[1,1].set(xlabel='C(u)',ylabel='S(u)',aspect='equal',title='D  Cornu spiral');axs[1,1].legend(fontsize=8)
fig.savefig('paper-2-fresnel.png',dpi=155,facecolor='white')

