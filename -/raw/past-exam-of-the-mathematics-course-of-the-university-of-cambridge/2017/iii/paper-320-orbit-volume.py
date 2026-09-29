"""Original schematic confocal orbit-volume sketch; not a computed trajectory.
Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7; unchanged root dependency pins.
Rename beside paper-320.bigb to paper-320-orbit-volume.py; output goes to CWD.
"""
from pathlib import Path
import struct
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
A,B=1.,4.
def rz(lam,mu):
 return np.sqrt((lam+A)*(mu+A)/(A-B)),np.sqrt(np.maximum(0,(lam+B)*(mu+B)/(B-A)))
def main():
 plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'figure.facecolor':'white','savefig.facecolor':'white'})
 fig=plt.figure(figsize=(11,5.000001),dpi=100,facecolor='white')
 left=fig.add_subplot(121);right=fig.add_subplot(122,projection='3d')
 mu=np.linspace(-B,-2,130)
 r1,z1=rz(1,mu);r2,z2=rz(4,mu)
 for sign in [-1,1]:
  left.fill(np.r_[r1,r2[::-1]],sign*np.r_[z1,z2[::-1]],color='#9cbfe0',edgecolor='#254f7c',lw=1.3)
 t=np.linspace(0,2*np.pi,300)
 for lam,color in [(1,'#bd593c'),(4,'#bd593c')]:
  left.plot(np.sqrt(lam+A)*np.cos(t),np.sqrt(lam+B)*np.sin(t),color=color,lw=1.5)
 for m,style in [(-2,'-'),(-3,':')]:
  rv=np.linspace(0,3,200);zv=np.sqrt((m+B)*(1+rv**2/abs(m+A)))
  for sign in [-1,1]:left.plot(rv,sign*zv,color='#488253',ls=style,lw=1.5)
 left.scatter([0,0],[np.sqrt(B-A),-np.sqrt(B-A)],c='black',s=15,zorder=4)
 left.annotate('Common foci',(0,np.sqrt(B-A)),(.25,3.12),arrowprops={'arrowstyle':'-','color':'black'},fontsize=10)
 left.text(2.17,.16,r'$\lambda=4$',color='#bd593c');left.text(1.22,-.25,r'$\lambda=1$',color='#bd593c')
 left.text(1.98,2.60,r'$\mu=-2$',color='#488253');left.text(1.05,.65,r'$\mu=-3$',color='#488253')
 left.set_xlim(-.15,3);left.set_ylim(-3.3,3.3);left.set_aspect('equal');left.set_xlabel('$R$');left.set_ylabel('$z$')
 left.axhline(0,color='#888888',lw=.7);left.axvline(0,color='#888888',lw=.7)
 left.set_title('Meridional section: allowed region',fontsize=12)
 # Opaque surface patches over a 285-degree sweep leave a geometric cutaway.
 phi=np.linspace(.12,1.7*np.pi,100)
 for lam,color in [(1,'#7199bc'),(4,'#a2c4e2')]:
  mm,pp=np.meshgrid(mu,phi);rr,zz=rz(lam,mm)
  for sign in [-1,1]:right.plot_surface(rr*np.cos(pp),rr*np.sin(pp),sign*zz,color=color,alpha=1,linewidth=0,shade=True)
 ll,pp=np.meshgrid(np.linspace(1,4,90),phi);rr,zz=rz(ll,-2)
 for sign in [-1,1]:right.plot_surface(rr*np.cos(pp),rr*np.sin(pp),sign*zz,color='#7ca786',alpha=1,linewidth=0,shade=True)
 for pp0 in [phi[0],phi[-1]]:
  for lam in [1,4]:
   rr,zz=rz(lam,mu)
   for sign in [-1,1]:right.plot(rr*np.cos(pp0),rr*np.sin(pp0),sign*zz,color='#24486a',lw=1.1)
  rr,zz=rz(np.linspace(1,4,100),-2)
  for sign in [-1,1]:right.plot(rr*np.cos(pp0),rr*np.sin(pp0),sign*zz,color='#24486a',lw=1.1)
 right.set_box_aspect((1,1,1.2));right.set_xlim(-2.6,2.6);right.set_ylim(-2.6,2.6);right.set_zlim(-2.8,2.8)
 right.view_init(elev=24,azim=-57);right.set_axis_off();right.set_title('Azimuthal sweep (cutaway)',fontsize=12)
 fig.subplots_adjust(left=.055,right=.99,bottom=.13,top=.9,wspace=.13)
 fig.text(.5,.025,r'Confocal spheroids bound $\lambda$; hyperboloids bound $\mu$. Generic nonresonant motion samples the swept volume.',ha='center',fontsize=10)
 p=Path.cwd()/(Path(__file__).stem+'.png');fig.savefig(p,dpi=100,facecolor='white',transparent=False);plt.close(fig)
 assert struct.unpack('>II',p.read_bytes()[16:24])==(1100,500)
 print(p)
if __name__=='__main__':main()
