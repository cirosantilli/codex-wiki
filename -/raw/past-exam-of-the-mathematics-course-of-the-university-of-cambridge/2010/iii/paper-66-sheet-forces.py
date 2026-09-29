"""Original viscous-sheet force sketch; Python 3.14 and pinned root dependencies.
Outputs paper-66-sheet-forces.png in caller CWD; honors MPLCONFIGDIR.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig,ax=plt.subplots(figsize=(9.2,4.1),layout='constrained',facecolor='white')
x=np.linspace(0,1,200);z=.36+.2*x+.04*x*x
ax.fill_between(x,-z,z,color='#cae6f2');ax.plot(x,z,color='#176a9c',lw=2);ax.plot(x,-z,color='#176a9c',lw=2);ax.plot([0,0],[-z[0],z[0]],color='#555555',ls='--');ax.plot([1,1],[-z[-1],z[-1]],color='#555555',ls='--')
def arrow(a,b,c):ax.annotate('',xy=b,xytext=a,arrowprops={'arrowstyle':'->','color':c,'lw':2})
# Tractions on vertical cuts (arrows define positive tensile sign).
arrow((0,0),(-.33,0),'#7c4c95');arrow((1,0),(1.33,0),'#7c4c95');ax.text(-.16,-.16,r'$-h\sigma_{xx}$',ha='center',color='#7c4c95');ax.text(1.19,-.16,r'$h\sigma_{xx}$',ha='center',color='#7c4c95')
# Four endpoint surface-tension pulls, tangent and away from retained slice.
for xx in [0,1]:
 zz=.36+.2*xx+.04*xx*xx;slope=.2+.08*xx;sgn=2*xx-1
 for side in [-1,1]:
  arrow((xx,side*zz),(xx+sgn*.27,side*zz+sgn*side*slope*.27),'#b74c2a');ax.text(xx+sgn*.19,side*zz+side*.11,r'$\gamma$',ha='center',color='#b74c2a')
# Uniform gas pressure directed inward on broad faces.
for xx in [.24,.52,.8]:
 zz=.36+.2*xx+.04*xx*xx;slope=.2+.08*xx
 for side in [-1,1]:arrow((xx-.035,side*(zz+.22)),(xx+.02,side*(zz-.015)),'#356b58')
ax.text(.51,.88,r'$p_a$: inward normal pressure',ha='center',color='#356b58');ax.text(.5,-.87,r'Cut traction is $\pm\boldsymbol{\sigma}\cdot\mathbf{e}_x$; shear parts are smaller-order.',ha='center',fontsize=10);ax.text(.5,-1.07,'Gravity and inertia are neglected; the symmetric vertical forces cancel.',ha='center',fontsize=10)
ax.annotate('',xy=(1,-.7),xytext=(0,-.7),arrowprops={'arrowstyle':'<->','color':'gray'});ax.text(.5,-.73,r'$\delta x$',ha='center',va='top');ax.text(.48,0,'liquid slice',ha='center',color='#176a9c');ax.set(xlim=(-.48,1.48),ylim=(-1.14,1.03));ax.set_axis_off();ax.set_title('Forces on a planar viscous-sheet slice (per unit transverse width)')
fig.savefig('paper-66-sheet-forces.png',dpi=130,facecolor='white',transparent=False)
