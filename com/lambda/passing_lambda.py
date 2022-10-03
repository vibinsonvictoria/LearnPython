''''
    passing lambda function into another function as argument
    lambda - can pass as input argument
'''

# you are defining the execution. How it wil work
# what process to execute, we are defining from outside
def list_process(lst,process):
    return [process(element) for element in lst ]




if __name__ =='__main__':
    lst = list(range(1,11))
    exponent_by_2_lambda  = lambda a : a * a
    exponent_by_3_lambda = lambda  a :  a*a*a
    res = list_process(lst,exponent_by_2_lambda)
    print(res)
    res = list_process(lst, exponent_by_3_lambda)
    print(res)