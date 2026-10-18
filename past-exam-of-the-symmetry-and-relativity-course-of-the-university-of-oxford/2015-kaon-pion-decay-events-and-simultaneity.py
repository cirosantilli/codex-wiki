from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":11,"font.family":"DejaVu Sans","figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})

c=.299792458;M,m,E=497.6,139.6,600.;p=np.sqrt(E*E-M*M);E1=M*M/(2*E);E2=E-E1;p1=np.sqrt(E1*E1-m*m)
t1,t2=15*E1/m,30*E2/m;r1=np.array([0,p1/m*c*15]);r2=np.array([p/m*c*30,-p1/m*c*30]);d=r2-r1;length=np.linalg.norm(d);n=d/length;beta=c*(t2-t1)/length;gamma=1/np.sqrt(1-beta*beta)
xi=np.array([r1@n,r2@n]);ct=c*np.array([t1,t2]);xp=gamma*(xi-beta*ct);ctp=gamma*(ct-beta*xi)
assert np.isclose(ctp[0],ctp[1]);separation=xp[1]-xp[0]
fig,axs=plt.subplots(1,3,figsize=(13.4,5),layout='constrained');ax=axs[0]
for r,name,col in [(r1,'first pion','#174c75'),(r2,'second pion','#b35b15')]:
 ax.annotate('',xy=r,xytext=(0,0),arrowprops=dict(arrowstyle='->',lw=2,color=col));ax.scatter(*r,color=col,s=50);ax.text(*(r+np.array([.7,.5])),name,color=col,fontsize=10)
ax.plot([r1[0],r2[0]],[r1[1],r2[1]],ls='--',color='gray');ax.scatter([0],[0],color='black',s=25);ax.set(xlim=(-2,28),ylim=(-13,8),xlabel='Lab x (m)',ylabel='Lab y (m)',title='Lab tracks and decay events');ax.set_aspect('equal');ax.grid(alpha=.15)
ax=axs[1];ax.scatter(xi,ct,color=['#174c75','#b35b15'],s=55);ax.plot(xi,ct,'--',color='gray');ax.text(xi[0],ct[0]+1.5,'A',ha='center');ax.text(xi[1],ct[1]+1.5,'B',ha='center')
z=np.linspace(0,20,100);ax.plot(xi[0]+z,ct[0]+z,color='#d7c5b0',ls=':',label='light slope from A');ax.text(10,8,r'$\Delta\xi=26.117$ m'+'\n'+r'$c\Delta t=18.715$ m',ha='center',fontsize=10)
ax.set(xlim=(-5,29),ylim=(0,31),xlabel='Along lab event separation (m)',ylabel='ct (m)',title='The connector is spacelike');ax.grid(alpha=.15)
ax=axs[2];ax.scatter(xp,ctp,color=['#174c75','#b35b15'],s=55);ax.plot(xp,ctp,'--',color='gray');ax.annotate('',xy=(xp[1],ctp[0]-1),xytext=(xp[0],ctp[0]-1),arrowprops=dict(arrowstyle='<->',lw=1.5))
ax.text(np.mean(xp),ctp[0]-3,f'{separation:.3f} m',ha='center',fontsize=12);ax.text(np.mean(xp),ctp[0]+3,'Same time in this frame',ha='center',fontsize=11)
ax.set(xlim=(min(xp)-4,max(xp)+4),ylim=(ctp[0]-7,ctp[0]+7),xlabel="Boosted coordinate (m)",ylabel="ct prime (m)",title=f'Boost speed = {beta:.4f} c');ax.grid(alpha=.15)
fig.suptitle('A Lorentz boost changes simultaneity, not the spacelike interval',fontsize=15)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=140,transparent=False)
