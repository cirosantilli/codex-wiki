"""Sketch equality asymptotes; write the opaque PNG basename only in caller cwd."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
x=np.geomspace(0.015,200,600)
# Smooth guide, not an exact transfer solution: x^4 at low x; log^2 x at high x.
power=(x*np.log1p(x)/(1+x))**2
fig,axes=plt.subplots(1,2,figsize=(10,4.4),dpi=100,facecolor='white')
for ax,y,title,ylabel in zip(axes,[power,power/x**3],['Dimensionless density power','Dimensional density power'],[r'$\mathscr{P}_c$ (arbitrary units)',r'$P_c$ (arbitrary units)']):
 ax.set_facecolor('white');ax.loglog(x,y,color='#264e83',lw=2.5)
 ax.axvline(1,color='#867660',ls=':',lw=1.4)
 ax.set_title(title,fontsize=13);ax.set_xlabel(r'$k\tau_{\rm eq}\simeq k/k_{\rm eq}$',fontsize=12);ax.set_ylabel(ylabel,fontsize=12)
 ax.grid(True,which='major',alpha=.2);ax.set_xlim(x[0],x[-1])
axes[0].text(.045,1.e-4,r'$\propto k^4$',fontsize=14,color='#264e83')
axes[0].text(7,7,r'$\propto\ln^2(k/k_{\rm eq})$',fontsize=12,color='#264e83')
axes[1].text(.027,.035,r'$\propto k$',fontsize=14,color='#264e83')
axes[1].text(5,.002,r'$\propto k^{-3}\ln^2(k/k_{\rm eq})$',fontsize=12,color='#264e83')
fig.suptitle('Matter-spectrum shape after matter-radiation equality',fontsize=15,y=.97)
fig.text(.5,.02,'Smooth asymptotic guide; overall normalization and scale-independent late growth omitted.',ha='center',fontsize=10,color='#444444')
fig.subplots_adjust(left=.08,right=.98,bottom=.18,top=.83,wspace=.30)
fig.savefig('paper-53-matter-spectrum.png',dpi=100,facecolor='white',transparent=False)
plt.close(fig)
