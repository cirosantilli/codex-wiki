"""Python 3.14; NumPy 2.3.5 and Matplotlib 3.10.7. Output goes to cwd."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
u=np.linspace(0,12,700)
fig,ax=plt.subplots(figsize=(7,4),dpi=100,facecolor='white')
ax.plot(u,np.sqrt(u/(1+u)),color='#225ea8',lw=2.5,label=r'$v_c/v_0=\sqrt{u/(1+u)}$')
ax.axhline(1,color='#555555',ls='--',label='Asymptotic circular speed')
ax.set(xlabel=r'Radius $u=r/a$',ylabel=r'Circular speed $v_c/v_0$',xlim=(0,12),ylim=(0,1.12),title='Cusped logarithmic spherical model')
ax.grid(alpha=.2);ax.legend(loc='lower right');fig.tight_layout()
fig.savefig('paper-62-logarithmic-rotation.png',facecolor='white',transparent=False)
