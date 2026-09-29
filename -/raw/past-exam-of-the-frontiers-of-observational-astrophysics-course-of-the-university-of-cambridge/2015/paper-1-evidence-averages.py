"""Original explanatory figure; Python3.14, NumPy2.3.5, Matplotlib3.10.7.
Write the PNG basename in the current working directory.
"""
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":10,"figure.facecolor":"white","savefig.facecolor":"white"})
fig,axs=plt.subplots(1,3,figsize=(10.7,4),gridspec_kw={'width_ratios':[2.1,1,1]},layout='constrained')
x=np.linspace(30,170,800);axs[0].plot(x,np.exp(-abs(x-100)/50),color='black',lw=2,label='Common likelihood / C')
vals=[5*(np.exp(-.8)-np.exp(-1)),5*(1-np.exp(-.2)),1-np.exp(-1)];colors=['#b07733','#287baf','#7c4e98']
for j,(lo,hi) in enumerate([(50,60),(90,110),(50,150)]):
 axs[0].plot([lo,hi],[-.12-.12*j]*2,color=colors[j],lw=6,solid_capstyle='butt')
 axs[0].plot([lo,hi],[vals[j]]*2,color=colors[j],lw=2,ls='--')
 axs[0].text(hi+2,-.12-.12*j,'ABC'[j],va='center',color=colors[j])
axs[0].set(xlabel=r'$\theta/u$',ylabel='Likelihood and interval averages',ylim=(-.47,1.1),title='Each prior is normalized over its interval');axs[0].legend(fontsize=8,loc='upper right');axs[0].grid(alpha=.18)
axs[1].bar(list('ABC'),vals,color=colors);axs[1].set(ylim=(0,1),ylabel=r'$Z_H/C$',title='Bayesian evidence');axs[1].grid(axis='y',alpha=.18)
w=np.array(vals)*[1,1,.3];w/=w.sum();axs[2].bar(list('ABC'),w,color=colors);axs[2].set(ylim=(0,1),ylabel='Probability',title='Posterior probability\n(prior odds 1:1:0.3)');axs[2].grid(axis='y',alpha=.18)
fig.savefig('paper-1-evidence-averages.png',dpi=165)
