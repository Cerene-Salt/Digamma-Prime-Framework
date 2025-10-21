import matplotlib.pyplot as plt

def plot_group_divergence(groups, metric_values, metric_name='φ'):
    """
    Plots symbolic divergence values for each group.
    groups: list of group names
    metric_values: list of divergence values (floats)
    metric_name: 'φ', 'δφ', or 'ϝ*'
    """
    plt.figure(figsize=(8, 5))
    bars = plt.bar(groups, metric_values, color='steelblue')
    plt.title(f'Symbolic Divergence by Group ({metric_name})')
    plt.ylabel(f'{metric_name} Value')
    plt.xlabel('Groups')
    plt.ylim(0, max(metric_values) * 1.2)

    # Annotate bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, height + 0.05, f'{height:.2f}', ha='center')

    plt.tight_layout()
    plt.show()
