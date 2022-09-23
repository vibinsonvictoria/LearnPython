'''
    Find Largest Number from Given List
    [1,2,3,4,5,6] => 6
'''

if __name__ =='__main__':
    lst = [1000,1,2,3,4,5,6,99,0,45,100,765]
    largest_number = sorted(lst,reverse=True)[0] if lst else None
    print(largest_number)






