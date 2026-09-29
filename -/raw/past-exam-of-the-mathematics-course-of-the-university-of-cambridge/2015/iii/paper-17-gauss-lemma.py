"""Gauss lemma on the round unit sphere. Python 3.14, NumPy 2.3.5,
Matplotlib 3.10.7. Write only the PNG basename to the process cwd.
Central Make controls the publication _media destination.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
r=np.linspace(0,1.12,34);theta=np.linspace(0,2*np.pi,110)
R,T=np.meshgrid(r,theta);X=np.sin(R)*np.cos(T);Y=np.sin(R)*np.sin(T);Z=np.cos(R)
fig=plt.figure(figsize=(5.5,3.5),dpi=120,facecolor='white')
ax=fig.add_subplot(111,projection='3d',proj_type='ortho');ax.set_facecolor('white')
ax.plot_surface(X,Y,Z,color='#c9d9e8',alpha=.20,linewidth=0,antialiased=True,shade=False)
for angle in np.linspace(-.7,-.7+2*np.pi,9)[:-1]:
 ax.plot(np.sin(r)*np.cos(angle),np.sin(r)*np.sin(angle),np.cos(r),color='#2469a1',linewidth=1.4)
rho=.76
ax.plot(np.sin(rho)*np.cos(theta),np.sin(rho)*np.sin(theta),np.full_like(theta,np.cos(rho)),color='#d87916',linewidth=2.7)
a=-.7;p=np.array([np.sin(rho)*np.cos(a),np.sin(rho)*np.sin(a),np.cos(rho)])
radial=np.array([np.cos(rho)*np.cos(a),np.cos(rho)*np.sin(a),-np.sin(rho)])
angular=np.array([-np.sin(a),np.cos(a),0.])
ax.quiver(*p,*(.28*radial),color='#164d7a',linewidth=2.8,arrow_length_ratio=.25)
ax.quiver(*p,*(.28*angular),color='#a54e05',linewidth=2.8,arrow_length_ratio=.25)
ax.scatter(*p,color='#202020',s=16,depthshade=False);ax.scatter(0,0,1,color='#202020',s=16,depthshade=False)
ax.text(0,0,1.055,'p',fontsize=11);ax.text(*(p+.34*radial),'Radial',fontsize=9,color='#164d7a');ax.text(*(p+.32*angular),'Angular',fontsize=9,color='#a54e05')
ax.set_xlim(-1,1);ax.set_ylim(-1,1);ax.set_zlim(.3,1.13);ax.set_box_aspect((1,1,.65));ax.view_init(elev=28,azim=-58);ax.set_axis_off()
fig.suptitle('Radial geodesics meet a geodesic sphere orthogonally',fontsize=11,y=.97)
fig.text(.5,.045,'Round unit sphere: radial and angular tangent vectors have inner product zero',ha='center',fontsize=8)
fig.subplots_adjust(left=0,right=1,bottom=.07,top=.89)
fig.savefig(Path.cwd()/'paper-17-gauss-lemma.png',dpi=120,facecolor='white',transparent=False)
plt.close(fig)
