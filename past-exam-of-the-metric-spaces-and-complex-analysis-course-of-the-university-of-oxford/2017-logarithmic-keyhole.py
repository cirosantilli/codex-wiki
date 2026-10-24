"""Original keyhole solution diagram emphasizing branch values and orientation."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig,ax=plt.subplots(figsize=(7.4,6),dpi=100,facecolor='white')
epsilon=.23;delta=.055;alpha=np.arcsin(delta);beta=np.arcsin(delta/epsilon)
theta=np.linspace(alpha,2*np.pi-alpha,601)
ax.plot(np.cos(theta),np.sin(theta),color='#1264a3',lw=2)
theta=np.linspace(2*np.pi-beta,beta,401)
ax.plot(epsilon*np.cos(theta),epsilon*np.sin(theta),color='#b54827',lw=2)
x0=np.sqrt(epsilon**2-delta**2);x1=np.sqrt(1-delta**2)
ax.plot([x0,x1],[delta,delta],color='#303030',lw=1.8)
ax.plot([x1,x0],[-delta,-delta],color='#303030',lw=1.8)
ax.axhline(0,color='#aaaaaa',lw=.7,zorder=0);ax.axvline(0,color='#aaaaaa',lw=.7,zorder=0)
ax.plot([0,1.30],[0,0],'--',color='#cc7777',lw=1,zorder=0)
for radius,angle,direction,color in [(1,1.8,1,'#1264a3'),(1,4.5,1,'#1264a3'),(epsilon,np.pi,-1,'#b54827')]:
    aa=angle-direction*.09;bb=angle+direction*.09
    ax.annotate('',xy=(radius*np.cos(bb),radius*np.sin(bb)),xytext=(radius*np.cos(aa),radius*np.sin(aa)),arrowprops=dict(arrowstyle='-|>',color=color,lw=1.8,mutation_scale=13))
for yy,start,end in [(delta,.48,.72),(-delta,.72,.48)]:
    ax.annotate('',xy=(end,yy),xytext=(start,yy),arrowprops=dict(arrowstyle='-|>',color='#303030',lw=1.8,mutation_scale=13))
ax.text(.62,.18,r'$L=\log x$',ha='center',fontsize=12)
ax.text(.62,-.22,r'$L=\log x+2\pi i$',ha='center',fontsize=12)
ax.text(0,1.08,'outer arc: counterclockwise',ha='center',fontsize=10,color='#1264a3')
ax.annotate('inner arc: clockwise',xy=(-epsilon,0),xytext=(-1.16,-.40),fontsize=10,color='#b54827',arrowprops=dict(arrowstyle='->',color='#b54827'))
ax.annotate(r'radius $\varepsilon$',xy=(0,epsilon),xytext=(-.45,.38),fontsize=10,arrowprops=dict(arrowstyle='->',color='#555555'))
ax.text(.76,-1.12,r'upper + lower $=-2\pi i\int_\varepsilon^1 f(x)\,dx$',ha='center',fontsize=12)
ax.text(-.38,-1.40,r'inner integral $=O(\varepsilon|\log\varepsilon|)\to0$',ha='center',fontsize=11)
ax.set(xlim=(-1.45,1.45),ylim=(-1.60,1.25))
ax.set_aspect('equal');ax.axis('off')
ax.set_title(r'Keyhole integral of $f(z)(L(z)-i\pi)$',fontsize=15,pad=10)
fig.subplots_adjust(left=.025,right=.975,top=.90,bottom=.035)
fig.savefig(Path(__file__).with_suffix('.png').name,facecolor='white',dpi=100)
plt.close(fig)
