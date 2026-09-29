"""Draw the three labeled scalar four-point bubbles.

Tested with Python 3.14, numpy 2.3.5 and matplotlib 3.10.7.
Writes paper-47-bubble-channels.png in the caller's working directory.
The caller's MPLCONFIGDIR, when supplied, is preserved.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig,axes=plt.subplots(1,3,figsize=(10.8,3.25),dpi=130,facecolor='white')
channels=[('s',[1,2,3,4],r'$q=p_1+p_2$'),('t',[1,3,2,4],r'$q=p_1+p_3$'),('u',[1,4,2,3],r'$q=p_1+p_4$')]
for ax,(name,labels,q) in zip(axes,channels):
    theta=np.linspace(0,np.pi,200)
    xx=.55*np.cos(theta)
    for sign in [1,-1]: ax.plot(xx,sign*.35*np.sin(theta),color='#17466f',lw=2)
    for vx,ex,j in [(-.55,-1.28,0),(.55,1.28,2)]:
        for dy,index in [(.61,j),(-.61,j+1)]:
            ax.plot([vx,ex],[0,dy],color='#17466f',lw=2)
            ax.text(ex,dy+(0.11 if dy>0 else -.14),f'$p_{labels[index]}$',ha='center',va='center',fontsize=13)
        ax.scatter([vx],[0],s=38,c='#17466f',zorder=4)
    ax.text(0,.53,r'$\ell$',ha='center',fontsize=12)
    ax.text(0,-.59,r'$\ell+q$',ha='center',fontsize=12)
    ax.text(0,-1.04,q,ha='center',fontsize=12)
    ax.set_title(f'{name} channel',fontsize=14,pad=5)
    ax.set_xlim(-1.5,1.5);ax.set_ylim(-1.2,1.05);ax.set_aspect('equal');ax.axis('off');ax.set_facecolor('white')
fig.suptitle('One-loop scalar four-point vertices: all external momenta incoming',fontsize=14,y=.98)
fig.subplots_adjust(left=.015,right=.985,bottom=.03,top=.83,wspace=.05)
fig.savefig('paper-47-bubble-channels.png',facecolor='white',transparent=False)
plt.close(fig)
