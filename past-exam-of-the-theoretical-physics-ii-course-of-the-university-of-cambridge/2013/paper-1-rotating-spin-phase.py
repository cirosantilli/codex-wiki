"""Original analytic illustration. Python 3.14, NumPy, Matplotlib; output to cwd."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig=plt.figure(figsize=(10,4.5),facecolor='white',layout='constrained')
ax=fig.add_subplot(121,projection='3d')
theta=np.pi/3;phi=np.linspace(0,2*np.pi,180);polar=np.linspace(0,theta,40);P,Q=np.meshgrid(phi,polar)
ax.plot_surface(np.sin(Q)*np.cos(P),np.sin(Q)*np.sin(P),np.cos(Q),color='#d8b352',alpha=.25,linewidth=0)
ax.plot(np.sin(theta)*np.cos(phi),np.sin(theta)*np.sin(phi),np.full_like(phi,np.cos(theta)),color='#2567a5',lw=2)
ax.quiver(0,0,0,np.sin(theta),0,np.cos(theta),color='#2567a5',arrow_length_ratio=.12,linewidth=2)
ax.plot([0,0],[0,0],[0,1.2],color='.3',lw=1);ax.text(0,0,1.22,'z');ax.text(.23,0,.6,r'$\theta=60^\circ$')
ax.text(-.8,-.55,1.05,r'Oriented cap $\mathcal{A}=\pi$')
ax.set(xlim=(-1,1),ylim=(-1,1),zlim=(0,1.3),xlabel='field x / B',ylabel='field y / B',zlabel='field z / B',title='Field direction traces a latitude')
ax.set_box_aspect((1,1,.85));ax.view_init(23,38)
bx=fig.add_subplot(122);w=np.linspace(.001,.7,700);splitting=np.sqrt(1-2*w*np.cos(theta)+w*w)
res=-np.pi+np.pi*(1-splitting)/w
bx.plot(w,res/np.pi,color='#2567a5',label='Exact cyclic phase minus adiabatic dynamical phase')
bx.axhline(-(1-np.cos(theta)),ls='--',color='#a34b32',label=r'Adiabatic limit $-\mathcal{A}/(2\pi)=-1/2$')
bx.set(xlabel=r'Drive frequency $\omega/B$',ylabel=r'Chosen phase representative / $\pi$',title='Upper spin branch; phases modulo 2π')
bx.grid(alpha=.2);bx.legend(fontsize=8,loc='lower left');bx.text(.03,.92,'Includes the spinor minus sign after 2π rotation',transform=bx.transAxes,fontsize=8)
fig.savefig('paper-1-rotating-spin-phase.png',dpi=150,facecolor='white');plt.close(fig)
