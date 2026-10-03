"""Original schematic density envelopes, not simulated Skyrme isosurfaces.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7 (Debian build).
Compatible with the unchanged root pyproject.toml pins. When installed beside
paper-308.bigb as paper-308-skyrmion-sketches.py, writes the matching PNG to CWD.
"""
import os
import struct
from pathlib import Path
os.environ.setdefault('MPLBACKEND','Agg')
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

BLUE='#497cb1';EDGE='#243f64'
def shell_faces(ax,vertices,faces,inner):
 """Draw opaque face bands around central apertures of regular polyhedra."""
 bands=[]
 for indices in faces:
  outer=vertices[np.array(indices)];center=outer.mean(axis=0);hole=center+inner*(outer-center)
  for i in range(len(indices)):
   j=(i+1)%len(indices);bands.append([outer[i],outer[j],hole[j],hole[i]])
  ax.plot(*np.vstack([hole,hole[0]]).T,color=EDGE,lw=.8)
 ax.add_collection3d(Poly3DCollection(bands,facecolors=BLUE,edgecolors=EDGE,linewidths=.6,alpha=1))
 for i,j in sorted({tuple(sorted((f[k],f[(k+1)%len(f)]))) for f in faces for k in range(len(f))}):
  ax.plot(*vertices[[i,j]].T,color=EDGE,lw=1)

def main():
 plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'figure.facecolor':'white','savefig.facecolor':'white','savefig.transparent':False})
 # The raster backend truncates binary floating-point sizes; this tiny surplus gives exactly 460 pixels.
 fig=plt.figure(figsize=(14,4.600001),dpi=100,facecolor='white')
 fig.subplots_adjust(left=.005,right=.995,bottom=.12,top=.85,wspace=.03)
 axes=[fig.add_subplot(1,4,i+1,projection='3d',facecolor='white') for i in range(4)]
 for ax in axes:
  ax.set_axis_off();ax.set_box_aspect((1,1,1));ax.set_xlim(-1.3,1.3);ax.set_ylim(-1.3,1.3);ax.set_zlim(-1.3,1.3);ax.view_init(elev=24,azim=35);ax.set_proj_type('ortho')
 theta=np.linspace(0,np.pi,55);az=np.linspace(0,2*np.pi,90);t,p=np.meshgrid(theta,az)
 axes[0].plot_surface(np.sin(t)*np.cos(p),np.sin(t)*np.sin(p),np.cos(t),color=BLUE,linewidth=0,antialiased=True,shade=True,alpha=1)
 # The toroidal aperture is geometric, not an artificial transparent face.
 u,v=np.meshgrid(np.linspace(0,2*np.pi,100),np.linspace(0,2*np.pi,40));R,r=.82,.29
 axes[1].plot_surface((R+r*np.cos(v))*np.cos(u),(R+r*np.cos(v))*np.sin(u),r*np.sin(v),color=BLUE,linewidth=0,antialiased=True,shade=True,alpha=1)
 verts=np.array([[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]],float)*.74
 shell_faces(axes[2],verts,[(0,1,2),(0,3,1),(0,2,3),(1,3,2)],.48)
 cube=np.array([[-1,-1,-1],[-1,-1,1],[-1,1,-1],[-1,1,1],[1,-1,-1],[1,-1,1],[1,1,-1],[1,1,1]],float)*.78
 shell_faces(axes[3],cube,[(0,1,3,2),(4,6,7,5),(0,4,5,1),(2,3,7,6),(0,2,6,4),(1,5,7,3)],.62)
 names=['Spherical hedgehog','Toroidal shell','Tetrahedral shell','Cubic shell']
 groups=[r'Spherical: $O(3)$',r'Axial: $D_{\infty h}$',r'Tetrahedral: $T_d$',r'Cubic: $O_h$']
 for i,ax in enumerate(axes):
  ax.set_title(f'$B={i+1}$\n'+names[i],pad=8,fontsize=12)
  ax.text2D(.5,-.03,groups[i],transform=ax.transAxes,ha='center',va='top',fontsize=11)
 fig.text(.5,.025,'Schematic baryon-density shapes and their spatial symmetries; field symmetries also involve isorotation.',ha='center',fontsize=10,color='#333333')
 output=Path.cwd()/(Path(__file__).stem+'.png')
 fig.savefig(output,dpi=100,facecolor='white',transparent=False)
 plt.close(fig)
 assert struct.unpack('>II',output.read_bytes()[16:24])==(1400,460)
 print(output)
if __name__=='__main__':main()
