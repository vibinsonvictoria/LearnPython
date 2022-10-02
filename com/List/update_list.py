'''
    - List
        * Mutable List
        * Can modify the original list
        * List Vs tuple
            List- mutable list
            Tuple - immutable list - once created we couldn't modify it. Will see more on tuple section.

'''

if __name__ == '__main__':
    lst = list(range(1, 10))
    print(f'Before Memory Location {hex(id(lst))}')
    print(*lst, sep=' ')
    for index, element in enumerate(lst):
        lst[index] = index * lst[index]
    print(lst)
    print(f'After Memory Location {hex(id(lst))}')  # all the operation will happen in the same list object
