"""Original explanatory figure; run under Python 3.14 with numpy and matplotlib.
Writes its PNG basename to the current working directory.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, FancyArrowPatch
plt.rcParams.update({"font.size":10,"axes.spines.top":False,"axes.spines.right":False,"figure.facecolor":"white","savefig.facecolor":"white"})
fig,axs=plt.subplots(2,2,figsize=(10,6.8),layout='constrained');a=axs[0,0]
x=np.linspace(0,5,800);a.plot(x,1/(1+x*x),label=r'$\mathrm{Re}\,\sigma/\sigma_0$');a.plot(x,x/(1+x*x),label=r'$\mathrm{Im}\,\sigma/\sigma_0$');a.axvline(1,ls=':',color='gray');a.plot([1,1],[.5,.5],'ko');a.set(xlabel=r'$\omega\tau$',ylabel='Normalized conductivity',title=r'Drude response, using $e^{-i\omega t}$');a.legend(frameon=False)
a=axs[0,1]
for j in range(5):
 a.add_patch(Circle((j,0),.13,color='#1766a5'));a.plot(j,0,'wo',ms=2)
 if j<4:
  xx=np.linspace(j+.13,j+.87,90);yy=.07*np.sin(12*np.pi*(xx-j-.13)/.74);a.plot(xx,yy,color='gray')
 a.annotate('',(j+.35,.3),(j,.3),arrowprops=dict(arrowstyle='->',color='#c33c29'))
a.annotate('',(2,-.45),(1,-.45),arrowprops=dict(arrowstyle='<->'));a.text(1.48,-.65,'a');a.text(1.8,.55,r'$U_n$');a.text(.25,.55,r'$M$',color='#1766a5');a.text(3.4,.55,r'$\alpha$',color='gray');a.set(xlim=(-.3,4.4),ylim=(-.85,.9),title='Longitudinal harmonic chain');a.axis('off')
a=axs[1,0];q=np.linspace(-1,1,800);a.plot(q,np.abs(np.sin(np.pi*q/2)),color='#1766a5');a.set(xlabel=r'$qa/\pi$',ylabel=r'$\omega/\omega_m$',title='One acoustic branch in the first zone',ylim=(0,1.12));a.axvline(0,color='gray',lw=.5)
a=axs[1,1];w=np.linspace(0,.999,800);a.plot(w,2/(np.pi*np.sqrt(1-w*w)),color='#1766a5');a.axvline(1,ls=':',color='gray');a.set(xlabel=r'$\omega/\omega_m$',ylabel=r'$\omega_m g(\omega)/N$',title='Both signs of wave number included',xlim=(0,1.04),ylim=(0,5));a.text(.2,3.8,r'$\int g(\omega)\,d\omega=N$')
fig.savefig('paper-2-drude-chain.png',dpi=170);plt.close(fig)
