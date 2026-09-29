"""Original carbon skeletons of nitrate-radical product channels, PNG in cwd."""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from tools.chemistry_diagram import bond,atom,finish,save
fig,axes=plt.subplots(1,2,figsize=(10.3,3.8),facecolor='white')
for i,ax in enumerate(axes):
    # Original labelled skeleton, not a traced source diagram.
    pts=[(-1.6,-.3),(-.65,.25),(.45,-.35),(1.45,.25) if i==0 else (.45,-1.3)]
    bond(ax,pts[0],pts[1]);bond(ax,pts[1],pts[2],2);bond(ax,pts[2],pts[3])
    bond(ax,pts[1],(-.65,1.02));atom(ax,(-.65,1.12),'CH3')
    if i==0:
        atom(ax,pts[0],'CH2');bond(ax,pts[0],(-2.35,-.65));atom(ax,(-2.55,-.74),'O-NO2',size=11)
        atom(ax,pts[3],'CH2');bond(ax,pts[3],(2.22,.62));atom(ax,(2.50,.72),'O-NO2',size=11)
        title='Dinitrate channel'
    else:
        atom(ax,pts[0],'CH2');bond(ax,pts[0],(-2.35,-.65));atom(ax,(-2.55,-.74),'O-NO2',size=11)
        atom(ax,pts[3],'CH');bond(ax,pts[3],(1.30,-1.75),2);atom(ax,(1.47,-1.85),'O')
        title='Nitrooxy aldehyde channel'
    finish(ax,(-3.45,3.3),(-2.2,1.55),title)
fig.suptitle('Allylic rearrangement followed by oxygen trapping',fontsize=14)
fig.text(.5,.03,'Carbon skeletons shown; radical-branching yields and an exclusive E/Z outcome are not specified.',ha='center',fontsize=10)
fig.tight_layout(rect=(0,.09,1,.90));save(fig,'paper-3-isoprene-products.png')
