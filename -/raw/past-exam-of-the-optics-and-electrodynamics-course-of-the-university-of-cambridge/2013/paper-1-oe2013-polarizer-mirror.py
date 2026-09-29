"""Original Jones-optics double-pass diagrams; PNG basename to cwd.
Python 3.14, Matplotlib. Detector/reflector is generic, with no biological model.
"""
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
fig,axes=plt.subplots(2,1,figsize=(10.2,5.6),layout='constrained')
for ax,index in zip(axes,[0,1]):
 ax.set(xlim=(-.25,10.4),ylim=(-1.1,1.65));ax.axis('off')
 order=['Q','P'] if index==0 else ['P','Q'];xs=[3.0,6.1]
 ax.text(0,.1,'Source /\ndetector',ha='center',va='center',fontsize=10)
 for x,name in zip(xs,order):
  col='#4b82b6' if name=='Q' else '#ba6258';ax.add_patch(Rectangle((x-.19,-.65),.38,1.3,facecolor=col,alpha=.65))
  ax.text(x,1.0,('B: ' if name=='Q' else 'A: ')+name,ha='center',fontsize=11)
 ax.add_patch(Rectangle((9.15,-.7),.16,1.4,facecolor='0.6',hatch='///'));ax.text(9.23,1.0,'Mirror',ha='center',fontsize=11)
 for start,end in [(.8,2.6),(3.4,5.7),(6.5,8.9)]:
  ax.annotate('',xy=(end,.25),xytext=(start,.25),arrowprops={'arrowstyle':'-|>','color':'#275e8e','lw':1.5})
  if index==1 and start==.8:ax.text(2.65,-.35,'×',ha='center',va='center',color='#8c5327',fontsize=16)
  else:ax.annotate('',xy=(start,-.35),xytext=(end,-.35),arrowprops={'arrowstyle':'-|>','color':'#8c5327','lw':1.5})
 outward=['Unpolarized','Unpolarized','x linear'] if index==0 else ['Unpolarized','x linear','Circular']
 backward=['Circular','x linear','x linear'] if index==0 else ['Blocked','y linear','Circular*']
 for x,fw,bw in zip([1.65,4.55,7.7],outward,backward):
  ax.text(x,.43,fw,ha='center',fontsize=9);ax.text(x,-.74,bw,ha='center',fontsize=9)
 ax.text(.2,1.43,'B nearest detector: reflected target visible' if index==0 else 'A nearest detector: ideal reflected target dark',fontsize=12,weight='bold')
fig.supxlabel('* Reflection reverses circular helicity because the propagation direction reverses.  P: linear polarizer; Q: quarter-wave plate at 45°.',fontsize=9)
fig.savefig('paper-1-oe2013-polarizer-mirror.png',dpi=140,facecolor='white')
