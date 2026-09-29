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

fig,axs=plt.subplots(3,1,figsize=(10,7));fig.subplots_adjust(hspace=.55,top=.92,bottom=.04)
rows=[('A · spectrum 4',[('Et CH₃','OCH₂','7 Hz'),('alkene CH₃','vinyl CH','1–1.5 Hz (each methyl)')]),
('C · spectrum 5',[('Et CH₃','OCH₂','7 Hz'),('OCH₂ Hₐ','OCH₂ Hᵦ','9–10 Hz'),('acetal CH','≡CH','2 Hz')]),
('B · spectrum 6',[('terminal H (trans)','vinyl CH','17 Hz'),('terminal H (cis)','vinyl CH','10 Hz'),('terminal Hₐ','terminal Hᵦ','1–2 Hz'),('vinyl CH','OCH₂','6 Hz'),('butanoate neighbors','CH₂ / CH₃','7–8 Hz')])]
for ax,(title,pairs) in zip(axs,rows):
 ax.set(xlim=(0,10),ylim=(-.1,len(pairs)));ax.axis('off');ax.set_title(title,loc='left',fontsize=13,color=BLUE)
 for y,(a,b,j) in enumerate(pairs):
  y=len(pairs)-1-y;ax.text(.2,y,a,va='center',fontsize=11);ax.text(9.8,y,b,ha='right',va='center',fontsize=11)
  ax.annotate('',(7.5,y),(3,y),arrowprops={'arrowstyle':'<->','color':BLUE});ax.text(5.25,y+.13,j,ha='center',fontsize=10,color=ORANGE)
fig.suptitle('Scalar-coupling partners · approximate J values',fontsize=15)
save(fig,Path(__file__).with_suffix('.png').name)
