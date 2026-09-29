"""A2 lattice plot; Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.

Run in the desired output directory. Make runs this generator in mirrored _media.
"""
import os
from pathlib import Path
os.environ.setdefault('MPLCONFIGDIR',str(Path.cwd()/'.matplotlib-cache'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def main():
 w1=np.array([.5,np.sqrt(3)/6]);w2=np.array([0,np.sqrt(3)/3])
 fig,ax=plt.subplots(figsize=(8.4,6.4),dpi=100,facecolor='white');ax.set_facecolor('white');pts={}
 for m in range(-8,9):
  for n in range(-8,9):
   v=m*w1+n*w2
   if -2.2<=v[0]<=2.2 and -1.65<=v[1]<=1.65:pts[m,n]=v
 for (m,n),v in pts.items():
  for d in [(1,0),(0,1),(-1,1)]:
   u=pts.get((m+d[0],n+d[1]))
   if u is not None:ax.plot([v[0],u[0]],[v[1],u[1]],color='#dce1e6',lw=.7,zorder=0)
 arr=np.array(list(pts.values()));roots=np.array([v for (m,n),v in pts.items() if (m-n)%3==0])
 ax.scatter(arr[:,0],arr[:,1],s=16,color='#999fa7',label='Weight lattice P',zorder=1)
 ax.scatter(roots[:,0],roots[:,1],s=29,color='#235d99',label='Root lattice Q (index 3)',zorder=2)
 arrows=[(w1,r'$\omega_1$','#c43d42',(.10,-.12)),(w2,r'$\omega_2$','#9a378b',(.10,.06)),(2*w1-w2,r'$\alpha_1$','#1558a5',(.07,.09)),(-w1+2*w2,r'$\alpha_2$','#158368',(-.30,.07))]
 for v,label,color,shift in arrows:
  ax.annotate('',xy=v,xytext=(0,0),arrowprops=dict(arrowstyle='-|>',lw=2.3,color=color),zorder=4)
  ax.text(*(v+shift),label,color=color,fontsize=15,zorder=5)
 ax.scatter([0],[0],s=45,color='black',zorder=6);ax.text(-.13,-.16,'0',fontsize=12)
 ax.set(xlim=(-2.25,2.25),ylim=(-1.7,1.85),aspect='equal');ax.set_xlabel('Horizontal coordinate');ax.set_ylabel('Vertical coordinate')
 ax.set_title(r'$A_2$: fundamental weights and simple roots',fontsize=15,pad=15)
 ax.legend(loc='lower right',framealpha=1,facecolor='white',fontsize=10)
 fig.subplots_adjust(left=.11,right=.96,bottom=.11,top=.88)
 fig.savefig('paper-302-a2-weight-lattice.png',dpi=100,facecolor='white',transparent=False);plt.close(fig)
if __name__=='__main__':main()
