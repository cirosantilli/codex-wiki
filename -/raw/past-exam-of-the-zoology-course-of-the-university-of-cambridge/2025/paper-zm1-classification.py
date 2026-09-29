"""Original ancestry schematic; Python 3.14, matplotlib 3.10.

Run from the desired output directory. Branch lengths are illustrative.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

TREE = {
    'Amniota': ('Mammals', 'Sauropsida'),
    'Sauropsida': ('Lepidosaurs', 'TurtleArchosaur'),
    'TurtleArchosaur': ('Turtles', 'Archosauria'),
    'Archosauria': ('Crocodilians', 'Birds'),
}
LEAVES = ['Mammals', 'Lepidosaurs', 'Turtles', 'Crocodilians', 'Birds']
X = {'Amniota': 0, 'Sauropsida': 0.8, 'TurtleArchosaur': 1.6, 'Archosauria': 2.4}
Y = {name: 4-i for i, name in enumerate(LEAVES)}

def position(node):
    if node in TREE:
        Y[node] = sum(position(ch) for ch in TREE[node])/2
    return Y[node]

position('Amniota')

def descendants(node):
    result = {node}
    for ch in TREE.get(node, ()):
        result |= descendants(ch)
    return result


def main():
    fig, axes = plt.subplots(1, 3, figsize=(13.2, 5.1), layout='constrained')
    panels = [
        ('Monophyletic', '#167248', descendants('Archosauria'), 'Archosauria: ancestry + all descendants'),
        ('Paraphyletic', '#b46b14', descendants('Sauropsida')-{'Birds'}, 'Traditional reptiles, excluding birds'),
        ('Polyphyletic', '#255caa', {'Mammals', 'Birds'}, 'Selected endotherms: mammals + birds'),
    ]
    for ax, (title, color, selected, subtitle) in zip(axes, panels):
        for parent, children in TREE.items():
            for child in children:
                child_x = X.get(child, 3.2)
                included = parent in selected and child in selected
                ax.plot([X[parent], X[parent], child_x], [Y[parent], Y[child], Y[child]],
                        color=color if included else '#b6bec5', lw=3 if included else 1.6,
                        solid_capstyle='round', zorder=1)
        for node in TREE:
            ax.scatter(X[node], Y[node], s=38, color=color if node in selected else '#b6bec5', zorder=3)
        for leaf in LEAVES:
            ax.scatter(3.2, Y[leaf], s=64, color=color if leaf in selected else '#b6bec5', zorder=3)
            ax.text(3.38, Y[leaf], leaf, va='center', fontsize=10,
                    color=color if leaf in selected else '#616a73')
        ax.text(0, -.7, subtitle.replace(': ', ':\n'), fontsize=10, color=color, va='top')
        ax.set_title(title, fontsize=14, color=color, weight='bold', pad=20)
        ax.set(xlim=(-.15, 5.4), ylim=(-1.45, 4.5))
        ax.axis('off')
    for ax, note in zip(axes, ('Ancestor and complete subtree selected',
                              'Ancestry retained; one branch excluded',
                              'Connecting ancestry excluded')):
        ax.text(0, 4.55, note, fontsize=9, color='#616a73')
    fig.suptitle('One ancestry, three membership rules', fontsize=17, weight='bold')
    fig.savefig('paper-zm1-classification.png', dpi=150, facecolor='white')
    plt.close(fig)

if __name__ == '__main__':
    main()
