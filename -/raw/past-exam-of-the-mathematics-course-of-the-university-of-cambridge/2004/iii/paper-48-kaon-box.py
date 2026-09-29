"""Original charged weak box diagram; Python 3.14, root NumPy/Matplotlib deps.

Emits paper-48-kaon-box.png to caller CWD and honors supplied MPLCONFIGDIR.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig,ax=plt.subplots(figsize=(9,4.5),facecolor='white')
ax.set_facecolor('white')
TL=np.array([0.,1.]);TR=np.array([3.,1.]);BL=np.array([0.,-1.]);BR=np.array([3.,-1.])
def fermion(a,b):
    a=np.asarray(a);b=np.asarray(b)
    ax.plot([a[0],b[0]],[a[1],b[1]],color='#172a3a',lw=1.9)
    middle=(a+b)/2;unit=(b-a)/np.linalg.norm(b-a)
    ax.annotate('',xy=middle+.2*unit,xytext=middle-.2*unit,arrowprops={'arrowstyle':'-|>','color':'#172a3a','lw':1.6})
fermion((-1.6,1),TL);fermion(TL,TR);fermion(TR,(4.6,1))
fermion(BL,(-1.6,-1));fermion(BR,BL);fermion((4.6,-1),BR)
def wavy(a,b):
    a=np.asarray(a);b=np.asarray(b);t=np.linspace(0,1,220)
    u=b-a;perp=np.array([-u[1],u[0]])/np.linalg.norm(u)
    points=a+t[:,None]*u+.09*np.sin(14*np.pi*t)[:,None]*perp
    ax.plot(points[:,0],points[:,1],color='#1d6ba0',lw=1.7)
wavy(BL,TL);wavy(TR,BR)
for p in [TL,TR,BL,BR]:ax.scatter(*p,s=22,color='#172a3a',zorder=3)
for text,x,y in [(r'$d$',-1.7,1),(r'$s$',4.75,1),(r'$\bar s$',-1.7,-1),(r'$\bar d$',4.75,-1),(r'$u_i$',1.5,1.25),(r'$u_j$',1.5,-1.38)]:
    ax.text(x,y,text,fontsize=17,ha='center',va='center')
ax.text(-.48,0,r'$W^+$',fontsize=16,color='#1d6ba0',ha='center')
ax.text(3.48,0,r'$W^+$',fontsize=16,color='#1d6ba0',ha='center')
ax.annotate('',xy=(-.22,.42),xytext=(-.22,-.42),arrowprops={'arrowstyle':'->','color':'#1d6ba0'})
ax.annotate('',xy=(3.22,-.42),xytext=(3.22,.42),arrowprops={'arrowstyle':'->','color':'#1d6ba0'})
ax.text(1.5,-1.92,r'Internal flavors: $i,j\in\{u,c,t\}$; black arrows denote fermion flow',ha='center',fontsize=11,color='#334155')
ax.text(1.5,-2.23,r'$K^0\ (d\bar s)\ \longrightarrow\ \bar K^0\ (s\bar d)$',ha='center',fontsize=14)
ax.set_title('Charged weak box contribution to neutral-kaon mixing',fontsize=14,pad=13)
ax.set_xlim(-2.1,5.1);ax.set_ylim(-2.45,1.8);ax.axis('off')
fig.tight_layout()
fig.savefig('paper-48-kaon-box.png',dpi=130,facecolor='white',transparent=False)
plt.close(fig)
