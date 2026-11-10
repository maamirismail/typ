import matplotlib.pyplot as plt

def draw(comparators, n_wires, path):
    """"
    draws comparator network diagram and saves it to path
    """
    fig, ax = plt.subplots(figsize=(6,2.5))
    for i in range(n_wires):
        ax.hlines(y=i, xmin=0, xmax=len(comparators)+1, color='black', linewidth=1.5)
        ax.text(-0.2, i, f'Wire {i}', ha='right', verticalalignment='center', fontsize=10)
    for step, (i, j) in enumerate(comparators, start=1):
        ax.vlines(x=step, ymin=i, ymax=j, color='red', linewidth=2)
        ax.plot([step, step], [i, j], color='red', linewidth=2)
    ax.set_ylim(n_wires - 0.5, -0.5)
    ax.set_xlim(-0.5, len(comparators) + 1.5)
    ax.axis('off')
    fig.savefig(path, bbox_inches='tight', dpi=300)

if __name__ == "__main__":
    draw([(0, 1), (1, 2), (0, 1)], 3, "results/median3_network.png")