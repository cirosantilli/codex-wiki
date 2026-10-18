"""Original force and Rossby-velocity diagrams; Python 3.14, NumPy, Matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'figure.facecolor':'white','axes.facecolor':'white'})
fig,axs=plt.subplots(2,2,figsize=(11.5,8.3),layout='constrained')
f=1.;alpha=.35
J=np.array([[0.,-1.],[1.,0.]])
for ax,sign,title in [(axs[0,0],1.,'East side of a northern-hemisphere low'),(axs[0,1],-1.,'East side of a northern-hemisphere high')]:
 P=np.array([sign,0.]);u=(f*J@P-alpha*P)/(f*f+alpha*alpha)
 forces=[(-P,'Pressure force','#4477aa'),(-f*J@u,'Coriolis force','#c96d24'),(-alpha*u,'Drag','#aa3377')]
 for force,label,col in forces:
  ax.annotate('',force,(0,0),arrowprops={'arrowstyle':'->','lw':3,'color':col})
  end=force*1.12
  if label=='Drag':end+=np.array([.15*sign,-.12*sign])
  if label=='Pressure force':end+=np.array([0,.14])
  ax.text(end[0],end[1],label,color=col,ha='center',va='center',fontsize=10)
 ax.annotate('',u*.8,(0,0),arrowprops={'arrowstyle':'->','ls':'--','color':'black','lw':1.5})
 ax.text(u[0]*.85,u[1]*.85+.15*sign,'Velocity',ha='center',fontsize=10)
 ax.plot(0,0,'ko');ax.text(-1.25,.85,'Centre lies west',fontsize=9)
 ax.text(.6,-.9,'East →',fontsize=10)
 ax.set_title(title,fontsize=11);ax.set_aspect('equal');ax.set_xlim(-1.55,1.55);ax.set_ylim(-1.1,1.1);ax.axis('off')
K=np.linspace(-4.5,4.5,1000)
a,b=axs[1]
a.plot(K,-1/(1+K*K),lw=2);a.axhline(0,color='0.5',ls='--')
a.set(xlabel=r'$K=kL_d$',ylabel=r'$(c_{px}-U)/(\beta L_d^2)$',title='Intrinsic zonal phase velocity',ylim=(-1.1,.18));a.grid(alpha=.2)
b.plot(K,(K*K-1)/(1+K*K)**2,lw=2);b.axhline(0,color='0.5',ls='--')
b.scatter([-np.sqrt(3),np.sqrt(3)],[.125,.125],s=20,color='black')
b.scatter([-1,1],[0,0],s=20,color='black');b.annotate('maximum = 1/8',(np.sqrt(3),.125),(2.3,-.4),arrowprops={'arrowstyle':'->'},fontsize=9)
b.set(xlabel=r'$K=kL_d$',ylabel=r'$(c_{gx}-U)/(\beta L_d^2)$',title='Intrinsic zonal group velocity',ylim=(-1.1,.25));b.grid(alpha=.2)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=110,facecolor='white')
