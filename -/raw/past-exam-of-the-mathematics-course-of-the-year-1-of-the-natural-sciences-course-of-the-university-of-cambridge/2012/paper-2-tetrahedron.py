"""Original face-normal diagram. Python 3.14; matplotlib 3.10.7, numpy 2.3.5.

Write the white PNG to cwd, normally the mirrored _media paper directory.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

O=np.array([0.,0.,0.]);P=np.array([2.,1.,0.]);Q=np.array([1.,2.,0.]);R=np.array([0.,1.,1.])
points=[O,P,Q,R]
fig=plt.figure(figsize=(6.4,5.2),layout='constrained',facecolor='white')
ax=fig.add_subplot(projection='3d')
faces=[[O,P,Q],[O,P,R],[O,R,Q],[P,Q,R]]
ax.add_collection3d(Poly3DCollection(faces,facecolors=['#dfedf3','#c8dfe8','#dae9ef','#f4b992'],alpha=.45,edgecolors='#415b68',linewidths=1.1))
for point,label,offset in [(O,'O',[-.15,-.16,-.06]),(P,'P',[.1,0,-.07]),(Q,'Q',[0,.08,-.06]),(R,'R',[0,.08,.06])]:
    ax.scatter(*point,color='#333333',s=24,depthshade=False)
    ax.text(*(point+offset),f'${label}$',fontsize=13)
C=(P+Q+R)/3;normal=np.array([1,1,2])/np.sqrt(6)
ax.quiver(*C,*(.8*normal),color='#c65c19',lw=2,arrow_length_ratio=.2)
ax.text(*(C+.9*normal),r'$\hat{\mathbf{n}}=(1,1,2)/\sqrt{6}$',color='#a64b13',fontsize=10)
ax.text(.9,.8,.02,r'$z=0$',fontsize=10,color='#52636b')
ax.set(xlim=(-.2,2.5),ylim=(-.3,2.6),zlim=(-.15,1.5))
ax.set_xlabel('$x$');ax.set_ylabel('$y$');ax.set_zlabel('$z$')
ax.view_init(elev=24,azim=-49);ax.set_box_aspect((1,1,.7))
ax.set_title('Tetrahedron and outward normal of face PQR')
fig.savefig(Path(__file__).with_suffix('.png').name,dpi=160,facecolor='white')
