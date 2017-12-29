from collections import Iterator

"""迭代"""

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)

for ch in 'ABC':
    print(ch)

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)

"""列表生成式"""

print(list(range(1, 11)))

L = []
for x in range(1, 11):
    L.append(x * x)
print(L)

print([x * x for x in range(1, 11)])

print([x * x for x in range(1, 11) if x % 2 == 0])

print([m + n for m in 'ABC' for n in 'XYZ'])

d = {'x': 'A', 'y': 'B', 'z': 'C'}

for k, v in d.items():
    print(k, '=', v)

L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])

"""生成器"""

g = (x * x for x in range(10))
for x in g:
    print(x)

"""迭代器"""

print(isinstance((x for x in range(10)), Iterator))
