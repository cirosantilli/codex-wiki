"""Original functional Hall-bar and MOS gate diagram; outputs to the working directory."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle

fig, (ax, side) = plt.subplots(1, 2, figsize=(12.4, 5.8), gridspec_kw={'width_ratios':[1.9,1]})
fig.patch.set_facecolor('white')
fig.suptitle('Separate transverse and longitudinal voltage measurements', fontsize=17, y=.98)
ax.set(xlim=(-1.3,10.3),ylim=(-2.8,5.3));ax.axis('off')
ax.add_patch(Rectangle((0,0),9,2.8,facecolor='#dcecf4',edgecolor='#24526a',lw=2))
for x,y in [(2,2.8),(7,2.8),(4.5,0),(4.5,2.8)]:
    ax.add_patch(Rectangle((x-.18,y-.16),.36,.32,facecolor='#e2a33c',edgecolor='#815a13'))
ax.annotate('',xy=(2.3,1.4),xytext=(-1.15,1.4),arrowprops={'arrowstyle':'->','lw':2.5,'color':'#24526a'})
ax.annotate('',xy=(10.1,1.4),xytext=(7.1,1.4),arrowprops={'arrowstyle':'->','lw':2.5,'color':'#24526a'})
ax.text(-.75,1.75,'I',fontsize=16)
ax.text(9.65,1.75,'I',fontsize=16)
ax.plot([2,2,7,7],[2.8,4.25,4.25,2.8],color='#815a13',lw=1.8)
ax.text(4.5,4.25,r'$V_{xx}$',ha='center',va='center',fontsize=16,bbox={'facecolor':'white','edgecolor':'#815a13','boxstyle':'round,pad=.3'})
ax.plot([4.5,4.5,8.65,8.65,4.5,4.5],[2.8,3.4,3.4,-.7,-.7,0],color='#a62d48',lw=1.8)
ax.text(8.65,1.4,r'$|V_H|$',ha='center',va='center',fontsize=15,bbox={'facecolor':'white','edgecolor':'#a62d48','boxstyle':'round,pad=.3'})
ax.annotate('',xy=(7,3.8),xytext=(2,3.8),arrowprops={'arrowstyle':'<->','color':'#444'})
ax.text(5.4,3.72,'L',fontsize=12,bbox={'facecolor':'white','edgecolor':'none','pad':1})
ax.annotate('',xy=(.7,2.8),xytext=(.7,0),arrowprops={'arrowstyle':'<->','color':'#444'})
ax.text(.9,1.4,'W',va='center',fontsize=12)
ax.add_patch(Circle((1,-1.3),.23,fill=False,lw=1.8));ax.plot(1,-1.3,'o',color='black',ms=3)
ax.text(1.45,-1.3,r'$B_z>0$: out of the page',va='center',fontsize=12)
ax.annotate('',xy=(7.8,-1.7),xytext=(6.3,-1.7),arrowprops={'arrowstyle':'->','lw':1.5});ax.text(7.95,-1.7,'+x',va='center',fontsize=12)
ax.text(4.5,-2.4,'Conventional current direction; voltmeters draw negligible current',ha='center',fontsize=10)
side.set(xlim=(0,4),ylim=(-.8,5.2));side.axis('off')
side.set_title('Gate-controlled channel',fontsize=14,pad=15)
for y,h,color,label in [(2.8,.45,'#e2a33c','Metal gate'),(1.7,1.1,'#eaeaea','Oxide insulator'),(.2,1.5,'#cce0d1','Silicon')]:
    side.add_patch(Rectangle((.25,y),3.45,h,facecolor=color,edgecolor='#555'))
    side.text(1.98,y+h/2,label,ha='center',va='center',fontsize=12)
side.plot([.3,3.65],[1.69,1.69],color='#a62d48',lw=4)
side.annotate('Thin electron channel',xy=(2.2,1.69),xytext=(2,3.85),ha='center',fontsize=11,arrowprops={'arrowstyle':'->','color':'#a62d48'})
side.text(2,-.35,'Gate voltage changes\nchannel electron density',ha='center',fontsize=12,linespacing=1.5)
fig.text(.5,.025,'Original functional diagram: no historical dimensions or measured data',ha='center',fontsize=11,color='#555')
fig.subplots_adjust(left=.02,right=.98,top=.84,bottom=.13,wspace=.12)
fig.savefig(Path(__file__).with_suffix('.png').name,dpi=110,facecolor='white')
plt.close(fig)
