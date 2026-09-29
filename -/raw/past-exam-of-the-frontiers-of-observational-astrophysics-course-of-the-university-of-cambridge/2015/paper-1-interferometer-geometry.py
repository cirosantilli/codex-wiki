"""Original explanatory figure; Python3.14, NumPy2.3.5, Matplotlib3.10.7.
Write the PNG basename in the current working directory.
"""
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":10,"figure.facecolor":"white","savefig.facecolor":"white"})
fig,axs=plt.subplots(1,2,figsize=(10,4.6),layout='constrained')
ax=axs[0];A=np.array([-1.7,0.]);B=np.array([1.7,0.]);th=np.deg2rad(26);al=np.deg2rad(10)
ax.plot([-2.1,2.1],[0,0],color='.5',lw=1)
for point,label in [(A,'Antenna A'),(B,'Antenna B')]:
 ax.scatter(*point,c='black',s=28,zorder=5);ax.text(point[0],-.18,label,ha='center',fontsize=9)
 ax.plot([point[0],0],[point[1],-1.08],color='#666666',lw=1.3)
 ax.annotate('',xy=point+2.2*np.array([np.sin(th),np.cos(th)]),xytext=point,arrowprops={'arrowstyle':'->','color':'#287baf','lw':1.7})
 ax.plot([point[0],point[0]+2.2*np.sin(th+al)],[0,2.2*np.cos(th+al)],color='#b44b36',ls='--',lw=1.4)
ax.text(0,-1.16,'Equal cable paths to correlator',ha='center',fontsize=9)
ax.scatter([0],[-1.08],marker='s',s=55,c='#444444');ax.text(0,-1.53,r'Compensate $b\sin\theta/c$; residual $\simeq b\alpha\cos\theta/c$',ha='center',fontsize=9)
ax.plot([A[0],A[0]],[0,2.3],ls=':',color='.6')
t=np.linspace(0,th,100);ax.plot(A[0]+.7*np.sin(t),.7*np.cos(t),color='#287baf');ax.text(A[0]+.13,.83,r'$\theta$',color='#287baf')
t=np.linspace(th,th+al,100);ax.plot(A[0]+1.05*np.sin(t),1.05*np.cos(t),color='#b44b36');ax.text(A[0]+.57,1.03,r'$\alpha$',color='#b44b36')
ax.annotate('',xy=(1.7,.12),xytext=(-1.7,.12),arrowprops={'arrowstyle':'<->','color':'.35'});ax.text(0,.21,r'East–west separation $b$',ha='center',fontsize=9)
ax.text(.1,2.18,'Blue: phase centre; dashed: offset source',fontsize=8,ha='center')
ax.set(xlim=(-2.25,3.2),ylim=(-1.75,2.5),title='Projected delay geometry (offset exaggerated)');ax.set_aspect('equal');ax.set_axis_off()
w=np.linspace(0,3.4,800);axs[1].plot(w,np.sinc(w),color='#287baf',lw=2);axs[1].axhline(0,color='.5',lw=.7);axs[1].scatter([1,2,3],[0,0,0],c='#b44b36',s=20)
axs[1].set(xlabel=r'$b\Delta\alpha\cos\theta/\lambda$',ylabel=r'$V/V(0)$',title='Uniform-source visibility');axs[1].grid(alpha=.18)
fig.savefig('paper-1-interferometer-geometry.png',dpi=165)
