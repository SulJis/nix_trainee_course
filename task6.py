from utils import print_dicts

list_ = [
    {'name': 'Alex', 'age': 25},
    {'name': 'Oleg', 'age': 23},
    {'name': 'Anna', 'age': 32},
    {'name': 'Igor', 'age': 50},
    {'name': 'Anton', 'age': 17},
]

filtered_list = list(filter(lambda x: x["age"] >= 18 and x["age"] <= 30, list_))
print("Filtered people:")
print_dicts(filtered_list)
