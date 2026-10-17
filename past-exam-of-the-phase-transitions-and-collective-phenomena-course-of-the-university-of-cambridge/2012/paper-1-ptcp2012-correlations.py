"""Original spin-wave correlation curves with exponential momentum regulator, a=1."""
import numpy as np
import matplotlib.pyplot as plt
r=np.geomspace(.01,1000,1200)
K=.8
# Each exponent is G(0)-G(r), evaluated with exp(-a*q), a=1.
D1=(r*np.arctan(r)-.5*np.log1p(r*r))/(np.pi*K)
D2=np.log((1+np.sqrt(1+r*r))/2)/(2*np.pi*K)
D3=(1-np.arctan(r)/r)/(2*np.pi**2*K)
fig,ax=plt.subplots(figsize=(8,4.8),facecolor='white',layout='constrained')
for d,exponent,color in [(1,D1,'#b95f18'),(2,D2,'#235f8a'),(3,D3,'#287448')]:
    ax.semilogx(r,np.exp(-exponent),color=color,lw=2,label=r'$d='+str(d)+'$')
limit=np.exp(-1/(2*np.pi**2*K))
ax.axhline(limit,color='#287448',lw=1,ls='--')
ax.annotate('Nonzero 3D limit',xy=(90,limit),xytext=(9,.78),arrowprops=dict(arrowstyle='->',color='#287448'),color='#287448')
ax.set(xlabel=r'Separation $r/a$',ylabel=r'$C_m(r)/\bar m^2$',ylim=(-.03,1.06),title='Infrared behavior of a regulated Gaussian phase model')
ax.legend(title=r'$\bar K a^{d-2}=0.8$');ax.grid(alpha=.15)
fig.savefig('paper-1-ptcp2012-correlations.png',dpi=165,facecolor='white')
plt.close(fig)
