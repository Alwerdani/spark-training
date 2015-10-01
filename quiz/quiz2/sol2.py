num = range(1, 101)


def fun(i):
    if i % 3 == 0 and i % 5 == 0:
        return 'FizzBuss'
    elif i % 3 == 0:
        return 'Fizz'
    elif i % 5 == 0:
        return 'Buzz'
    else:
        return i

print '\n'.join(map(str, map(fun, num)))
