"""Original contact-Bose-gas Bogoliubov spectrum; Python 3.14."""
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,3,700)
fig,ax=plt.subplots(figsize=(7,3.8),layout='constrained')
ax.plot(x,x*np.sqrt(1+x*x),lw=2,color='#2158a0',label=r'Bogoliubov: $y=x\sqrt{1+x^2}$')
ax.plot(x,x,'--',color='#b24b18',label='Sound limit: y = x')
ax.plot(x,x*x,':',color='#397c49',label=r'Leading particle limit: $y\sim x^2$')
ax.set(xlabel=r'$x=q/(2mc)$',ylabel=r'$y=\omega/(2mc^2)$',title=r'$c=\sqrt{g\rho_0/m}$; crossover at $x\sim1$',xlim=(0,3),ylim=(0,10))
ax.legend(fontsize=9);ax.spines[['top','right']].set_visible(False)
fig.savefig('paper-1-bose-spectrum.png',dpi=155,facecolor='white')
