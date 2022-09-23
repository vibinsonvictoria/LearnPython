'''
    Find Largest Number from Given List
    [1,2,3,4,5,6] => 6
'''

def findMax(lst):
    if len(lst) ==0:
        return None
    max = lst[0]
    for number in lst[1::]:
        if max < number:
            max = number
    return max




if __name__ =='__main__':
    lst = [1000,1,2,3,4,5,6,99,0,45,100,765]
    largest_number = max(lst) # built-in function
    print(largest_number)
    largest_number = findMax(lst)
    print(largest_number)
    largest_number = findMax([])
    print(largest_number)
    largest_number = findMax([10])
    print(largest_number)





