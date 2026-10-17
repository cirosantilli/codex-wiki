"""Original oscillator and membrane-mode plots; output PNG basename to cwd."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10})
fig,axs=plt.subplots(2,2,figsize=(12,9),layout='constrained')
t=np.linspace(0,12,1500)
for g in [.25,1,2]:
 if g<1:
  wd=np.sqrt(1-g*g);x=np.exp(-g*t)*(np.cos(wd*t)+g/wd*np.sin(wd*t))
 elif g==1:x=(1+t)*np.exp(-t)
 else:
  s=np.sqrt(g*g-1);x=np.exp(-g*t)*(np.cosh(s*t)+g/s*np.sinh(s*t))
 axs[0,0].plot(t,x,label=f'γ/ω₀={g:g}')
axs[0,0].set(xlabel='ω₀ t',ylabel='displacement / initial displacement',title='A  Displaced and released from rest')
axs[0,0].axhline(0,color='gray',lw=.7);axs[0,0].legend()
rt=np.sqrt(3)
def kick(t):return (.015-.015*rt)*np.exp(-t/rt)+(.015*rt-.005)*np.exp(-rt*t)
t=np.linspace(0,3,1000);sample=np.arange(0,3.01,.5)
axs[0,1].plot(t,1000*kick(t));axs[0,1].plot(sample,1000*kick(sample),'o')
cross=rt/2*np.log((.015*rt-.005)/(.015*rt-.015))
axs[0,1].axhline(0,color='gray',lw=.7);axs[0,1].axvline(cross,color='tab:red',ls=':',label=f'crossing {cross:.4f}s')
axs[0,1].set(xlabel='time (s)',ylabel='displacement (mm)',title='B  Kicked overdamped oscillator');axs[0,1].legend()
q=np.linspace(0,6,700)
for n in [1,2,3]:axs[1,0].plot(q,np.sqrt(q*q+n*n),label=f'n={n}')
axs[1,0].plot(q,q,'k:',label='unbounded sheet');axs[1,0].set(xlabel='axial wavevector kₓ b/π',ylabel='frequency / first cutoff',title='C  Dispersion of clamped-sheet modes');axs[1,0].legend()
u=np.linspace(0,1,700);profile1=np.sin(np.pi*u)+np.sin(2*np.pi*u);profile2=np.sin(np.pi*u)-np.sin(2*np.pi*u)
axs[1,1].plot(u,profile1,label='input profile')
axs[1,1].plot(u,profile2,label='at x₁; common temporal phase removed')
axs[1,1].set(xlabel='transverse coordinate y/b',ylabel='relative profile amplitude',title='D  First relative phase reversal;x₁=0.2446m');axs[1,1].legend(fontsize=8)
fig.savefig('paper-2-damping-and-guidance.png',dpi=155,facecolor='white')

