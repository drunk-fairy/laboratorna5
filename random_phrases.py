# Task 4.1
import random

names = ['Mary', 'Lucy', 'Tom', 'Sally', 'Peter', 'Jane', 'John']
verbs = ['loves', 'hates', 'eats', 'brings', 'buys', 'has', 'takes']
foods = ['chocolate', 'apples', 'oranges', 'candies', 'sandwiches', 'cookies', 'pineapples']

random.shuffle(names)
n = names[1]

random.shuffle(verbs)
v = verbs[1]

random.shuffle(foods)
f = foods[1]

print(n + ' ' + v + ' ' + f)

