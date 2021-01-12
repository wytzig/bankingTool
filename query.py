import json
import ast


filename = "resources/queries"


def create_query():
    global filename
    with open(filename, "a") as file:
        name = input("What is the name (key) of the query?: ")
        values_input = input("What are the search values? (separate by comma): ")

        list_of_values = values_input.split(",")
        query = {name: list_of_values}
        file.write(json.dumps(query) + "\n")
        print("appended the following line to database: ", query)


def read_queries():
    global filename
    with open(filename, "r") as file:
        try:
            for line in file:
                file_line_dic = ast.literal_eval(line)
                print(file_line_dic)
        finally:
            print("finished reading")
