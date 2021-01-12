from _multiprocessing import send

import plotting
import readingcsv


def user_input_switch():
    txt_input = input("Welcome to this ASN_BANK application!\n"
                      "Option 1. Enter a csv file_name to scan\n"
                      "Option 2. Create a new group with search queries\n"
                      "Option 3. Print all search queries\n"    # Still in progress
                      "Option 4. Print this message again\n"
                      "Enter a number: ")
    return input_switch(txt_input)


def input_switch(input_arg):
    if input_arg == "1":
        readingcsv.ask_csv_file()
        return False
    elif input_arg == "2":
        plotting.plot_histo(readingcsv.global_expense_value_dictionary)
        return False
    elif input_arg == "4":
        user_input_switch()
        return False
    else:
        print("default, exiting program..")
        return True


if __name__ == '__main__':
    while True:
        if user_input_switch():
            break
    # file names: resources/0708742548_28122020_215932.csv
