"""Original cut-and-glue illustration; Python 3.14, NumPy 2.3, Matplotlib 3.10."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
fig, axes = plt.subplots(2,2,figsize=(11,7.5), facecolor='white')
red='#b92d32'; blue='#176c9f'

def side(ax, a, b, text, color='#333333', label_offset=.16):
    a,b=np.array(a),np.array(b)
    d=b-a; n=np.array([d[1],-d[0]])/np.linalg.norm(d)
    ax.plot([a[0],b[0]],[a[1],b[1]],color=color,lw=2)
    mid=(a+b)/2
    ax.annotate('',xy=mid+.11*d,xytext=mid-.11*d,arrowprops=dict(arrowstyle='->',color=color,lw=1.7))
    p=mid+label_offset*n
    ax.text(*p,text,ha='center',va='center',fontsize=13,color=color)
for row in range(2):
    ax=axes[row,0]
    v=np.array([[0.,0.],[2.,0.],[2.,2.],[0.,2.]])
    ax.fill(v[:,0],v[:,1],color='#f1f7fb')
    for i,label in enumerate(['$x$','$A$','$x$','$B$']):
        side(ax,v[i],v[(i+1)%4],label,blue if i%2==0 else '#333333',.24)
        p=v[i]+.22*(v[i]-[1,1]);ax.text(*p,f'$v_{i}$',ha='center',va='center',fontsize=10)
    a,b=(v[0],v[2]) if row==0 else (v[1],v[3])
    ax.annotate('',xy=b,xytext=a,arrowprops=dict(arrowstyle='->',color=red,lw=2,ls='--'))
    ax.text(.92,1.18,'$d$',color=red,fontsize=14)
    ax.set(xlim=(-.65,2.65),ylim=(-.65,2.65),aspect='equal')
    ax.axis('off')
    ax.set_title('Cut $v_0v_2$' if row==0 else 'Cut $v_1v_3$',fontsize=13)
    ax=axes[row,1]
    p=np.array([[3.,0.],[2.,1.35],[0.,0.],[2.,-1.35]])
    ax.fill(p[:,0],p[:,1],color='#f1f7fb')
    labels=['$A$','$d^{-1}$','$d^{-1}$','$B^{-1}$'] if row==0 else ['$d$','$B$','$A^{-1}$','$d$']
    for i,label in enumerate(labels):side(ax,p[i],p[(i+1)%4],label,red if 'd' in label else '#333333',.19)
    ax.annotate('',xy=(3,0),xytext=(0,0),arrowprops=dict(arrowstyle='->',color=blue,lw=1.6,ls='--'))
    ax.text(1.5,.1,'old $x$ seam',ha='center',fontsize=10,color=blue)
    ax.text(1.5,-1.95,r'Reverse and cycle: $ddA^{-1}B$' if row==0 else r'Cycle: $A^{-1}ddB$',ha='center',fontsize=13)
    ax.set(xlim=(-.55,3.55),ylim=(-2.2,1.85),aspect='equal')
    ax.axis('off');ax.set_title('Glue the two old $x$ sides',fontsize=13)
fig.suptitle('Two cuts that move a repeated edge pair together',fontsize=16)
fig.tight_layout(rect=(0,0,1,.95))
fig.savefig(Path.cwd()/'2014-crosscap-slide.png',dpi=170,facecolor='white')
