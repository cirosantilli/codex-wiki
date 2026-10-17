"""Original explanatory figure; Python 3.14, NumPy and Matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white','savefig.facecolor':'white'})

fig,axs=plt.subplots(1,2,figsize=(9,4.5),layout='constrained')
z=np.linspace(0,1,501);ns=np.arange(1,500)[:,None]
for age,color in [(.05,'#cc7a1f'),(.3,'#a44b77'),(1,'#307eac')]:
 theta=1-z+np.sum(2*(-1.)**(ns+1)/(np.pi*ns)*np.exp(-ns**2*age)*np.sin(ns*np.pi*z),axis=0)
 axs[0].plot(theta,z,color=color,label=fr'$t/\tau_0={age}$')
axs[0].plot(1-z,z,'k--',label='old-age limit')
axs[0].set(xlabel=r'$(T-T_0)/(T_1-T_0)$',ylabel=r'height $z/a$',title='Intended hot-ridge cooling model');axs[0].legend(fontsize=8);axs[0].grid(alpha=.15)
a=1e5;rho=3000;rw=1000;g=10;b=rho*4e-5*1300;h=b*a/(2*(rho-rw));y=np.linspace(0,h+a,1000)
p=np.where(y<h,(rho-rw)*g*y,g*b/(2*a)*(a-(y-h))**2)
axs[1].fill_betweenx(y/1000,0,p/1e6,color='#88b3c8',alpha=.6);axs[1].plot(p/1e6,y/1000,color='#285f7d')
axs[1].axhline(h/1000,ls=':',color='k');axs[1].text(3,10,'old seafloor at 3.9 km',fontsize=8)
axs[1].invert_yaxis();axs[1].set(xlabel='ridge minus old-column pressure / MPa',ylabel='depth below ridge seafloor / km',title='Area under curve = force per ridge length')
axs[1].text(5,88,r'$F=2.75\times10^{12}$ N/m'+'\n(with topographic term)',fontsize=9)

fig.savefig(Path(__file__).stem+'.png',dpi=150,bbox_inches='tight',facecolor='white');plt.close(fig)
