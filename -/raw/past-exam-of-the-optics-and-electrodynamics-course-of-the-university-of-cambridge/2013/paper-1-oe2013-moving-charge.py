"""Original angular field strengths; Python 3.14, NumPy, Matplotlib. PNG to cwd."""
import numpy as np
import matplotlib.pyplot as plt
theta=np.linspace(0,2*np.pi,3001)
fig,ax=plt.subplots(subplot_kw={'projection':'polar'},figsize=(5.3,5.2),layout='constrained')
for beta,color in [(0,'0.35'),(.8,'#1770af'),(.98,'#c35c28')]:
 field=(1-beta*beta)/(1-beta*beta*np.sin(theta)**2)**1.5
 ax.plot(theta,field,color=color,lw=1.8,label=fr'$v/c={beta}$')
ax.set_rmax(5.4);ax.set_rticks([1,3,5]);ax.set_rlabel_position(40)
ax.set_title('Motion along 0°: field strength at fixed separation\nRadius on plot: '+r'$E/E_{\mathrm{Coulomb}}$',pad=24,fontsize=11)
ax.legend(loc='lower center',bbox_to_anchor=(.5,-.24),ncol=3,fontsize=8)
fig.savefig('paper-1-oe2013-moving-charge.png',dpi=140,facecolor='white')
