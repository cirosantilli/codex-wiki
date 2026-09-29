"""Original paraxial two-ray construction; all plot lengths in centimetres."""
import numpy as np
import matplotlib.pyplot as plt
fig,ax=plt.subplots(figsize=(10,4.5),facecolor='white',layout='constrained')
f=30.;d=10.;objx=-60.;objy=5.;imgx=28.75;imgy=-1.875
ax.axhline(0,color='.6',lw=.8)
for xx,name in [(0,'Lens 1'),(10,'Lens 2')]:
    ax.annotate('',(xx,10),(xx,-10),arrowprops=dict(arrowstyle='<->',color='#325976',lw=2))
    ax.text(xx,-11,name,ha='center',fontsize=11)
for col,initial_slope in [('#b4681c',0),('#287391',-objy/60)]:
    y1=objy+initial_slope*(0-objx);slope1=initial_slope-y1/f
    y2=y1+slope1*d;slope2=slope1-y2/f
    ax.plot([objx,0,10,imgx],[objy,y1,y2,imgy],color=col,lw=1.8)
    ax.plot([10,60],[y2,y2+slope1*50],color=col,lw=1,ls='--',alpha=.6)
ax.annotate('',(objx,objy),(objx,0),arrowprops=dict(arrowstyle='->',lw=2,color='#333333'))
ax.annotate('',(imgx,imgy),(imgx,0),arrowprops=dict(arrowstyle='->',lw=2,color='#333333'))
ax.text(objx,6.1,'Object',ha='center');ax.annotate('Real image\nx = 28.75 cm',(imgx,imgy),xytext=(36,-7),arrowprops=dict(arrowstyle='->'),fontsize=11)
ax.text(60,-7,'Lens 1 alone\nx = 60 cm',ha='center',fontsize=10,color='.4')
ax.set(xlim=(-68,70),ylim=(-13,12),xlabel='Position from lens 1 (cm)',ylabel='Paraxial height (chosen scale)',title='Lens 2 intercepts rays converging toward a virtual object')
fig.savefig('paper-1-ia2010-lenses.png',dpi=160,facecolor='white');plt.close(fig)
