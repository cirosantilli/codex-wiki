"""Original explanatory plot. Python 3.14, numpy, matplotlib.
Run from the destination directory; writes a PNG basename to cwd.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'figure.facecolor':'white','savefig.facecolor':'white','font.size':10,'axes.spines.top':False,'axes.spines.right':False})
fig=plt.figure(figsize=(12,4.1),layout='constrained');gs=fig.add_gridspec(1,4,width_ratios=[1,1,1,1.6])
for j,(phi,end,name) in enumerate([(np.pi/2,np.pi/2,'+x'),(0,np.pi/2,'+y'),(0,np.pi,'−z')]):
 a=fig.add_subplot(gs[0,j],projection='3d');u=np.linspace(0,2*np.pi,80)
 for z in [-.65,0,.65]:
  r=np.sqrt(1-z*z);a.plot(r*np.cos(u),r*np.sin(u),np.full_like(u,z),color='lightgray',lw=.6)
 for az in [0,np.pi/2]:a.plot(np.sin(u)*np.cos(az),np.sin(u)*np.sin(az),np.cos(u),color='lightgray',lw=.6)
 t=np.linspace(0,end,300);xx=np.sin(phi)*np.sin(t);yy=np.cos(phi)*np.sin(t);zz=np.cos(t);a.plot(xx,yy,zz,color='#1766a5',lw=3);a.scatter([0,xx[-1]],[0,yy[-1]],[1,zz[-1]],color=['black','#c33c29'],s=25)
 a.set(xlim=(-1.1,1.1),ylim=(-1.1,1.1),zlim=(-1.1,1.1),xlabel='x',ylabel='y',zlabel='z',title=f'Rotating-frame target {name}');a.set_xticks([]);a.set_yticks([]);a.set_zticks([]);a.view_init(elev=20,azim=35);a.set_box_aspect((1,1,1));a.grid(False)
a=fig.add_subplot(gs[0,3]);r=np.linspace(0,2.5,600);a.plot(r,1/(1+r*r),color='#1766a5',lw=2);a.axhline(.5,ls='--',color='#c33c29');a.axvline(1,ls=':',color='gray');a.text(.15,.55,'Equator requires half transfer',fontsize=8);a.set(xlabel=r'$|\Delta|/\Omega$',ylabel='Maximum transferred population',ylim=(0,1.05),title='One fixed detuned pulse');fig.suptitle('Rotating axes at left; laboratory targets require the stated final-phase adjustment',fontsize=11)
fig.savefig('paper-1-spin-pulses.png',dpi=170);plt.close(fig)
