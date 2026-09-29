from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11})

fig=plt.figure(figsize=(11,8),layout='constrained',facecolor='white');gs=fig.add_gridspec(3,3,height_ratios=[1,1,.9])
ax=fig.add_subplot(gs[0,:]);t=np.array([-.4,0,1.7,2.5,4.2,4.6]);F=[1,1,.55,.55,1,1];ax.plot(t,F,color='#126782',lw=2);ax.set(xlabel='Time after first contact (hours)',ylabel='Relative flux (schematic)',ylim=(.4,1.1),title='Central eclipse: 1.7 h ingress, 0.8 h totality, 1.7 h egress')
for x in [0,1.7,2.5,4.2]:ax.axvline(x,color='gray',ls=':',lw=1)
ax=fig.add_subplot(gs[1,:]);ax.set(xlim=(-1,11),ylim=(-1.1,1.2));ax.set_aspect('equal');ax.axis('off')
from matplotlib.patches import Circle
for center,sep,lab in [(0,1.68,'First contact'),(3,.32,'Totality begins'),(6,-.32,'Totality ends'),(9,-1.68,'Last contact')]:
 ax.add_patch(Circle((center,0),.7,color='#e9b949'));ax.add_patch(Circle((center+sep*.7,0),.476,color='#126782',alpha=.8));ax.text(center,-.95,lab,ha='center',fontsize=10)
lon=np.linspace(-np.pi,np.pi,181);lat=np.linspace(-np.pi/2,np.pi/2,91);X,Y=np.meshgrid(lon,lat)
fields=[np.exp(-(Y/.15)**2)*(1+.2*np.cos(4*X)),np.cos(Y)*np.cos(X),np.sin(8*X+3*Y)*np.cos(7*Y)+.4*np.sin(17*X-2*Y)]
for j,(field,title) in enumerate(zip(fields,['Galactic dust band','Kinematic dipole','Residual CMB patches'])):
 ax=fig.add_subplot(gs[2,j],projection='mollweide');ax.pcolormesh(X,Y,field,cmap='coolwarm',shading='auto');ax.set_xticklabels([]);ax.set_yticklabels([]);ax.grid(alpha=.3);ax.set_title(title,fontsize=11)
fig.suptitle('Original schematic sky maps; patterns and eclipse flux depth are illustrative, not measured data.',fontsize=11)

fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white',transparent=False,metadata={'Software':'Matplotlib'})
plt.close(fig)
