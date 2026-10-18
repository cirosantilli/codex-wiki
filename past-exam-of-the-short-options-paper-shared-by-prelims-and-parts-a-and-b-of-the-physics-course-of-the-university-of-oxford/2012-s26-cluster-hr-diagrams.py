"""Original schematic cluster populations; curves are not stellar model isochrones.
Python 3.14, numpy 2.3.5, matplotlib 3.10.7. Writes only CWD basename PNG.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig,axs=plt.subplots(1,2,figsize=(10.6,4.5),sharey=True,layout='constrained',facecolor='white')
for a in axs:
 a.set(xscale='log',xlim=(35000,2500),ylim=(-4,5),xlabel='Effective temperature (K)');a.set_xticks([30000,10000,5000,3000],['30000','10000','5000','3000']);a.grid(alpha=.18)
axs[0].set_ylabel(r'Luminosity $\log_{10}(L/L_\odot)$')
a=axs[0];a.plot([26000,18000,10000,6500,5000,3500,2800],[4.6,3.3,1.6,.3,-.6,-2,-3],color='#27678e',lw=2);a.plot([4500,3500,3000],[-.3,-.65,-1.0],color='#b76b29',ls='--',lw=2)
a.scatter([18000,4000],[4.5,4.3],color='#b76b29',s=25);a.text(23000,2.1,'Main sequence',rotation=-49,fontsize=9);a.annotate('Hot turnoff',xy=(26000,4.6),xytext=(12500,4.0),arrowprops=dict(arrowstyle='->'),fontsize=9);a.text(4600,.15,'Pre-main-sequence',fontsize=9,ha='center');a.text(15500,4.75,'Possible evolved massive stars',fontsize=9,ha='center');a.set_title('Young open cluster (schematic)')
b=axs[1];b.plot([6500,5800,5000,3500,2800],[.35,0,-.6,-2,-3],color='#27678e',lw=2);b.plot([6500,5300,4400,3700,3300],[.35,.6,1.2,2.2,3.2],color='#b76b29',lw=2);b.plot([15000,10000,7000,5000],[1.65,1.65,1.65,1.65],color='#b14865',lw=2);b.plot([5000,4100,3400],[1.7,2.5,3.4],color='#b76b29',ls='--',lw=1.5);b.plot([25000,16000,10000,6500],[-1.5,-2.1,-2.9,-3.7],color='#666666',lw=2)
b.annotate('Low-mass turnoff',xy=(6500,.35),xytext=(21000,.15),arrowprops=dict(arrowstyle='->'),fontsize=9);b.text(8500,1.9,'Horizontal branch',fontsize=9);b.text(4400,2.4,'RGB / AGB',rotation=65,fontsize=9);b.text(21000,-2.8,'White dwarfs',fontsize=9);b.set_title('Old globular cluster (schematic)')
fig.savefig('2012-s26-cluster-hr-diagrams.png',dpi=150,facecolor='white',metadata={'Software':'Matplotlib'})
