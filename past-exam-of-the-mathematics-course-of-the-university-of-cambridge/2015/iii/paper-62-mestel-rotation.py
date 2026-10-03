"""Python 3.14; NumPy 2.3.5 and Matplotlib 3.10.7. Output goes to cwd."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
u=np.linspace(.02,8,500)
fig,ax=plt.subplots(figsize=(6.5,3.2),dpi=100,facecolor='white')
ax.plot(u,np.ones_like(u),color='#238b45',lw=2.5)
ax.set(xlabel=r'Radius $R/R_0$ (arbitrary reference $R_0$)',ylabel=r'Circular speed $v_c/v_M$',xlim=(0,8),ylim=(0,1.4),title=r'Mestel disk: $\Sigma(R)\propto R^{-1}$')
ax.grid(alpha=.2);fig.tight_layout()
fig.savefig('paper-62-mestel-rotation.png',facecolor='white',transparent=False)
