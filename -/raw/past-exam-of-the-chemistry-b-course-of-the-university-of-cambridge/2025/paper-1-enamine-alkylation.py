"""Original schematic electron flow for a Stork alkylation; output to cwd."""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
import matplotlib.pyplot as plt
from tools.chemistry_diagram import *
fig,axs=plt.subplots(3,1,figsize=(11,7.2),layout='constrained',facecolor='white')
def base(ax,c,n=False,eno=False,carbonyl=True,alkyl=False):
 x,y=c;atom(ax,(x-1,y),'R¹');bond(ax,(x-.7,y),(x,y));bond(ax,(x,y),(x+1,y),2 if eno else 1);atom(ax,(x+1.7,y),'R²');bond(ax,(x+1,y),(x+1.4,y))
 if carbonyl:bond(ax,(x,y),(x,y+.8),2);atom(ax,(x,y+.8),'O')
 if n:bond(ax,(x,y),(x,y+.8),1 if eno else 2);atom(ax,(x,y+.8),'N(Pyr)' if eno else 'N⁺(Pyr)')
 if alkyl:bond(ax,(x+1,y),(x+1,y-.8));atom(ax,(x+1,y-.9),'CH₂CN')
 return (x,y),(x+1,y)
a=axs[0];base(a,(.6,0));atom(a,(-1.15,1.2),':NH(Pyr)');curly(a,(-.7,1.1),(.5,.1),-.2);curly(a,(.65,.5),(.67,.85),-.6)
flow(a,(2.6,0),(4.3,0),'addition, −H₂O');base(a,(5.3,0),n=True,carbonyl=False);flow(a,(7.5,0),(8.8,0),'−H⁺');base(a,(9.8,0),n=True,eno=True,carbonyl=False)
a.text(6,-1.25,'Carbinolamine → iminium → enamine; R² side denotes the selected α carbon.',ha='center',fontsize=11);finish(a,(-1.9,12),(-1.6,1.7),'1. Reversible enamine formation')
a=axs[1];_,alpha=base(a,(.5,.1),n=True,eno=True,carbonyl=False);atom(a,(3.5,.1),'CH₂–CN');atom(a,(3.5,.95),'Br');bond(a,(3.5,.3),(3.5,.75));curly(a,(1,.1),(3.1,.1),-.4);curly(a,(3.5,.55),(3.5,.9),-.65);curly(a,(.5,.83),(.48,.3),-.7);flow(a,(5,.1),(6.6,.1),'C alkylation');base(a,(8,.1),n=True,carbonyl=False,alkyl=True);finish(a,(-1.1,11),(-1.35,1.75),'2. Enamine carbon attacks BrCH₂CN; bromide leaves')
a=axs[2];base(a,(.5,0),n=True,carbonyl=False,alkyl=True);atom(a,(-1.25,.9),'H₂O:');curly(a,(-.85,.8),(.4,.1),-.2);curly(a,(.55,.45),(.57,.9),-.65);flow(a,(3.2,0),(5.2,0),'H⁺ transfers; C–N cleavage');base(a,(7,0),carbonyl=True,alkyl=True);atom(a,(10,.2),'+ HN(Pyr)');finish(a,(-2,11.5),(-1.4,1.4),'3. Hydrolysis restores the ketone')
save(fig,'paper-1-enamine-alkylation.png')
