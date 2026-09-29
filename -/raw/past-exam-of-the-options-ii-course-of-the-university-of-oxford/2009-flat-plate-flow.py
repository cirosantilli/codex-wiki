"""Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7; output in CWD."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
x=np.linspace(-2.6,2.6,650);y=np.linspace(-1.9,1.9,500)
X,Y=np.meshgrid(x,y);Z=X+1j*Y;a=1;alpha=np.pi/4
S=np.sqrt(Z-a)*np.sqrt(Z+a)
with np.errstate(divide='ignore',invalid='ignore'):Q=np.cos(alpha)-1j*np.sin(alpha)*Z/S
mask=((np.abs(Y)<.025)&(np.abs(X)<a+.03))|(np.abs(Z-a)<.045)|(np.abs(Z+a)<.045)
u=np.ma.array(Q.real,mask=mask);v=np.ma.array(-Q.imag,mask=mask)
fig,ax=plt.subplots(figsize=(9,6.6),facecolor='white');ax.set_facecolor('white')
ax.streamplot(x,y,u,v,density=1.5,color='#367ea9',linewidth=.8,arrowsize=1)
ax.plot([-a,a],[0,0],color='#222222',linewidth=4,label='Plate')
st=a/np.sqrt(2)
ax.scatter([st,-st],[.025,-.025],s=45,color='#c64035',zorder=6)
ax.annotate('upper-face stagnation',(st,.025),xytext=(-.1,.65),arrowprops={'arrowstyle':'->'},fontsize=10)
ax.annotate('lower-face stagnation',(-st,-.025),xytext=(-2.2,-.65),arrowprops={'arrowstyle':'->'},fontsize=10)
ax.set(xlabel='$x/a$',ylabel='$y/a$',xlim=(-2.6,2.6),ylim=(-1.9,1.9),title='Flat-plate potential flow at forty-five degrees')
ax.set_aspect('equal');fig.tight_layout();fig.savefig('2009-flat-plate-flow.png',dpi=160,facecolor='white');plt.close(fig)
