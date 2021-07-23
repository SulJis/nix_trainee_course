def print_dicts(data):
    """
    Prints a list of dictionaries
    """
    for dictionary in data:
        for key, val in dictionary.items():
            print(f"{key}\t{val}")
        print("-----------------------")
