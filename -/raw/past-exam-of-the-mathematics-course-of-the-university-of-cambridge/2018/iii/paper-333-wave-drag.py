"""Original mD=1 schematic; run in its directory. Dependencies in pyproject.toml."""
from pathlib import Path
import os
os.environ.setdefault('MPLCONFIGDIR','/tmp/2018-paper-333-mpl-cache')
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
y=np.linspace(0,1,161); z=np.linspace(-4,4,321); Y,Z=np.meshgrid(y,z)
C=.25*(np.exp(-np.abs(Z-1))-np.exp(-np.abs(Z+1)))
F=np.where(Z<-1,-1,np.where(Z>1,0,(Z-1)/2))
Cp=.25*(-np.sign(Z-1)*np.exp(-np.abs(Z-1))+np.sign(Z+1)*np.exp(-np.abs(Z+1)))
Fp=np.where(np.abs(Z)<1,.5,0); U=Cp-Fp
U[np.isclose(np.abs(Z),1)]=-.5*np.exp(-1)*np.sinh(1)
acc=U*np.sin(np.pi*Y); density=-C*np.cos(np.pi*Y)
res=C*np.sin(np.pi*Y); eul=(C-F)*np.sin(np.pi*Y)
vres=Cp*np.sin(np.pi*Y); wres=-np.pi*C*np.cos(np.pi*Y)
veul=U*np.sin(np.pi*Y); weul=-np.pi*(C-F)*np.cos(np.pi*Y)
fig,axs=plt.subplots(2,2,figsize=(10,6),dpi=100,facecolor='white',layout='constrained')
for ax,data,title in [(axs[0,0],acc,'Zonal acceleration: westward throughout'),(axs[0,1],density,'Density tendency: opposite signs above and below')]:
    ax.contourf(Y,Z,data,levels=np.linspace(-.8,.8,25),cmap='RdBu_r')
    ax.contour(Y,Z,data,levels=[0],colors='#333333',linewidths=.7)
    ax.set_title(title,fontsize=10)
axs[0,0].text(.5,0,'negative',ha='center',color='#222222',fontsize=10)
axs[0,1].text(.22,1.1,'negative',ha='center',color='#222222',fontsize=9)
axs[0,1].text(.78,1.1,'positive',ha='center',color='#222222',fontsize=9)
axs[0,1].text(.22,-1.1,'positive',ha='center',color='#222222',fontsize=9)
axs[0,1].text(.78,-1.1,'negative',ha='center',color='#222222',fontsize=9)
for ax,chi,v,w,title in [(axs[1,0],res,vres,wres,'Residual circulation: two closed cells'),(axs[1,1],eul,veul,weul,'Eulerian circulation: open to the lower region')]:
    ax.contour(Y,Z,chi,levels=12,colors='#819cb1',linewidths=.7)
    ax.streamplot(y,z,v,w,density=.75,color='#183c5b',linewidth=.9,arrowsize=1.05)
    ax.set_title(title,fontsize=10)
for ax in axs.flat:
    for edge in [-1,1]:ax.axhline(edge,color='#666666',linestyle='--',linewidth=.7)
    ax.set(xlabel=r'$y/L$',ylabel=r'$z/D$',xlim=(0,1),ylim=(-4,4))
fig.savefig(Path.cwd()/'paper-333-wave-drag.png',facecolor='white',transparent=False,dpi=100)
plt.close(fig)
