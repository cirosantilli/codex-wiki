"""Generate security-2015-mirror-mask.png in the current working directory.

Tested with Python 3.14.4, Matplotlib 3.10.7 and NumPy 2.3.5.
The example illustrates the exact mirror-parity invariant, not empirical security.
"""
import os
os.environ.setdefault('MPLCONFIGDIR', '/tmp/security-2015-matplotlib')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

k = [1, 0, 0, 0, 1, 0]
x = [1, 0, 1, 1, 0, 0]
r = k[::-1]
s = [a ^ b for a, b in zip(k, r)]
c = [a ^ b for a, b in zip(x, s)]
assert s == s[::-1]
assert [x[i] ^ x[5-i] for i in range(3)] == [c[i] ^ c[5-i] for i in range(3)]
colors = ['#d6eee9', '#dce9fa', '#ffebcc', '#ffebcc', '#dce9fa', '#d6eee9']
fig = plt.figure(figsize=(9.2, 5.0), dpi=120, facecolor='white')
ax = fig.add_axes([0, 0, 1, 1])
ax.set(xlim=(0, 9.2), ylim=(0, 5.0))
ax.axis('off')
ax.text(4.6, 4.65, 'A random key can still produce a structured mask', ha='center', fontsize=16, weight='bold')
ax.text(4.6, 4.26, 'Equal mask bits at mirror positions cancel in the pair parity', ha='center', fontsize=11, color='#404040')
rows = [(r'Key $k$', k), (r'Reversed key $\mathrm{rev}(k)$', r),
        (r'Mask $s=k\oplus\mathrm{rev}(k)$', s), (r'Plaintext $x$', x),
        (r'Ciphertext $c=x\oplus s$', c)]
for j, (label, bits) in enumerate(rows):
    y = 3.65 - j * .56
    ax.text(3.3, y, label, ha='right', va='center', fontsize=12)
    for i, bit in enumerate(bits):
        ax.add_patch(Rectangle((3.6 + i * .65, y - .22), .55, .44,
                               facecolor=colors[i], edgecolor='#666666', linewidth=.7))
        ax.text(3.875 + i * .65, y, str(bit), ha='center', va='center', fontsize=14)
for i in range(6):
    ax.text(3.875 + i * .65, 3.99, str(i+1), ha='center', fontsize=10, color='#555555')
ax.text(4.6, .62, r'$x_1\oplus x_6=c_1\oplus c_6=1\qquad x_2\oplus x_5=c_2\oplus c_5=0\qquad x_3\oplus x_4=c_3\oplus c_4=0$', ha='center', fontsize=12)
ax.text(4.6, .20, 'These three plaintext parities are visible without the key.', ha='center', fontsize=11, weight='bold')
fig.savefig('security-2015-mirror-mask.png', dpi=120, facecolor='white', transparent=False, metadata={'Software': 'security-2015-mirror-mask.py'})
plt.close(fig)
