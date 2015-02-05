'Compute the sum of squares in different ways giving a tour through time'

n = 1000000

# 1990:  Plain Python -- Vanilla

result = []
for i in range(n):
    s = i*i
    result.append(s)
print sum(result)


# 2000:  List Comprehensions -- Chocolate

print sum([i*i for i in range(n)])


# 2002:  Generators -- Peanut Butter

def squares(n):
    for i in xrange(n):
        s = i*i
        yield s
print sum(squares(n))


# 2005:  Generator Expressions -- Reeses KitKatBars

print sum(i*i for i in xrange(n))
