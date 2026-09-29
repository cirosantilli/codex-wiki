"""Original Newman projection and product for the open Felkin-Anh model."""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle
from tools.chemistry_diagram import *
fig,axs=plt.subplots(1,2,figsize=(12,4.7),layout='constrained',facecolor='white')
a=axs[0];a.add_patch(Circle((0,0),.38,ec='0.4',fc='white'))
for th,label in [(np.pi,'L'),(np.pi/3,'Me'),(5*np.pi/3,'H')]:
 end=1.15*np.array([np.cos(th),np.sin(th)]);bond(a,(0,0),end,color=BLUE);atom(a,1.3*end,label)
bond(a,(0,.38),(0,1.3),2);atom(a,(0,1.5),'O');bond(a,(0,-.38),(0,-1.3));atom(a,(0,-1.5),'Ph');a.plot(0,0,'o',color=BLUE,ms=5)
flow(a,(1.9,-.6),(.3,-.15));atom(a,(2.05,-.9),'Me–MgBr',size=11);a.text(-1.7,-2.1,'View: Cα (front) → carbonyl C (rear)',fontsize=11);a.text(-1.7,-2.55,'L = CH(Ph)CH₂CH₂OMe',fontsize=11);finish(a,(-2,2.8),(-2.8,2),'Approach opposite L, passing H')
a=axs[1];Cbeta=(-.8,.1);Calpha=(.2,-.5);Cnew=(1.2,.1);bond(a,Cbeta,Calpha);bond(a,Calpha,Cnew);bond(a,Cbeta,(-1.8,-.5));bond(a,(-1.8,-.5),(-2.7,.1));atom(a,(-3.3,-.15),'MeO')
wedge(a,Cbeta,(-.8,1),True);atom(a,(-.8,1.2),'Ph');wedge(a,Calpha,(.2,-1.45),True);atom(a,(.2,-1.65),'Me')
bond(a,Cnew,(2.2,-.45));atom(a,(2.45,-.6),'Ph');wedge(a,Cnew,(1.65,1.05),False);atom(a,(1.8,1.3),'OH');wedge(a,Cnew,(.65,1.05),True);atom(a,(.5,1.3),'Me');a.text(1.25,-.45,'S',color=ORANGE,fontsize=14)
a.text(-2.7,-2.35,'At the new centre: OH > Ph > Cα chain > Me',fontsize=11);finish(a,(-3.75,3.1),(-2.8,2),'Predicted major alcohol; existing centres retained')
save(fig,'paper-1-felkin-addition.png')
