"""Higgs-gauge vertices. Tested Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Emits an opaque PNG basename to CWD and respects caller MPLCONFIGDIR.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def wave(ax, a, b):
    a,b=np.array(a),np.array(b)
    d=b-a;normal=np.array([-d[1],d[0]])/np.linalg.norm(d)
    t=np.linspace(0,1,401)
    pts=a[:,None]+d[:,None]*t+normal[:,None]*.027*np.sin(14*np.pi*t)
    ax.plot(*pts,color='#1565c0',lw=1.8)

def scalar(ax,a,b,label):
    ax.plot([a[0],b[0]],[a[1],b[1]],ls='--',color='#333333',lw=1.7)
    ax.text(b[0],b[1]+.025,label,ha='center',va='bottom',fontsize=13)

fig,axes=plt.subplots(2,2,figsize=(9,6),layout='constrained')
for ax,kind,two in zip(axes.flat,('W','Z','W','Z'),(False,False,True,True)):
    v=(.5,.53)
    for point,label in [((.17,.17),r'$W^+_\mu$' if kind=='W' else r'$Z_\mu$'),
                        ((.83,.17),r'$W^-_\nu$' if kind=='W' else r'$Z_\nu$')]:
        wave(ax,v,point);ax.text(point[0],point[1]-.07,label,ha='center',fontsize=13)
    for pt in ([ (.25,.9),(.75,.9)] if two else [(.5,.94)]):scalar(ax,v,pt,r'$H$')
    ax.plot(*v,'o',ms=4,color='black')
    den='v^2' if two else 'v'
    ax.text(.5,-.02,rf'$2i M_{kind}^2 g_{{\mu\nu}}/{den}$',ha='center',fontsize=15)
    ax.set(xlim=(0,1),ylim=(-.13,1.08));ax.axis('off')
fig.savefig('paper-54-higgs-vertices.png',dpi=140,facecolor='white',transparent=False)
plt.close(fig)
