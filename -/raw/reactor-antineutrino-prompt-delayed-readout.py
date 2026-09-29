"""Original functional reactor-antineutrino readout, not a historical apparatus reproduction."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,Circle
fig,(a,b)=plt.subplots(1,2,figsize=(12.4,6),gridspec_kw={'width_ratios':[1.2,1]});fig.patch.set_facecolor('white')
fig.suptitle('One reaction, two detection times',fontsize=18,y=.97)
a.set(xlim=(-1.1,6.7),ylim=(-.8,6.1));a.axis('off')
for y,label,col in [(4.5,'Scintillator I','#d5e8f0'),(3.6,r'Water target A + CdCl$_2$','#f2e9ca'),(2.7,'Scintillator II (shared)','#d5e8f0'),(1.8,r'Water target B + CdCl$_2$','#f2e9ca'),(.9,'Scintillator III','#d5e8f0')]:
 a.add_patch(Rectangle((.15,y),5.3,.65,facecolor=col,edgecolor='#526b75',lw=1.5));a.text(5.23,y+.325,label,ha='right',va='center',fontsize=10)
a.annotate('',xy=(.95,3.93),xytext=(-.8,5.75),arrowprops={'arrowstyle':'->','color':'#315f9c','lw':2});a.text(-.75,5.8,r'Reactor $\bar\nu_e$',fontsize=12)
a.add_patch(Circle((1.0,3.93),.08,color='#a3364c'))
a.annotate('',xy=(1.9,3.93),xytext=(1.15,3.93),arrowprops={'arrowstyle':'->','color':'#ae7922','lw':2});a.text(2.02,3.93,r'$n$',va='center',fontsize=13)
a.annotate('',xy=(.5,4.78),xytext=(1.0,4.03),arrowprops={'arrowstyle':'->','color':'#a3364c','lw':2})
a.annotate('',xy=(1.55,3.02),xytext=(1.0,3.83),arrowprops={'arrowstyle':'->','color':'#a3364c','lw':2})
a.text(.8,4.17,r'$e^+$',ha='right',fontsize=11,color='#a3364c')
a.text(2.8,.15,'Two target layers, three detector layers.\nSignal arrows show mechanisms, not measured tracks.',ha='center',fontsize=10,linespacing=1.5)
b.set(xlim=(-.3,6.2),ylim=(-.5,5.6));b.axis('off');b.set_title('Correlate detector pulses',fontsize=14,pad=15)
b.annotate('',xy=(5.9,1.7),xytext=(.1,1.7),arrowprops={'arrowstyle':'->','lw':1.5});b.text(6.0,1.7,'Time',fontsize=11,va='center')
b.plot([.3,.8,.8,.95,.95,2.3,2.3,2.45,2.45,5.5],[1.7,1.7,3.2,3.2,1.7,1.7,2.65,2.65,1.7,1.7],color='#a3364c',lw=2)
b.text(.85,3.65,r'Prompt $e^+$ signal',ha='center',fontsize=12)
b.text(3.6,3.25,'Delayed capture\ngamma-ray signal',ha='center',fontsize=12,linespacing=1.4)
b.annotate('',xy=(4.8,1.05),xytext=(.88,1.05),arrowprops={'arrowstyle':'<->','color':'#315f9c','lw':1.6});b.text(2.85,.6,'Accepted delay window W',ha='center',fontsize=11)
b.text(2.8,4.85,r'$\bar\nu_e+p\ \to\ e^++n$',ha='center',fontsize=16)
b.text(2.8,-.15,'Pulse heights and delays require calibration.\nUnrelated pulses can form accidental pairs.',ha='center',fontsize=11,linespacing=1.45)
fig.text(.5,.03,'Functional teaching schematic, not to scale. Pulse heights and spacings are illustrative, not historical measurements.',ha='center',fontsize=10,color='#555')
fig.subplots_adjust(left=.035,right=.97,top=.86,bottom=.13,wspace=.14)
fig.savefig(Path(__file__).with_suffix('.png').name,dpi=110,facecolor='white');plt.close(fig)
