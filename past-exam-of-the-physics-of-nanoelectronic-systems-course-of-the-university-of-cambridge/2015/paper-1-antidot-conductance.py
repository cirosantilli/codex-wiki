"""Original explanatory figure; Python3.14, NumPy2.3.5, Matplotlib3.10.7.
Output uses the PNG basename in the current working directory.
"""
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":10,"figure.facecolor":"white","savefig.facecolor":"white"})
fig,axs=plt.subplots(1,2,figsize=(9.6,4.2),layout='constrained')
x=np.linspace(.2,5.8,2000)
def dips(x,centers,width,depth):
 return sum(depth*width**2/((x-p)**2+width**2) for p in centers)
for width,depth,label in [(.035,.28,'Weak opposite-edge coupling'),(.095,.7,'Stronger resonant backscattering')]:
 g=2-dips(x,np.arange(1,6),width,depth)
 axs[0].plot(x,g,lw=1.6,label=label)
axs[0].set(xlabel=r'Flux coordinate $BA_{\rm eff}/\Phi_0$ (fixed-area model)',ylabel=r'$G/(e^2/h)$',ylim=(1.1,2.06),title='Resonant dips on a two-channel plateau');axs[0].legend(fontsize=8,loc='lower left');axs[0].grid(alpha=.15)
v=np.linspace(0,6,2400);base=.5*(1+np.tanh((v-.6)/.15))+.5*(1+np.tanh((v-3.3)/.18))
res=dips(v,[1.1,1.8,2.5],.045,.35)+dips(v,[3.9,4.6,5.3],.055,.45)
axs[1].plot(v,np.maximum(0,base-res),color='#287baf',lw=1.7)
axs[1].set(xlabel='Gate opening coordinate (illustrative)',ylabel=r'$G/(e^2/h)$',ylim=(-.07,2.06),title='Gate changes transmission and resonance energy');axs[1].grid(alpha=.15)
fig.suptitle('Illustrative resonance patterns; no absolute field or gate calibration assumed')
fig.savefig('paper-1-antidot-conductance.png',dpi=165)
