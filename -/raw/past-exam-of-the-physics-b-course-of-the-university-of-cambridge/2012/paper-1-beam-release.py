"""Original modal evolution and spectrum of the released parabolic beam."""
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10})
x=np.linspace(0,1,601);n=np.arange(1,401,2)
A=-8/(np.pi**3*n**3);S=np.sin(np.pi*n[:,None]*x)
fig,axs=plt.subplots(1,2,figsize=(9.1,3.8),layout='constrained',gridspec_kw={'width_ratios':[1.45,1]})
for frac,label in [(0,'0'),(.125,'1/8'),(.5,'1/2'),(1,'1')]:
 y=(A*np.cos(n*n*np.pi*frac))@S
 axs[0].plot(x,y,label=rf'$\omega_1t/\pi={label}$',lw=1.6)
axs[0].set(xlabel=r'$x/L$',ylabel=r'$y/(aL^2)$',title='Release, straight passage, inversion')
axs[0].legend(fontsize=8,loc='upper right');axs[0].grid(alpha=.2)
k=np.arange(1,10,2);axs[1].stem(k,1/k**3,basefmt=' ')
axs[1].set(yscale='log',xlabel='Odd mode n',ylabel=r'$|A_n/A_1|$',title='Displacement spectrum',xticks=k)
for j in k:axs[1].annotate(rf'$\omega/\omega_1={j*j}$',(j,1/j**3),xytext=(0,7),textcoords='offset points',ha='center',fontsize=8)
axs[1].set_ylim(.0009,2);axs[1].grid(alpha=.2)
for ax in axs:ax.spines[['top','right']].set_visible(False)
fig.savefig('paper-1-beam-release.png',dpi=170,facecolor='white');plt.close(fig)
