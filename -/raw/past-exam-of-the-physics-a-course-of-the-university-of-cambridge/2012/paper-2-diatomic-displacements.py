"""Original calculated illustration; Python3.14,NumPy,Matplotlib; PNG output to cwd."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig,axs=plt.subplots(2,1,figsize=(8,3.8),facecolor='white',layout='constrained')
for ax,kind in zip(axs,['Acoustic, long wavelength: same displacement','Optical, zone centre: opposite displacements; M = 3m']):
 for j in range(8):
  heavy=j%2==0;u=.28 if ax is axs[0] else (-.18 if heavy else .54)
  ax.plot([j,j+1] if j<7 else [j,j], [0,0],color='.6',lw=1,zorder=1)
  ax.scatter(j,0,s=180 if heavy else 65,color='#2f6a99' if heavy else '#c67431',zorder=3)
  ax.annotate('',xy=(j+u,.32),xytext=(j,.32),arrowprops=dict(arrowstyle='->',lw=2,color='#2f6a99' if heavy else '#c67431'))
  ax.text(j,-.27,'M' if heavy else 'm',ha='center')
 ax.set(xlim=(-.6,8),ylim=(-.45,.55),title=kind);ax.axis('off')
axs[1].text(7.5,-.15,r'$Mu_M+mu_m=0$',ha='right',fontsize=10)
fig.savefig('paper-2-diatomic-displacements.png',dpi=150,facecolor='white');plt.close(fig)
