from _multiprocessing import send

import plotting
import readingcsv


def user_input_switch():
    txt_input = input("Welcome to this ASN_BANK application!\n"
                      "Option 1. Enter a csv file_name to scan\n"
                      "Option 2. Create a new group with search queries\n"
                      "Option 3. Print all search queries\n"
                      "Option 4. Print this message again\n"
                      "Enter a number: ")
    input_switch(txt_input)


def set_csv_file_location():
    return readingcsv.ask_csv_file()


def exit_program():
    return print("default, exiting program..")


def input_switch(input_arg):
    program_functions = {
        1: set_csv_file_location,
        3: plotting.plot_histo,
        4: user_input_switch,
        9: exit_program
    }
    func = program_functions.get(input_arg, lambda: "exiting program..")
    print(func())


if __name__ == '__main__':
    user_input_switch()
    # file names: resources/0708742548_28122020_215932.csv
