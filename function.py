from functools import reduce
import time
import functools


def fmtime(date):
    return time.strftime('%Y-%m-%d %H:%M:%S', date)


"""map返回一个序列，可转换成list或tuple"""


def f(x):
    return x * x


r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(tuple(r))

"""reduce把结果继续和序列的下一个元素做累积计算"""


def add(x, y):
    return x + y


print(reduce(add, [1, 3, 5, 7, 9]))

"""filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素"""


def is_odd(n):
    return n % 2 == 1


print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))

print(sorted([36, 5, -12, 9, -21]))
print(sorted(['bob', 'about', 'Zoo', 'Credit']))
# 忽略大小写
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
# 反向排序
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))

"""函数作为返回值"""


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


f = lazy_sum(1, 3, 5, 7, 9)
print(f())

"""返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量"""


def count():
    fs = []

    def fu(j):
        return j * j

    for i in range(1, 4):
        fs.append(fu(i))
    return fs


f1, f2, f3 = count()
print(f1)
print(f2)
print(f3)

"""lambda匿名函数"""
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

"""在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）"""


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


# 把@log放到now()函数的定义处，相当于执行了语句：now = log(now)
@log
def now():
    print(fmtime(time.localtime()))


now()


def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@log('execute')
def now2():
    print(fmtime(time.localtime(time.time())))


now2()
print(now.__name__)
print(now2.__name__)

"""偏函数"""
print(int('12345'))
print(int('12345', base=8))
print(int('12345', 16))
print(int('1000000', 2))

int2 = functools.partial(int, base=2)
print(int2('1010101'))
print(max(1, 2, 3, 4))
print(max((list(range(1, 6)))))
print(max([x * x for x in range(1, 9)]))
