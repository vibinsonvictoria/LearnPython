
def addition(a,b):
    return a+b

def multiplication(a,b):
    return a * b

if __name__ == '__main__':
    res = addition(10,2)
    print(f'Addition result {res}')
    res = multiplication(10, 2)
    print(f'Multiplication result {res}')
    # using lambda function. we write lamda function in single line
    addition_lambda = lambda a,b : a+b
    multiplication_lambda = lambda a,b : a * b
    res = addition_lambda(10,2)
    print(f'Addition lambda result {res}')
    res = multiplication_lambda(10, 2)
    print(f'Multiplication lambda result {res}')
