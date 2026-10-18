"""Original relaxation, energy landscape, waiting density and chain response."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 11, 'axes.spines.top': False, 'axes.spines.right': False})
fig, axes=plt.subplots(2,2,figsize=(11,7.6),layout='constrained',facecolor='white')
a=axes[0,0]; t=np.linspace(0,6,400)
a.plot(t,.8*(1-np.exp(-t)),lw=2,color='#355a9b')
a.axhline(.8,color='grey',ls=':',label=r'$B_\infty=0.8$ (illustrative)')
a.set(xlabel=r'$(k_f+k_b)t$',ylabel='$B(t)$',ylim=(0,1),title='A  Two-state relaxation from A'); a.legend(frameon=False)
a=axes[0,1]; d=7.; A=7.9; F=5.; x=np.linspace(-5.5,9,1200)
U=lambda x: A*(1-np.cos(2*np.pi*x/d))-F*x
s=F*d/(2*np.pi*A); theta=np.arcsin(s); xm=d*theta/(2*np.pi)
barriers=np.array([-d/2-d*theta/(2*np.pi),d/2-d*theta/(2*np.pi)])
a.plot(x,U(x)-U(xm),lw=2,color='#8b5292')
a.scatter([xm],[0],color='#269572',zorder=4,label='dwell minimum')
a.scatter(barriers,U(barriers)-U(xm),color='#bd7820',zorder=4,label='adjacent barriers')
a.set(xlabel='position (nm)',ylabel='energy above dwell (pN nm)',title='B  Tilted sinusoid: A = 7.9, F = 5')
a.legend(frameon=False,fontsize=9)
a=axes[1,0]; u=np.linspace(0,7,500)
a.plot(u,u*np.exp(-u),lw=2,color='#269572'); a.axvline(1,color='grey',ls=':')
a.set(xlabel=r'$u=(k_f+k_b)t$',ylabel='dimensionless conditional density',title='C  Two consecutive forward exits')
a.text(2,.28,'mode u = 1\nmean u = 2')
a=axes[1,1]; u=np.linspace(.001,8,500); L=1/np.tanh(u)-1/u
# Plot force against extension, without using inconsistent source parameters.
a.plot(L,u,lw=2,color='#355a9b',label='FJC orientational law')
a.plot(L,3*L,ls='--',color='#bd7820',label='weak-force tangent')
a.set(xlabel=r'$\langle R_z\rangle/(Nb)$',ylabel=r'$fb/(k_BT)$',title='D  Entropic elasticity, no segment stretch')
a.legend(frameon=False,fontsize=9)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=110,facecolor='white')
