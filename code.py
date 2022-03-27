from decorator import function, paramitrezed_f, paramitrezed_ff

@function
def summ(a,b):
    return a+b

@function
def devide(a,b):
    return a / b

summ(a=5,b=3)
devide(a=10.6, b=2)

@paramitrezed_f('file_2.json')
def multi(a,b):
    return a*b

multi(4,3)


nested_list = [
['a', 'b', 'c'],
['d', 'e', 'f', 'h', False],
[1, 2, None],
]

@paramitrezed_ff('file_3.json')
def flat_generator(nested_list):
    for values in nested_list:
        for value in values:
            yield value

flat_generator(nested_list)
