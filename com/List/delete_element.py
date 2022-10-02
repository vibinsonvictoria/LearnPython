'''

    how to delete the element from the list
    options are :
     - del lst[index]
     - lst.pop - remove last element
     -lst.pop(index) - Removes the specified index
     - clear  - delete all the elements in the list
     - del lst - delete list object from memory


'''

if __name__ == '__main__':
    lst = list(range(1,11))
    print(lst)
    print('delete element at specified index')
    del lst[0]
    print(lst)
    #del lst[100] # if index > len(lst) - it will throw index erro
    #print(lst)
    lst.pop() # remove last element from the list
    print(lst)
    lst.pop(2) # index start with 0
    print(lst)
    lst.clear() # remove all the element from the list.
    print(lst) # return empty list
    lst = list(range(1,11)) # reloading the element again.
    print(lst)
    del lst
    #print(lst) # will get an NameError- we deleted list object(lst) from Memory .