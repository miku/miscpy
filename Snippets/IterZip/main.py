
data = list(range(10))

i1 = iter(data)
i2 = iter(data)

print(list(zip(i1, i2)))