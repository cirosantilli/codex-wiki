"""Original explanatory figure. Python 3.14, numpy 2.3.5, matplotlib 3.10.7.
Run through the root Makefile; the PNG basename is written to the current directory.
"""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon
from tools.chemistry_diagram import bond, atom, ring, wedge, curly, flow, finish, save
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})
fig,axs=plt.subplots(2,2,figsize=(13,7),layout='constrained')
def repeat(a,c=(0,0),sub=None,sat=False):
 p=np.array([[-.8,.4],[0,.95],[.8,.4],[.5,-.65],[-.5,-.65]])+c
 ring(a,p);bond(a,p[0],p[0]+[-.6,.5]);bond(a,p[2],p[2]+[.6,.5]);bond(a,p[0]+[-.6,.5],p[0]+[-1.2,.1],1 if sat else 2);bond(a,p[2]+[.6,.5],p[2]+[1.2,.1],1 if sat else 2)
 if sub:bond(a,p[3],p[3]+[.65,-.35]);atom(a,p[3]+[1.0,-.55],sub,11)
 finish(a,(-2.1,2.65),(-1.5,1.7))
repeat(axs[0,0]);axs[0,0].set_title('A: unsaturated local polynorbornene fragment');axs[0,0].text(0,-1.35,'backbone links continue through neighbouring repeats',ha='center',fontsize=9)
repeat(axs[0,1],sub=r'CO$_2$Me');axs[0,1].set_title('B: ester-bearing second-block fragment')
repeat(axs[1,0],sub=r'CH$_2$OH',sat=True);axs[1,0].set_title('C: saturated, hydroxyl-functional fragment')
a=axs[1,1];p=np.array([[-.8,.4],[0,.95],[.8,.4],[.5,-.65],[-.5,-.65]]);ring(a,p)
for i,delta in [(0,[-.75,.55]),(2,[.75,.55])]:bond(a,p[i],p[i]+delta);atom(a,p[i]+np.array(delta)*1.45,'CHO')
a.text(0,-1.4,'aldehydes after reductive backbone cleavage',ha='center',fontsize=10);finish(a,(-2,2),(-1.65,1.6),'Ozonolysis fragment; repeat stereochemistry retained')
fig.suptitle('Original connectivity sketches; alkene geometry and end groups not fixed',fontsize=14)
save(fig,'paper-2-polymer-connectivity.png')
