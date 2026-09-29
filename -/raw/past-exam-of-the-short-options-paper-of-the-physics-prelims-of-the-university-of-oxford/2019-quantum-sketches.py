"""Original quantum-physics solution diagrams; Python 3.14, NumPy, Matplotlib."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
import numpy as np
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white'})
fig,(a,b,c)=plt.subplots(1,3,figsize=(14,4.7),layout='constrained')
x=np.linspace(.00001,18,1400)
# x = h nu/(k_B T_0); density scale fixed for both temperatures.
f=x**3/np.expm1(x);hot=x**3/np.expm1(x/1.5)
a.plot(x,f,label=r'$T=T_0$',lw=2);a.fill_between(x,0,f,alpha=.25)
a.plot(x,hot,label=r'$T=1.5T_0$',lw=2)
a.set(xlabel=r'Frequency $h\nu/(k_BT_0)$',ylabel='Spectral energy density (common units)',title='Planck spectra: area gives total density')
a.set_xlim(0,18);a.set_ylim(bottom=0);a.legend(loc='upper right');a.annotate(r'$u(T_0)=\int U_\nu\,d\nu$',(3,.6),(8,2),arrowprops={'arrowstyle':'->'},ha='center')
b.set_aspect('equal');b.set_xlim(-1.55,1.65);b.set_ylim(-1.45,1.5);b.axis('off');b.set_title('Compton scattering: electron initially at rest')
theta=np.deg2rad(48);ep=.0002426;Eprime=1/(1+ep*(1-np.cos(theta)))
pout=Eprime*np.array([np.cos(theta),np.sin(theta)]);pe=np.array([1.,0.])-pout
phi=np.arctan2(-pe[1],pe[0])
def arrow(start,end,color):b.annotate('',end,start,arrowprops={'arrowstyle':'->','lw':2,'color':color})
arrow((-1.4,0),(0,0),'#4477aa');arrow((0,0),pout*1.55,'#4477aa');arrow((0,0),pe*1.55,'#c96d24')
b.plot(0,0,'ko',ms=4);b.plot([0,1.55],[0,0],':',color='0.6')
b.add_patch(Arc((0,0),1,1,theta1=0,theta2=48));b.text(.55,.2,r'$\theta$')
b.add_patch(Arc((0,0),.65,.65,theta1=-np.rad2deg(phi),theta2=0));b.text(.32,-.28,r'$\phi$')
b.text(-1.5,.2,r'Incoming photon'+'\n'+r'$p_\gamma=h\nu/c$',ha='left')
b.text(.5,1.25,r'Outgoing photon'+'\n'+r"$p_\gamma'=h\nu'/c$",ha='center')
b.text(1.05,-1.25,r'Recoil electron'+'\n'+r'$p_e\simeq m_ev$',ha='center')
b.text(-1.5,-.85,r'Initial electron: $p_e=0$'+'\n'+r'Incident direction: $+x$',ha='left')
z=np.linspace(0,1,600);linear=np.sqrt(3)*z;ground=np.sqrt(2)*np.sin(np.pi*z)
c.plot(z,linear,label=r'$\sqrt{L}\,\Psi=\sqrt{3}\,x/L$',lw=2);c.plot(z,ground,label=r'$\sqrt{L}\,\psi_1=\sqrt{2}\sin(\pi x/L)$',lw=2)
c.axvspan(0,1/3,alpha=.13,color='0.5');c.plot([1,1],[0,np.sqrt(3)],':',color='#4477aa')
c.annotate('Nonzero left limit\nat the right wall',(1,np.sqrt(3)),(.68,2.03),arrowprops={'arrowstyle':'->'},ha='center',fontsize=9)
c.text(.17,.48,'Left-third\nposition test',ha='center',fontsize=9)
c.set(xlabel=r'Position $x/L$',ylabel='Dimensionless amplitude',title='Position interval and global mode overlap',xlim=(0,1.02),ylim=(0,2.3));c.legend(loc='upper left',fontsize=9)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=110,facecolor='white')
