import datetime

counter = 0
def function(old_function):
    def new_function(*args, **kwargs):
        global counter
        counter +=1
        a = {'Date': str(datetime.datetime.now())}
        name_fun = {'Name function': old_function.__name__}
        params = {'Parametrs': [args, kwargs]}
        result = old_function(*args, **kwargs)
        list_ = [counter, a, name_fun, params, {'Result':result}]
        with open('file_1.json', 'a') as document:
            document.write(str(list_))
        return result
    return new_function

def paramitrezed_f(parameter):
    def decor(foo):
        def new_f(*args, **kwargs):
            a = {'Date': str(datetime.datetime.now())}
            name_fun = {'Name function': foo.__name__}
            params = {'Parametrs': [args, kwargs]}
            result = foo(*args, **kwargs)
            list_ = [counter, a, name_fun, params, {'Result':result}]
            with open(parameter, 'w') as file:
                file.write(str(list_))
            return result
        return new_f
    return decor

#декоратор для 3 пунтка дз:
def paramitrezed_ff(parameter):
    def decor(foo):
        def new_f(*args, **kwargs):
            a = {'Date': str(datetime.datetime.now())}
            name_fun = {'Name function': foo.__name__}
            params = {'Parametrs': [args, kwargs]}
            result = foo(*args, **kwargs)
            list_ = [counter, a, name_fun, params, {'Result':result}]
            with open(parameter, 'w') as file:
                file.write(str(list_))
            return result
        return new_f
    return decor
