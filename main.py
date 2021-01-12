import plotting
import readingcsv
import query


def user_input_switch():
    txt_input = input("Welcome to this ASN_BANK application!\n"
                      "Option 1. Enter a csv file_name to scan\n"
                      "Option 2. Read csv in memory\n"
                      "Option 3. Plot current data\n"
                      "Option 4. Create search query\n"
                      "Option 5. Show all search queries\n"
                      "Option 9. Print this message again\n"
                      "Enter a number: ")
    return input_switch(txt_input)


def input_switch(input_arg):
    if input_arg == "1":
        readingcsv.ask_csv_file()
        return False
    elif input_arg == "2":
        readingcsv.read_csv()
    elif input_arg == "3":
        plot_name = input("What is the name of the fig?: ")
        plotting.plot_histo(readingcsv.get_global_expense_value_dictionary(), plot_name)
        return False
    elif input_arg == "4":
        query.create_query()
    elif input_arg == "5":
        query.read_queries()
    elif input_arg == "9":
        return False
    else:
        print("default, exiting program..")
        return True


if __name__ == '__main__':
    # file names: resources/0708742548_28122020_215932.csv
    while True:
        print("======================")
        if user_input_switch():
            break
        print("\n\n")

