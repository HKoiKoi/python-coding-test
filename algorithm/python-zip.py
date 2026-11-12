# 기본 문법
# zip(*iterables, strict=False)

names = ["shiroko", "aru", "chinatsu"]
attacks = [3878, 4209, 1706]

for name, attack in zip(names, attacks):
    print(name, attack)
    # shiroko 3878
    # aru 4209
    # chinatsu 1706

zip(names, attacks)  # <zip object at 0x1030f6540>
list(zip(names, attacks))  # [('shiroko', 3878), ('aru', 4209), ('chinatsu', 1706)]

pairs = zip(names, attacks)
list(pairs)  # [('shiroko', 3878), ('aru', 4209), ('chinatsu', 1706)]
list(pairs)  # []

ages = [16, 16, 15]

for name, attack, age in zip(names, attacks, ages):
    print(f"{name}({age}세) 공격력: {attack}")
    # shiroko(16세) 공격력: 3878
    # aru(16세) 공격력: 4209
    # chinatsu(15세) 공격력: 1706

list(zip([1, 2, 3], ["a", "b"]))  # [(1, 'a'), (2, 'b')]

# list(zip([1, 2, 3], ["a", "b"], strict=True))  # ValueError: zip() argument 2 is shorter than argument 1

from itertools import zip_longest

list(zip_longest([1, 2, 3], ["a", "b"], fillvalue="-"))  # [(1, 'a'), (2, 'b'), (3, '-')]

pairs = [("shiroko", 3878), ("aru", 4209), ("chinatsu", 1706)]

names, attacks = zip(*pairs)
print(names)  # ('shiroko', 'aru', 'chinatsu')
print(attacks)  # (3878, 4209, 1706)

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

list(zip(*matrix))  # [(1, 4), (2, 5), (3, 6)]

dict(zip(names, attacks))  # {'shiroko': 3878, 'aru': 4209, 'chinatsu': 1706}

for i, (name, attack) in enumerate(zip(names, attacks)):
    print(i, name, attack)
    # 0 shiroko 3878
    # 1 aru 4209
    # 2 chinatsu 1706

numbers = [1, 3, 6, 10]

diffs = [b - a for a, b in zip(numbers, numbers[1:])]  # [2, 3, 4]

a = [1, 2, 3]
b = [4, 5, 6]

[x + y for x, y in zip(a, b)]  # [5, 7, 9]
all(x < y for x, y in zip(a, b))  # True

sorted_pairs = sorted(zip(attacks, names), reverse=True)  # [(4209, 'aru'), (3878, 'shiroko'), (1706, 'chinatsu')]
