"""Original polarization analyzers in three Pauli bases; Python 3.14."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
fig,axes=plt.subplots(3,1,figsize=(9.0,5.5),facecolor='white')
fig.subplots_adjust(left=.04,right=.96,bottom=.06,top=.90,hspace=.36)
for a,basis in zip(axes,['Z','X','Y']):
    a.set(xlim=(0,1),ylim=(0,1));a.axis('off');a.text(.01,.5,basis+' basis',fontsize=13,va='center')
    a.annotate('',xy=(.97,.5),xytext=(.17,.5),arrowprops={'arrowstyle':'->','color':'#126782','lw':1.7})
    if basis=='Y':
        a.add_patch(Rectangle((.27,.28),.17,.44,facecolor='white',edgecolor='#126782',zorder=3));a.text(.355,.5,'QWP\nQ = diag(1, −i)',ha='center',va='center',fontsize=10,zorder=4)
    if basis in ['X','Y']:
        a.add_patch(Rectangle((.49,.28),.16,.44,facecolor='white',edgecolor='#126782',zorder=3));a.text(.57,.5,'HWP\n22.5°',ha='center',va='center',fontsize=11,zorder=4)
    a.add_patch(Rectangle((.73,.34),.08,.32,facecolor='white',edgecolor='#25394c',zorder=3));a.text(.77,.5,'PBS',ha='center',va='center',fontsize=10,zorder=4)
    a.annotate('',xy=(.77,.95),xytext=(.77,.66),arrowprops={'arrowstyle':'->','color':'#a34100','lw':1.5})
    labels={'Z':('H','V'),'X':('+X','−X'),'Y':('+Y = R','−Y = L')}[basis]
    a.text(.97,.68,'D+: '+labels[0],ha='right',fontsize=11);a.text(.81,.89,'D−: '+labels[1],ha='left',fontsize=11)
fig.suptitle('Wave plates rotate the chosen basis into H/V before detection',fontsize=16,y=.98)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=110,facecolor='white',transparent=False,metadata={'Software':'Matplotlib'})
plt.close(fig)
