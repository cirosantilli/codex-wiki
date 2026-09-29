"""Original nearest-neighbour chain spectra and displacements. Python 3.14, numpy, matplotlib."""
import numpy as np
import matplotlib.pyplot as plt
fig,ax=plt.subplots(1,3,figsize=(12,3.9),layout='constrained',facecolor='white')
q=np.linspace(-np.pi,np.pi,501);ax[0].plot(q/np.pi,2*abs(np.sin(q/2)),lw=2);ax[0].set(xlabel=r'$qa/\pi$',ylabel=r'$\omega/\sqrt{\alpha/m}$',title='Monatomic first zone',ylim=(0,2.2))
q=np.linspace(-np.pi/2,np.pi/2,501);M=3.;m=1.;disc=np.sqrt((M+m)**2-4*M*m*np.sin(q)**2);low=np.sqrt((M+m-disc)/(M*m));high=np.sqrt((M+m+disc)/(M*m))
ax[1].plot(q/np.pi,low,lw=2,label='Acoustic');ax[1].plot(q/np.pi,high,lw=2,label='Optical');ax[1].set(xlabel=r'$qa/\pi$',ylabel=r'$\omega/\sqrt{\alpha/m}$',title='Diatomic first zone, M = 3m',xlim=(-.55,.68),ylim=(0,2.2));ax[1].legend(fontsize=8,loc='upper left')
wl=np.sqrt(2/M);wh=np.sqrt(2/m);ax[1].annotate('',xy=(.58,wh),xytext=(.58,wl),arrowprops=dict(arrowstyle='<->'));ax[1].text(.6,1.1,'Gap',rotation=90,fontsize=8)
for y,label,opt in [(1,'Acoustic, q near 0',False),(0,'Optical, q = 0',True)]:
 for j in range(6):
  heavy=j%2==1;disp=(-.11 if heavy else .33) if opt else .25
  ax[2].scatter([j],[y],s=95 if heavy else 35,color='C1' if heavy else 'C0');ax[2].annotate('',xy=(j+disp,y+.18),xytext=(j,y+.18),arrowprops=dict(arrowstyle='->',lw=1.3))
 ax[2].text(-.25,y-.30,label,fontsize=9)
ax[2].set(xlim=(-.5,5.6),ylim=(-.5,1.6),title='Schematic relative displacements');ax[2].axis('off')
for a in ax[:2]:a.grid(alpha=.18)
fig.savefig('paper-2-chain-phonons.png',dpi=150,facecolor='white')
