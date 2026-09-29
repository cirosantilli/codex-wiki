"""Original calculated squeezed-vacuum conditional statistics. Output PNG basename to cwd."""
import numpy as np
import matplotlib.pyplot as plt
r=.7;mean=np.sinh(r)**2;n=np.arange(81);p=np.zeros(81);p[0]=1/np.cosh(r)
for m in range(40):p[2*m+2]=p[2*m]*(2*m+1)/(2*m+2)*np.tanh(r)**2
pm=np.zeros_like(p);pp=np.zeros_like(p);pm[:-1]=(n[1:])*p[1:]/mean;pp[1:]=n[1:]*p[:-1]/(mean+1)
assert abs(p.sum()-1)<1e-12 and np.max(abs(pm-pp))<1e-12
fig,ax=plt.subplots(1,2,figsize=(9.5,3.5),layout='constrained')
ax[0].bar(n[:16]-.18,p[:16],width=.36,label='Original squeezed vacuum (even)');ax[0].bar(n[:16]+.18,pm[:16],width=.36,label='Conditional addition / subtraction (odd)');ax[0].set(xlabel='Photon number n',ylabel='Normalized probability',title=f'Chosen squeezing r = {r}');ax[0].set_xticks(range(0,16,2));ax[0].legend(fontsize=8)
rr=np.linspace(.01,1,300);s=np.sinh(rr)**2
ax[1].plot(rr,s,label='Original mean');ax[1].plot(rr,1+3*s,label='Both normalized conditional means',lw=2);ax[1].plot(rr,(3*s+1)*(s+1),'--',label='Raw added moment');ax[1].plot(rr,s*(3*s+1),'--',label='Raw subtracted moment');ax[1].set(xlabel='Squeezing r',ylabel='Occupation or unnormalized moment',title='Normalization changes the comparison');ax[1].legend(fontsize=8);ax[1].grid(alpha=.2)
fig.savefig('paper-1-conditioned-photon-statistics.png',dpi=150,facecolor='white')
