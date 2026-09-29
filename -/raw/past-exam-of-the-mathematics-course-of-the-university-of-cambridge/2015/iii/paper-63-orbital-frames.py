from pathlib import Path
import os
import tempfile
os.environ.setdefault("MPLCONFIGDIR", str(Path(tempfile.gettempdir()) / "codex-wiki-matplotlib"))
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({"font.size": 10, "savefig.facecolor": "white"})

Id, Ip, Od, Op = np.deg2rad([87, 88, 45, 49])
A=np.cos(Id)*np.sin(Ip)*np.cos(Op-Od)-np.sin(Id)*np.cos(Ip)
B=np.sin(Ip)*np.sin(Op-Od)
Om=np.arctan2(B,A)
Im=np.arccos(np.cos(Id)*np.cos(Ip)+np.sin(Id)*np.sin(Ip)*np.cos(Op-Od))
fig=plt.figure(figsize=(8.6,4.4),dpi=100,facecolor='white')
ax=fig.add_subplot(121)
for ang,color,r,label in [(Od,'#1269a8',1.,'Disk sky node: 45 degrees'),(Op,'#ca551b',.78,'Planet sky node: 49 degrees')]:
 ax.arrow(0,0,r*np.sin(ang),r*np.cos(ang),width=.008,head_width=.05,color=color,length_includes_head=True,label=label)
 ax.plot([-r*np.sin(ang),0],[-r*np.cos(ang),0],color=color,ls=':',lw=1.5)
ax.scatter([0],[0],s=45,color='#e6ac00',zorder=4)
ax.text(-.16,.07,'Star')
ax.axhline(0,color='gray',lw=.7);ax.axvline(0,color='gray',lw=.7)
ax.set(xlim=(-.95,.95),ylim=(-.95,.95),xlabel='Sky Y coordinate',ylabel='Sky X coordinate (North)',title='Sky plane: Z points toward observer')
ax.set_aspect('equal');ax.legend(loc='lower center',fontsize=8)
ax=fig.add_subplot(122,projection='3d')
xp=np.array([np.cos(Om),np.sin(Om),0.])
yp=np.array([-np.sin(Om)*np.cos(Im),np.cos(Om)*np.cos(Im),np.sin(Im)])
zp=np.cross(xp,yp);t=np.linspace(0,2*np.pi,300)
ax.plot(np.cos(t),np.sin(t),np.zeros_like(t),color='#1269a8',label='Disk plane')
c=.8*(xp[:,None]*np.cos(t)+yp[:,None]*np.sin(t));ax.plot(*c,color='#ca551b',label='Planet plane')
for v,col,label in [(np.array([1.,0,0]),'#1269a8','x'),(np.array([0.,1.,0]),'#1269a8','y'),(np.array([0.,0.,1.]),'#1269a8','z'),(xp,'#ca551b',"x': mutual node"),(zp,'#ca551b',"z': planet normal")]:
 ax.quiver(0,0,0,*v,length=1.05,color=col,arrow_length_ratio=.08);
 if label in ['x','y']:ax.text(*(1.17*v),label,fontsize=9,transform=ax.transAxes)
ax.text2D(.08,.14,rf'$I_m={np.rad2deg(Im):.3f}^\circ$'+'\n'+rf'$\Omega_m={np.rad2deg(Om):.3f}^\circ$',fontsize=9,transform=ax.transAxes)
ax.text2D(.35,.78,'z: disk normal',color='#1269a8',fontsize=9,transform=ax.transAxes)
ax.text2D(.35,.73,"z': planet normal",color='#ca551b',fontsize=9,transform=ax.transAxes)
ax.text2D(.65,.56,"x': mutual node",color='#ca551b',fontsize=9,transform=ax.transAxes)
ax.scatter([0],[0],[0],color='#e6ac00',s=30)
ax.set(xlim=(-1.15,1.15),ylim=(-1.15,1.15),zlim=(-.5,1.2),title='Disk coordinates: actual small mutual tilt')
ax.view_init(elev=22,azim=-48);ax.set_axis_off();ax.legend(loc='lower left',fontsize=8)
fig.subplots_adjust(left=.08,right=.99,bottom=.13,top=.88,wspace=.12)
fig.savefig(Path.cwd()/'paper-63-orbital-frames.png',dpi=100,facecolor='white')
