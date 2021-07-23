list1 = ["Oleg", "Vasya", "Anna"]
list2 = ["Ivanov", "Sidorov", "Petrova"]
full_names = list(zip(list1, list2))
for person in full_names:
    print(person)
