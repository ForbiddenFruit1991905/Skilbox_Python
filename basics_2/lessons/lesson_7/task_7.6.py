names = ['A', 'B', 'C']
ages = [20, 30, 40]

people = zip(names, ages)
for i_person in people:
    print(i_person)

people_2 = dict(zip(names, ages))
print(people_2)

people_3 = list(zip(names, ages))
print(people_3)

people_4 = {
    i_name: i_age + 10
    for i_name, i_age in zip(names, ages)
}
print(people_4)