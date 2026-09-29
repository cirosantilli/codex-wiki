"""Original all-point Arrhenius calculation for NST IA Chemistry 2025 Q5."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

T=np.array([260.,280.,300.,320.,340.])
k_scaled=np.array([6.2,13.,23.,34.,64.])
x=1000/T
y=np.log(k_scaled)
m,b=np.polyfit(x,y,1)
fig,ax=plt.subplots(figsize=(6.8,4.3),facecolor='white')
xx=np.linspace(x.min()-.04,x.max()+.04,200)
ax.plot(xx,m*xx+b,color='#24628d',label='Unweighted least-squares fit')
ax.scatter(x,y,s=42,color='#b35625',zorder=3,label='Supplied rate data')
for xi,yi,ti in zip(x,y,T):ax.annotate(f'{ti:.0f} K',(xi,yi),xytext=(6,7),textcoords='offset points',fontsize=9)
ax.set_xlabel(r'$1000\,\mathrm{K}/T$')
ax.set_ylabel(r'$\ln[k_1/(10^6\,\mathrm{cm^3\,mol^{-1}\,s^{-1}})]$')
ax.text(.04,.08,rf'$y={m:.4f}x+{b:.4f}$'+'\n'+rf'$E_a={-1000*m*8.3145/1000:.2f}\ \mathrm{{kJ\,mol^{{-1}}}}$',transform=ax.transAxes,fontsize=11)
ax.legend(frameon=False,fontsize=9,loc='upper right')
ax.grid(alpha=.2)
ax.spines[['top','right']].set_visible(False)
fig.tight_layout()
fig.savefig('2025-arrhenius-fit.png',dpi=150,facecolor='white',bbox_inches='tight')
plt.close(fig)
