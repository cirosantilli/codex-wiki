"""Original hole/COM and slope-coordinate diagrams. Python 3.14,
NumPy 2.3, Matplotlib 3.10. Outputs only basename PNG in the CWD.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,Arc
fig,axs=plt.subplots(1,2,figsize=(10.4,4.9),facecolor='white');R=1.;ro=.4;d=ro**3/(R*R-ro*ro)
a=axs[0];a.add_patch(Circle((0,0),R,color='#dceaf0',ec='#263849',lw=1.8));a.add_patch(Circle((ro,0),ro,color='white',ec='#b14c29',lw=1.7));a.scatter([0,ro,-d],[0,0,0],s=[18,22,18],c=['#263849','#b14c29','#236b8e'],zorder=5)
a.text(0,.10,'C',ha='center');a.text(ro,.10,'H',ha='center',color='#b14c29');a.annotate('G: remaining centre of mass',(-d,0),xytext=(-1.12,-.55),arrowprops={'arrowstyle':'->'},fontsize=9,color='#236b8e')
a.annotate('',xy=(ro,-.15),xytext=(0,-.15),arrowprops={'arrowstyle':'<->','color':'#b14c29'});a.text(.12,-.29,r'$r_o$',ha='center',color='#b14c29');a.plot([0,-.7],[0,.714],color='#263849',ls=':');a.text(-.47,.43,'R');a.set_title('Fixed axle at H; centre of mass at G')
a=axs[1];alpha=.27;theta=.6;C=np.array([0.,.3]);normal=np.array([np.sin(alpha),np.cos(alpha)]);tangent=np.array([np.cos(alpha),-np.sin(alpha)]);contact=C-normal
line=np.array([contact-1.6*tangent,contact+1.6*tangent]);a.plot(line[:,0],line[:,1],color='#263849',lw=2)
a.add_patch(Circle(C,R,color='#dceaf0',ec='#263849',lw=1.8));H=C+ro*np.array([np.sin(theta),np.cos(theta)]);a.add_patch(Circle(H,ro,color='white',ec='#b14c29',lw=1.7));a.scatter(*C,s=18,c='#263849');a.scatter(*H,s=18,c='#b14c29');a.text(*[C[0]-.15,C[1]-.1],'C');a.text(*[H[0]+.11,H[1]+.09],'H',color='#b14c29')
a.plot([C[0],C[0]],[C[1],C[1]+1.18],ls=':',color='gray');a.add_patch(Arc(C,.9,.9,theta1=90-np.degrees(theta),theta2=90,color='#b14c29'));a.text(.10,.90,r'$\theta$',color='#b14c29')
a.annotate('Increasing s = Rθ',xy=contact+1.3*tangent+.16*normal,xytext=contact+.2*tangent+.16*normal,arrowprops={'arrowstyle':'->'},fontsize=9)
a.text(-1.23,-1.28,r'$y_H=y_C+r_o\cos(s/R)$',fontsize=11);a.set_title('Rolling coordinate measured from vertical')
for a in axs:a.set_aspect('equal');a.set(xlim=(-1.35,1.55),ylim=(-1.4,1.6));a.axis('off')
fig.tight_layout();fig.savefig(Path('2014-perforated-wheel-geometry.png'),dpi=140,facecolor='white')
