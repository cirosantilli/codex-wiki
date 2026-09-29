"""Original harmonic-potential sketches. Python 3.14; matplotlib 3.10.7, numpy 2.3.5.

Save the white PNG to cwd, normally the corresponding _media directory.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig,(left,right)=plt.subplots(1,2,figsize=(9.0,4.8),layout='constrained',facecolor='white')
levels=[-.8,-.4,0,.4,.8]
colors=['#0072b2','#0072b2','#555555','#d55e00','#d55e00']
for value,color in zip(levels,colors):
    ang=np.pi*value/2
    endpoint=min(2.3/max(np.cos(ang),1e-9),2.3/max(abs(np.sin(ang)),1e-9))
    q=np.linspace(.025,endpoint,80)
    left.plot(q*np.cos(ang),q*np.sin(ang),color=color,lw=1.7)
    ll=.83*endpoint
    left.text(ll*np.cos(ang)+.04,ll*np.sin(ang),f'{value:g}',fontsize=10,color=color)
left.axvline(0,color='#444444',lw=1.3)
left.set(xlim=(-.1,2.5),ylim=(-2.5,2.5),xlabel='$u$',ylabel='$v$',title=r'Ray contours: $\Phi/\alpha$')
left.text(.08,2.27,r'$+\alpha$',color='#b94b00');left.text(.08,-2.38,r'$-\alpha$',color='#0072b2')
left.set_aspect('equal')
x=np.linspace(-1.02,1.02,600);X,Y=np.meshgrid(x,x);r2=X*X+Y*Y
potential=np.ma.masked_where(r2>=1,2/np.pi*np.arctan2(2*Y,1-r2))
cs=right.contour(X,Y,potential,levels=levels,colors=colors,linewidths=1.4)
label_positions=[]
for value in levels:
    tangent=np.tan(np.pi*value/2)
    ordinate=0 if value==0 else (np.sqrt(1+tangent*tangent)-1)/tangent
    label_positions.append((0,ordinate))
right.clabel(cs,inline=True,fmt='%g',fontsize=10,manual=label_positions)
p=np.linspace(0,np.pi,400)
right.plot(np.cos(p),np.sin(p),color='#d55e00',lw=3)
right.plot(np.cos(p),-np.sin(p),color='#0072b2',lw=3)
right.scatter([-1,1],[0,0],s=35,facecolors='white',edgecolors='#333333',zorder=5)
right.text(0,1.08,r'$+V\quad(v>0)$',ha='center',color='#b94b00')
right.text(0,-1.17,r'$-V\quad(v<0)$',ha='center',color='#0072b2')
right.set(xlim=(-1.25,1.25),ylim=(-1.3,1.3),xlabel='$x$',ylabel='$y$',title=r'Disk contours: $\Psi/V$')
right.set_aspect('equal');right.grid(alpha=.15)
fig.savefig(Path(__file__).with_suffix('.png').name,dpi=160,facecolor='white')
