

if __name__ == '__main__':
    numbers_list = list(range(1,11))
    print(numbers_list)
    #approach - 1 #Not recommended
    print('Approach - 1')
    print('*'*15)
    for index in range(0,len(numbers_list)):
        print(numbers_list[index],end=' ')

    #approach 2 - using enhanced for loop
    print('')
    print('Approach - 2')
    print('*' * 15)
    for element in numbers_list:
        print(element,end=' ')
    print('')
    print('Approach - 3') # create index with element
    print('*' * 15)
    for index,element in enumerate(numbers_list,start=0): # start =1 , then it will start index position from 1
        print(index,element)
