import matplotlib.pyplot as plt
import pandas as pd


global global_csv_name
global global_expense_value_dictionary


def ask_csv_file():
    txt = input("give in the name of the file, including the dir as seen from the root of this project: ")

    global global_csv_name
    global_csv_name = txt
    print("using: ", global_csv_name)


def read_csv(search_query):
    result = {}
    file = open(global_csv_name)
    # Set total values for later injection
    cum_changed_value = 0
    name_cum_changed_value = search_query
    try:
        for line in file:
            # Process file line
            line_list = line.split(",")
            other_account_column = line_list[17]
            changed_amount_column = float(line_list[10])
            result[other_account_column] = changed_amount_column
            # Add to cum number
            cum_changed_value += changed_amount_column
    finally:
        file.close()
        result[name_cum_changed_value] = cum_changed_value
        print(result)
        print(result[name_cum_changed_value])
        return result


def plot_histo(dictionary_to_plot, search_query):
    dataframe = pd.DataFrame({'keys': dictionary_to_plot.keys(), 'values': dictionary_to_plot.values()})
    dataframe_sorted = dataframe.sort_values(['values'])
    print(dataframe_sorted)
    # print(dataframe_sorted.keys(search_query))

    plt.figure(figsize=(18, 9))
    plt.bar('keys', 'values', data=dataframe_sorted)

    # set figure details
    plt.xlabel("keys")
    plt.ylabel("values")
    plt.xticks([])
    plt.show()


def user_input_switch():
    txt_input = input("Welcome to this ASN_BANK application!\n"
                      "Option 1. Enter a csv file_name to scan\n"
                      "Option 2. Create a new group with search queries\n"
                      "Option 3. Print all search queries\n"
                      "Option 4. Print this message again\n"
                      "Enter a number: ")
    input_switch(txt_input)


def input_switch(input_arg):
    switcher = {
        1: ask_csv_file()
    }
    func = switcher.get(input_arg, lambda: "invalid option selected!")
    func()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # csv_dic = read_csv("resources/0708742548_28122020_215932.csv", "totaal")
    # plot_histo(csv_dic, "totaal")
    user_input_switch()

