"""Original solution diagram. Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7. Output to current working directory."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path
plt.rcParams.update({"figure.facecolor":"white","axes.facecolor":"white","font.size":10,"axes.spines.top":False,"axes.spines.right":False})

from math import erfc,exp,sqrt
fig,axs=plt.subplots(1,3,figsize=(13,3.7),layout='constrained')
c=1.25;D=.015;t=np.linspace(.03,1.6,500);x=1
response=np.array([.5*erfc((x-c*z)/(2*sqrt(D*z)))+.5*exp(c*x/D)*erfc((x+c*z)/(2*sqrt(D*z))) for z in t])
axs[0].plot(t,np.where(t<1/c,0,1),label='Zero diffusion');axs[0].plot(t,response,label='Positive diffusion');axs[0].set(xlabel='Time at x=1',ylabel='Normalized discharge rise',title='Small-step hydrograph');axs[0].legend(fontsize=8)
x=np.linspace(0,2*np.pi,300)
for ax,F in zip(axs[1:],(.7,1.4)):
 bed=.1*np.cos(x);surface=.1*F**2/(F**2-1)*np.cos(x)+1
 ax.plot(x,bed,label='Bed');ax.plot(x,surface,label='Free surface');ax.fill_between(x,bed,surface,color='#d4ecff',alpha=.5);ax.set(xlabel='Downstream coordinate',ylabel='Elevation',title=('Dune phase: F<1' if F<1 else 'Antidune phase: F>1'));ax.set_xticks([0,np.pi,2*np.pi],['0','π','2π']);ax.legend(fontsize=8)
fig.savefig(Path.cwd()/'2010-river-response.png',dpi=150,facecolor='white');plt.close(fig)
