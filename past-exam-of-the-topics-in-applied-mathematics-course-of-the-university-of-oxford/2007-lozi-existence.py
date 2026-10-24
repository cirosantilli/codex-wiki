# Tested with Python3.14.4,numpy2.3.5,matplotlib3.10.7. Writes PNG to CWD.
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.patches import Patch
x,y=np.meshgrid(np.linspace(-2.5,2.5,700),np.linspace(-2,4,700));pos=y<1+x;neg=y>1-x;z=pos.astype(int)+2*neg.astype(int)
fig,ax=plt.subplots(figsize=(7,5),facecolor='white');ax.pcolormesh(x,y,z,cmap=ListedColormap(['#ffffff','#c6def3','#f5d2c5','#d8c5ed']),shading='nearest',vmin=0,vmax=3)
a=np.linspace(-2.5,2.5,400);ax.plot(a,1+a,'--',color='#235e9b',label='$b=1+a$');ax.plot(a,1-a,'--',color='#a94729',label='$b=1-a$');ax.axhline(0,color='gray',lw=.6);ax.axvline(0,color='gray',lw=.6)
handles=[Patch(facecolor=c,label=l)for c,l in [('#ffffff','No fixed point'),('#c6def3','Positive fixed point only'),('#f5d2c5','Negative fixed point only'),('#d8c5ed','Both; also one genuine two-cycle')]];ax.legend(handles=handles,loc='upper left',fontsize=8);ax.set(xlim=(-2.5,2.5),ylim=(-2,4),xlabel='$a$',ylabel='$b$',title='Lozi map: regions of fixed-point existence');ax.text(1.55,2.9,'$b=1+a$',rotation=32,fontsize=10);ax.text(1.45,-.7,'$b=1-a$',rotation=-32,fontsize=10);fig.tight_layout()
fig.savefig('2007-lozi-existence.png',dpi=160,facecolor='white')
