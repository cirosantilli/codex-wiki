import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, FancyArrowPatch
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False,'figure.facecolor':'white','savefig.facecolor':'white'})

fig,ax=plt.subplots(1,3,figsize=(11,3.8),layout='constrained')
e=np.linspace(-2,2,500);up=.9*np.exp(-((e+.55)/.65)**2)+.15;down=.6*np.exp(-((e-.55)/.65)**2)+.15
ax[0].plot(up,e,label=r'$D_\uparrow$');ax[0].plot(-down,e,label=r'$D_\downarrow$');ax[0].axhline(0,color='k',ls=':',label=r'$E_F$');ax[0].set(xlabel='Spin-resolved DOS (schematic)',ylabel='Energy relative to Fermi level',title='Exchange-split final states');ax[0].legend(fontsize=9)
for i,(name,spacer) in enumerate([('GMR','Metal'),('TMR','Insulator')]):
 y=1.7-i*1.2
 for x,w,col,lab in [(0,1,'#8ab6d6','Pinned'),(1,.9,'0.85',spacer),(1.9,1,'#8ab6d6','Free')]:
  ax[1].add_patch(Rectangle((x,y-.22),w,.5,facecolor=col,edgecolor='k'));ax[1].text(x+w/2,y+.45,lab,ha='center',fontsize=9)
 ax[1].annotate('',xy=(.8,y),xytext=(.2,y),arrowprops={'arrowstyle':'->','lw':2});ax[1].annotate('',xy=(2.4,y+.2),xytext=(2.4,y-.13),arrowprops={'arrowstyle':'->','lw':2});ax[1].text(-.15,y-.55,name,fontsize=10)
ax[1].set(xlim=(-.3,3.2),ylim=(-.5,2.7),title='Same magnetic readout; different spacer');ax[1].axis('off')
t=np.linspace(0,np.pi,600);p=.36;ax[2].plot(t/np.pi,1+.5*(1-np.cos(t)),label='GMR: chosen resistance law');ax[2].plot(t/np.pi,(1+p)/(1+p*np.cos(t)),label='TMR: DOS model');ax[2].axvline(.5,color='.6',ls=':');ax[2].set(xlabel=r'Relative angle $\theta/\pi$',ylabel=r'$R(\theta)/R_P$',title='Bias near a finite angular slope');ax[2].legend(fontsize=8);ax[2].text(.03,1.85,'Chosen parameters, not material data',fontsize=8)
fig.savefig('paper-1-spin-sensors.png',dpi=155)
