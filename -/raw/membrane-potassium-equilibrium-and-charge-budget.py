"""Two independent chosen membrane models; Python 3.14, matplotlib 3.10.7.

Run from _media. No physiological measurements or inferred geometry.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

R, T, F = 8.314, 310.0, 96485.0
C, VM = 5e-12, -.070
E_CHARGE, N_A = 1.602176634e-19, 6.02214076e23
C_IN, VOLUME_L = 140.0, 1e-12

def equilibrium_voltage(c_out_mM):
    return R*T/F*np.log(np.asarray(c_out_mM)/C_IN)

q = C*VM
excess = abs(q)/E_CHARGE
inventory = (C_IN/1000)*VOLUME_L*N_A
fraction = excess/inventory
plt.rcParams.update({'font.family':'DejaVu Sans', 'font.size':12, 'text.color':'#213344'})
fig = plt.figure(figsize=(12,6.2), dpi=120, facecolor='white')
grid = fig.add_gridspec(1,2, left=.09,right=.98,bottom=.23,top=.81,wspace=.35)
a = fig.add_subplot(grid[0,0])
x = np.geomspace(1,280,500)
a.plot(x, 1000*equilibrium_voltage(x), color='#176b91', lw=2.5)
a.axhline(0,color='#66727a',lw=1)
a.set_xscale('log')
a.set(xlim=(1,280), ylim=(-145,30), xlabel='Outside potassium concentration (mM)', ylabel='$E_K$ (mV; inside minus outside)')
a.set_xticks([1,5,10,50,140,280], ['1','5','10','50','140','280'])
a.grid(alpha=.18)
a.set_title('A  Only K⁺ permeates, passive equilibrium', fontsize=13,pad=18)
for co in (5,10,140):
    a.plot(co,1000*equilibrium_voltage(co),'o',color='#b35c12',markersize=7)
a.annotate('5 mM: −89.01 mV',xy=(5,1000*equilibrium_voltage(5)),xytext=(1.25,-123),fontsize=11,arrowprops={'arrowstyle':'->','color':'#b35c12'})
a.annotate('10 mM: −70.50 mV',xy=(10,1000*equilibrium_voltage(10)),xytext=(15,-101),fontsize=11,arrowprops={'arrowstyle':'->','color':'#b35c12'})
a.annotate('140 mM: 0 mV',xy=(140,0),xytext=(17,15),fontsize=11,arrowprops={'arrowstyle':'->','color':'#b35c12'})
a.text(.03,.97,'Chosen: $T=310$ K, inside 140 mM',transform=a.transAxes,va='top',fontsize=10)
a.spines[['top','right']].set_visible(False)

b = fig.add_subplot(grid[0,1]); b.axis('off'); b.set(xlim=(0,10),ylim=(0,10))
b.set_title('B  Independent capacitor charge budget',fontsize=13,pad=18)
b.text(5,9.7,'Chosen: $C=5$ pF, $V_m=-70$ mV',ha='center',fontsize=12)
b.add_patch(Rectangle((4.65,7.1), .7,1.7,facecolor='#ead4dd',edgecolor='#87546c'))
for y in (7.45,8.3):
    b.text(4.1,y,'−',ha='center',va='center',fontsize=21,color='#176b91')
    b.text(5.9,y,'+',ha='center',va='center',fontsize=21,color='#b35c12')
b.text(1.8,7.9,'Inside\n$Q=CV_m$',ha='center',va='center',fontsize=12)
b.text(8.1,7.9,'Outside\n$-Q$',ha='center',va='center',fontsize=12)
b.text(5,6.6,'Inner excess: $Q=-3.5\\times10^{-13}$ C',ha='center',fontsize=12)
b.text(5,5.55,f'{excess/1e6:.2f} million\nmonovalent charge equivalents',ha='center',va='center',fontsize=15,color='#176b91',linespacing=1.4)
b.text(5,3.95,'Compare chosen reservoir: 1 pL, 140 mM K⁺',ha='center',fontsize=11)
b.text(5,3.0,f'{inventory/1e9:.1f} billion potassium ions',ha='center',fontsize=14)
b.text(5,1.6,f'Ratio = {fraction:.2e}\n= {fraction*100:.5f}% ≈ 1 in {1/fraction:,.0f}',ha='center',va='center',fontsize=14,linespacing=1.5,bbox={'facecolor':'#edf6fa','edgecolor':'none','pad':10})
fig.suptitle('Selective-ion equilibrium and small charge separation',fontsize=18,y=.96)
fig.text(.5,.89,'All inputs chosen for illustration; the panels are separate models, not experimental data.',ha='center',fontsize=11)
fig.text(.5,.035,'The −70 mV capacitor example is independent of the −89.01 mV equilibrium example.\nCharge imbalance is compared with a reservoir inventory; no cell geometry is inferred.',ha='center',fontsize=11,linespacing=1.5)
fig.savefig(Path(__file__).stem+'.png',facecolor='white',transparent=False)
plt.close(fig)
