
if __name__ =='__main__':
    lst =['a','b','c',100,1,2,3,'d']
    lst_of_numbers = [element for element in lst if isinstance(element,int)]
    print(lst_of_numbers)