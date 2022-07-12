import random

c = [random.randint(1, 10) for i in range(1, 11)]
b = [random.randint(1, 10) for k in range(1, 11)]
a = set(c)
d = set(b)
print("Обьеденение: " + str(a.union(b)))
print("intersection: " + str(a.intersection(b)))
print("difference: " + str(a.difference(b)))

print("Первое множество: " + str(a))
print("Второе множество: " + str(d))

