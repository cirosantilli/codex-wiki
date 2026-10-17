"""Original explanatory figure. Python 3.14, NumPy and Matplotlib.
Write the PNG basename to the current working directory for the mirrored Make target.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":10,"figure.facecolor":"white","axes.facecolor":"white"})
fig,axs=plt.subplots(1,2,figsize=(10,4.2),layout='constrained')
a=axs[0];b=np.array([3.,0.]);s=np.array([.45,np.sqrt(1-.45**2)]);par=np.dot(b,s)*s;perp=b-par
for x in [np.zeros(2),b]:
 a.annotate('',xy=x+1.8*s,xytext=x,arrowprops={'arrowstyle':'<-','color':'#376b91','lw':1.5})
a.plot([0,3],[0,0],color='.25',lw=2);a.scatter([0,3],[0,0],s=45,color='#222222');a.text(-.12,-.2,'Antenna 1',ha='right');a.text(3.1,-.2,'Antenna 2',ha='left')
a.plot([0,par[0]],[0,par[1]],'--',color='#a85422',lw=1.5);a.text(par[0]-.5,par[1]+.05,r'$\mathbf{b}\cdot\mathbf{s}$',color='#a85422')
a.plot([0,perp[0]],[0,perp[1]],color='#784595',lw=2);a.plot([perp[0],3],[perp[1],0],'--',color='.6');a.text(perp[0]*.5,perp[1]*.5-.32,r'$b_p=|\mathbf{b}_\perp|$',color='#784595')
a.text(1.5,.1,'Physical baseline b',ha='center');a.text(1.5,1.7,'Parallel incoming rays',color='#376b91',ha='center');a.set(xlim=(-.7,4.6),ylim=(-1.8,2.1),aspect='equal',title='Geometric projection (arbitrary scale)');a.axis('off')
a=axs[1];H=np.linspace(-.45,.45,1400);P=.5*(1+np.cos(2*np.pi*4*np.sin(H)));a.plot(H,P,color='#6e4591',lw=2,label='Before fringe stopping');a.axhline(1,color='#27856c',ls='--',label='Reference phase removed');a.set(xlabel=r'Hour angle $H=\Omega_\oplus(t-t_0)$',ylabel=r'Source power / $4P_a$',ylim=(-.06,1.13),title='Antenna pointing tracks the source');a.legend(loc='lower center',fontsize=9);a.grid(alpha=.18);a.text(.03,.90,r'Illustrative $(b/\lambda)\cos\delta=4$',transform=a.transAxes,fontsize=9)
fig.savefig('paper-1-interferometer-fringes.png',dpi=150,facecolor='white');plt.close(fig)
