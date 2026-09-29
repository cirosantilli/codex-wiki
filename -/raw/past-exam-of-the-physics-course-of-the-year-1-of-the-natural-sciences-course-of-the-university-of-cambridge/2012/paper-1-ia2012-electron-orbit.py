import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
r=.1395225713;a=.5;th=np.linspace(0,2*np.pi,500)
fig,ax=plt.subplots(figsize=(6.5,5.5),layout='constrained')
ax.add_patch(Circle((0,0),a,fill=False,lw=2,color='#555'))
x=r*np.sin(th);y=r*(1-np.cos(th));ax.plot(x,y,color='#2475aa',lw=2.5)
ax.scatter([0,0],[0,r],s=[45,35],color=['black','#c94a39'],zorder=5)
ax.annotate('tube axis / entry',xy=(0,0),xytext=(-.47,-.14),arrowprops=dict(arrowstyle='->',color='#555'),fontsize=11)
ax.annotate('guiding centre',xy=(0,r),xytext=(.2,.14),arrowprops=dict(arrowstyle='->',color='#c94a39'),color='#c94a39',fontsize=11)
ax.annotate('',xy=(0,2*r),xytext=(0,0),arrowprops=dict(arrowstyle='<->',color='#468b50',lw=1.5));ax.text(-.08,r, r'$2r_L$',ha='right',color='#468b50',fontsize=12)
i=100;ax.annotate('',xy=(x[i+15],y[i+15]),xytext=(x[i],y[i]),arrowprops=dict(arrowstyle='->',color='#2475aa',lw=2))
ax.text(-.43,.38,r'$B$ towards viewer',fontsize=10);ax.text(.27,-.38,'tube wall',fontsize=10)
ax.set(xlim=(-.56,.56),ylim=(-.54,.54),aspect='equal',xlabel='Transverse x (mm)',ylabel='Transverse y (mm)',title=r'On-axis entry: $\theta=3^\circ$,  $2r_L=0.279$ mm');ax.grid(alpha=.18)
fig.savefig('paper-1-ia2012-electron-orbit.png',dpi=160,facecolor='white')
