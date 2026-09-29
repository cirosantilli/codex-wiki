"""Original explanatory diagram; Python 3.14, matplotlib and numpy.
Run from the desired output directory; the PNG is written to that directory.
"""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Circle
from tools.chemistry_diagram import bond, atom, ring, wedge, curly, flow, finish, save, BLUE, ORANGE
plt.rcParams.update({'font.size':11,'font.family':'DejaVu Sans'})
fig,axs=plt.subplots(2,2,figsize=(13,8.3),layout='constrained')
def draw(ax,stage):
    sugar=np.array([[.7,0],[.3,.7],[-.5,.7],[-.9,0],[-.5,-.7],[.3,-.7]])
    ring(ax,sugar);atom(ax,sugar[1],'O');atom(ax,sugar[0],'C1',size=10)
    ch=(-.95,1.35);wedge(ax,sugar[2],ch,True);atom(ax,ch,'CH₂OH',size=10)
    # Unchanged sugar hydroxyl substituents are deliberately suppressed.
    c2=np.array([2.25,0]);c3=np.array([2.8,.7]);ft=np.array([3.6,.5]);fb=np.array([3.6,-.5]);nh=np.array([2.8,-.7])
    ring(ax,[c2,c3,ft,fb,nh],{0:2} if stage!=2 else {})
    ring(ax,[ft,[4.35,.9],[5.1,.5],[5.1,-.5],[4.35,-.9],fb],{0:2,2:2,4:2})
    atom(ax,nh,'NH');atom(ax,c2,'C2',size=10);bond(ax,c3,(2.65,1.25));atom(ax,(2.65,1.25),'R',size=10)
    if stage==0:
        wedge(ax,sugar[0],(1.45,.55),True);atom(ax,(1.45,.55),'O–LG',size=10)
        curly(ax,(1.04,.25),(1.55,.65),-.35)
        ax.text(.3,-1.4,'Leaving-group activation and C1–O cleavage',ha='center',fontsize=10)
    elif stage==1:
        ax.text(.83,.18,'+',color=ORANGE,fontsize=16);atom(ax,(1.45,-1.0),'LG⁻',size=10)
        curly(ax,(2.5,.32),(.83,.05),.35)
        ax.text(1.8,-1.5,'I1: oxocarbenium / counterion; indole attacks at C2',ha='center',fontsize=10)
    elif stage==2:
        wedge(ax,sugar[0],c2,False);bond(ax,c2,(2.1,-.65));atom(ax,(2.1,-.65),'H',size=10)
        ax.text(2.95,.45,'+',color=ORANGE,fontsize=16);atom(ax,(1.6,-1.1),'B:',size=10)
        curly(ax,(1.7,-1.0),(2.06,-.65),-.3);curly(ax,(2.18,-.3),(2.48,.3),-.4)
        ax.text(1.8,-1.7,'I2: C–C-bonded σ complex; base removes C2–H',ha='center',fontsize=10)
    else:
        wedge(ax,sugar[0],c2,False)
        ax.text(1.7,-1.4,'Aromatic C-linked product; N–H retained',ha='center',fontsize=10)
    finish(ax,(-1.55,5.45),(-2,1.8))
for ax,stage,title in zip(axs.flat,range(4),['1. Activated donor + 3-substituted indole','2. Dissociation, then carbon attack','3. Deprotonation and rearomatization','4. Opposite-face product']):draw(ax,stage);ax.set_title(title,fontsize=12)
fig.suptitle('Purely chemical proposal; LG = activated diphosphate, R = unchanged C3 substituent\nUnchanged sugar OH groups omitted; solid/hashed bonds show opposite anomeric faces.',fontsize=12)
save(fig,'paper-2-glycosylation-mechanism.png')
