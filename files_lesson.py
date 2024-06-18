import json


# with open('sw.json', 'r') as f:
#     skywalker = json.loads(f.read())
#
# print(skywalker['name'])
#
# with open('skywalker.json', 'a') as s:
#     s.writelines(json.dumps(skywalker))

# person = {'name': 'ivan', 'surname': 'ivanov',
#           'adress': {'city': 'moscow', 'street': 'red square', 'house': 1}}

def get_person():
    name = input('name')
    surname = input('surname')
    city = input('city')
    street = input('street')
    house = int(input('house'))

    adress = {'city': city, 'street': street, 'house': house}
    person = {'name': name, 'surname': surname,
              'adress': adress}
    return person


def save_person(person):
    old = read_person()


    try:
        old['people'].append(person)
    except KeyError:
        old = {'people': []}
        old['people'].append(person)

    with open('people.json', 'w') as people:
        people.write(json.dumps(old, indent=4))


def read_person():
    with open('people.json', 'r') as f:
        people = f.read()
        people_dict = json.loads(people)
    return people_dict


# def read_person_old():
#     res = []
#     with open('people.json', 'r') as f:
#         people = f.readlines()
#         for human in people:
#             person = json.loads(human)
#             res.append(person)
#     return res


if __name__ == '__main__':
    person = get_person()
    save_person(person)
    print(read_person())
