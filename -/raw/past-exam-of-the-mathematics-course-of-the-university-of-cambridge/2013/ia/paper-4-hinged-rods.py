"""Python3.14; NumPy2.3.5/Matplotlib3.10.7. PNG basename only in cwd.
Caller MPLCONFIGDIR is honored; no hardcoded cache paths.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
theta=np.deg2rad(28)
A=np.array([0.,0.]);B=2*np.array([np.cos(theta),np.sin(theta)]);C=np.array([4*np.cos(theta),0.])
G1=(A+B)/2;G2=(B+C)/2
fig,ax=plt.subplots(figsize=(7.5,3.5),dpi=120,facecolor='white')
ax.set_facecolor('white')
ax.axhline(0,color='black',lw=1.4)
ax.plot([A[0],B[0]],[A[1],B[1]],color='#0072b2',lw=5)
ax.plot([B[0],C[0]],[B[1],C[1]],color='#d55e00',lw=5)
for pos,label,offset in [(A,'A = O',(-.08,-.2)),(B,'B',(0,.13)),(C,'C',(.04,-.2))]:
    ax.scatter(*pos,color='black',s=32,zorder=5)
    ax.text(*(pos+np.array(offset)),label,fontsize=12,ha='center')
for pos,label in [(G1,'G₁'),(G2,'G₂')]:
    ax.scatter(*pos,color='white',edgecolor='black',s=55,zorder=5)
    ax.text(pos[0],pos[1]+.13,label,fontsize=11,ha='center')
phi=np.linspace(0,theta,40)
ax.plot(.65*np.cos(phi),.65*np.sin(phi),color='black',lw=1)
ax.text(.72,.13,'θ',fontsize=13)
ax.annotate('',xy=(C[0]+.43,.08),xytext=(C[0]-.12,.08),
            arrowprops={'arrowstyle':'->','color':'black','lw':1.3})
ax.text(C[0]+.2,.21,'slides',fontsize=10,ha='center')
ax.annotate('',xy=(B[0],.015),xytext=(B[0],B[1]-.04),
            arrowprops={'arrowstyle':'<->','color':'#555555','lw':1})
ax.text(B[0]+.06,.29,'2l sin θ',fontsize=10)
ax.text(G1[0]-.2,G1[1]-.2,'length 2l',fontsize=10,color='#0072b2')
ax.text(G2[0]+.1,G2[1]-.23,'length 2l',fontsize=10,color='#d55e00')
ax.text(0,1.4,'Arch coordinates with maintained floor contact',fontsize=13)
ax.set_xlim(-.4,4.35);ax.set_ylim(-.38,1.62);ax.set_aspect('equal');ax.axis('off')
fig.subplots_adjust(left=.025,right=.985,bottom=.05,top=.99)
fig.savefig('paper-4-hinged-rods.png',dpi=120,facecolor='white',transparent=False)
plt.close(fig)
