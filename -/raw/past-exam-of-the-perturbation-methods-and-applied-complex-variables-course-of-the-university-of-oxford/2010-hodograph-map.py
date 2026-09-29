"""Original diagram; Python 3.14, NumPy/Matplotlib in root pyproject.toml.
Writes PNG to the current working directory.
"""
import numpy as np
import matplotlib.pyplot as plt
fig,axs=plt.subplots(1,2,figsize=(9,3.8),layout='constrained',facecolor='white')
blue,orange,green='#2875a9','#c45c21','#29845c'
a=axs[0];a.axhspan(0,1,color='#edf3f6')
a.plot([-3,0],[0,0],color=blue,lw=3);a.plot([0,3],[0,0],color=orange,lw=3);a.plot([-3,3],[1,1],color=green,lw=3)
a.scatter([0],[0],color='black',s=25,zorder=3);a.text(.08,.08,'B: w = 0')
a.text(-1.8,.08,'AB',color=blue);a.text(1.4,.08,'BC',color=orange)
a.text(-.8,.85,"free surface A′C′",color=green)
a.annotate('',xy=(2.5,.5),xytext=(-2.5,.5),arrowprops={'arrowstyle':'->','color':'#555555'})
a.text(-2.7,.56,'upstream');a.text(1.25,.56,'downstream')
a.set(xlim=(-3,3),ylim=(-.2,1.2),xlabel='Re w = φ',ylabel='Im w = ψ',title='Potential plane: strip',yticks=[0,1])
a=axs[1];theta=np.linspace(-np.pi/2,0,200)
a.fill(np.r_[0,np.cos(theta),0],np.r_[0,np.sin(theta),0],color='#edf3f6')
a.plot([0,1],[0,0],color=blue,lw=3);a.plot([0,0],[0,-1],color=orange,lw=3);a.plot(np.cos(theta),np.sin(theta),color=green,lw=3)
a.text(.04,.05,'B: q = 0');a.text(.88,.07,'A: q = 1');a.text(.04,-1.09,'C: q = −i');a.text(.58,-.65,"A′C′",color=green)
a.set(xlim=(-.15,1.2),ylim=(-1.2,.2),xlabel='Re q = u',ylabel='Im q = −v',title='Hodograph plane: quarter disk')
a.set_aspect('equal')
for a in axs:a.spines[['top','right']].set_visible(False);a.set_facecolor('white')
fig.savefig('2010-hodograph-map.png',dpi=155,facecolor='white')
