"""Schematic source levels. Python 3.14, matplotlib 3.10.
Writes only 2015-charmonium-levels.png in the current directory.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig,ax=plt.subplots(figsize=(8.6,5.1),facecolor='white')
levels=[(.45,3.00,r'$\eta_c:\ 1\,{}^1S_0$',r'$0^{-+}$'),(1.65,3.06,r'$J/\psi:\ 1\,{}^3S_1$',r'$1^{--}$'),(.45,3.65,r'$\eta_c(2S):\ 2\,{}^1S_0$',r'$0^{-+}$'),(1.65,3.69,r'$\psi(2S):\ 2\,{}^3S_1$',r'$1^{--}$'),(2.95,3.525,r'$h_c:\ 1\,{}^1P_1$',r'$1^{+-}$'),(4.15,3.45,r'$\chi_{c0}:\ 1\,{}^3P_0$',r'$0^{++}$'),(5.35,3.51,r'$\chi_{c1}:\ 1\,{}^3P_1$',r'$1^{++}$'),(6.55,3.58,r'$\chi_{c2}:\ 1\,{}^3P_2$',r'$2^{++}$')]
for x,y,label,jpc in levels:
    color='#236b8e' if jpc in (r'$0^{-+}$',r'$0^{++}$',r'$2^{++}$') else '#343434'
    ax.plot([x-.38,x+.38],[y,y],lw=3,color=color);ax.text(x,y+.027,label,ha='center',fontsize=10);ax.text(x,y-.048,jpc,ha='center',fontsize=11,color=color)
ax.set(xlim=(-.05,7.05),ylim=(2.9,3.85),ylabel='Approximate source diagram position (GeV)');ax.set_xticks([]);ax.spines[['top','right','bottom']].set_visible(False)
ax.set_yticks([3,3.2,3.4,3.6,3.8]);ax.grid(axis='y',alpha=.18);ax.set_title('Charmonium: radial, orbital and spin assignments',pad=12)
fig.text(.54,.015,'Blue levels allow two real photons. Heights are schematic, not precision masses.',ha='center',fontsize=9)
fig.tight_layout(rect=(0,.04,1,1));fig.savefig(Path('2015-charmonium-levels.png'),dpi=140,facecolor='white')
