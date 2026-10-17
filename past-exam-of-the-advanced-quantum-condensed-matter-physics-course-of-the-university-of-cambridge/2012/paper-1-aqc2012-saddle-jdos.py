"""Original teaching figure; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7. Writes PNG basename to cwd."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
plt.rcParams.update({"font.size":11,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})

fig,(a,b)=plt.subplots(1,2,figsize=(10.0,4.4),layout='constrained')
eta=.16;y=np.linspace(-np.sqrt(1-eta),np.sqrt(1-eta),500);r=np.sqrt(y*y+eta)
a.plot(r,y,color='#27638c',lw=2.2,label=r'$\delta>0$');a.plot(-r,y,color='#27638c',lw=2.2)
a.plot(y,r,color='#bd6528',lw=2.2,label=r'$\delta<0$');a.plot(y,-r,color='#bd6528',lw=2.2)
a.plot([-1,1],[-1,1],':',color='.55',label=r'$\delta=0$');a.plot([-1,1],[1,-1],':',color='.55')
a.plot([-1,1,1,-1,-1],[-1,-1,1,1,-1],color='.35',lw=1)
a.set(xlim=(-1.12,1.12),ylim=(-1.12,1.12),xlabel=r'$k_x/\Lambda$',ylabel=r'$k_y/\Lambda$',title='Both branches inside a square cutoff');a.set_aspect('equal');a.legend(loc='upper center',fontsize=9);a.grid(alpha=.1)
z=np.geomspace(1e-4,.8,500);I=2*np.arcsinh(1/np.sqrt(z));Isq=2*np.arcsinh(np.sqrt(1-z)/np.sqrt(z));Ilog=np.log(4/z)
b.semilogx(z,I,lw=2.5,label='Fixed y cutoff');b.semilogx(z,Isq,lw=1.8,label='Strict square cutoff');b.semilogx(z,Ilog,'--',color='.4',label=r'$\ln(4/\eta)$')
b.set(xlabel=r'$\eta/\Lambda^2=\delta/(A\Lambda^2)$',ylabel='Contour integral I',title='Same leading logarithm');b.legend(loc='upper right',fontsize=9);b.grid(alpha=.13)
fig.savefig(Path(__file__).stem+'.png',dpi=150,facecolor='white');plt.close(fig)
