"""Original explanatory plot. Tested with Python 3.14, NumPy and Matplotlib.
Write the PNG basename into the current working directory (Make mirrors it).
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":11,"figure.facecolor":"white","axes.facecolor":"white"})
fig,axs=plt.subplots(1,2,figsize=(9,3.8),layout='constrained');m=np.linspace(-1,1,800);d=.5
for b,color in [( .3,'#377eb8'),(0,'#555555'),(-.3,'#c33e36')]:axs[0].plot(m,b*m*m+d*m**4,color=color,label=f'b = {b:g}')
axs[0].axhline(0,color='.7',lw=.6);axs[0].set(xlabel='Signed component along chosen axis',ylabel='Free energy',title='Illustrative quartic coefficient d = 1/2');axs[0].legend();axs[0].grid(alpha=.15)
T=np.linspace(0,1.6,800);meq=np.sqrt(np.maximum(1-T,0));axs[1].plot(T,meq,color='#71459a',lw=2);axs[1].axvline(1,color='.6',ls='--',lw=1);axs[1].set(xlabel=r'$T/T_c$',ylabel=r'$|\mathbf{m}|_{\rm eq}$',title='Continuous onset',ylim=(-.04,1.06));axs[1].grid(alpha=.2);axs[1].text(.15,.12,'Mean-field exponent 1/2',transform=axs[1].transAxes,fontsize=10)
fig.savefig('paper-1-landau-ferromagnet.png',dpi=150,facecolor='white');plt.close(fig)
