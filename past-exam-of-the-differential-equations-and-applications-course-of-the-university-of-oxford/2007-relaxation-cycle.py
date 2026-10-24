# Tested with Python3.14.4,numpy2.3.5,matplotlib3.10.7. Output is written to CWD.
import numpy as np
import matplotlib.pyplot as plt
G=.5
f=lambda y:y-y*y+G*y**3/3
lo=(1-np.sqrt(1-G))/G;hi=(1+np.sqrt(1-G))/G
bottom=3/G-2*hi;top=3/G-2*lo
fig,ax=plt.subplots(figsize=(7,5),facecolor='white')
for a,b,color,style in [(-1.2,lo,'#147d6c','-'),(lo,hi,'#9c7373','--'),(hi,5.2,'#147d6c','-')]:
 y=np.linspace(a,b,250);ax.plot(f(y),y,style,color=color,lw=2)
for a,b in [(bottom,lo),(top,hi)]:
 y=np.linspace(a,b,200);ax.plot(f(y),y,color='#2048aa',lw=3)
 m=(a+b)/2;dy=np.sign(b-a)*.18;ax.annotate('',xy=(f(m+dy),m+dy),xytext=(f(m-dy),m-dy),arrowprops={'arrowstyle':'->','color':'#2048aa','lw':2})
for y0,y1 in [(lo,top),(hi,bottom)]:
 ax.annotate('',xy=(f(y0),y1),xytext=(f(y0),y0),arrowprops={'arrowstyle':'->','color':'#bd4328','lw':2.3})
ax.axhline(2,color='gray',ls=':',label=r'$y=α=2$')
ax.scatter([f(lo),f(hi)],[lo,hi],color='black',zorder=5)
ax.text(f(lo)+.15,lo-.15,r'$y_-$');ax.text(f(hi)-.48,hi+.06,r'$y_+$')
ax.set(xlabel='$x$',ylabel='$y$',title='Slow arcs and fast jumps of a cubic relaxation oscillator',xlim=(-2.5,2),ylim=(-1.3,5.3))
ax.text(.03,.97,'Green: attracting cubic branches\nDashed: repelling cubic branch\nBlue: slow drift; red: fast jumps',transform=ax.transAxes,va='top',fontsize=9,bbox={'facecolor':'white','alpha':.9,'edgecolor':'none'})
ax.legend(loc='lower right');ax.grid(alpha=.18);fig.tight_layout();fig.savefig('2007-relaxation-cycle.png',dpi=160,facecolor='white')
