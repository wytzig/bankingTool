global global_csv_name
global global_expense_value_dictionary


def get_global_expense_value_dictionary():
    return global_expense_value_dictionary


def ask_csv_file():
    txt = input("Give in the name of the file, including the dir as seen from the root of this project: ")
    global global_csv_name
    global_csv_name = txt
    print("using: ", global_csv_name)


def read_csv():
    result = {}                         # Init values
    global global_csv_name
    cum_changed_value = 0               # Init value for total calculation
    file = open(global_csv_name)        # Open file
    try:
        for line in file:                # Process file line
            line_list = line.split(",")
            other_account_column = line_list[17]
            changed_amount_column = float(line_list[10])
            result[other_account_column] = changed_amount_column        # Create dic with x the name and y the value
            cum_changed_value += changed_amount_column                  # Add to cum number
    finally:
        file.close()
        result["total"] = cum_changed_value
        print(result)
        print("total is: ", result["total"])   # Total value based on the search query
        global global_expense_value_dictionary
        global_expense_value_dictionary = result
