import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,Rectangle
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False,'figure.facecolor':'white','savefig.facecolor':'white'})

fig,ax=plt.subplots(1,2,figsize=(10,3.7),layout='constrained');r=np.linspace(-1,1,400)
ax[0].plot(2*(1-r*r),r,label='Fully developed laminar tube');ax[0].plot(np.ones_like(r),r,'--',label='Uniform comparison profile');ax[0].plot([0,2.3],[-1,-1],'k');ax[0].plot([0,2.3],[1,1],'k');ax[0].set(xlabel='Axial speed / cross-section mean',ylabel='Radial coordinate / tube radius',title='Same mean; different boundary behaviour');ax[0].legend(fontsize=8,loc='center left')
a=ax[1];a.add_patch(Rectangle((0,-.45),4,.9,facecolor='#edf5fa',edgecolor='k'))
for x in [.7,3.1]:a.plot([x,x],[.45,1],'k');a.add_patch(Rectangle((x-.2,1),.4,.28,facecolor='white',edgecolor='k'))
a.text(.7,1.4,r'$p_1$',ha='center');a.text(3.1,1.4,r'$p_2$',ha='center');a.annotate('',xy=(3.6,0),xytext=(.4,0),arrowprops={'arrowstyle':'->','lw':2});a.text(2,-.8,r'$Q=\pi a^4(p_1-p_2)/(8\eta L)$',ha='center');a.text(2,-1.3,'Collect volume per time; measure radius and temperature',ha='center',fontsize=9);a.set(xlim=(-.3,4.3),ylim=(-1.55,1.85),title='Pressure and discharge are independent readouts');a.axis('off')
fig.savefig('paper-1-fluid-flow.png',dpi=155)
