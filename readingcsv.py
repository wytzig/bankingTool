global global_csv_name
global global_expense_value_dictionary


def ask_csv_file():
    txt = input("Give in the name of the file, including the dir as seen from the root of this project: ")

    global global_csv_name
    global_csv_name = txt
    print("using: ", global_csv_name)


def read_csv(search_query):
    result = {}
    global global_csv_name
    file = open(global_csv_name)
    # Set total values for later injection, search query here is the position in the dic..
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
        global global_expense_value_dictionary
        global_expense_value_dictionary = result
