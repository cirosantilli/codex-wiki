"""Original local dispersions and bound electron-hole excitation energy diagram."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig,(ax,levels)=plt.subplots(1,2,figsize=(10.6,5.1),gridspec_kw={'width_ratios':[1.2,1]},facecolor='white')
q=np.linspace(-.6,.6,250)
ax.plot(q,.620+.541*q*q,color='#245f8a',lw=2,label='Conduction electron: 0.2397 me')
ax.plot(q,-.620-.180*q*q,color='#a34f26',lw=2,label='Valence hole: 0.7205 me')
ax.annotate('',xy=(0,.620),xytext=(0,-.620),arrowprops={'arrowstyle':'<->','color':'black'})
ax.text(.035,0,'Eg = 1.240 eV',va='center',fontsize=10)
ax.set(xlabel='Dimensionless wavevector ka along x',ylabel='One-electron band energy (eV)',title='Isotropic quadratic approximation near Γ',ylim=(-.9,.95));ax.grid(alpha=.18);ax.legend(loc='upper center',fontsize=9)
levels.set(xlim=(0,5),ylim=(1.19,1.257));levels.spines[['top','right','bottom']].set_visible(False)
levels.set_xticks([]);levels.set_ylabel('Pair excitation energy above valence maximum (eV)')
levels.set_title('Optical exciton series below the gap')
levels.axhspan(1.24,1.257,color='#e6eef4')
levels.hlines(1.24,.4,2.8,color='black',ls='--',lw=1.5)
levels.text(2.95,1.24,'Unbound pair\n1.24000 eV',va='center',fontsize=10)
for n,en in [(1,1.2017589511),(2,1.2304397378)]:
    levels.hlines(en,.4,2.8,color='#245f8a',lw=2)
    levels.text(2.95,en,f'n = {n}\n{en:.5f} eV',va='center',fontsize=10)
levels.text(1.6,1.249,'Free-pair continuum',ha='center',fontsize=10)
levels.text(2.3,1.1925,'R* = 38.24 meV',ha='center',fontsize=10)
fig.text(.5,.012,'Exciton energies are electron–hole excitation energies, not added one-electron band states.',ha='center',fontsize=10)
fig.tight_layout(rect=(0,.04,1,1))
fig.savefig('paper-2-band-excitons.png',dpi=150,facecolor='white',bbox_inches='tight')
plt.close(fig)
