
if __name__ == '__main__':
    s = {1,2,3,4,5,1,2,2}
    print(f'original set : {s}')
    s.pop()
    print(f'After pop : {s}') # remove first element.
    #s.pop(1) # Error. Can't remove the element by index
