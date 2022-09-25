import matplotlib.pyplot as plt
import numpy as np


def plot_control_variant_diff(trace, title, xlimit=60, bins=50, xlabel="% change"):
    control_farray = np.array(trace["posterior"]["control"]).flatten()
    variant_farray = np.array(trace["posterior"]["variant"]).flatten()
    diff = variant_farray - control_farray
    diff_perc = (diff / control_farray.mean()) * 100
    densities, edges = np.histogram(
        diff_perc, density=True, bins=bins, range=(-xlimit, xlimit)
    )
    densities = densities * np.diff(edges) * 100
    plt.subplots(figsize=(16, 8))
    for i in range(edges.shape[0]):
        if edges[i] >= 0:
            break

    plt.bar(
        edges[:i],
        densities[:i],
        width=np.diff(edges[: i + 1]),
        color="orange",
        edgecolor="red",
        align="edge",
    )
    plt.bar(
        edges[i:-1],
        densities[i:],
        np.diff(edges[i:]),
        color="lightgreen",
        edgecolor="green",
        align="edge",
    )
    plt.axvline(0, color="black", linestyle="--")
    plt.axvline(
        diff_perc.mean(),
        color="blue",
        linestyle="-",
        label=f"mean change ({diff_perc.mean():.2f}%)",
    )
    plt.xlabel(xlabel)
    plt.ylabel("% chance")
    plt.title(title)
    plt.legend(fontsize=15)
    return plt.gcf()
