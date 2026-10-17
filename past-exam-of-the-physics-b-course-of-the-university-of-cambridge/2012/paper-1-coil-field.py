"""Original field-line plot from direct loop Biot-Savart integration."""
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10})
s=np.linspace(-2.6,2.6,151);z=np.linspace(-2.7,2.7,161);S,Z=np.meshgrid(s,z)
Bx=np.zeros_like(S);Bz=np.zeros_like(S)
for phi in np.arange(480)*2*np.pi/480:
 den=(S*S+1-2*S*np.cos(phi)+Z*Z)**1.5
 Bx+=Z*np.cos(phi)/den
 Bz+=(1-S*np.cos(phi))/den
mask=(np.hypot(S-1,Z)<.09)|(np.hypot(S+1,Z)<.09)
Bx[mask]=np.nan;Bz[mask]=np.nan
fig,ax=plt.subplots(figsize=(6,5.6),layout='constrained')
ax.streamplot(s,z,Bx,Bz,density=1.28,color='#176ca1',linewidth=.9,arrowsize=1.1)
ax.scatter([-1],[0],s=110,facecolor='white',edgecolor='black',zorder=5);ax.scatter([-1],[0],s=11,c='black',zorder=6)
ax.scatter([1],[0],s=110,facecolor='white',edgecolor='black',zorder=5);ax.scatter([1],[0],s=45,marker='x',c='black',zorder=6)
ax.text(-1.0,-.32,'Loop wire',ha='center',bbox={'facecolor':'white','edgecolor':'none','alpha':.9},fontsize=9)
ax.axvline(0,color='.5',ls=':',lw=.7)
ax.set(xlim=(-2.6,2.6),ylim=(-2.7,2.7),xlabel=r'$x/R$',ylabel=r'$z/R$',title='Circular-loop field: up through the centre, return outside')
ax.set_aspect('equal');ax.spines[['top','right']].set_visible(False)
fig.savefig('paper-1-coil-field.png',dpi=170,facecolor='white');plt.close(fig)
