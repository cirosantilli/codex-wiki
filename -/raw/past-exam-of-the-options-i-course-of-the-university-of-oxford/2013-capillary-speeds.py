"""Original diagram; Python 3.14.4, numpy 2.3.5, matplotlib 3.10.7.
Run with CWD the matching _media directory; output is relative to CWD.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
q=np.linspace(.12,3.5,900)
cp=np.sqrt((q+1/q)/2)
cg=(1+3*q*q)/(2*np.sqrt(2*q*(1+q*q)))
fig,ax=plt.subplots(figsize=(7.4,4.5),layout='constrained',facecolor='white')
ax.plot(q,cp,label=r'phase speed $c_p$',color='#176aa5',lw=2)
ax.plot(q,cg,label=r'group speed $c_g$',color='#bc5227',lw=2)
ax.axvline(1,color='#888888',ls='--',lw=1);ax.plot(1,1,'ko',ms=4)
ax.annotate('equal speeds at phase minimum',(1,1),(1.5,.72),arrowprops=dict(arrowstyle='->',color='#555555'),fontsize=10)
ax.text(.22,2.0,'crests move forward\nthrough the packet',fontsize=10)
ax.text(2.0,.90,'crests drift backwards\nrelative to the packet',fontsize=10)
ax.set(xlabel=r'$k/k_c$',ylabel=r'speed / $(4gT/\rho)^{1/4}$',xlim=(.12,3.5),ylim=(.65,2.2))
ax.set_title('Deep-water gravity-capillary waves');ax.legend(frameon=False,loc='upper right')
ax.spines[['top','right']].set_visible(False)
fig.savefig('2013-capillary-speeds.png',dpi=120,facecolor='white')
