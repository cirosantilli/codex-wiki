from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})

from matplotlib.patches import Polygon,Circle
fig,ax=plt.subplots(1,3,figsize=(11.2,3.4))
a=ax[0]
a.add_patch(Polygon([[.2,.2],[.72,.2],[.72,.72],[.2,.72]],closed=True,fill=False,lw=1.5))
a.plot([.2,.38,.9,.72],[.72,.9,.9,.72],color='black');a.plot([.72,.9,.9],[.2,.38,.9],color='black')
for start,end,label in [((.46,.2),(.46,.02),r'$\tau_1$'),((.72,.46),(.98,.46),r'$\tau_2$'),((.38,.81),(.2,.99),r'$\tau_3$')]:
 a.annotate('',xy=end,xytext=start,arrowprops={'arrowstyle':'->','color':'tab:blue','lw':2});a.text(*end,label,fontsize=11)
a.text(.02,-.17,r'$e_i=\Delta\ell_i/\ell_i$; tension is positive',fontsize=9)
a.set(title='Normal stresses and strains',xlim=(-.07,1.12),ylim=(-.25,1.13),aspect='equal');a.axis('off')
a=ax[1];a.add_patch(Circle((0,0),1,fill=False,lw=1.5))
for ang in np.linspace(0,2*np.pi,9)[:-1]:
 xy=.73*np.array([np.cos(ang),np.sin(ang)]);d=.23*np.array([-np.sin(ang),np.cos(ang)])
 a.arrow(*xy,*d,width=.012,head_width=.08,color='tab:orange',length_includes_head=True)
a.plot([0,.73],[0,0],':',color='gray');a.text(.35,.05,r'$r$');a.text(-1,-1.38,r'Shear strain $r\phi/h$; traction $Gr\phi/h$',fontsize=9)
a.set(title='Twist: tangential displacement',xlim=(-1.2,1.2),ylim=(-1.6,1.2),aspect='equal');a.axis('off')
a=ax[2];a.plot([-1,1],[-.3,-.3],color='black',lw=3);a.plot([-1,1],[.1,.55],color='tab:blue',lw=3)
for x in np.linspace(-1,1,7):a.plot([x,x],[-.3,.325+.225*x],color='gray',lw=.8)
a.axvline(0,ls=':',color='gray');a.annotate('',xy=(1,.6),xytext=(1,.325),arrowprops={'arrowstyle':'<->'});a.text(.25,.72,r'$\Delta z=y\theta$');a.text(-1,-.64,r'Normal strain $y\theta/h$; traction $My\theta/h$',fontsize=9)
a.text(-.9,-.13,'Bonded thin layer',fontsize=8)
a.set(title='Tilt: differential extension',xlim=(-1.25,1.25),ylim=(-.95,1.15),aspect='equal');a.axis('off')

fig.tight_layout()
fig.savefig(Path(__file__).stem+'.png',dpi=140,facecolor='white',bbox_inches='tight')
plt.close(fig)
