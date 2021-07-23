from utils import print_dicts

people = [
    {
        "name": "Oleg",
        "age": 23
    },
    {
        "name": "Vasya",
        "age": 19
    }
]

print("Unsorted people:")
print_dicts(people)

sorted_people = sorted(people, key=lambda x: x["age"])

print("\nSorted people:")
print_dicts(sorted_people)
