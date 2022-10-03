
import math

def get_function(fn_name):
    match fn_name:
        case 'double' : return lambda a: a * a
        case 'sqrt'   : return lambda a : math.sqrt(a)
        case _        : return lambda a: a

def execution_engine(lst,process):
    return [process(element) for element in lst ]

if __name__ =='__main__':
    lst= list(range(1,11))
    res = execution_engine(lst,get_function('double'))
    print(res)
    res = execution_engine(lst, get_function('sqrt'))
    print(res)
    res = execution_engine(lst, get_function('nonfunction'))
    print(res)