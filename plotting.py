import matplotlib.pyplot as plt
import pandas as pd


def plot_histo(dictionary_to_plot, name_of_plot):
    dataframe = pd.DataFrame({'keys': dictionary_to_plot.keys(), 'values': dictionary_to_plot.values()})
    dataframe_sorted = dataframe.sort_values(['values'])
    print(dataframe_sorted)

    plt.figure(figsize=(18, 9))
    plt.bar('keys', 'values', data=dataframe_sorted)

    # set figure details
    plt.xlabel("keys")
    plt.ylabel("values")
    plt.xticks([])
    fig_name = "output/" + name_of_plot + ".png"
    print(fig_name)
    plt.savefig(fig_name)
