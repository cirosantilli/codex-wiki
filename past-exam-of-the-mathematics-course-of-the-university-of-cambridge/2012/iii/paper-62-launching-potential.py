"""Original local magnetocentrifugal-launching geometry and potential plot.

Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Writes only the PNG basename in caller CWD; respects caller MPLCONFIGDIR.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Arc

fig,(geometry,profile)=plt.subplots(1,2,figsize=(10,4.4),dpi=100,facecolor='white',gridspec_kw={'width_ratios':[1,1.55]})
colors=['#2373aa','#d88917','#9d334c']
angles=[20,30,40]
s=np.linspace(0,.45,301)
geometry.axhline(0,color='#555555',linewidth=2)
geometry.plot([0,0],[0,.45],'--',color='#666666',linewidth=1)
for deg,color in zip(angles,colors):
    a=np.radians(deg)
    geometry.plot(s*np.sin(a),s*np.cos(a),color=color,linewidth=2,label=str(deg)+'°')
    geometry.text(s[-1]*np.sin(a)+.012,s[-1]*np.cos(a),str(deg)+'°',color=color,fontsize=11)
geometry.scatter([0],[0],color='black',s=24,zorder=5)
geometry.add_patch(Arc((0,0),.22,.22,theta1=50,theta2=90,color='#333333'))
geometry.text(.048,.105,r'$\alpha$',fontsize=12)
geometry.text(-.025,-.037,r'$R_0$',ha='center',fontsize=12)
geometry.set_xlim(-.035,.39)
geometry.set_ylim(-.045,.48)
geometry.set_aspect('equal')
geometry.set_xlabel(r'$(R-R_0)/R_0$')
geometry.set_ylabel(r'$z/R_0$')
geometry.set_title('Straight lines corotating with the footpoint',fontsize=11)
x=np.linspace(0,.4,501)
for deg,color in zip(angles,colors):
    a=np.sin(np.radians(deg))
    potential=-1/np.sqrt(1+2*a*x+x*x)-.5*(1+a*x)**2+1.5
    profile.plot(x,potential,color=color,linewidth=2,label=str(deg)+'°')
profile.axhline(0,color='#666666',linewidth=.8)
profile.set_xlabel(r'Distance along the field line, $s/R_0$')
profile.set_ylabel(r'$[\Phi_{\rm eff}(s)-\Phi_{\rm eff}(0)]/(GM/R_0)$')
profile.set_title('Local effective potential',fontsize=12)
profile.legend(title='Inclination to vertical',frameon=False,loc='lower left',fontsize=10)
profile.grid(alpha=.2)
profile.set_ylim(-.07,.037)
profile.text(.018,.034,'30° is marginal at quadratic order;\nits outward cubic term is negative.',fontsize=10,va='top')
fig.subplots_adjust(left=.075,right=.98,bottom=.16,top=.86,wspace=.35)
fig.savefig('paper-62-launching-potential.png',dpi=100,facecolor='white',transparent=False)
plt.close(fig)
