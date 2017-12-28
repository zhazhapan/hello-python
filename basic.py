print("hello python")
print('\\\t\\')
print(r'\\\t\\')
print('''line1
line2
line3''')
print(not (True and False or True))

a = "variable"
print(a)
a = 1111
print(a)
print(10 / 3)
print(10 // 3)

print("包含中文")
print(ord('a'))
print(ord('四'))
print(chr(66))
print(chr(33333))
print('\u4e2d\u6587')
x = b'ABC'
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
print(len(x))
print('Hi, %s, you have $%d.' % ('Michael', 1000000))
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))
print("AAbbssA".replace('A', 'zzzzzzzzzzzzzzzzzzzz'))

classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
print(len(classmates))
print(classmates[0])
print(classmates[1])
print(classmates[2])
print(classmates[-1])
print(classmates[-2])
print(classmates[-3])
classmates.append('Adam')
print(classmates)
classmates.pop()
print(classmates)
classmates.pop(0)
print(classmates)

t = (1, 2)
print(t)
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)

age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

names = ['Michael', 'Bob', 'Tracy']
names.sort()
for name in names:
    print(name)

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)

print(list(range(99)))

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

n = 0
while n <= 100:
    n = n + 1
    if n > 10:
        break
    else:
        continue
print('END')

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d)
print(d['Bob'])
print('Tracy' in d)
print(d.get('Michael'))

# 不重复
s = set([1, 2, 3])
print(s)
s2 = set([2, 3, 4, 5])
print(s & s2)
print(s | s2)
s.remove(1)
print(s)
