"""Three real quadratic surfaces, including the symmetric part of a printed matrix."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig=plt.figure(figsize=(12.5,4.8));fig.subplots_adjust(left=.01,right=.96,bottom=.04,top=.83,wspace=.2);center=np.array([-1.,0.,0.]);u=np.linspace(0,2*np.pi,38);v=np.linspace(0,np.pi,26);U,V=np.meshgrid(u,v);sphere=np.stack((np.sin(V)*np.cos(U),np.sin(V)*np.sin(U),np.cos(V)),axis=-1)
matrices=[np.array([[2.,0.,1.],[0.,1.,0.],[1.,0.,2.]]),np.array([[2.,0.,1.],[0.,-1.,0.],[1.,0.,2.]]),np.array([[2.,0.,1.],[0.,1.,.5],[1.,.5,2.]])]
for i,S in enumerate(matrices):
 ax=fig.add_subplot(1,3,i+1,projection='3d');vals,vec=np.linalg.eigh(S)
 if i==1:
  phi,Y=np.meshgrid(np.linspace(0,2*np.pi,38),np.linspace(-2.5,2.5,25));coords=np.stack((np.sqrt(3+Y*Y)*np.cos(phi)/np.sqrt(3),Y,np.sqrt(3+Y*Y)*np.sin(phi)),axis=-1);basis=np.column_stack((np.array([1,0,1])/np.sqrt(2),np.array([0,1,0]),np.array([1,0,-1])/np.sqrt(2)));pts=coords@basis.T+center
  title="A′: one-sheet hyperboloid\ndistance 1; y unbounded"
 else:
  pts=(sphere*np.sqrt(3/vals))@vec.T+center;title='A: ellipsoid\ndistance 1; max y = √3'if i==0 else 'Symmetric part of A″\ndistance ≈ 0.990; max y = √(18/5)'
 ax.plot_wireframe(pts[:,:,0],pts[:,:,1],pts[:,:,2],rstride=3,cstride=3,color='#3080ac',alpha=.55,lw=.65)
 nearest=center+np.sqrt(3/vals[-1])*vec[:,-1];ax.plot(*np.stack((center,nearest)).T,color='#bd4b28',lw=2.4);ax.scatter(*center,color='black',s=18)
 ax.set(title=title,xlabel='x',ylabel='y',zlabel='z');ax.view_init(elev=20,azim=-56);ax.set_box_aspect((1,1,1));ax.tick_params(labelsize=8)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=140,facecolor='white')
