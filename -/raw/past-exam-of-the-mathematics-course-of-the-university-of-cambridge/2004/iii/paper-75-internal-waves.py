"""Original frame/ray sketch. Python 3.14, numpy 2.3, matplotlib 3.10.
Writes a single opaque PNG basename to caller CWD; preserves MPLCONFIGDIR.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig,ax=plt.subplots(1,3,figsize=(12.5,4),layout='constrained',facecolor='white')
k,m,U=1,1.5,1
x=np.linspace(-2,2,200);z=np.linspace(0,2.5,180);X,Z=np.meshgrid(x,z)
for a,frame in zip(ax[:2],['Fluid frame','Terrain frame']):
    a.contour(X,Z,k*X+m*Z,levels=np.arange(-2,7,.85),colors='#c4c4c4',linewidths=.8)
    a.set(xlabel="x'" if frame=='Fluid frame' else 'x',ylabel='z',title=frame,xlim=(-2,2),ylim=(0,2.5),aspect='equal')
    a.text(.02,.95,'Grey: phase lines',transform=a.transAxes,va='top',fontsize=9)
D=k*k+m*m
cp=np.array([-U*k*k/D,-U*k*m/D]);cg=np.array([-U*m*m/D,U*k*m/D]);lab=cg+np.array([U,0])
start=np.array([.4,1.25])
for vec,color,label in [(cg,'#126ba0','group'),(cp,'#a62d22','phase')]:
    end=start+1.5*vec
    ax[0].annotate('',xy=end,xytext=start,arrowprops={'arrowstyle':'->','color':color,'lw':2})
    ax[0].text(end[0]-.2,end[1]+.12,label,color=color,fontsize=9)
ax[0].plot([1.2,-1.8],[0,2],'--',color='#126ba0',lw=1)
end=start+1.5*lab
ax[1].annotate('',xy=end,xytext=start,arrowprops={'arrowstyle':'->','color':'#126ba0','lw':2})
ax[1].text(end[0]-.2,end[1]+.12,'group',color='#126ba0',fontsize=9)
ax[1].text(-1.9,.25,'Phase pattern stationary',fontsize=9)
ax[1].plot([-1.3,.3],[0,2.4],'--',color='#126ba0',lw=1)
H=1.6
xx=np.linspace(0,4.2,200);zz=np.linspace(0,H,150);XX,ZZ=np.meshgrid(xx,zz)
W=-np.sin(k*XX)*np.sin(m*(H-ZZ))/np.sin(m*H)
ax[2].contourf(XX,ZZ,W,levels=13,cmap='RdBu_r',alpha=.4)
ax[2].axhline(H,color='black',lw=2);ax[2].axhline(0,color='black',lw=2)
px=[.1,.1+H/m,.1+2*H/m,.1+3*H/m];pz=[0,H,0,H]
ax[2].plot(px,pz,color='#126ba0',lw=2)
for j in range(3):
    a=.55
    ax[2].annotate('',xy=(px[j]+a*(px[j+1]-px[j]),pz[j]+a*(pz[j+1]-pz[j])),xytext=(px[j]+.35*(px[j+1]-px[j]),pz[j]+.35*(pz[j+1]-pz[j])),arrowprops={'arrowstyle':'->','color':'#126ba0','lw':2})
ax[2].set(xlabel='x',ylabel='z',title='Rigid-lid standing field',ylim=(-.08,H+.22),xlim=(0,4.2),aspect='equal')
ax[2].text(.1,H+.08,'Rigid lid',fontsize=9)
ax[2].text(.1,.1,'Energy reflects downstream',fontsize=9,bbox={'facecolor':'white','alpha':.8,'edgecolor':'none'})
fig.savefig('paper-75-internal-waves.png',dpi=120,facecolor='white',transparent=False)
