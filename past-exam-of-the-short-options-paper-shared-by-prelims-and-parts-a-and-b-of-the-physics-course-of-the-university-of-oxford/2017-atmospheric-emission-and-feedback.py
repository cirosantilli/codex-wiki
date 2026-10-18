from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':12})

fig,axs=plt.subplots(1,2,figsize=(10,4.8),layout='constrained',facecolor='white')
tau=np.geomspace(.01,100,600)
for factor,col,label in [(1,'#126782','Original abundance'),(2,'#b14c2e','Double abundance'),(.5,'#75458d','Half abundance')]:
 B=1+.25*np.maximum(np.log(tau/(factor*.3)),0);axs[0].plot(B,tau,color=col,label=label)
axs[0].set_yscale('log');axs[0].invert_yaxis();axs[0].set(xlabel='Relative Planck radiance',ylabel='Downward optical depth',title='Fixed temperatures, remapped depth');axs[0].legend(fontsize=10)
S=1360;sig=5.670374419e-8;Te=(.7*S/(4*sig))**.25;A=4*sig*Te**3-1.5-S*.003/4;B=S*.0002/4;T=np.linspace(0,17,500);N=3.7-A*T+B*T*T
axs[1].plot(T,N,color='#126782');axs[1].axhline(0,color='gray');roots=np.sort(np.roots([B,-A,3.7]));axs[1].scatter(roots,[0,0],color=['#126782','#b14c2e']);axs[1].annotate('Stable',xy=(roots[0],0),xytext=(1.5,-1.3),arrowprops={'arrowstyle':'->'});axs[1].annotate('Unstable',xy=(roots[1],0),xytext=(11,2.5),arrowprops={'arrowstyle':'->'});axs[1].set(xlabel='Surface warming (K)',ylabel=r'Net heating ($\mathrm{W\,m^{-2}}$)',title='Quadratic albedo-feedback model')

fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white',transparent=False,metadata={'Software':'Matplotlib'})
plt.close(fig)
