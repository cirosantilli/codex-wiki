"""Original base-pair maps, checked against the two specified sequences."""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
import matplotlib.pyplot as plt
import numpy as np
from tools.chemistry_diagram import *
fig,axs=plt.subplots(3,1,figsize=(10,7.6),layout='constrained',facecolor='white')
s='TCGACTCAACAGTCG';rc=s.translate(str.maketrans('ACGT','TGCA'))[::-1];assert rc=='CGACTGTTGAGTCGA'
a=axs[0];top='CGACT';bottom='GCTGA'
for i,(u,v) in enumerate(zip(top,bottom)):
 atom(a,(i,1),u,color=BLUE);atom(a,(i,0),v,color=BLUE);bond(a,(i,.7),(i,.3),style='--',lw=1)
atom(a,(-1,1),'5′ T');atom(a,(-1,0),'3′');a.text(5,.9,'C',fontsize=12);a.text(5.7,.6,'A',fontsize=12);a.text(5.7,.1,'A',fontsize=12);a.text(5,-.25,'C',fontsize=12);a.plot([4.4,4.8,5.5,5.5,4.8,4.4],[1,1.25,.9,0,-.45,0],color='0.65');finish(a,(-2,14),(-.8,1.8),'Monomeric hairpin: five pairs, CAAC loop, one dangling T')
a=axs[1];top='CGACTCAACAGTCG';bottom=top[::-1]
for i,(u,v) in enumerate(zip(top,bottom)):
 atom(a,(i,1),u,color=BLUE);atom(a,(i,0),v,color=GREEN)
 if i<5 or i>=9:bond(a,(i,.7),(i,.3),style='--',lw=1)
 else:a.add_patch(plt.Rectangle((i-.44,-.3),.88,1.6,color='0.9',zorder=0))
atom(a,(-1,1),'5′ T');atom(a,(-1,0),'3′');atom(a,(14,1),'3′');atom(a,(14,0),'T 5′');finish(a,(-2,15),(-.8,1.8),'Self-duplex: two paired arms and a central mismatch/bubble region')
a=axs[2];bottom=s.translate(str.maketrans('ACGT','TGCA'))
for i,(u,v) in enumerate(zip(s,bottom)):
 atom(a,(i,1),u,color=BLUE);atom(a,(i,0),v,color=GREEN);bond(a,(i,.7),(i,.3),style='--',lw=1)
atom(a,(-1,1),'5′');atom(a,(-1,0),'3′');atom(a,(15,1),'3′');atom(a,(15,0),'5′');finish(a,(-2,16),(-.8,1.8),'Complementary heteroduplex: all fifteen base pairs')
save(fig,'paper-1-dna-states.png')
