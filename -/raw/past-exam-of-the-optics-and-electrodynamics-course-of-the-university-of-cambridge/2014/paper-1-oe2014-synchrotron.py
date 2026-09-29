"""Original educational diagram. Python 3.14, NumPy and Matplotlib; writes a PNG basename in the current working directory."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white'})
from matplotlib.patches import Arc
fig,ax=plt.subplots(figsize=(7,4.2),layout='constrained')
phi=np.linspace(-1.4,1.4,400);R=2.1;x=R*np.sin(phi);y=R*(1-np.cos(phi));ax.plot(x,y,color='#225c91',lw=2)
ax.scatter([0],[0],s=40,color='#225c91');ax.text(-.25,-.2,'Charge',ha='right')
ax.annotate('',xy=(1,0),xytext=(0,0),arrowprops={'arrowstyle':'->','lw':2,'color':'#225c91'});ax.text(.6,-.24,r'$\mathbf{v}$',color='#225c91')
ax.annotate('',xy=(0,1.0),xytext=(0,0),arrowprops={'arrowstyle':'->','lw':1.5,'color':'#555'});ax.text(-.15,.8,r'$\mathbf{a}$',ha='right')
ang=.15;xx=np.linspace(0,3.1,30);ax.fill_between(xx,-np.tan(ang)*xx,np.tan(ang)*xx,color='#edc982',alpha=.45)
for a in [-ang,0,ang]:ax.plot(xx,xx*np.tan(a),color='#b5781e',lw=1.2)
ax.text(2.25,.7,r'Beaming angle $\sim1/\gamma$',ha='center',color='#8e5e16')
ax.text(-1.5,1.8,'Curved trajectory',ha='center',color='#225c91');ax.text(.6,-.9,r'$\omega_c\simeq3\gamma^3c/(2\rho)$',ha='center',fontsize=13)
ax.set(xlim=(-2.5,3.3),ylim=(-1.2,2.2),aspect='equal',title='Radiation near the instantaneous velocity tangent');ax.axis('off')
fig.savefig('paper-1-oe2014-synchrotron.png',dpi=150,facecolor='white');plt.close(fig)
