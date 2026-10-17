import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,Rectangle
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False,'figure.facecolor':'white','savefig.facecolor':'white'})

fig,ax=plt.subplots(2,2,figsize=(10,7.3),layout='constrained');gamma=5/3

def path(a,x,y,col='#17639b'):
 x=np.asarray(x);y=np.asarray(y);a.plot(x,y,color=col,lw=2);j=len(x)//2;d=max(1,len(x)//12);a.annotate('',xy=(x[j+d],y[j+d]),xytext=(x[j-d],y[j-d]),arrowprops={'arrowstyle':'->','color':col,'lw':1.7})
def label(a,x,y,t,off=(4,4)):a.plot(x,y,'ko',ms=3);a.annotate(t,(x,y),xytext=off,textcoords='offset points',fontsize=10)
# Carnot: ideal-gas nR=1, Th=2,Tc=1.
Th=2.;Tc=1.;V1=1.;V2=2.;factor=(Th/Tc)**(1/(gamma-1));V3=V2*factor;V4=V1*factor
v=np.linspace(V1,V2,120);path(ax[0,0],v,Th/v,'crimson');v=np.linspace(V2,V3,120);path(ax[0,0],v,(Th/V2)*(V2/v)**gamma);v=np.linspace(V3,V4,120);path(ax[0,0],v,Tc/v,'#2a8050');v=np.linspace(V4,V1,120);path(ax[0,0],v,(Tc/V4)*(V4/v)**gamma)
for v,p,t in [(V1,Th/V1,'1'),(V2,Th/V2,'2'),(V3,Tc/V3,'3'),(V4,Tc/V4,'4')]:label(ax[0,0],v,p,t)
ax[0,0].set(xlabel='Volume (chosen units)',ylabel='Pressure (chosen units)',title='Carnot: clockwise pressure-volume cycle',ylim=(0,2.3));ax[0,0].text(1.1,1.8,'Heat in',color='crimson');ax[0,0].text(3.4,.37,'Heat out',color='#2a8050')
ds=np.log(V2/V1);temps=[Th,Th,Tc,Tc,Th];ent=[0,ds,ds,0,0]
for i in range(4):path(ax[0,1],np.linspace(temps[i],temps[i+1],80),np.linspace(ent[i],ent[i+1],80),['crimson','#17639b','#2a8050','#17639b'][i])
for T,S,t in zip(temps[:-1],ent[:-1],['1','2','3','4']):label(ax[0,1],T,S,t)
ax[0,1].set(xlabel='Temperature',ylabel='Entropy relative to state1',title='Carnot: S vertical, T horizontal',xlim=(.8,2.3),ylim=(-.12,.85));ax[0,1].text(2.07,.25,'Heat in',rotation=90,color='crimson',fontsize=9);ax[0,1].text(.86,.25,'Heat out',rotation=90,color='#2a8050',fontsize=9)
# Brayton: A-B at high pressure; nR=1 and Cp=5/2.
ph=4.;pl=1.;rat=(ph/pl)**((gamma-1)/gamma);TA=2.;TB=4.;TC=TB/rat;TD=TA/rat;VA=TA/ph;VB=TB/ph;VC=TC/pl;VD=TD/pl
v=np.linspace(VA,VB,100);path(ax[1,0],v,np.full_like(v,ph),'crimson');v=np.linspace(VB,VC,100);path(ax[1,0],v,ph*(VB/v)**gamma);v=np.linspace(VC,VD,100);path(ax[1,0],v,np.full_like(v,pl),'#2a8050');v=np.linspace(VD,VA,100);path(ax[1,0],v,pl*(VD/v)**gamma)
for V,P,t in [(VA,ph,'A'),(VB,ph,'B'),(VC,pl,'C'),(VD,pl,'D')]:label(ax[1,0],V,P,t)
ax[1,0].set(xlabel='Volume (chosen units)',ylabel='Pressure (chosen units)',title='Brayton: two isobars and two adiabats',ylim=(.5,4.7));ax[1,0].text(.55,4.3,'Heat in',color='crimson');ax[1,0].text(1.5,.65,'Heat out',color='#2a8050')
cp=gamma/(gamma-1);SB=cp*np.log(TB/TA)
T=np.linspace(TA,TB,120);path(ax[1,1],T,cp*np.log(T/TA),'crimson');path(ax[1,1],np.linspace(TB,TC,120),np.full(120,SB));T=np.linspace(TC,TD,120);path(ax[1,1],T,cp*np.log(T/TD),'#2a8050');path(ax[1,1],np.linspace(TD,TA,120),np.zeros(120))
for T,S,t in [(TA,0,'A'),(TB,SB,'B (hottest)'),(TC,SB,'C'),(TD,0,'D (coldest)')]:label(ax[1,1],T,S,t)
ax[1,1].set(xlabel='Temperature',ylabel='Entropy relative to A',title='Brayton: nonisothermal heat transfer',ylim=(-.24,2.05),xlim=(.8,4.8))
fig.suptitle('Original ideal-gas model cycles; arrows show positive-work direction',fontsize=12)
fig.savefig('paper-1-engine-cycles.png',dpi=155)
