"""Original fits of supplied numerical data; Python 3.14, NumPy and Matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white','savefig.facecolor':'white'})
x=np.array([0,20,50,70,100,120,150,170,200,220,250,270,300.]);dt=np.array([23,21,19,17,16,15,15,15,17,18,20,22,25.]);ta=np.array([35,38,34,36,30,28,34,26,35,34,36,35,37.])
m,b,c=np.polyfit(x-150,dt**2,2);x0=150-b/(2*m);B=c-b*b/(4*m);grid=np.linspace(0,300,400)
fig,axs=plt.subplots(1,3,figsize=(12.4,3.7),layout='constrained')
axs[0].errorbar(x,dt,yerr=.5,fmt='o',ms=4,color='#246d9c',label='given differences ±0.5 s');axs[0].plot(grid,np.sqrt(m*(grid-x0)**2+B),color='#bd7831',label='hyperbolic fit');axs[0].axvspan(x0-15,x0+15,color='#246d9c',alpha=.09);axs[0].axvline(x0,color='grey',lw=.7,ls=':');axs[0].set(xlabel='horizontal position (km)',ylabel='arrival difference (s)',title='Clock offsets cancel locally');axs[0].legend(fontsize=7)
q=(x-x0)**2/1e4;g=np.linspace(0,2.6,200);axs[1].errorbar(q,dt**2,yerr=dt,fmt='o',ms=4,color='#246d9c');axs[1].plot(g,1e4*m*g+B,color='#bd7831');axs[1].set(xlabel=r'$(x-x_0)^2$ (10⁴ km²)',ylabel=r'$(\Delta t)^2$ (s²)',title='Slope fixes the speed difference')
g=np.linspace(14,26,200);fit=np.polyfit(dt,ta,1);axs[2].plot(dt,ta,'o',color='#246d9c',ms=4);axs[2].plot(g,g+15,label='ratio 2, origin 15 s',lw=1.8,color='#bd7831');axs[2].plot(g,.8*g+np.mean(ta-.8*dt),label='ratio 2.25',ls='--',color='#7a5d9b');axs[2].plot(g,np.polyval(fit,g),label='free-slope fit',ls=':',color='#333333');axs[2].set(xlabel='arrival difference (s)',ylabel='absolute A reading (s)',title='Clock scatter limits the ratio check');axs[2].legend(fontsize=7)
for ax in axs:ax.grid(alpha=.17)
fig.savefig(Path(__file__).stem+'.png',dpi=145,bbox_inches='tight',facecolor='white');plt.close(fig)
