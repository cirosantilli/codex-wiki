"""Draw the flavour nonet. Tested: Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.

Writes only paper-42-meson-weights.png in the caller's current working directory.
The caller supplies MPLCONFIGDIR; this generator does not override it.
"""
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig,ax=plt.subplots(figsize=(9,6.5),dpi=100,facecolor='white')
fig.subplots_adjust(left=.09,right=.93,bottom=.11,top=.86)
ax.set_facecolor('white')
vertices=[(1,0),(.5,1),(-.5,1),(-1,0),(-.5,-1),(.5,-1),(1,0)]
ax.plot(*zip(*vertices),color='#71869a',lw=1.7,zorder=1)
ax.axhline(0,color='#d4dae0',lw=1,zorder=0)
ax.axvline(0,color='#d4dae0',lw=1,zorder=0)
for x,y in vertices[:-1]:ax.scatter(x,y,s=65,color='#155a93',zorder=3)
ax.scatter(0,0,s=80,color='#ac4d24',zorder=3)
labels=[(1,0,r'$\pi^+:\ u\bar d$',(15,0),'left','center'),(-1,0,r'$\pi^-:\ d\bar u$',(-15,0),'right','center'),(.5,1,r'$K^+:\ u\bar s$',(10,12),'left','bottom'),(-.5,1,r'$K^0:\ d\bar s$',(-10,12),'right','bottom'),(.5,-1,r'$\bar K^0:\ s\bar d$',(10,-12),'left','top'),(-.5,-1,r'$K^-:\ s\bar u$',(-10,-12),'right','top')]
for x,y,text,offset,ha,va in labels:ax.annotate(text,(x,y),xytext=offset,textcoords='offset points',ha=ha,va=va,fontsize=14)
ax.annotate('Two octet states: '+r'$\pi^0,\ \eta_8$'+'\nSeparate singlet: '+r'$\eta_1$',(0,0),xytext=(0,43),textcoords='offset points',ha='center',va='bottom',fontsize=12,bbox=dict(boxstyle='round,pad=.45',fc='white',ec='#ac4d24'),arrowprops=dict(arrowstyle='-',color='#ac4d24'))
ax.set_xlim(-1.65,1.65);ax.set_ylim(-1.55,1.6)
ax.set_aspect(math.sqrt(3)/2)
ax.set_xticks([-1,-.5,0,.5,1]);ax.set_yticks([-1,0,1])
ax.set_xlabel(r'Isospin component $I_3$',fontsize=13)
ax.set_ylabel(r'Flavour hypercharge $Y=B+S$',fontsize=13)
for spine in ax.spines.values():spine.set_color('#a2acb5')
ax.tick_params(labelsize=11)
fig.suptitle('Pseudoscalar flavour nonet',fontsize=19,y=.985)
fig.text(.5,.90,'Triplet × antitriplet = octet + singlet',ha='center',fontsize=16)
fig.savefig('paper-42-meson-weights.png',dpi=100,facecolor='white',transparent=False)
plt.close(fig)
