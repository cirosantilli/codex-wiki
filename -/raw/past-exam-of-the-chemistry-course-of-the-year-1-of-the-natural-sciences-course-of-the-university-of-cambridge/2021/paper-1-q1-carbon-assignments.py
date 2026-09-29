"""Original solution diagram. Python 3.14 / matplotlib 3.10 / numpy 2.3.
Run from the mirrored media directory; output is written to cwd.
"""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from tools.chemistry_diagram import bond,atom,ring,curly,flow,finish,save,BLUE,ORANGE

fig,axs=plt.subplots(3,1,figsize=(10,7.2));fig.subplots_adjust(hspace=.43,top=.93,bottom=.04)
rows=[('A · spectrum 2',r'EtO–C(=O)–CH=C(CH$_3$)$_2$',
      'C=O 167     vinyl CH 116     alkene C 157',
      'OCH₂ 60     Et methyl 14     alkene methyls {28, 21}'),
      ('B · spectrum 3',r'CH$_2$=CH–CH$_2$–O–C(=O)–CH$_2$–CH$_2$–CH$_3$',
      'vinyl CH₂ 118     vinyl CH 133     OCH₂ 65     C=O 173',
      'acyl-α CH₂ 36     next CH₂ 19     terminal methyl 14'),
      ('C · spectrum 1',r'HC≡C–CH(OCH$_2$CH$_3$)$_2$',
      'terminal ≡CH 74     internal ≡C 79     acetal CH 91',
      'equivalent OCH₂ carbons 61     equivalent methyl carbons 15')]
for ax,(title,s,a,b) in zip(axs,rows):
 ax.axis('off');ax.set_title(title,loc='left',fontsize=13,color=BLUE);ax.text(.5,.77,s,ha='center',fontsize=17);ax.text(.5,.40,a,ha='center',fontsize=12);ax.text(.5,.10,b,ha='center',fontsize=12)
fig.suptitle('Derived ¹³C assignments · δ / ppm (approximate)',fontsize=15)
save(fig,Path(__file__).with_suffix('.png').name)
