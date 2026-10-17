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
a=axs[0,0];pts=np.array([[-1.8,.3],[-.9,-.2],[0,.3],[.9,-.2],[1.8,.3]]);bond(a,pts[0],pts[1]);bond(a,pts[1],pts[2]);bond(a,pts[2],pts[3]);bond(a,pts[3],pts[4]);wedge(a,pts[1],pts[1]+[0,-.7],True);atom(a,pts[1]+[0,-.85],'OH');wedge(a,pts[3],pts[3]+[0,-.7],False);atom(a,pts[3]+[0,-.85],'OH');atom(a,pts[0]+[-.45,0],'R');atom(a,pts[4]+[.55,0],r'CH$_2$OTIPS');a.text(0,1,'hydroxyl-tethered hydride delivery',ha='center');finish(a,(-2.5,3),(-1.5,1.5),'Anti-1,3-diol relationship')
a=axs[0,1];p=np.array([[-1.8,.3],[-.6,-.25],[.6,.3],[1.8,-.25]]);
for i in range(3):bond(a,p[i],p[i+1])
atom(a,p[0],'AuxNCO',11);atom(a,p[-1],'CH=CHPh',11);wedge(a,p[1],p[1]+[0,-.8],True);atom(a,p[1]+[0,-1],'Me');wedge(a,p[2],p[2]+[0,.8],True);atom(a,p[2]+[0,1],'OH');a.text(-.6,.05,'R',ha='center',color='#245c9f');a.text(.6,-.1,'S',ha='center',color='#245c9f');finish(a,(-3,3),(-1.5,1.8),'Syn aldol: wedged methyl at the labelled centre')
a=axs[1,0];atom(a,(0,.7),r'HOCH$_2$—CH(OH)—CH$_2$—CH=CH—Me',12);a.text(0,.05,'E alkene; original secondary stereocentre retained',ha='center');a.text(0,-.55,'No newly created tetrahedral stereocentre in H',ha='center',color='#245c9f');finish(a,(-3.8,3.8),(-1.4,1.5),'Epoxide opening, alkyne reduction and debenzylation')
a=axs[1,1];p=np.array([[0,-1],[.9,-.5],[.9,.5],[0,1],[-.9,.5],[-.9,-.5]]);ring(a,p);atom(a,p[0],'O');subs=[(1,[.9,-.45],'R',False),(2,[.9,.45],'Me',True),(3,[0,.85],'OH',False),(5,[-.9,-.45],r'CH$_2$OH',False)]
for i,d,t,f in subs:wedge(a,p[i],p[i]+d,f);atom(a,p[i]+np.array(d)*1.35,t,10)
for i in range(1,6):a.text(p[i,0]*.74,p[i,1]*.74,str(i+1),fontsize=8,color='#245c9f')
a.text(0,-1.6,'R = aldehyde-derived chiral side chain',ha='center',fontsize=9);finish(a,(-2.5,2.5),(-1.85,2.3),'Prins product: preferred chair relationships')
save(fig,'paper-2-stereochemical-products.png')
