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

fig,axs=plt.subplots(3,1,figsize=(10.5,8));fig.subplots_adjust(hspace=.42,top=.93,bottom=.04)
rows=[('A · spectrum 4',r'EtO–C(=O)–CH=C(CH$_3$)$_2$',
'Et CH₃ 1.3 (t, 3H)    OCH₂ 4.15 (q, 2H)    vinyl CH 5.7 (m, 1H)',
'alkene CH₃ groups 1.9 and 2.2 (3H each; small allylic d)'),
('B · spectrum 6',r'CH$_2$=CH–CH$_2$–O–C(=O)–CH$_2$–CH$_2$–CH$_3$',
'vinyl CH₂ 5.2–5.35 (two dd, 1H each)    vinyl CH 5.95 (ddt, 1H)',
'OCH₂ 4.6 (d, 2H)    α-CH₂ 2.3 (t, 2H)    β-CH₂ 1.65 (m, 2H)    CH₃ 0.95 (t, 3H)'),
('C · spectrum 5',r'HC≡C–CH(OCH$_2$CH$_3$)$_2$',
'≡CH 2.55 (d, 1H)    acetal CH 5.25 (d, 1H)    Et CH₃ 1.25 (t, 6H)',
'OCH₂ proton types 3.6 and 3.75 (2H each; ABX₃-type pattern)')]
for ax,(title,s,a,b) in zip(axs,rows):
 ax.axis('off');ax.set_title(title,loc='left',fontsize=13,color=BLUE);ax.text(.5,.77,s,ha='center',fontsize=16);ax.text(.5,.41,a,ha='center',fontsize=11);ax.text(.5,.10,b,ha='center',fontsize=10.6)
fig.suptitle('Derived ¹H assignments · δ / ppm (approximate)',fontsize=15)
save(fig,Path(__file__).with_suffix('.png').name)
