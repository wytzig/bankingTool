import matplotlib.pyplot as plt
import pandas as pd


def print_name(name):
    print(name)


def read_csv(file_name):
    result = {}
    file = open(file_name)
    try:
        for line in file:
            line_list = line.split(",")
            other_account_column = line_list[17]
            changed_amount_column = float(line_list[10])
            result[other_account_column] = changed_amount_column

    finally:
        file.close()
        print(result)
        return result


def plot_histo(dictionary_to_plot):
    dataframe = pd.DataFrame({'keys': dictionary_to_plot.keys(), 'values': dictionary_to_plot.values()})
    dataframe_sorted = dataframe.sort_values(['values'])
    print(dataframe_sorted)

    plt.figure(figsize=(18, 9))
    plt.bar('keys', 'values', data=dataframe_sorted)

    # set figure details
    plt.xlabel("keys")
    plt.ylabel("values")
    plt.xticks([])
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    csv_dic = read_csv("resources/0708742548_28122020_215932.csv")
    plot_histo(csv_dic)

