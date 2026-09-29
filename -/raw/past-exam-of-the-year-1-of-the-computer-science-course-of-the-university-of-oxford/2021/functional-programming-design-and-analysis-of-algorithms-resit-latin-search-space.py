from pathlib import Path
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ns=list(range(1,8))
naive=[n*n*math.log10(n) for n in ns]
permuted=[n*math.lgamma(n+1)/math.log(10) for n in ns]
assert 4**16==4294967296 and math.factorial(4)**4==331776
fig,ax=plt.subplots(figsize=(7.6,4.0),dpi=100,facecolor='white')
ax.set_facecolor('white')
ax.plot(ns,naive,'o-',label=r'Arbitrary rows: $n^{n^2}$',color='#2166ac')
ax.plot(ns,permuted,'s-',label=r'Permutation rows: $(n!)^n$',color='#d6604d')
ax.set_xlabel('Order n');ax.set_ylabel('log10(number of candidates)')
ax.set_xticks(ns);ax.grid(alpha=.22)
ax.set_title('Latin-square generation grows before filtering',fontsize=13,pad=12)
ax.annotate('4.29 billion',xy=(4,naive[3]),xytext=(2.9,naive[3]+8),arrowprops={'arrowstyle':'->','color':'#2166ac'},fontsize=10)
ax.legend(loc='upper left',frameon=False)
fig.tight_layout();fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),facecolor='white',transparent=False)
