"""Characteristic strip for y*u_x+u_y=u. Python 3.14; NumPy/Matplotlib."""
import numpy as np
import matplotlib.pyplot as plt
fig,ax=plt.subplots(figsize=(6.5,5),facecolor='white');y=np.linspace(-2.3,2.3,500)
ax.fill_betweenx(y,1+y*y/2,2+y*y/2,color='#cce7f5',label='Uniquely determined strip')
for s in [1,1.25,1.5,1.75,2]:
 x=s+y*y/2;ax.plot(x,y,color='#1769aa',lw=1.7 if s in [1,2] else .8)
 j=300;ax.annotate('',xy=(x[j+14],y[j+14]),xytext=(x[j],y[j]),arrowprops={'arrowstyle':'->','color':'#1769aa'})
ax.plot([1,2],[0,0],color='#a33c0b',lw=4,label='Initial segment')
ax.text(1.1,-1.3,r'$x=1+y^2/2$',rotation=-42,fontsize=10);ax.text(3.5,1.55,r'$x=2+y^2/2$',rotation=42,fontsize=10)
ax.set(xlim=(.3,5),ylim=(-2.3,2.3),xlabel='$x$',ylabel='$y$',title=r'Characteristics: $x=s+y^2/2$, $1\leq s\leq2$');ax.grid(alpha=.15);ax.legend(loc='upper left',fontsize=9);fig.tight_layout();fig.savefig('2006-characteristic-strip.png',dpi=150,facecolor='white')
