"""Original image construction and local-stiffness calculations. Python 3.14; output cwd."""
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({"axes.titlesize":10,"axes.labelsize":10})
fig,ax=plt.subplots(1,2,figsize=(9,3.8),layout='constrained');a=ax[0];xx=np.linspace(-1.5,1.5,200);a.fill_between(xx,abs(xx),1.7,color='#eef7f4');a.plot(xx,xx,'k-');a.plot(xx,-xx,'k-')
for x,y,name,col in [(0,1,'real +q','#007f60'),(-1,0,'image -q','#c14343'),(1,0,'image -q','#c14343'),(0,-1,'image +q','#3169b2')]:
 a.scatter([x],[y],s=90,c=col,zorder=4);a.annotate(name,(x,y),xytext=(5,8),textcoords='offset points',fontsize=9)
a.annotate('',xy=(0,.5),xytext=(0,.9),arrowprops=dict(arrowstyle='->',lw=2,color='#007f60'));a.text(.07,.6,'net force');a.set(xlim=(-1.7,1.7),ylim=(-1.5,1.7),aspect='equal',xlabel='x / height',ylabel='y / height',title='Images enforce both conductor potentials')
eta=np.linspace(0,.55,300);ratio=(np.sqrt(2)+.25)/(1/np.sqrt(2)-.25);a=ax[1];a.plot(eta,1-2*eta,label=r'Vertical restoring stiffness $k_y/k$');a.plot(eta,ratio*eta,label=r'Lateral force gradient $D_x/k$');a.axhline(0,color='.4',lw=.8);a.set(xlabel=r'$\eta=\beta/(k y_e^3)$',ylabel='Dimensionless local coefficient',title='Vertical softening and lateral force gradient');a.legend(fontsize=8);a.grid(alpha=.2)
fig.savefig('paper-1-image-wedge.png',dpi=150,facecolor='white')
