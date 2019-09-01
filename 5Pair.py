def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
def car(cons):
    return cons(lambda a, b: a)
def cdr(cons):
    return cons(lambda a, b: b)
print(car(cons(3, 4)))
print(cdr(cons(3, 4)))