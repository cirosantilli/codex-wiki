"""Original explanatory figure; Python3.14, NumPy2.3.5, Matplotlib3.10.7.
Write the PNG basename in the current working directory.
"""
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":10,"figure.facecolor":"white","savefig.facecolor":"white"})
x=np.linspace(0,1,4000);star=np.ones_like(x);iodine=np.ones_like(x)
for pos,depth,width in [(.14,.4,.014),(.42,.6,.021),(.76,.33,.016)]:star*=1-depth*np.exp(-.5*((x-pos)/width)**2)
for pos,depth in [(.08,.3),(.18,.4),(.27,.28),(.4,.35),(.52,.5),(.59,.3),(.71,.42),(.84,.3),(.93,.45)]:iodine*=1-depth*np.exp(-.5*((x-pos)/.004)**2)
sigma=.006;dx=x[1]-x[0];grid=np.arange(-.04,.04,dx);kernel=np.exp(-.5*(grid/sigma)**2);kernel/=kernel.sum();mult=star*iodine
conv=np.convolve(np.pad(mult,len(kernel),mode='edge'),kernel,mode='same')[len(kernel):-len(kernel)]
fig,axs=plt.subplots(3,1,figsize=(8.2,6.1),sharex=True,layout='constrained')
axs[0].plot(x,star,color='#287baf',label='Stellar template');axs[0].plot(x,iodine,color='#b07733',alpha=.75,label='Iodine transmission');axs[0].legend(fontsize=8,ncol=2)
axs[1].plot(x,mult,color='#6e5598',label='Product before convolution');axs[1].legend(fontsize=8)
axs[2].plot(x,conv,color='#287baf',label='After line-spread convolution');axs[2].legend(fontsize=8)
for ax in axs:ax.set(ylabel='Relative intensity',ylim=(.3,1.07));ax.grid(alpha=.18)
axs[0].set_title('Illustrative stellar and iodine absorption spectra');axs[-1].set_xlabel('Arbitrary spectral coordinate')
fig.savefig('paper-1-iodine-forward-model.png',dpi=160)
