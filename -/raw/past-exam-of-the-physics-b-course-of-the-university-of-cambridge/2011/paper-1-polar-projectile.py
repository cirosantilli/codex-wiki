import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,Rectangle
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False,'figure.facecolor':'white','savefig.facecolor':'white'})

u=500.;g=9.81;Om=7.2921e-5;tf=np.sqrt(2)*u/g;tt=np.linspace(0,tf,400);xx=u/np.sqrt(2)*tt;zz=u/np.sqrt(2)*tt-g*tt**2/2;yy=-Om*u/np.sqrt(2)*tt**2
fig,ax=plt.subplots(1,2,figsize=(10,3.8),layout='constrained')
ax[0].plot(xx/1000,zz/1000);ax[0].axhline(0,color='.6');ax[0].set(xlabel='Downrange (km)',ylabel='Height (km)',title='Leading vertical trajectory');ax[0].text(2,1,r'$45^\circ$ launch; uniform gravity',fontsize=10)
ax[1].plot(xx/1000,np.zeros_like(xx),'k--',label='Uncorrected aim');ax[1].plot(xx/1000,yy,label='First-order rotating-frame path');ax[1].plot(xx[-1]/1000,yy[-1],'o');ax[1].annotate(f'{abs(yy[-1]):.0f} m right',xy=(xx[-1]/1000,yy[-1]),xytext=(12,-130),arrowprops={'arrowstyle':'->'});ax[1].set(xlabel='Downrange (km)',ylabel='Leftward displacement (m)',title='Top view; transverse scale enlarged');ax[1].legend(fontsize=8,loc='lower left');ax[1].set_ylim(-160,20)
fig.suptitle('Flat local model at North pole; no drag or planetary-curvature correction',fontsize=12)
fig.savefig('paper-1-polar-projectile.png',dpi=155)
