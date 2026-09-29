"""Original teaching plot. Python3.14, NumPy and Matplotlib. Writes basename PNG to cwd."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
d=.1e-3;W=.2e-3;lam=500e-9
y=np.linspace(-.14e-3,.14e-3,3001);th=np.linspace(-.012,.012,2501)
small_width=.008e-3
narrow=((abs(y+d/2)<small_width/2).astype(float)-(abs(y-d/2)<small_width/2).astype(float))
step=((y>=-W/2)&(y<0)).astype(float)-((y>=0)&(y<=W/2)).astype(float)
s=np.pi*W*np.sin(th)/(2*lam);uniform=np.sinc(2*s/np.pi)**2;split=np.sinc(s/np.pi)**2*np.sin(s)**2
fig,axs=plt.subplots(2,2,figsize=(10.5,7.3),layout='constrained')
axs[0,0].plot(y*1e3,narrow,color='#28679b');axs[0,0].set(title='Narrow-pair field transmission',xlabel='Aperture coordinate (mm)',ylabel='Amplitude transmission',ylim=(-1.4,1.4))
axs[0,0].text(.5,.97,'Slit widths illustrative',transform=axs[0,0].transAxes,ha='center',va='top',fontsize=9)
axs[0,1].plot(th*1e3,np.sin(np.pi*d*np.sin(th)/lam)**2,color='#a14c2c');axs[0,1].set(title='Narrow-pair intensity: phase reversal',xlabel='Observation angle (mrad)',ylabel='Intensity / its maximum',ylim=(-.05,1.1))
axs[1,0].plot(y*1e3,step,color='#276d4e');axs[1,0].set(title='Half-slit field transmission',xlabel='Aperture coordinate (mm)',ylabel='Amplitude transmission',ylim=(-1.4,1.4))
axs[1,1].plot(th*1e3,uniform,':',color='gray',label='Uniform slit');axs[1,1].plot(th*1e3,split,color='#2c689b',label='Half with phase reversal');axs[1,1].set(title='Finite full-width aperture',xlabel='Observation angle (mrad)',ylabel='Intensity / uniform central peak',ylim=(-.04,1.1));axs[1,1].legend(fontsize=9)
for ax in axs.flat:ax.grid(alpha=.2)

fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=140,facecolor='white')
