'''
    input: ['a','b','c','d',100,1,2,'r']
    output = 100
    Find first integer number

'''
if __name__=='__main__':
    lst = ['a','b','c','d',100,1,2,'r']
    approach_1 = next((element for element in lst if isinstance(element,int)),None)
    print(approach_1)
    approach_2 =next(filter(int.__instancecheck__,lst),None)
    print(approach_2)