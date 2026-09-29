"""Cubic-force effective potential and an inverse-fifth-power offset circle."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
import numpy as np

plt.rcParams.update({'font.size':10,'axes.titlesize':12,'figure.facecolor':'white','savefig.facecolor':'white'})
fig,axes=plt.subplots(1,2,figsize=(10.2,4.0),layout='constrained')
ax=axes[0];r=np.linspace(.35,1.85,600);V=.5/r**2+.25*r**4;E=1.6;roots=np.roots([1,0,-4*E,2]);turn=sorted(np.sqrt(z.real) for z in roots if abs(z.imag)<1e-9 and z.real>0)
ax.axvspan(*turn,color='#d7ebd4',alpha=.7);ax.plot(r,V,color='#176a9e',linewidth=2.3);ax.axhline(E,color='#b35a26',linestyle='--',label='Finite energy');ax.scatter([1],[.75],color='#176a9e',s=25);ax.scatter(turn,[E,E],color='#b35a26',s=25)
ax.annotate('Stable circular orbit',xy=(1,.75),xytext=(1.25,.45),arrowprops={'arrowstyle':'->'},fontsize=9,ha='center');ax.set(xlabel='Radius $r$',ylabel=r'$U_{\rm eff}$',title=r'$F=-r^3$, with $J=m=k=1$',xlim=(.35,1.85),ylim=(0,4.5));ax.grid(alpha=.18);ax.legend(fontsize=9)
ax=axes[1];phi=np.linspace(-np.pi,np.pi,600);ax.plot(1+np.cos(phi),np.sin(phi),color='#176a9e',linewidth=2.3);P=np.array([1+np.cos(np.deg2rad(65)),np.sin(np.deg2rad(65))]);angle=np.degrees(np.arctan2(P[1],P[0]))
ax.plot([0,2.08],[0,0],color='#999999',linewidth=.8);ax.plot([1,P[0]],[0,P[1]],color='#777777',linestyle='--');ax.annotate('',xy=P,xytext=(0,0),arrowprops={'arrowstyle':'->','color':'#b24d25','linewidth':1.5});ax.add_patch(Arc((0,0),.75,.75,theta1=0,theta2=angle,color='#b24d25'));ax.text(.43,.12,r'$\theta$',color='#b24d25');ax.text(P[0]*.5-.02,P[1]*.5+.07,'$r$',color='#b24d25');ax.text((1+P[0])/2+.05,P[1]/2,'$a$');ax.scatter([0,1,P[0]],[0,0,P[1]],s=[35,18,25],c=['#b24d25','#777777','#176a9e']);ax.text(-.02,-.18,'Force centre',ha='center',fontsize=9);ax.text(1,-.18,'Circle centre',ha='center',fontsize=9);ax.text(1.1,-1.19,r'$r=2a\cos\theta,\quad F\propto-r^{-5}$',ha='center')
ax.set(title='Force centre on the circular trajectory',xlim=(-.35,2.3),ylim=(-1.28,1.2));ax.set_aspect('equal');ax.axis('off')
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=130,facecolor='white',transparent=False,metadata={'Software':'Matplotlib'});plt.close(fig)
