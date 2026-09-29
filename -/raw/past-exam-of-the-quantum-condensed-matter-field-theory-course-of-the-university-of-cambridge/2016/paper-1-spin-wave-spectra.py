"""Original explanatory plot. Tested with Python3.14, NumPy and Matplotlib.
The literal PNG basename is written in cwd for the mirrored Make target.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":11,"figure.facecolor":"white","axes.facecolor":"white"})
k=np.linspace(-np.pi,np.pi,1201);fig,axs=plt.subplots(1,2,figsize=(10,4.1),layout='constrained')
for alpha,color in [(0,'#555555'),(.2,'#3d7da8'),(1.,'#a44c37')]:
 Delta=1+alpha;energy=np.sqrt(np.maximum(Delta**2-np.cos(k)**2,0));axs[0].plot(k,energy,label=r'$\alpha='+str(alpha)+'$',color=color,lw=2)
axs[0].set(xlabel='Rotated lattice momentum k',ylabel=r'$\epsilon_k/(2JS)$',title='Easy axis and isotropic limit');axs[0].legend(fontsize=10);axs[0].grid(alpha=.18)
Delta=.5;energy=np.sqrt(np.maximum((1-np.cos(k))*(1+Delta*np.cos(k)),0));axs[1].plot(k,energy,color='#704293',lw=2,label=r'$\alpha=-0.5$');axs[1].scatter([0,np.pi],[0,np.sqrt(2*(1-Delta))],color='#704293',zorder=3);axs[1].annotate('Gapless in-plane mode',xy=(0,0),xytext=(-2.7,.35),arrowprops={'arrowstyle':'->'},fontsize=10);axs[1].set(xlabel='Chosen local-frame momentum k',ylabel=r'$\epsilon_k/(2JS)$',title='Easy plane: one acoustic mode',ylim=(-.06,1.3));axs[1].legend(loc='upper center');axs[1].grid(alpha=.18)
for a in axs:a.set_xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi],[r'$-\pi$',r'$-\pi/2$','0',r'$\pi/2$',r'$\pi$'])
fig.savefig('paper-1-spin-wave-spectra.png',dpi=150,facecolor='white');plt.close(fig)
