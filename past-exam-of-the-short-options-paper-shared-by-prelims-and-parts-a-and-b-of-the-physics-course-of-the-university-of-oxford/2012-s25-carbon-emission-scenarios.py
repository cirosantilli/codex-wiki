"""Original trajectories of the supplied linear carbon model, not measured data.
Python 3.14, numpy 2.3.5, matplotlib 3.10.7. Writes only CWD basename PNG.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
C0=279.;b0=.005;b1=.25;E0=.02;g=.03
year=np.linspace(1800,2500,1401);t=year-1800
prior=C0+(b1*E0/b0)*(g*np.exp(-b0*t)+b0*np.exp(g*t))/(g+b0)
c00=C0+(b1*E0/b0)*(g*np.exp(-b0*200)+b0*np.exp(g*200))/(g+b0)
e00=E0*np.exp(g*200);ceq=C0+b1*e00/b0
zero=np.where(t<=200,prior,C0+(c00-C0)*np.exp(-b0*(t-200)))
held=np.where(t<=200,prior,ceq+(c00-ceq)*np.exp(-b0*(t-200)))
fig,axs=plt.subplots(2,1,figsize=(7.6,5.5),sharex=True,layout='constrained',facecolor='white')
for ax in axs:ax.axvline(2000,color='#888888',ls=':',lw=1);ax.grid(alpha=.2)
axs[0].plot(year,zero,label='Zero emissions after 2000',lw=2,color='#27678e');axs[0].plot(year,held,label='Emissions held at year-2000 rate',lw=2,color='#ba6529');axs[0].axhline(ceq,color='#ba6529',ls='--',lw=1);axs[0].text(1815,ceq-25,f'Constant-emission limit: {ceq:.2f} ppmv',fontsize=9);axs[0].set(ylabel='CO₂ concentration (ppmv)',ylim=(260,710));axs[0].legend(loc='center right',fontsize=9)
axs[1].plot(year,3*np.log2(zero/C0),lw=2,color='#27678e');axs[1].plot(year,3*np.log2(held/C0),lw=2,color='#ba6529');axs[1].set(xlabel='Calendar year',ylabel='Equilibrium warming (K)',xlim=(1800,2500),ylim=(-.1,4.1));axs[1].text(1815,3.7,'Equilibrium response; no assumed thermal lag',fontsize=9)
fig.savefig('2012-s25-carbon-emission-scenarios.png',dpi=150,facecolor='white',metadata={'Software':'Matplotlib'})
