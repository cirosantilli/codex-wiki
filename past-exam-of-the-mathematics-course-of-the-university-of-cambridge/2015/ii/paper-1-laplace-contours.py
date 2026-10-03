import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig,ax=plt.subplots(2,1,figsize=(8,3.6),dpi=100)
for j,a in enumerate(ax):
 a.axhline(0,color='.6',lw=1);a.plot([0,1],[0,0],color='royalblue',lw=4)
 a.annotate('',xy=(.7,0),xytext=(.3,0),arrowprops=dict(arrowstyle='->',color='royalblue',lw=2))
 a.text(.5,.16,r'$C_1: 0\to1$',ha='center',color='royalblue')
 a.plot([0,1],[0,0],'ko',ms=4);a.text(0,-.18,'0',ha='center');a.text(1,-.18,'1',ha='center')
 a.set(xlim=(-2,3),ylim=(-.4,.65));a.axis('off')
 if j==0:
  a.plot([-1.8,0],[0,0],color='firebrick',lw=4);a.annotate('',xy=(-.4,0),xytext=(-1.3,0),arrowprops=dict(arrowstyle='->',color='firebrick',lw=2))
  a.text(-1,.16,r'$C_2: -\infty\to0$',ha='center',color='firebrick');a.text(-1.8,-.18,r'$-\infty$',ha='center')
  a.text(-1.95,.48,r'$x>0$: decay at negative infinity',fontsize=11)
 else:
  a.plot([1,2.8],[0,0],color='darkorange',lw=4);a.annotate('',xy=(2.5,0),xytext=(1.5,0),arrowprops=dict(arrowstyle='->',color='darkorange',lw=2))
  a.text(2,.16,r'$C_2: 1\to+\infty$',ha='center',color='darkorange');a.text(2.8,-.18,r'$+\infty$',ha='center')
  a.text(-1.95,.48,r'$x<0$: decay at positive infinity',fontsize=11)
fig.suptitle('Real Laplace contours with continuous branch on each interval',fontsize=11)
fig.subplots_adjust(left=.04,right=.98,top=.86,bottom=.02,hspace=.15)
fig.savefig('paper-1-laplace-contours.png',facecolor='white',transparent=False)
