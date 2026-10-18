from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11})

fig,axs=plt.subplots(1,2,figsize=(10,4.5),layout='constrained',facecolor='white')
x=np.linspace(-2.8,2.8,600);X,Y=np.meshgrid(x,x);net=X*Y<-np.abs(X+Y);down=net&(np.abs(X)<1)
axs[0].contourf(X,Y,net.astype(int)+down.astype(int),levels=[-.5,.5,1.5,2.5],colors=['white','#dcebf0','#126782']);axs[0].axhline(0,color='gray',lw=.5);axs[0].axvline(0,color='gray',lw=.5);axs[0].set(xlabel=r'$x_1=L/f_1$',ylabel=r'$x_2=L/f_2$',title='Pale: net focusing; dark: both foci downstream')
lam=np.geomspace(.5e-9,10e-6,700)
def prod(f):
 sr2=lam*2/(16*np.pi**2);sp2=lam/2
 return np.sqrt((f*3e-9*2+sr2)*(f*3e-9/2+sp2)*(f*3e-11*2+sr2)*(f*3e-11/2+sp2))
ratio=prod(1)/prod(.1);axs[1].semilogx(lam*1e9,ratio,color='#126782');axs[1].axvline(10,color='#b14c2e',ls='--');axs[1].axhline(1,color='gray',ls=':');axs[1].set(xlabel='Wavelength (nm)',ylabel='Brightness factor',title='Tenfold emittance reduction; fixed beta = 2 m')

fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white',transparent=False,metadata={'Software':'Matplotlib'})
plt.close(fig)
