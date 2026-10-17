"""Original analytic explanatory figure; Python 3.14, NumPy and Matplotlib.
Run in the desired output directory. No examination figure or external image used.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False})
c=np.linspace(415,505,600)
forcing=5.4*np.log(c/415)
increment=5.4*np.log((c+2.5)/c)
fig,axs=plt.subplots(1,2,figsize=(9.2,4),layout='constrained')
axs[0].plot(c,forcing,color='#2479ad',lw=2,label='Accumulated from 415 ppm')
axs[0].plot(c,increment,color='#d87b28',lw=2,label='Next 2.5 ppm increment')
axs[0].set(xlabel='CO2 baseline concentration (ppm)',ylabel='Forcing (W m$^{-2}$)',title='Two distinct forcing references')
axs[0].legend(fontsize=8)
values=[2367.33795,1965.89227,73443.77535]
labels=['415 to 417.5 ppm','500 to 502.5 ppm','415 to 500 ppm']
bars=axs[1].barh(labels,values,color=['#d87b28','#d87b28','#2479ad'])
axs[1].set_xscale('log');axs[1].set_xlim(100,180000)
for bar,val in zip(bars,values):axs[1].text(val*1.08,bar.get_y()+bar.get_height()/2,f'{val:,.0f}',va='center',fontsize=9)
axs[1].set(xlabel='One-year equivalent SO2 mass (source tons)',title='Using the stipulated linear calibration')
fig.savefig('paper-id-forcing-reference.png',dpi=170,facecolor='white')
