"""An original two-relation factor-base example for N=77.

Output goes to CWD; environment/dependencies are specified in pyproject.toml.
"""
from pathlib import Path
from math import gcd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

assert pow(13, 2, 77) == 15 and pow(40, 2, 77) == 60
X, Y = 13*40 % 77, 30
assert X == 58 and pow(X,2,77) == pow(Y,2,77)
assert (gcd(X-Y,77), gcd(X+Y,77)) == (7,11)
fig, axes = plt.subplots(1, 2, figsize=(10.6, 4.7), dpi=120, facecolor='white', gridspec_kw={'width_ratios':[1.05,1]})
for ax in axes: ax.axis('off'); ax.set_facecolor('white')
ax = axes[0]; ax.set_title('Record exponents over the base (2, 3, 5)', fontsize=13, pad=18)
data = [['13² mod 77 = 15', '0', '1', '1'], ['40² mod 77 = 60', '2', '1', '1'], ['Sum of exponents', '2', '2', '2'], ['Sum modulo 2', '0', '0', '0']]
table=ax.table(cellText=data, colLabels=['Relation / combination','2','3','5'], cellLoc='center', colWidths=[0.64,0.12,0.12,0.12], bbox=[0,0.30,1,0.63]); table.auto_set_font_size(False); table.set_fontsize(10.5)
for (row,col),cell in table.get_celld().items():
    cell.set_edgecolor('#9caab3'); cell.set_linewidth(0.8)
    if row == 0: cell.set_facecolor('#e6ebf1'); cell.get_text().set_fontweight('bold')
    elif row in [3,4]: cell.set_facecolor('#dceee3')
ax.text(0.5, 0.13, '15 × 60 = 2² × 3² × 5² = 900 = 30²\nAll prime exponents become even.', ha='center', va='center', fontsize=12)
ax=axes[1]; ax.set_title('Multiply inputs and extract factors', fontsize=13, pad=18)
boxes=[('X = 13 × 40 mod 77 = 58\nY = √900 = 30',0.80),('X² ≡ Y² (mod 77)\nBoth square residues equal 53',0.49),('gcd(58 − 30, 77) = 7\ngcd(58 + 30, 77) = 11',0.18)]
for text,y in boxes: ax.text(0.5,y,text,ha='center',va='center',fontsize=12,bbox=dict(boxstyle='round,pad=0.6',facecolor='#e6eff4' if y>0.2 else '#dceee3',edgecolor='#687784'))
for lo,hi in [(0.60,0.68),(0.29,0.37)]:ax.annotate('',xy=(0.5,lo),xytext=(0.5,hi),arrowprops=dict(arrowstyle='->',linewidth=1.6,color='#687784'))
fig.text(0.5,0.025,'Even exponent sums make a square; the greatest-common-divisor step extracts factors.',ha='center',fontsize=10)
fig.subplots_adjust(left=0.035,right=0.98,top=0.88,bottom=0.13,wspace=0.16)
fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),facecolor='white');plt.close(fig)
